import os
import sys
import time
from colorama import init, Fore, Style, Back

def limpiarPantalla():
    """Limpia la consola. Funciona en Windows ('cls') y Unix/Linux/macOS ('clear')."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(mensaje="Presione Enter para continuar..."):
    """Muestra un mensaje y espera a que el usuario presione Enter."""
    input(f"{Fore.CYAN}{mensaje}{Style.RESET_ALL}")