

def bienvenida():
 print()
 print()
 print("       d8888   888    888    .d88888b.     8888888b.      .d8888b.           d8888     8888888b.     .d88888b.")  
 print("      d88888   888    888   d88P   Y88b    888   Y88b    d88P  Y88b         d88888     888   Y88b   d88P   Y88b") 
 print("     d88P888   888    888   888     888    888    888    888    888        d88P888     888    888   888     888") 
 print("    d88P 888   8888888888   888     888    888   d88P    888              d88P 888     888    888   888     888") 
 print("   d88P  888   888    888   888     888    8888888P      888             d88P  888     888    888   888     888")
 print("  d88P   888   888    888   888     888    888 T88b      888    888     d88P   888     888    888   888     888") 
 print(" d8888888888   888    888   Y88b. .d88P    888  T88b     Y88b  d88P    d8888888888     888  .d88P   Y88b. .d88P") 
 print("d88P     888   888    888     Y88888P      888   T88b      Y8888P     d88P     888     8888888P       Y88888P")  
                 
def menu():
    print("")
    print("")
    print("")
    print("                                       *********MENÚ************")
    print("                                              1-Jugar")
    print("                                              2-Puntuaciones")
    print("                                              3-Salir")
    print("                                       *********MENÚ************")
    opcion= int(input("Elija una opción:  "))
    if opcion==1:
       print("no puedo importar monigote")
    elif opcion==2:
        print("alan 30000 puntos")
    if opcion==3:
        print("Saliste del juego")
        return False


    
bienvenida()

menu()