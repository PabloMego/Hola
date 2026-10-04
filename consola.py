# Versión simple para consola / terminal

print("¡Hola! Bienvenido al programa.")
respuesta = input("\nDile hola al programa (escribe aquí): ")

if "hola" in respuesta.lower():
    print("¡Qué alegría! ¡Hola de vuelta a ti también! 😊👋")
else:
    print(f"¡Mucho gusto! Dijiste: '{respuesta}'. ¡Saludos! ✨")

# input() evita que la ventana de la consola se cierre inmediatamente en Windows
input("\nPresiona Enter para salir...")
