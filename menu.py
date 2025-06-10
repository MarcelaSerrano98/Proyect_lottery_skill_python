menu1 ="""
---------------------------------------------------
__      ___   ______  ____ ____  __  ___              
||     // \\  | || | ||    || \\ || // \\             
||    ((   ))   ||   ||==  ||_// || ||=||             
||__|  \\_//    ||   ||___ || \\ || || ||             
                                                      
--------------------------------------------------    
   Bienvenido a SIMULOTO, simulador de lotería        
--------------------------------------------------    
   Selecciona una opción:                             
--------------------------------------------------    
   1. 📝 Explicar reglas                            
   2. 🎮 Jugar con números aleatorios               
   3. 🎮 Jugar con números ingresados
   4. 🎮 Jugar con boletos personalizados
   5. 🛒 Comprar boletos de lotería                  
   6. 📝 Crear boleto personalizado                  
   7. 📜 Historial de partidas                      
   8. 🚪 Salir                                      
--------------------------------------------------
""" 
menu2 = """
---------------------------------------------------
            MENU DE REGISTRO Y LOGIN
---------------------------------------------------
   1.  📝 Registro de usuario                      
   2.  🔑 Login de usuario                         
   3.  🚪 Salir                                    
---------------------------------------------------
"""

def menu_reglas():
    print("""
          MENU DE REGLAS
---------------------------------------------------
        1. 📝 Reglas del juego normal o modo aleatorio
        2. 📝 Reglas del juego con boletos
        3. 🚪 Volver al menu principal
        """)
     

def reglas_juego_normal():
    print("Las reglas del juego normal o modo aleatorio son las siguientes:")
    print("""
            1.  Deberas escoger 5 números o se te asiganaran 5 números aleatorios dependiendo de tu eleccion de juego.
            2.  Jugaras contra la maquina, que tambien escogera 5 numeros aleatorios.
            3.  Estos numeros deberan ser del 1 al 50, Se te daran de regreso otros 5 numeros entre este mismo rango.
            4.  Ingresas con 3 vidas.
            5.  Si aciertas 2 o mas numeros, podras volver a jugar con los mismos numeros o con otros 5 numeros.
            6.  Si no tienes ningun acierto, perderas una vida.
            7.  Por acierto acumulas 1 punto, cuanto mas aciertas, mas puntos obtendras.
            8.  Un total de 5 puntos obtendras una vida extra, mas oportunidades de ganar.
            9.  Si aciertas 5 numeros en una partida, ganaras el juego.
            10. Si pierdes todas tus vidas, perderas el juego. Se reinician tus vidas, deberas empezar de nuevo.
            11. Si ganas el juego, te ganaras un cafe gratis☕.
            
           """)
def reglas_juego_con_comprar_boletos():
    print("""
        1.  Se te dara una lista de boletos disponibles.
        2.  Deberas escoger un boleto.
        3.  Compites con la maquina, que tambien escogera 5 numeros aleatorios.
        4.  Ingresas con 3 vidas.
        5.  Si aciertas 2 o mas numeros, podras volver a jugar con el mismo boleto o con otros 5 numeros.
        5.  Si no tienes ningun acierto, perderas una vida.
        6.  Por acierto acumulas 1 punto, cuanto mas aciertas, mas puntos obtendras.
        7.  Un total de 5 puntos obtendras una vida extra, mas oportunidades de ganar.
        8.  Si aciertas 5 numeros, ganaras el juego, y te ganaras un cafe gratis☕.
        9.  Si pierdes todas tus vidas, perderas el juego.
        10. Si pierdes el juego se reinician tus vidas, deberas empezar de nuevo.
        """)

