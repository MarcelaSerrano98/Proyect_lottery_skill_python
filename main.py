import random
import json
import os
from menu import *
import time


def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')


def leerJson(path: str):
    try:
        with open(path, mode='r') as file:
            contenido = file.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except FileNotFoundError:
        with open(path, mode='w') as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError:
        return []

def escribirJson(path: str, data):
    try:
        with open(path, mode='w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"❌ Error al escribir en el archivo {path}: {str(e)}")

numeros_ingresados = leerJson('numeros_ingresados.json')
numeros_generados_automaticos = leerJson('numeros_generados_automaticos.json')
usuarios = leerJson('usuarios.json')
vida = 3


def Reglas():
    while True:
        print(menu_reglas())
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                reglas_juego_normal()
                input("↩️ Presiona enter para continuar")
                limpiarConsola()  
            elif opcion == 2:
                reglas_juego_con_comprar_boletos()
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 3:
                print("👋 Saliendo del menu de reglas")
                limpiarConsola()
                break
            else:
                print("❌ Opción no válida")
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
                continue
        except ValueError:
            print("❌ Opción no válida")
            print("📌 La opción debe ser un número entero")
            input("↩️ Presiona enter para continuar")
            limpiarConsola()
            continue
        
        
        
def registro_usuario():
    try:
        nombre = input("📝 Ingrese su nombre: ").strip()
        edad = input("📝 Ingrese su edad: ").strip()
        contraseña = input("📝 Ingrese su contraseña: ").strip()
        
        if not nombre or not edad or not contraseña:
            print("❌ No se puede registrar un usuario sin nombre, edad o contraseña")
            return None
            
        for usuario in usuarios:
            if usuario.get('nombre') == nombre:
                print("❌ Ya existe un usuario con ese nombre")
                return None
        
        nuevo_usuario = {
            'nombre': nombre,
            'edad': edad,
            'contraseña': contraseña,
            'puntos': 0,
            'vida': 3
        }
        
        usuarios.append(nuevo_usuario)
        escribirJson('usuarios.json', usuarios)
        print("✅ Usuario registrado con éxito")
        return nuevo_usuario
    except Exception as e:
        print(f"❌ Error al registrar usuario: {str(e)}")
        return None

def login_usuario():
    try:
        nombre = input("📝 Ingrese su nombre: ").strip()
        contraseña = input("📝 Ingrese su contraseña: ").strip()
        
        if not nombre or not contraseña:
            print("❌ Debe ingresar nombre y contraseña")
            return None
            
        for usuario in usuarios:
            if usuario.get('nombre') == nombre and usuario.get('contraseña') == contraseña:
                print("✅ Usuario logueado con éxito")
                return usuario
        print("❌ Usuario o contraseña incorrectos")
        return None
    except Exception as e:
        print(f"❌ Error al hacer login: {str(e)}")
        return None

def Jugar_numeros_ingresados(min : int, max : int):
    print ("📝 Por favor ingrese 5 números enteros")
    print(f"📌 Los numeros deben ser del {min} al {max}")
    temp= numeros_ingresados
    numeros=[]
    
    while True:
        numeros.clear()
        for i in range(5):
            try:
                numero= int(input(f"📝 Ingrese el numero {i+1}: "))
                if numero < min or numero > max:
                    print("❌ El numero debe ser del 1 al 50")
                    print("Intenta nuevamente")
                    break
                else:
                    numeros.append(numero)  
            except ValueError:
                print("❌ El numero debe ser un entero")
                print("Intenta nuevamente")
                break
        if len(numeros) == 5:
            break
    temp.append(numeros)
    escribirJson('numeros_ingresados.json',temp)
    print("✅ Numeros ingresados con exito")
    return numeros
    
    



def jugar_numeros_automaticos(): 
    temp = numeros_generados_automaticos
    numeros = random.sample(range(1, 50), 5)
    temp.append(numeros)
    escribirJson('numeros_generados_automaticos.json', temp)
    print(f"✅ Numeros generados con exito:")
    return numeros

def guardar_partida(usuario_actual, numeros_persona, numeros_maquina, aciertos=None, puntos_acumulados=None, vidas_restantes=None, modo_juego="", resultado=""):
    try:
        historial = leerJson('historial_partidas.json')
        if historial is None:
            historial = []
        
        nueva_partida = {
            'fecha': time.strftime("%Y-%m-%d %H:%M:%S"),
            'usuario': usuario_actual['nombre'],
            'modo_juego': modo_juego,
            'numeros_persona': numeros_persona,
            'numeros_maquina': numeros_maquina,
            'resultado': resultado,
            'numero': len(historial) + 1
        }

        # Solo agregar estos campos si no es modo boletos personalizados
        if modo_juego != "boletos_personalizados":
            nueva_partida['aciertos'] = aciertos
            nueva_partida['puntos_acumulados'] = puntos_acumulados
            nueva_partida['vidas_restantes'] = vidas_restantes
        
        historial.append(nueva_partida)
        escribirJson('historial_partidas.json', historial)
        print("✅ Partida guardada en el historial")
    except Exception as e:
        print(f"❌ Error al guardar la partida: {str(e)}")

def jugar_con_boleto_personalizado(usuario):
    try:
        with open("boletos_personalizados.json", "r") as f:
            boletos = json.load(f)
    except FileNotFoundError:
        print("❌ No hay boletos personalizados creados aún.")
        return

    if usuario['nombre'] not in boletos or not boletos[usuario['nombre']]:
        print("❌ No tienes boletos personalizados registrados.")
        return

    def pintar_boletos():
        print(f"\n🎟️ Boletos personalizados de {usuario['nombre']}:")
        for nombre in boletos[usuario['nombre']]:
            print(f" - {nombre}: {boletos[usuario['nombre']][nombre]}")

    while True:
        pintar_boletos()
        nombre_boleto = input("\nEscribe el nombre del boleto que quieres usar: ")
        if nombre_boleto in boletos[usuario['nombre']]:
            break
        else:
            print("❌ Ese boleto no existe.")
            print("Intenta nuevamente")
            continue


    boleto = boletos[usuario['nombre']][nombre_boleto]
    numeros_sorteo = (random.sample(range(1, 46), 5))

    print("\n🎰 Números sorteados:", numeros_sorteo)
    print("🎟️ Tu boleto:", (boleto))

    aciertos = set(boleto) & set(numeros_sorteo)
    if len(aciertos) == 0:
        print(f"✅ Aciertos: ({len(aciertos)})")
    else:
        print(f"✅ Aciertos: ({len(aciertos)}) - Numeros en los que acertaste: {aciertos}")

    if len(aciertos) >= 3:
        print("🎉 ¡Felicidades! ¡Ganaste el premio mayor!")
        print("Ganaste un cafe gratis")
        guardar_partida(
            usuario,
            boleto,
            numeros_sorteo,
            len(aciertos),
            0,  # puntos no se modifican
            usuario['vida'],  # vidas no se modifican
            "boletos_personalizados",
            "¡GANADOR! Obtuvo café gratis"
        )
    elif len(aciertos) == 2:
        print("Muy cerca, pero no fue suficiente")
        print("Intenta nuevamente")
        guardar_partida(
            usuario,
            boleto,
            numeros_sorteo,
            len(aciertos),
            0,  # puntos no se modifican
            usuario['vida'],  # vidas no se modifican
            "boletos_personalizados",
            "Muy cerca, pero no fue suficiente"
        )
    else:
        print("😕 Sigue intentando, la suerte llegará")
        print("Intenta nuevamente")
        guardar_partida(
            usuario,
            boleto,
            numeros_sorteo,
            len(aciertos),
            0,  # puntos no se modifican
            usuario['vida'],  # vidas no se modifican
            "boletos_personalizados",
            "Perdiste"
        )
    
    escribirJson('usuarios.json', usuarios)
    

def escoger_boletos():
    boletos = leerJson('boletos.json')
    while True:
        print("Boletos disponibles:")
        for i, boleto in enumerate(boletos, 1):
            print(f"{i}. 📝 {boleto['nombre']}")
            print(f"   📌 {boleto['numeros']}")

        opcion_boletos = input("📝 Elige el número o nombre del boleto: ")

        try:
            opcion_num = int(opcion_boletos)
            if 1 <= opcion_num <= len(boletos):
                boleto_comprado = boletos[opcion_num-1]['numeros']
                print(f"✅ Has escogido el boleto: {boletos[opcion_num-1]['nombre']}")
                return boleto_comprado
            else:
                print("❌ Boleto no válido")
                print(f"📌 Los numeros deben ser del 1 al {len(boletos)}")
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
                
        except ValueError:
            print("❌ Boleto no válido")
            print("📌 La opción debe ser un número entero")
            input("↩️ Presiona enter para continuar")
            limpiarConsola()
            continue

            for boleto in boletos:
                if boleto['nombre'] == opcion_boletos:
                    boleto_comprado = boleto['numeros']
                    print(f"✅ Has escogido el boleto: {boleto['nombre']}")
                    return boleto_comprado
    return None

def vidas(vida, modo_juego="", numeros_fijos=None, boleto_comprado=None):
    if vida == 0:
        puntos = 0
        vida = 3
        usuario_actual['vida'] = vida 
        usuario_actual['puntos'] = puntos
        escribirJson('usuarios.json', usuarios)
        print(f"❌ Has perdido el juego\n❌ Perdiste tu acumulado de puntos: {puntos}")
        print("👋 Mejor suerte para la proxima")
        validar = False
        return None
        
    elif vida >= 1 and vida <= 3:
        usuario_actual['vida'] = vida
        escribirJson('usuarios.json', usuarios)
        print(f"💖 Vidas: {usuario_actual['vida']}")
        print(f"💰 Puntos: {usuario_actual['puntos']}")
        while True:
            nuevo_juego = input("Desea jugar con los mismos numeros? (s/n)")
            if nuevo_juego.lower() == "s":
                if modo_juego == "manual":
                    numeros_persona = leerJson('numeros_ingresados.json')[-1]
                    numeros_maquina = jugar_numeros_automaticos()
                    print(f"🎮 Jugando con tus números anteriores: {numeros_persona}")
                    comparar_numeros(numeros_persona, numeros_maquina, vida, usuario_actual['puntos'], modo_juego)
                elif modo_juego == "automatico":
                    print(f"🎮 Continuando con tus números: {numeros_fijos}")
                    numeros_maquina = jugar_numeros_automaticos()
                    comparar_numeros(numeros_fijos, numeros_maquina, vida, usuario_actual['puntos'], modo_juego, numeros_fijos)
                elif modo_juego == "boletos":
                    print("📌En este modo tu mismo debes escoger el boleto que quieres jugar")
                    print("🔄️Puedes escoger el mismo boleto con el que jugaste anteriormente")
                    boleto_comprado = escoger_boletos()
                    if boleto_comprado is not None:
                        numeros_maquina = jugar_numeros_automaticos()
                        comparar_numeros(boleto_comprado, numeros_maquina, vida, usuario_actual['puntos'], modo_juego, boleto_comprado)
                    else:
                        print("❌ No se pudo seleccionar un boleto válido")
                break
            elif nuevo_juego.lower() == "n":
                if modo_juego == "manual":
                    Jugar_numeros_ingresados(1,50)
                    numeros_maquina = jugar_numeros_automaticos()
                    comparar_numeros(numeros_ingresados[-1], numeros_maquina, vida, usuario_actual['puntos'], modo_juego)
                elif modo_juego == "automatico":
                    print("\n🎮 Generando nuevos números para ti...")
                    numeros_persona = jugar_numeros_automaticos()
                    print(f"🎮 Tus nuevos números son: {numeros_persona}")
                    print("🎮 Generando nuevos números para la maquina...")
                    numeros_maquina = jugar_numeros_automaticos()
                    comparar_numeros(numeros_persona, numeros_maquina, vida, usuario_actual['puntos'], modo_juego, numeros_persona)
                elif modo_juego == "boletos":
                    boleto_comprado = escoger_boletos()
                    if boleto_comprado is not None:
                        numeros_maquina = jugar_numeros_automaticos()
                        comparar_numeros(boleto_comprado, numeros_maquina, vida, usuario_actual['puntos'], modo_juego, boleto_comprado)
                    else:
                        print("❌ No se pudo seleccionar un boleto válido")
                break

            else:   
                print("❌ Opción no válida. Por favor, elija 's' o 'n'")
            
    else:
        pass

def vida_extra(vida):
    if usuario_actual['puntos'] >= 5:
        vida += 1
        usuario_actual['vida'] = vida
        usuario_actual['puntos'] = 0  
        escribirJson('usuarios.json', usuario_actual)
        print(f"💖 ¡Has ganado una vida extra! Ahora tienes {vida} vidas✔️")
        print("💰 Tus puntos se han reiniciado a 0")
        return vida
    return vida

def guardar_partida(usuario_actual, numeros_persona, numeros_maquina, aciertos, puntos_acumulados, vidas_restantes, modo_juego, resultado):
    try:
        historial = leerJson('historial_partidas.json')
        if historial is None:
            historial = []
        
        nueva_partida = {
            'fecha': time.strftime("%Y-%m-%d %H:%M:%S"),
            'usuario': usuario_actual['nombre'],
            'modo_juego': modo_juego,
            'numeros_persona': numeros_persona,
            'numeros_maquina': numeros_maquina,
            'aciertos': aciertos,
            'puntos_acumulados': puntos_acumulados,
            'vidas_restantes': vidas_restantes,
            'resultado': resultado,
            'numero': len(historial) + 1
        }
        
        historial.append(nueva_partida)
        escribirJson('historial_partidas.json', historial)
        print("✅ Partida guardada en el historial")
    except Exception as e:
        print(f"❌ Error al guardar la partida: {str(e)}")

def mostrar_historial(usuario_actual):
    historial = leerJson('historial_partidas.json')
    if not historial:
        print("❌ No hay partidas registradas")
        return
    
    # Filtrar partidas del usuario actual
    historial_usuario = [partida for partida in historial if partida['usuario'] == usuario_actual['nombre']]
    
    if not historial_usuario:
        print(f"❌ No hay partidas registradas para el usuario {usuario_actual['nombre']}")
        return
    
    print("📜 HISTORIAL DE PARTIDAS 📜")
    print("-" * 50)
    
    for partida in historial_usuario:
        print(f"\n📅 Fecha: {partida['fecha']}")
        print(f"👤 Usuario: {partida['usuario']}")
        print(f"🎮 Modo de juego: {partida['modo_juego']}")
        print(f"🎲 Números jugados: {partida['numeros_persona']}")
        print(f"🎲 Números máquina: {partida['numeros_maquina']}")
        print(f"🎯 Aciertos: {partida['aciertos']}")
        print(f"💰 Puntos acumulados: {partida['puntos_acumulados']}")
        print(f"💖 Vidas restantes: {partida['vidas_restantes']}")
        print(f"🏆 Resultado: {partida['resultado']}")
        print("-" * 50)

def comparar_numeros(dato1, dato2, vida, puntos, modo="manual", numeros_fijos=None):
    numeros_acertados = [n for n in dato1 if n in dato2]
    print(f"🚹 Numeros persona: {dato1}")
    print(f"💻 Numeros maquina: {dato2}")
    aciertos = len(numeros_acertados)
    print(f"🎯 Aciertos: {aciertos}")
    
    if aciertos == 0:
        vida -= 1
        print("❌ No has acertado ningun numero, has perdido una vida")
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "Perdió una vida"
        )
        vidas(vida, modo, numeros_fijos)
        return vida
        
    elif aciertos == 1:
        print("💰 Has ganado 1 punto")
        usuario_actual['puntos'] += 1
        vida = vida_extra(vida)
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "Ganó 1 punto"
        )
        escribirJson('usuarios.json', usuarios)
        vidas(vida, modo, numeros_fijos)

    elif aciertos == 2:
        print("💰 Has ganado 2 puntos")
        usuario_actual['puntos'] += 2
        vida = vida_extra(vida)
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "Ganó 2 puntos"
        )
        escribirJson('usuarios.json', usuarios)
        vidas(vida, modo, numeros_fijos)
        
    elif aciertos == 3:
        print("💰 Has ganado 3 puntos")
        usuario_actual['puntos'] += 3
        vida = vida_extra(vida)
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "Ganó 3 puntos"
        )
        escribirJson('usuarios.json', usuarios)
        vidas(vida, modo, numeros_fijos)
        
    elif aciertos == 4:
        print("💰 Has ganado 4 puntos")
        usuario_actual['puntos'] += 4
        vida = vida_extra(vida)
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "Ganó 4 puntos"
        )
        escribirJson('usuarios.json', usuarios)
        vidas(vida, modo, numeros_fijos)
        
    elif aciertos == 5:
        print("🎉 Ganaste el juego, FELICITACIONES🎉")
        print(f"☕ Ganaste un cafe gratis")
        print(f"💰 Tus puntos son: {usuario_actual['puntos']}")
        vida = vida_extra(vida)
        guardar_partida(
            usuario_actual,
            dato1,
            dato2,
            aciertos,
            usuario_actual['puntos'],
            vida,
            modo,
            "¡GANADOR! Obtuvo café gratis"
        )
        escribirJson('usuarios.json', usuarios)
        vidas(vida, modo, numeros_fijos)
    
    else:
        pass

def historial_partidas():
    historial = leerJson('historial_partidas.json')
    if historial:
        print("Historial de partidas:")
        for partida in historial:
            print(f"  🎮 Partida {partida['numero']}:")
            print(f"  🚹 Numeros persona: {partida['numeros_persona']}")
            print(f"  💻 Numeros maquina: {partida['numeros_maquina']}")
            print(f"  🎯 Aciertos: {partida['aciertos']}")
            print(f"  💰 Puntos: {partida['puntos']}")
            print(f"  💖 Vidas: {partida['vida']}")
            print(f"  ")

def crear_boleto_personalizado(usuario):
    nombre_boleto = input("Ingresa un nombre para tu boleto personalizado: ")
    numeros = []

    while len(numeros) < 5:
        try:
            numero = int(input(f"Número {len(numeros)+1}: "))
            if numero < 1 or numero > 45:
                print("El número debe estar entre 1 y 45.")
            elif numero in numeros:
                print("Número repetido. Intenta con otro.")
            else:
                numeros.append(numero)
        except ValueError:
            print("Ingresa un número válido.")

    # Cargar archivo o inicializar si no existe o está vacío
    try:
        with open("boletos_personalizados.json", "r") as f:
            contenido = f.read().strip()
            if contenido:
                boletos = json.loads(contenido)
            else:
                boletos = {}
    except (FileNotFoundError, json.JSONDecodeError):
        boletos = {}

    if usuario['nombre'] not in boletos:
        boletos[usuario['nombre']] = {}

    boletos[usuario['nombre']][nombre_boleto] = numeros

    # Guardar archivo
    with open("boletos_personalizados.json", "w") as f:
        json.dump(boletos, f, indent=4)

    print(f"✅ Boleto '{nombre_boleto}' guardado exitosamente para {usuario['nombre']}.")


    
def menu_principal(usuario_actual):
    while True:
        print(menu1)  
        try:
            opcion = int(input("📝Elige una opción: "))
            if opcion == 1:
                Reglas()
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 2:
                print("\nGenerando tus números...")
                numeros_persona_fijos = jugar_numeros_automaticos()
                print("\nGenerando números de la máquina...")
                maquina = jugar_numeros_automaticos()
                print("\nComparando números...")
                comparar_numeros(numeros_persona_fijos, maquina, usuario_actual['vida'], usuario_actual['puntos'], "automatico", numeros_persona_fijos)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
                
            elif opcion == 3:
                Jugar_numeros_ingresados(1, 50)
                numeros_maquina = jugar_numeros_automaticos()
                comparar_numeros(numeros_ingresados[-1], numeros_maquina, usuario_actual['vida'], usuario_actual['puntos'], "manual", None)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 4:
                jugar_con_boleto_personalizado(usuario_actual)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 5:
                boleto_comprado = escoger_boletos()
                if boleto_comprado:
                    numeros_maquina = jugar_numeros_automaticos()
                    comparar_numeros(boleto_comprado, numeros_maquina, usuario_actual['vida'], usuario_actual['puntos'], "boletos", boleto_comprado)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
               
            elif opcion == 6:
                crear_boleto_personalizado(usuario_actual)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 7:
                mostrar_historial(usuario_actual)
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
            elif opcion == 8:
                salir = input("¿Está seguro que desea salir? (s/n): ")
                if salir.lower() == "s":
                    print("👋 Gracias por jugar")
                    return
                elif salir.lower() == "n":
                    limpiarConsola()
                    continue
                else:
                    print("❌ Opción no válida")
                    print("📌 Las opciones válidas son: s, n")
                    input("↩️ Presiona enter para continuar")
                    limpiarConsola()
                    continue
            else:
                print("❌ Opción no válida")
                print("📌 Las opciones válidas son: 1, 2, 3, 4, 5, 6")
                input("↩️ Presiona enter para continuar")
                limpiarConsola()
                continue
        
        except ValueError:
            print("❌ Opción no válida")
            print("📌 La opción debe ser un número entero")
            input("↩️ Presiona enter para continuar")
            limpiarConsola()
            continue


while True:
    print(menu2)

    try:
        opcion = int(input("📝 Elige una opción: "))
        if opcion == 1:
            registro_usuario()
           
        elif opcion == 2:
            usuario_actual = login_usuario()
            if usuario_actual:
                menu_principal(usuario_actual)
            
        elif opcion == 3:
            print("👋 Gracias por jugar")
            break
        else:
            print("❌ Opción no válida")
            print("📌 Las opciones válidas son: 1, 2, 3")
            input("↩️ Presiona enter para continuar")
            limpiarConsola()
            continue

    except ValueError:
        print("❌ Opción no válida")
        print("📌 La opción debe ser un número entero")
        input("↩️ Presiona enter para continuar")
        limpiarConsola()
        continue
    
