import tkinter as tk

def main():
    # Mensaje también en consola
    print("¡Hola! Bienvenido al programa.")

    # Crear la ventana gráfica
    root = tk.Tk()
    root.title("Saludo")
    root.geometry("380x200")
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
    lbl_saludo.pack(pady=(10, 5))

    # Mensaje o texto secundario
    lbl_subtexto = tk.Label(
        frame,
        text="¡Te damos la bienvenida al programa!",
        font=("Segoe UI", 11),
        fg="#4b5563",
        bg="#f4f6f8"
    )
    lbl_subtexto.pack(pady=(0, 20))

    # Botón de aceptar/cerrar
    btn_cerrar = tk.Button(
        frame,
        text="Aceptar",
        command=root.destroy,
        font=("Segoe UI", 10, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=6,
        cursor="hand2"
    )
    btn_cerrar.pack()

    # Mantener la ventana abierta
    root.mainloop()

if __name__ == "__main__":
    main()
