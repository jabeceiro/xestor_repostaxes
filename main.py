"""
Módulo principal da aplicación de xestión de repostaxes.
Encárgase de cargar os datos, mostrar o menú e xestionar as opcións do usuario.
"""

from app import io


def main():
    """
    Punto de entrada da aplicación.
    Xestiona o menú principal e as accións do usuario.
    """
    repostaxes = io.cargar_repostaxes()

    while True:
        print()     # liña en branco de separación
        io.mostrar_menu()
        opcion = io.pedir_opcion_menu()
        
        match opcion:
            case 1:
                io.rexistrar_repostaxe_desde_input(repostaxes)
            case 2:
                io.mostrar_historial(repostaxes)
            case 3:
                io.mostrar_gasto_total(repostaxes)
            case 4:
                io.mostrar_consumo_medio(repostaxes)
            case 5:
                io.mostrar_resumo(repostaxes)   
            case 6:
                io.gardar_repostaxes(repostaxes)
                print("\n✅ Datos gardados.")
            case 0:
                print("\nSaíndo da aplicación...")
                print("Ata logo!")
                break
            case _:
                print("\n❌ Opción non válida.")
                print("Introduce un número do 0 ao 6.",sep="\n")


if __name__ == "__main__":
    main()