import os 


# Función para grabar los datos de un vehículo
def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    precio = float(input("Ingrese el precio del vehículo: "))
    multas = {'monto': float(input("Ingrese el monto de las multas: ")),
              'fecha': input("Ingrese la fecha de las multas: ")}
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    dueño = input("Ingrese el nombre del dueño del vehículo: ")

    if (patente) == 6 and 2 <= (marca) <= 15 and precio > 5000000:
        # Guardar los datos o realizar alguna acción con la información ingresada
        print("Vehículo registrado correctamente.")
    else:
        print("Error en los datos ingresados.")

# Función para buscar un vehículo por su patente
def buscar_vehiculo():
    patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
    # Realizar la búsqueda en los datos almacenados y mostrar la información correspondiente
    print("Información del vehículo buscado.")

# Función para imprimir certificados
def imprimir_certificados():
    certificados = ['Emisión de contaminantes', 'Anotaciones vigentes', 'Multas']
    patente_auto = input("Ingrese la patente del auto para imprimir los certificados: ")
    datos_dueño = input("Ingrese los datos del dueño actual: ")
    
    for certificado in certificados:
        monto = ()
        print(f"Certificado: {certificado}\nPatente del auto: {patente_auto}\nDatos del dueño: {datos_dueño}\nMonto: ${monto}")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        grabar_vehiculo()
    elif opcion == '2':
        buscar_vehiculo()
    elif opcion == '3':
        imprimir_certificados()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

