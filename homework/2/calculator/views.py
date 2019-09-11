from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method == "GET":
        context = init()
    if request.method == "POST":
        if "num" in request.POST.keys():
            context = updateValue(request)
        elif "opt" in request.POST.keys():
            context = updateOpt(request)
        else:
            context = error();
    return render(request, 'calculator/calculator.html', context)

def init():
    context = {"display" : 0, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "", "error" : 0}
    return context

def error():
    context = {"display" : "ERROR", "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "", "error" : 1}
    return context

def updateValue(request):
    val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    opt = ['+', '-', '*', '/', '=']
    if "cur_val" in request.POST and "pre_opt" in request.POST:
        cur_val = request.POST["cur_val"]
        pre_opt = request.POST["pre_opt"]
        if pre_opt in opt and isinteger(cur_val):
            cur_val = int(cur_val)
            if request.POST["num"] in val:
                display = cur_val * 10 + int(request.POST["num"])
                context = {"display" : display, "cur_val" : display, "pre_val" : request.POST["pre_val"], "pre_opt" : pre_opt, "cur_opt" : "", "error" : 0}
                return context
    return error()

def updateOpt(request):
    val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    opt = ['+', '-', '*', '/', '=']
    if "pre_opt" in request.POST and "pre_val" in request.POST and "cur_val" in request.POST and "cur_opt" in request.POST:
        pre_opt = request.POST["pre_opt"]
        pre_val = request.POST["pre_val"]
        cur_val = request.POST["cur_val"]
        cur_opt = request.POST["cur_opt"]
        if pre_opt in opt and (cur_opt in opt or cur_opt == "") and isinteger(cur_val) and isinteger(pre_val):
            cur_val = int(cur_val)
            pre_val = int(pre_val)
            if cur_opt == "=":
                if "display" in request.POST:
                    display = request.POST["display"]
                else:
                    return error()
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

            if request.POST["opt"] in opt:
                if request.POST["opt"] == "=":
                    context = {"display" : display, "cur_val" : 0, "pre_val" : 0, "pre_opt" : "+", "cur_opt" : "=", "error" : 0}
                    return context
                else:
                    pre_opt = request.POST["opt"]
                    context = {"display": display, "cur_val": 0, "pre_val" : display, "pre_opt" : pre_opt, "cur_opt" : pre_opt, "error" : 0}
                    return context
    return error()

def isinteger(str):
    val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if not (str[0] in val) and str[0] != '-':
        return False
    else:
        for i in range(1, len(str)):
            if not (str[i] in val):
                return False
    return True
