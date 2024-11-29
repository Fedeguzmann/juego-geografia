import random
def juego_geografia():
    """
    Juego de geografía donde el jugador responde preguntas sobre países y capitales.
    """
    preguntas = [{"pregunta": "¿Cual es la capital de Francia?", "respuesta": "paris"},
        {"pregunta": "¿En que continente esta Brasil?", "respuesta": "america"},
        {"pregunta": "¿Cual es el pais mas grande del mundo?", "respuesta": "rusia"},
        {"pregunta": "¿Cual es el río más largo del mundo?", "respuesta": "amazonas"},
        {"pregunta": "¿En que continente esta Egipto?", "respuesta": "africa"},
        {"pregunta": "¿Donde queda Barcelona?", "respuesta": "españa"},
        {"pregunta": "¿Cual es la capital de Alemania?", "respuesta": "berlin"}]
    print("\nBienvenido al juego de Geografía!")
    while True:
        pregunta_seleccionada = random.choice(preguntas)
        print("\n" + pregunta_seleccionada["pregunta"])
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == pregunta_seleccionada["respuesta"]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta_seleccionada['respuesta']}")
            continuar = input("¿Quieres responder otra pregunta? (si/no): ").strip().lower()
        if continuar != "si":
            print("¡Gracias por jugar! Hasta pronto.")
            break
juego_geografia()