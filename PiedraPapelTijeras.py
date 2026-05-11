import random

def piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    
    eleccion_usuario = input("Elige piedra,papel o tijeras:").lower()
    
    eleccion_pc = random.choice(opciones)
    
    print(f"PC eligió: {eleccion_pc}")
    
    if eleccion_usuario == eleccion_pc:
        print("Es un empate")
    elif(eleccion_usuario == "piedra" and eleccion_pc == "tijeras") or \
        (eleccion_usuario == "papel" and eleccion_pc == "piedra") or \
        (eleccion_usuario == "tijeras" and eleccion_pc == "papel"):
        print("!Ganaste")
    else:
        print("Perdiste, suerte la proxima vez. Deposita 500 pesos en la mesa")
        
piedra_papel_tijeras()