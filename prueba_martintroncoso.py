#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}


def stock_marca(marca):
    marca = marca.lower()
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f"{modelo}: Stock - {stock[modelo][1]}")

def busqueda_precio(p_min, p_max):
    encontrados = []
    for modelo, datos in productos.items():
        if stock[modelo][1] > 0 and p_min <= stock[modelo][0] <= p_max:
            encontrados.append(f"{datos[0]}-{modelo}")
            
    if encontrados:
        for item in sorted(encontrados):
            print(item)
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def main():
    while True:
        print("Menú principal")
        print("1- Stock marca")
        print("2- Busqueda por precio")
        print("3- Actualizar precio")
        print("4- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion =="1":
            marca = input("Ingrese la marca: ")
            stock_marca(marca)

        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

        elif opcion == "3":
            while True:
                modelo = input("Ingrese el modelo del notebook: ")
                try:
                    precio = int(input("Ingrese el nuevo precio: "))
                    if actualizar_precio(modelo, precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("Debe ingresar un valor numérico válido para el precio.")
                respuesta = input("¿Desea actualizar otro precio? (sí/no): ").lower()
                if respuesta != 'sí':
                    break


        elif opcion == '4':
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción válida!!")
            
            
main()