from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method == "GET":
        context = init()
    if request.method == "POST":
        if "num" in request.POST.keys():
            context = updateValue(request)
        if "opt" in request.POST.keys():
            context = updateOpt(request)
    return render(request, 'calculator/calculator.html', context)

def init():
    context = {"display" : 0, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "", "error" : 0}
    return context

def error():
    context = {"display" : "ERROR", "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "", "error" : 1}
    return context

def updateValue(request):
    cur_val = int(request.POST["cur_val"])
    display = cur_val * 10 + int(request.POST["num"])
    pre_opt = request.POST["pre_opt"]
    context = {"display" : display, "cur_val" : display, "pre_val" : request.POST["pre_val"],
    "pre_opt" : pre_opt, "cur_opt" : "", "error" : 0}
    return context

def updateOpt(request):
    pre_opt = request.POST["pre_opt"]
    pre_val = int(request.POST["pre_val"])
    cur_val = int(request.POST["cur_val"])
    cur_opt = request.POST["cur_opt"]
    if cur_opt == "=":
        display = request.POST["display"]
    else:
        if cur_opt == "*" or cur_opt == "/":
            cur_val = 1
        if pre_opt == "+":
            display = pre_val + cur_val
        if pre_opt == "-":
            display = pre_val - cur_val
        if pre_opt == "*":
            display = pre_val * cur_val
        if pre_opt == "/":
            if cur_val == 0:
                return error()
            display = int(pre_val / cur_val)

    if request.POST["opt"] == "=":
        context = {"display" : display, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "=", "error" : 0}
        return context
    else:
        pre_opt = request.POST["opt"]
        context = {"display": display, "cur_val": 0, "pre_val" : display, "pre_opt" : pre_opt, "cur_opt" : pre_opt, "error" : 0}
        return context
