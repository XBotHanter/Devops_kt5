def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def Multiply(a,b):
    return a*b

def Div(a,b):
    if(b==0): return "На ноль делить нельзя"
    else: return a/b

def calc(a,b,str):
    if(str=="Сложить"): return sum(a,b)
    elif(str=="Вычесть(отнять)"): return sub(a,b)
    elif(str=="Умножить"):return Multiply(a,b)
    elif(str=="Деление"): return Div(a,b)
    else:return "Такой операции нет"


print(calc(30,12,"Сложить"))
#(v2.0.1) - Исправлен баг с выбором операций






