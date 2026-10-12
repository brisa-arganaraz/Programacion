#Ingresar un importe por input, transformarlo a número real (float), luego mostrar el
#importe ingresado, el 25% del mismo, y el importe con el descuento calculado.

importe = float(input("ingrese un importe:"))
descuento = importe * 0.25
total = importe - descuento
print("el importe es de ", importe, "con el descuento del 25% es ", total)
