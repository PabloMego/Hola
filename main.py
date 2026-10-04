import tkinter as tk

def main():
    # Mensaje también en consola
    print("¡Hola! Bienvenido al programa.")

    # Crear la ventana gráfica
    root = tk.Tk()
    root.title("Saludo")
    root.geometry("420x240")
    root.resizable(False, False)
    root.configure(bg="#f4f6f8")

    # Centrar la ventana en la pantalla
    root.eval('tk::PlaceWindow . center')

    # Marco interior con padding
    frame = tk.Frame(root, bg="#f4f6f8", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Texto del saludo principal
    lbl_saludo = tk.Label(
        frame,
        text="¡Hola!",
        font=("Segoe UI", 26, "bold"),
        fg="#111827",
        bg="#f4f6f8"
    )
    lbl_saludo.pack(pady=(5, 5))

    # Mensaje o texto secundario
    lbl_subtexto = tk.Label(
        frame,
        text="¡Te damos la bienvenida al programa!",
        font=("Segoe UI", 11),
        fg="#4b5563",
        bg="#f4f6f8",
        wraplength=380,
        justify="center"
    )
    lbl_subtexto.pack(pady=(0, 20))

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
        lbl_subtexto.config(text=msg, fg="#059669")
        print(f"Usuario respondió ({contador['veces']}): {msg}")

    # Contenedor de botones
    btn_frame = tk.Frame(frame, bg="#f4f6f8")
    btn_frame.pack(pady=(5, 0))

    # Botón para decirle hola de vuelta
    btn_responder = tk.Button(
        btn_frame,
        text="¡Hola de vuelta! 👋",
        command=responder_hola,
        font=("Segoe UI", 10, "bold"),
        bg="#10b981",
        fg="white",
        activebackground="#059669",
        activeforeground="white",
        relief="flat",
        padx=16,
        pady=8,
        cursor="hand2"
    )
    btn_responder.pack(side="left", padx=6)

    # Botón para cerrar
    btn_cerrar = tk.Button(
        btn_frame,
        text="Cerrar",
        command=root.destroy,
        font=("Segoe UI", 10),
        bg="#e5e7eb",
        fg="#374151",
        activebackground="#d1d5db",
        activeforeground="#111827",
        relief="flat",
        padx=16,
        pady=8,
        cursor="hand2"
    )
    btn_cerrar.pack(side="left", padx=6)

    # Mantener la ventana abierta
    root.mainloop()

if __name__ == "__main__":
    main()
