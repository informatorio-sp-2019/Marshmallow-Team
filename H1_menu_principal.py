import pantalla_del_juego
from colorama import Fore, init
import os
init(autoreset=True)

def bienvenida():
    os.system("cls")
    print()
    print()
    # print(Fore.CYAN+"       d8888   888    888    .d88888b.     8888888b.      .d8888b.           d8888     8888888b.     .d88888b.")  
    # print(Fore.CYAN+"      d88888   888    888   d88P   Y88b    888   Y88b    d88P  Y88b         d88888     888   Y88b   d88P   Y88b") 
    # print(Fore.CYAN+"     d88P888   888    888   888     888    888    888    888    888        d88P888     888    888   888     888") 
    # print(          "    d88P 888   8888888888   888     888    888   "+Fore.YELLOW+"d88P    888"+Fore.RESET+"              d88P 888     888    888   888     888") 
    # print(          "   d88P  888   888    888   888     888    888888"+Fore.YELLOW+"8P      888"+Fore.RESET+"             d88P  888     888    888   888     888")
    # print(Fore.CYAN+"  d88P   888   888    888   888     888    888 T88b      888    888     d88P   888     888    888   888     888") 
    # print(Fore.CYAN+" d8888888888   888    888   Y88b. .d88P    888  T88b     Y88b  d88P    d8888888888     888  .d88P   Y88b. .d88P") 
    # print(Fore.CYAN+"d88P     888   888    888     Y88888P      888   T88b      Y8888P     d88P     888     8888888P       Y88888P")  
    print(Fore.CYAN+" "*20+" █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ ")
    print(Fore.CYAN+" "*20+"██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗")
    print(          " "*20+"███████║███████║██║   ██║█████"+Fore.YELLOW+"█╔╝██║"+Fore.RESET+"     ███████║██║  ██║██║   ██║")
    print(          " "*20+"██╔══██║██╔══██║██║   ██║██╔══"+Fore.YELLOW+"██╗██║"+Fore.RESET+"     ██╔══██║██║  ██║██║   ██║")
    print(Fore.CYAN+" "*20+"██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝")
    print(Fore.CYAN+" "*20+"╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝")

                 
def menu():
    tt="MENU"
    print("\n"*3+" "*20+tt.center(60,"*"))
    print(" "*46+"1-Jugar\n"+" "*46+"2-Puntuaciones\n"+" "*46+"3-Salir")
    print(" "*20+tt.center(60,"*"))
    opcion= input("Elija una opción:  ")
    if opcion=="1":
       pantalla_del_juego.pantalla(3,0)
    elif opcion=="2":
        import pantalla_puntuacion
    elif opcion=="3":
        print("\n Saliste del juego")
        return False
    else:
        print("\n   Opcion incorrecta")
        input()
        iniciar()

def iniciar():
    
    bienvenida()

    menu()

iniciar()