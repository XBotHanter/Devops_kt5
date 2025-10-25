def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def Multiply(a,b):
    return a*b

def Div(a,b):
    if(b==0): return "На ноль делить нельзя"
    else: return a/b

print(sum(10,20))#выведет 30
print(sub(20,10))#выведет 10
print(Multiply(10,5))#выведет 50
print(Div(50,10))#выведет 5
#(v1.3.1) - В функции деления мы исправили баг с делением на 0




