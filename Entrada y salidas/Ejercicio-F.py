#Ingresar un importe por input, transformarlo a número real (float), luego mostrar el
#importe ingresado, el 10% del mismo, y el importe con el incremento calculado

importe = float(input("ingrese un importe: "))
incremento = importe * 0.10
total = importe + incremento 
print("el importe es de", importe, "mas el 10% su importe es de", total)