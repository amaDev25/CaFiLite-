from menu import menu

def main():
    """
    funcion principal del programa
    """
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEl programa fue detenido por teclado")

if __name__ == "__main__":
    main()