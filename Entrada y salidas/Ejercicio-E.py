#Ingresar dos números por input, transformarlos a enteros (int), realizar la operación
#aritmética de división, pero para obtener y mostrar el resto (operador módulo) entre
#el dividendo (numero_uno) y el divisor (numero_dos).
#Ejemplo: "El resto es 0." 

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))

resto = num1 % num2

print("El resto es" , resto,) 