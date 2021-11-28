Cedula= eval(input("ingrese el numero de identificación"))
Rol= input("ingrese el rol dentro de la univeridad (profesor o estudiante)")
CodProducto=input("ingrese el codigo del producto a comprar")
CantidadProducto= eval(input("ingrese la cantidad de producto a llevar"))
PrecioProducto= eval(input("ingrese el precio por unidad de producto"))
if Rol == "profesor":
    Pago= CantidadProducto*PrecioProducto*0.8
else:
        Pago = CantidadProducto*PrecioProducto*0.5

print ("el ", Rol," con numero de identificación ", Cedula, " debe pagar ", Pago, " por el producto ", CodProducto)

