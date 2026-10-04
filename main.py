import os
import tkinter as tk
from PIL import Image, ImageTk

# Paleta de colores personalizada
COLOR_PRIMARIO = "#7d1212"      # Color Primario (Rojo oscuro / Granate)
COLOR_SECUNDARIO = "#cd0e0e"    # Color Secundario (Rojo vibrante)
COLOR_ACENTO = "#cdfeeb"        # Color de Acento (Menta suave)

# Ruta del logo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "logo.jpg")

def main():
    # Mensaje en consola
    print("¡Hola! Bienvenido al programa.")

    # Crear la ventana gráfica
    root = tk.Tk()
    root.title("Saludo")
    root.geometry("420x430")
    root.resizable(False, False)
    root.configure(bg=COLOR_PRIMARIO)

    # Centrar la ventana en la pantalla
    root.eval('tk::PlaceWindow . center')

    # Marco interior con padding
    frame = tk.Frame(root, bg=COLOR_PRIMARIO, padx=20, pady=15)
    frame.pack(expand=True, fill="both")

    # Cargar y mostrar el logo
    logo_photo = None
    if os.path.exists(LOGO_PATH):
        try:
            img = Image.open(LOGO_PATH)
            # Redimensionar conservando proporción estética
            img = img.resize((120, 130), Image.Resampling.LANCZOS)
            logo_photo = ImageTk.PhotoImage(img)

            # Establecer también como icono de la ventana / barra de tareas
            root.iconphoto(False, logo_photo)

            lbl_logo = tk.Label(
                frame,
                image=logo_photo,
                bg=COLOR_PRIMARIO
            )
            lbl_logo.image = logo_photo  # Mantener referencia
            lbl_logo.pack(pady=(5, 8))
        except Exception as e:
            print(f"No se pudo cargar el logo: {e}")

    # Texto del saludo principal con el color de acento
    lbl_saludo = tk.Label(
        frame,
        text="¡Hola!",
        font=("Segoe UI", 26, "bold"),
        fg=COLOR_ACENTO,
        bg=COLOR_PRIMARIO
    )
    lbl_saludo.pack(pady=(2, 4))

    # Mensaje o texto secundario
    lbl_subtexto = tk.Label(
        frame,
        text="¡Te damos la bienvenida al programa!",
        font=("Segoe UI", 11),
        fg="#ffffff",
        bg=COLOR_PRIMARIO,
        wraplength=370,
        justify="center"
    )
    lbl_subtexto.pack(pady=(0, 16))

    # Lógica para responder el saludo
    respuestas = [
        "¡Qué alegría! ¡Hola a ti también! 😊",
        "¡Hola otra vez! Qué gusto saludarte 👋",
        "¡Qué amable eres! Me alegra que respondas 😄",
        "¡Saludos! Espero que tengas un excelente día ✨",
    ]
    contador = {"veces": 0}

    def responder_hola():
        msg = respuestas[contador["veces"] % len(respuestas)]
        contador["veces"] += 1
        # Al responder, el texto resalta con el color de acento
        lbl_subtexto.config(text=msg, fg=COLOR_ACENTO, font=("Segoe UI", 11, "bold"))
        print(f"Usuario respondió ({contador['veces']}): {msg}")

    # Contenedor de botones
    btn_frame = tk.Frame(frame, bg=COLOR_PRIMARIO)
    btn_frame.pack(pady=(5, 5))

    # Botón con Color Secundario (#cd0e0e)
    btn_responder = tk.Button(
        btn_frame,
        text="¡Hola de vuelta! 👋",
        command=responder_hola,
        font=("Segoe UI", 10, "bold"),
        bg=COLOR_SECUNDARIO,
        fg="white",
        activebackground="#a50a0a",
        activeforeground=COLOR_ACENTO,
        relief="flat",
        padx=18,
        pady=8,
        cursor="hand2"
    )
    btn_responder.pack(side="left", padx=8)

    # Botón secundario para cerrar
    btn_cerrar = tk.Button(
        btn_frame,
        text="Cerrar",
        command=root.destroy,
        font=("Segoe UI", 10, "bold"),
        bg="#5a0b0b",
        fg=COLOR_ACENTO,
        activebackground="#420808",
        activeforeground="white",
        relief="flat",
        padx=18,
        pady=8,
        cursor="hand2"
    )
    btn_cerrar.pack(side="left", padx=8)

    # Mantener la ventana abierta
    root.mainloop()

if __name__ == "__main__":
    main()
