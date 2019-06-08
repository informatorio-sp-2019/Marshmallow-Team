

from os import system
def pantalla_puntuacion():
    system ("cls")
    print(""".______    __    __  .__   __. .___________. __    __       ___        ______  __    ______   .__   __. 
    |   _  \  |  |  |  | |  \ |  | |           ||  |  |  |     /   \      /      ||  |  /  __  \  |  \ |  | 
    |  |_)  | |  |  |  | |   \|  | `---|  |----`|  |  |  |    /  ^  \    |  ,----'|  | |  |  |  | |   \|  | 
    |   ___/  |  |  |  | |  . `  |     |  |     |  |  |  |   /  /_\  \   |  |     |  | |  |  |  | |  . `  | 
    |  |      |  `--'  | |  |\   |     |  |     |  `--'  |  /  _____  \  |  `----.|  | |  `--'  | |  |\   | 
    | _|       \______/  |__| \__|     |__|      \______/  /__/     \__\  \______||__|  \______/  |__| \__| 
                                                                                                            """)
    while True:
        opcion= input("presione 1 para Volver:  ")
        if opcion=="1":
            from H1_menu_principal import menu, bienvenida
            H1_menu_principal.bienvenita()
            H1_menu_principal.menu()
            
        elif opcion!="1":
            continue
    

pantalla_puntuacion()
