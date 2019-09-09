from django.shortcuts import render

val = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
opt = ["+", "-", "*", "/", "="]

# Create your views here.
def calculator(request):
    if request.method == "GET":
        context = init()
    if request.method == "POST":
        if "num" in request.POST.keys():
            context = updateValue(request, val)
        if "opt" in request.POST.keys():
            context = updateOpt(request, opt)
    return render(request, 'calculator/calculator.html', context)

def init():
    context = {"display" : 0, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "error" : 0}
    return context

def error():
    context = {"display" : "E", "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "error" : 1}
    return context

def updateValue(request, val):
    cur_val = int(request.POST["cur_val"])
    display = cur_val * 10 + int(request.POST["num"])
    pre_opt = request.POST["pre_opt"]
    context = {"display" : display, "cur_val" : display, "pre_val" : request.POST["pre_val"], "pre_opt" : pre_opt, "error" : 0}
    return context

def updateOpt(request, opt):
    pre_opt = request.POST["pre_opt"]
    pre_val = int(request.POST["pre_val"])
    cur_val = int(request.POST["cur_val"])
    if pre_opt == "+":
        display = pre_val + cur_val
    if pre_opt == "-":
        display = pre_val - cur_val
    if pre_opt == "*":
        display = pre_val * cur_val
    if pre_opt == "/":
        if request.POST["opt"] == "=" and cur_val == 0:
            context = error()
            return context
        display = int(pre_val / cur_val);
    if request.POST["opt"] == "=":
        context = {"display" : display, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "error" : 0}
        return context
    else:
        pre_opt = request.POST["opt"]
        context = {"display": display, "cur_val": 0, "pre_val" : display, "pre_opt" : pre_opt, "error" : 0}
        return context
