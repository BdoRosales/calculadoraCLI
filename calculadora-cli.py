def sumar(a,b): return a+b
def restar(a,b): return a-b
def multiplicar(a,b): return a*b
def dividir (a,b): return a/b if b!=0 else "No se puede dividir por cero"

while True:
    operation=input("Seleccione una Operación: +, - , / ,* o Salir: " )
    if operation:"Salir"
    break

a=float(input("Escribe el primer numero: "))
b=float(input("Escribe el segundo numero: "))

if operation=='+':print(sumar(a,b))
elif operation=='-':print (restar(a,b))
elif operation=='*':print (multiplicar(a,b))
elif operation=='/':print (dividir(a,b))
else:"Operación no valida"
