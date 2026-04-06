#Ejercicio 1
print("-" * 25)
print("Caja del Kiosco")
print("-" * 25)

nombre_cliente = input("Ingrese su nombre: ") .strip()

while nombre_cliente.isalpha() == False:
    print("Por favor ingresá un nombre válido: ")
    nombre_cliente = input("Ingrese su nombre: ")
    if nombre_cliente == "":
        print("No puede continuar sin escribir su nombre!")
        nombre_cliente = input("Ingrese su nombre: ") .strip()


cant_productos = int(input("Ingrese la cantidad de productos: ")) 
while cant_productos <=0:
    print("Por favor ingrese una cantidad de productos mayor a 0")
    cant_productos = int(input("Ingrese la cantidad de productos: ")) 

total = 0
total_descuento = 0
total_ahorro = 0

for producto in range (cant_productos):
    precio = input(f"Ingrese el precio del producto {producto + 1}: " )
    while precio.isdigit() == False:
        print("Por favor ingresá solo números")
        precio = input(f"Ingresá el precio del producto {producto + 1}: ")
    
    precio = int(precio)
    precio_original = precio
    descuento = input("El producto tiene descuento? S/N: ")  .lower()
    while descuento != "s" and descuento != "n":
        print("Por favor intgresá S o N")
        descuento = input("El producto tiene descuento? S/N: ")
    if descuento == "s":
        ahorro = int(precio) * 0.10
        precio = int(precio) - int(ahorro)
        total_ahorro += int(ahorro)
        total_descuento += int(precio)
    else:
        total_descuento += int(precio)

    total += precio_original

    print(f"Producto {producto + 1} - Precio: {precio} - Descuento: {descuento}")


print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cant_productos}")
print(f"Total sin descuentos = {total}")
print(f"Total con descuentos = {total_descuento}")
print(f"Ahorro: {total_ahorro}")
print(f"Promedio por producto: {total_descuento / cant_productos} ")



#Ejercicio 2
print("-" * 25)
print("Acceso al campus y menú seguro")
print("-" * 25)

usuario = "alumno"
contraseña = "python123"
intentos = 0


for i in range(3):
    print(f"Intento {intentos + 1}/3 ")
    in_usuario = input("Ingresá tu usuario: ")
    in_contraseña = input("Ingresá tu contraseña: ")
    print(f"Usuario: {in_usuario} Clave: {in_contraseña}")
    if usuario != in_usuario or contraseña != in_contraseña:
        print("Credenciales inválidas")
        intentos += 1
        if intentos == 3:
            print("Cuenta BLOQUEADA")
            break
    elif usuario == in_usuario and contraseña == in_contraseña:
        print("Acceso concedido")
        break

print("=" * 10)

print("Ingresá 1 / 2 / 3 / 4 para navegar")
entrada_usuario = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")

while entrada_usuario.isdigit() == False or int(entrada_usuario) < 1 or int(entrada_usuario) > 4:
    print("Error: Ingresá una opción válida (1, 2, 3, 4)")
    entrada_usuario = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")
entrada_usuario = int(entrada_usuario)

while int(entrada_usuario) != 4:

    if entrada_usuario == 1:
        print("Estado: Inscripto")
    elif entrada_usuario == 2:
        print("Cambio de clave /MÍNMO 6 CARACTERES/")
        cambio_clave = input("Ingresá tu nueva clave: ")
        confirmacion_cambio = input("Volvé a ingresar tu nueva clave:")
        if len(cambio_clave) < 6:
            print("Cambio de clave rechazado, debe tener mínimo 6 caracteres.")
        elif len(cambio_clave) >= 6 and cambio_clave != confirmacion_cambio:
            print("Las claves que ingresaste no coinciden.")
        elif len(cambio_clave) >= 6 and cambio_clave == confirmacion_cambio:
            print("Clave cambiada con éxito!")
            contraseña = cambio_clave
    elif entrada_usuario == 3:
        print("¡Todo esfuerzo tiene sus frutos!")

    entrada_usuario = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")
    while entrada_usuario.isdigit() == False or int(entrada_usuario) < 1 or int(entrada_usuario) > 4:
        print("Error: Ingresá una opción válida")
        entrada_usuario = input("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")
    entrada_usuario = int(entrada_usuario)
    
print("Saliendo...")


#Ejercicio 3
print("-" * 25)
print("Agenda de turnos con nombres")
print("-" * 25)

nombre_operador = input("Ingrese su nombre de operador: ") .strip()
ocupados_lunes = 0
ocupados_martes = 0
turnos_lunes = 0
turnos_martes = 0

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while nombre_operador.isalpha() == False or nombre_operador == "":
    if nombre_operador.isalpha() == False and nombre_operador != "":
        print("Por favor ingrese solo letras")
        nombre_operador = input("Ingrese su nombre: ") .strip()
    elif nombre_operador == "":
        print("No puede seguir sin escribir su nombre")
        nombre_operador = input("Ingrese su nombre: ") .strip()

opciones_menu = input(f"\n--------------------\nBienvenido {nombre_operador}\n--------------------\n 1) Reservar turnos\n 2) Cancelar turno (por nombre)\n 3) Ver agenda del día\n 4) Ver resumen general\n 5) Cerrar sistema\n --------------------\nIngrese una opción: ") .strip()


while opciones_menu.isdigit() == False or int(opciones_menu) < 1 or int(opciones_menu) > 5 or opciones_menu == "":

    if opciones_menu == "":
        print("ERROR: no podés ingresar un dato vacío")
    elif opciones_menu.isdigit() == False:
        print("Por favor ingresá 1 , 2 , 3 , 4 o 5")
    elif int(opciones_menu) < 1 or int(opciones_menu) > 5:
        print("Opción ingresada fuera de rango, ingresá 1 , 2 , 3 , 4 o 5")
    
    opciones_menu = input(f"\n--------------------\nBienvenido {nombre_operador}\n--------------------\n 1) Reservar turnos\n 2) Cancelar turno (por nombre)\n 3) Ver agenda del día\n 4) Ver resumen general\n 5) Cerrar sistema\n --------------------\nIngrese una opción: ") .strip()

opciones_menu = int(opciones_menu)

while int(opciones_menu) != 5:
    if opciones_menu == 1:

        print("Ingrese sus datos para reservar un turno")
        dia = input("Ingrese día deseado\n1) Lunes\n2) Martes\nIngrese la opción:  ")
        
        while dia == "" or dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            if dia == "":
                print("No puede ingresar un dato vacio")
            elif dia.isdigit() == False:
                print("Ingrese un número válido")
            elif int(dia) < 1 or int(dia) > 2:
                print("Número fuera de rango, ingrese 1 o 2")
            dia = input("Ingrese día deseado\n1) Lunes\n2) Martes\nIngrese la opción:   ")
        
        if int(dia) == 1:
            print("Elegiste día LUNES")
            nombre_paciente = input("Ingrese nombre del paciente: ") .strip()

            
            while nombre_paciente.isalpha() == False or nombre_paciente == "":
                if nombre_paciente.isalpha() == False and nombre_paciente != "":
                    print("Por favor ingrese solo letras")
                    nombre_paciente = input("Ingrese nombre del paciente: ") .strip()
                elif nombre_paciente == "":
                    print("No puede seguir sin escribir su nombre")
                    nombre_paciente = input("Ingrese nombre del paciente: ") .strip()

            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("\n--------------------\nYa tiene un turno reservado ese día\n--------------------\n")
            elif lunes1 == "":
                lunes1 = nombre_paciente
                ocupados_lunes += 1
                turnos_lunes += 1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            elif lunes2 == "":
                lunes2 = nombre_paciente
                ocupados_lunes += 1
                turnos_lunes += 1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            elif lunes3 == "":
                lunes3 = nombre_paciente
                ocupados_lunes += 1
                turnos_lunes += 1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            elif lunes4 == "":
                lunes4 = nombre_paciente
                ocupados_lunes +=1
                turnos_lunes += 1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            else:
                print("\n--------------------\nNo hay turnos disponibles ese día\n--------------------\n")
        
        elif int(dia) == 2:
            print("Elegiste día MARTES")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip()

            while nombre_paciente.isalpha() == False or nombre_paciente == "":
                if nombre_paciente.isalpha() == False and nombre_paciente != "":
                    print("Por favor ingrese solo letras")
                    nombre_paciente = input("Ingrese nombre del paciente: ") .strip()
                elif nombre_paciente == "":
                    print("No puede seguir sin escribir su nombre")
                    nombre_paciente = input("Ingrese nombre del paciente: ") .strip()

            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("\n--------------------\nYa tiene un turno reservado para ese día\n--------------------\n")
            elif martes1 == "":
                martes1 = nombre_paciente
                ocupados_martes += 1
                turnos_martes +=1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            elif martes2 == "":
                martes2 = nombre_paciente
                ocupados_martes += 1
                turnos_martes +=1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            elif martes3 == "":
                martes3 = nombre_paciente
                ocupados_martes += 1
                turnos_martes +=1
                print("\n--------------------\nTurno agendado\n--------------------\n")
            else:
                print("\n--------------------\nNo hay turnos disponibles ese día\n--------------------\n")
            
    elif opciones_menu == 2:
            #FALTA VALIDAR ESTAS OPCIONES!
        dia_cancelar = input("\n--------------------\nSeleccione día para borrar sus turnos\n--------------------\n1) Lunes\n2) Martes\n--------------------\nSeleccione el día: ")
        
        
        while dia_cancelar == "" or dia_cancelar.isdigit() == False or int(dia_cancelar) < 1 or int(dia_cancelar) > 2:
            if dia_cancelar == "":
                print("No puede ingresar un dato vacio")
            elif dia_cancelar.isdigit() == False:
                print("Ingrese un número válido")
            elif int(dia_cancelar) < 1 or int(dia_cancelar) > 2:
                print("Número fuera de rango, ingrese 1 o 2")
            dia_cancelar = input("Ingrese día deseado\n1) Lunes\n2) Martes\nIngrese la opción:   ")

        if int(dia_cancelar) == 1:
            nombre_paciente = input("Ingrese el nombre del paciente para cancelar su turno: ")

            while nombre_paciente.isalpha() == False or nombre_paciente == "":
                if nombre_paciente.isalpha() == False and nombre_paciente != "":
                    print("Por favor ingrese solo letras")
                    nombre_paciente = input("Ingrese su nombre: ") .strip()
                elif nombre_paciente == "":
                    print("No puede seguir sin escribir su nombre")
                    nombre_paciente = input("Ingrese su nombre: ") .strip()


            if  nombre_paciente != lunes1 and nombre_paciente != lunes2 and nombre_paciente != lunes3 and nombre_paciente != lunes4:
                print("\n--------------------\nEl paciente no tiene turnos este día\n--------------------\n")
            elif nombre_paciente == lunes1:
                lunes1 = ""
                ocupados_lunes -= 1
                turnos_lunes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
            elif nombre_paciente == lunes2:
                lunes2 = ""
                ocupados_lunes -= 1
                turnos_lunes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
            elif nombre_paciente == lunes3:
                lunes3 = ""
                ocupados_lunes -= 1
                turnos_lunes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
            elif nombre_paciente == lunes4:
                lunes4 = ""
                ocupados_lunes -= 1
                turnos_lunes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
        elif int(dia_cancelar) == 2:
            nombre_paciente = input("Ingrese el nombre del paciente para cancelar su turno: ")

            while nombre_paciente.isalpha() == False or nombre_paciente == "":
                if nombre_paciente.isalpha() == False and nombre_paciente != "":
                    print("Por favor ingrese solo letras")
                    nombre_paciente = input("Ingrese su nombre: ") .strip()
                elif nombre_paciente == "":
                    print("No puede seguir sin escribir su nombre")
                    nombre_paciente = input("Ingrese su nombre: ") .strip()

            if nombre_paciente != martes1 and nombre_paciente != martes2 and nombre_paciente != martes3:
                print("\n--------------------\nEl paciente no tiene turnos este día\n--------------------\n")
            elif nombre_paciente == martes1:
                martes1 = ""
                ocupados_martes -= 1
                turnos_martes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
            elif nombre_paciente == martes2:
                martes2 = ""
                ocupados_martes -= 1
                turnos_martes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")
            elif nombre_paciente == martes3:
                martes3= ""
                ocupados_martes -= 1
                turnos_martes -= 1
                print("\n--------------------\nTurno cancelado\n--------------------\n")

    elif opciones_menu == 3:
        print("\n--------------------\nMostrando agenda\n--------------------\n")   

        print("\n--------------------\nAgenda del día lunes\n--------------------\n")
        
        if lunes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1: " , lunes1)

        if lunes2 == "":
            print("Turno 2: Libre")
        else:
            print("Turno 2: " , lunes2)

        if lunes3 == "":
            print("Turno 3: Libre")
        else:
            print("Turno 3: " , lunes3)

        if lunes4 == "":
            print("Turno 4: Libre")
        else:
            print("Turno 4: " , lunes4)

        print("\n--------------------\nAgenda del día martes\n--------------------\n")

        if martes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1: ", martes1)
        
        if martes2 == "":
            print("Turno 2: Libre")
        else:
            print("Turno 2: " , martes2)
        
        if martes3 == "":
            print("Turno 3: Libre")
        else:
            print("Turno 3: " , martes3)
            


    elif opciones_menu == 4:
        
        print("\n--------------------\nResumen general\n--------------------\n")


        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes


        print(f"El día lunes tiene {ocupados_lunes} turnos ocupados y {libres_lunes} turnos libres")

        print(f"El día martes tiene {ocupados_martes} turnos ocupados y {libres_martes} turnos libres")

        if turnos_lunes > turnos_martes:
            print(f"El día lunes tiene más turnos ocupados: {turnos_lunes} turnos, mientras que el martes tiene {turnos_martes} turnos.")
        elif turnos_lunes < turnos_martes:
            print(f"El día martes tiene más turnos ocupados: {turnos_martes} turnos, mientras que el lunes tiene {turnos_lunes} turnos.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")




    opciones_menu = input(f"\n--------------------\nBienvenido {nombre_operador}\n--------------------\n 1) Reservar turnos\n 2) Cancelar turno (por nombre)\n 3) Ver agenda del día\n 4) Ver resumen general\n 5) Cerrar sistema\n --------------------\nIngrese una opción: ") .strip()


    while opciones_menu.isdigit() == False or int(opciones_menu) < 1 or int(opciones_menu) > 5 or opciones_menu == "":

        if opciones_menu == "":
            print("ERROR: no podés ingresar un dato vacío")
        elif opciones_menu.isdigit() == False:
            print("Por favor ingresá 1 , 2 , 3 , 4 o 5")
        elif int(opciones_menu) < 1 or int(opciones_menu) > 5:
            print("Opción ingresada fuera de rango, ingresá 1 , 2 , 3 , 4 o 5")
    
        opciones_menu = input(f"\n--------------------\nBienvenido {nombre_operador}\n--------------------\n 1) Reservar turnos\n 2) Cancelar turno (por nombre)\n 3) Ver agenda del día\n 4) Ver resumen general\n 5) Cerrar sistema\n --------------------\nIngrese una opción: ") .strip()

    opciones_menu = int(opciones_menu)

print("¡Saliendo del sistema!")

#Ejercicio 4
print("-" * 25)
print("Escape Room: La Bóveda")
print("-" * 25)

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0


nombre_agente = input("Ingrese el nombre del agente (solo letras): ")
print("-" * 25)

while nombre_agente.isalpha() == False or nombre_agente == "":
    if nombre_agente == "":
        print("-" * 25)
        print("No podés dejar este campo vacío")
        print("-" * 25)
        nombre_agente = input("Ingrese el nombre del agente: ")
    elif nombre_agente.isalpha() == False:
        print("Por favor ingrese un nombre (solo letras) ")
        print("-" * 25)
        nombre_agente = input("Ingrese el nombre del agente: ")

print("-" * 25)
print("\nBienvenido Agente" , nombre_agente)
print("-" * 25)


print("\nSos el agente" , nombre_agente , "y estás intentando abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.")
print("-" * 25)
print("Estadísticas del jugador:\nEnergía = " , energia , "\nTiempo = " , tiempo)
print("-" * 25)

opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()

while opciones_menu.isdigit() == False or opciones_menu == "" or int(opciones_menu) < 1 or int(opciones_menu) > 3:
    if opciones_menu == "":
        print("-" * 25)
        print("No podés jugar sin elegir una opción /1 , 2 , 3/")
        print("-" * 25)
        opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()
    elif opciones_menu.isdigit() == False:
        print("-" * 25)
        print("Por favor ingresá una opción numérica /1 , 2 , 3/")
        print("-" * 25)
        opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()
    else:
        print("-" * 25)
        print("Por favor ingresá una opción dentro del rango indicado /1 , 2 , 3/")
        print("-" * 25)
        opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()

opciones_menu = int(opciones_menu)



while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:


    if opciones_menu == 1:
        print("¡Forzaste la cerradura!")
        forzadas_seguidas += 1

        if forzadas_seguidas == 3:
            print("Forzaste muchas veces la cerradura!")
            print("Se activó la alarma y no abriste la cerradura!")
            alarma = True
            energia -=20
            tiempo -= 2
        else:
            if energia < 40:
        
                print("¡Riesgo de alarma!")
                evadir = input("Ingresá un número del 1 al 3 para evadir la alarma: ")
        
                while evadir.isdigit() == False or evadir == "" or int(evadir) < 1 or int(evadir) > 3:

                    if evadir == "":
                        print("-" * 25)
                        print("No podés continuar sin ingresar un número!")
                        print("-" * 25)
                        evadir = input("Ingresá un número del 1 al 3 para evadir la alarma: ")
                    elif evadir.isdigit() == False:
                        print("-" * 25)
                        print("El código es solo numérico! /1 , 2 o 3/")
                        print("-" * 25)
                        evadir = input("Ingresá un número del 1 al 3 para evadir la alarma: ")
                    else:
                        print("Ingresá un código dentro del rango indicado! /1 , 2 , 3/")
                        evadir = input("Ingresá un número del 1 al 3 para evadir la alarma: ")
        
                evadir = int(evadir)

                if evadir == 3:
                    print("Código equivocado, se ACTIVÓ LA ALARMA!")
                    energia -= 20
                    tiempo -= 2
                    alarma = True
            
                else:
                    print("Alarma evadida, abriste una cerradura! ")
                    cerraduras_abiertas += 1
                    energia -= 20
                    tiempo -= 2
                    print(f"Tenés {energia} puntos de energía y {tiempo} puntos de tiempo!")
            else:
                print("Abriste una cerradura!")
                cerraduras_abiertas += 1
                energia -= 20
                tiempo -= 2
                print(f"Tenés {energia} puntos de energía y {tiempo} puntos de tiempo!")
    
    elif opciones_menu == 2:
        
        forzadas_seguidas = 0

        print("Estás hackeando el panel!")
        energia -= 10
        tiempo -= 3

        for clave in range (4):
            entrada_clave = input("Ingresá letras para sumarlas al código (8 letras = 1 cerradura): ") .strip()

            while entrada_clave.isalpha() == False or entrada_clave == "" or len(entrada_clave) > 1:
                if entrada_clave == "":
                    print("No podés seguir sin ingresar las letras")
                    entrada_clave = input("Ingresá letras para sumarlas al código (8 letras = 1 cerradura): ") .strip()
                elif len(entrada_clave) > 1:
                    print("Tenés que ingresar de a 1 dígito a la vez!")
                    entrada_clave = input("Ingresá letras para sumarlas al código (8 letras = 1 cerradura): ") .strip()
                else:
                    print("Por favor ingresá solo letras")
                    entrada_clave = input("Ingresá letras para sumarlas al código (8 letras = 1 cerradura): ") .strip()

            codigo_parcial += entrada_clave
            print("Tu código parcial es: ", codigo_parcial)
            
            if len(codigo_parcial) == 8:
                print("Código de 8 dígitos detectado, cerradura abierta!")
                cerraduras_abiertas += 1

    elif opciones_menu == 3:

        forzadas_seguidas = 0

        print("Estás descansando!")

        if energia == 100:
            print("No podés recargar más de 100 de energía")
            energia = energia
            tiempo -= 1
        else:
            energia += 15
            tiempo -= 1
            if energia > 100:
                print("Máximo de energía alcanzado!")
                energia = 100
        
        if alarma == True:
            energia -= 10


    print("-" * 25)
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print("-" * 25)

    opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()

    while opciones_menu.isdigit() == False or opciones_menu == "" or int(opciones_menu) < 1 or int(opciones_menu) > 3:
        if opciones_menu == "":
            print("-" * 25)
            print("No podés jugar sin elegir una opción /1 , 2 , 3/")
            print("-" * 25)
            opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear   panel\n3) Descansar\nIngresá la opción: ").strip()
        elif opciones_menu.isdigit() == False:
            print("-" * 25)
            print("Por favor ingresá una opción numérica /1 , 2 , 3/")
            print("-" * 25)
            opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear   panel\n3) Descansar\nIngresá la opción: ").strip()
        else:
            print("-" * 25)
            print("Por favor ingresá una opción dentro del rango indicado /1 , 2 , 3/")
            print("-" * 25)
            opciones_menu = input("Acciones de juego\n1) Forzar cerradura\n2) Hackear panel\n3) Descansar\nIngresá la opción: ").strip()

    opciones_menu = int(opciones_menu)
        
if cerraduras_abiertas == 3:
    print("VICTORIA! Abriste la bóveda!")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energía")
elif tiempo <= 0:
    print("DERROTA: Se acabó el tiempo")
else:
    print("DERROTA: El sistema se bloqueó por alarma")


#Ejercicio 5
print("-" * 25)
print("Bienvenido a la ARENA DEL GLADIADOR")
print("-" * 25)

gladiador = input("Identifíquese GLADIADOR (solo letras): ").strip()

while gladiador.isalpha() == False or gladiador == "":
    if gladiador == "":
        print("-" * 25)
        print("No puedes entrar al campo sin un nombre!")
        print("-" * 25)
        gladiador = input("Identifíquese GLADIADOR (solo letras): ")
    else:
        print("-" * 25)
        print("Tu nombre de gladiador solo puede contener letras!")
        print("-" * 25)
        gladiador = input("Identifíquese GLADIADOR (solo letras): ")

print("Bienvenido, Gladiador", gladiador , "!")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base = 15 #Ataque pesado
daño_base_enemigo = 12
turno_gladiador = True #Profesor/a esto lo habíamos usado con match case en el pre-ingreso, no lo uso dentro de la lógica del juego porque no use match case, pero lo incluí por consigna. 

while vida_gladiador > 0 and vida_enemigo > 0:
    
    print("Turno GLADIADOR")
    print("-" * 25)
    print("Vida gladiador: " , vida_gladiador)
    print("Pociones restantes: ", pociones)
    print("Vida del enemigo: " , vida_enemigo)

    menu_opciones = input("\nSelecciona tu acción\n-------------------------\n1) Ataque pesado\n2) Ráfaga veloz\n3) Curar\n-------------------------\nIngrese opción: ") .strip()

    while menu_opciones.isdigit() == False or menu_opciones == "" or int(menu_opciones) < 1 or int(menu_opciones) > 3:
        
        if menu_opciones == "":
            print("-" * 25)
            print("No podes avanzar sin ingresar una opción (1 , 2 o 3)")
            print("-" * 25)
            menu_opciones = input("\nSelecciona tu acción\n-------------------------\n1) Ataque pesado\n2) Ráfaga veloz\n3) Curar\n-------------------------\nIngrese opción: ").strip()
        elif menu_opciones.isdigit() == False:
            print("-" * 25)
            print("Por favor ingrese solo números enteros (1 , 2 o 3)")
            print("-" * 25)
            menu_opciones = input("\nSelecciona tu acción\n-------------------------\n1) Ataque pesado\n2) Ráfaga veloz\n3) Curar\n-------------------------\nIngrese opción: ").strip()
        else:
            print("-" * 25)
            print("Por favor ingrese 1 , 2 o 3")
            print("-" * 25)
            menu_opciones = input("\nSelecciona tu acción\n-------------------------\n1) Ataque pesado\n2) Ráfaga veloz\n3) Curar\n-------------------------\nIngrese opción: ").strip()
        
    menu_opciones = int(menu_opciones)

    if menu_opciones == 1:
            print("\nEscogiste ataque pesado!")
            if vida_enemigo < 20:
                print("El enemigo está en estado crítico! Aprovechas y le acestas un golpe crítico.")
                golpe_critico = daño_base * 1.5
                vida_enemigo -= golpe_critico
                print("Atacaste al enemigo con un golpe crítico por" , golpe_critico , "puntos de daño!")
            else:
                print("Golpeas al enemigo con tu ataque pesado!")
                vida_enemigo -= daño_base
                print("Atacaste al enemigo por" , daño_base , "puntos de vida!")
        
    elif menu_opciones == 2:
            print("\nEscogiste ráfaga veloz!")

            for golpe in range (3):
                print("> Golpe conectado por 5 de daño")
                vida_enemigo -= 5
            

    elif menu_opciones == 3:
            print("\nEscogiste curarte!")

            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                if vida_gladiador > 100:
                     print("Usaste tu poción, pero el máximo de HP es de 100 puntos")
                     vida_gladiador = 100
            elif pociones == 0:
                print("\nNo te quedan pociones!")
            

    turno_gladiador = False 


    print("Turno ENEMIGO")
    print("El enemigo te atacó por 12 puntos de daño!")
    vida_gladiador -= daño_base_enemigo
    turno_gladiador = True

if vida_gladiador > 0:
    print("VICTORIA! el Gladiador" , gladiador , "ha ganado la batalla!")
else:
    print("DERROTA. Has caído en combate")