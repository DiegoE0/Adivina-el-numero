import random

def Adivinar_el_numero():
    print("¡Bienvenido al juego de adivinar el número!")
    
    while True:
        try:
            max_rango = int(input("Por favor, introduce el número máximo del rango: "))
            if max_rango <= 1:
                print("El número máximo debe ser mayor que 1. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")
    
    max_intentos = max(1, max_rango // 20)
    print(f"Tendrás {max_intentos} intentos para adivinar el número.")
    
    numero_adivinar = random.randint(1, max_rango)
    
    vector_resultados = ["falló"] * max_rango
    vector_resultados[numero_adivinar - 1] = "acertó"
    
    intentos = 0
    while intentos < max_intentos:
        try:
            intento_usuario = int(input(f"Intento {intentos + 1}/{max_intentos}. Introduce un número entre 1 y {max_rango}: "))
            intentos += 1
            
            if intento_usuario < 1 or intento_usuario > max_rango:
                print(f"Por favor, introduce un número dentro del rango (1-{max_rango}).")
                continue
            
            if intento_usuario == numero_adivinar:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
            elif intento_usuario < numero_adivinar:
                print("El número a adivinar es mayor.")
            else:
                print("El número a adivinar es menor.")
        
        except ValueError:
            print("Entrada inválida. Eso cuenta como un intento.")
            intentos += 1
    
    if intentos == max_intentos and intento_usuario != numero_adivinar:
        print(f"Lo siento, has agotado todos los intentos. El número era {numero_adivinar}.")
    
    print("\nResultado final del vector:")
    print(vector_resultados)

Adivinar_el_numero()

