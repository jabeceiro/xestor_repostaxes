"""
Módulo principal da aplicación de xestión de repostaxes.
Encárgase de:
- Cargar os datos almacenados en data/datos.json ao iniciar a aplicación.
- Mostrar o menú principal e xestionar a interacción co usuario.
- Coordinar as chamadas ás funcións de entrada/saída (io.py) e á lóxica de negocio (funciones.py).
- Manter o estado de cambios pendentes mediante a bandeira 'datos_modificados'.
- Gardar automaticamente os datos ao saír se existen modificacións sen gardar.
"""

from app import io


def main():
    """
    Punto de entrada da aplicación.
    Xestiona o menú principal e as accións do usuario así como tamén 
    coordinar as operacións de carga, modificación e gardado de datos.
    """
    repostaxes = io.cargar_repostaxes()
    datos_modificados = False
    
    while True:
        print()     # liña en branco de separación
        io.mostrar_menu(datos_modificados)
        opcion = io.pedir_opcion_menu()
        
        match opcion:
            case 1:
                io.rexistrar_repostaxe_desde_input(repostaxes)
                datos_modificados = True
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
                datos_modificados = False
                print("\n✅ Datos gardados.")
            case 0:
                # Gardado automático ao saír 
                if datos_modificados: 
                    print("\nGardando cambios antes de saír...") 
                    io.gardar_repostaxes(repostaxes) 
                    print("✅ Datos gardados correctamente.")
                    
                print("\nSaíndo da aplicación...")
                print("Ata logo!")
                break
            case _:
                print("\n❌ Opción non válida.")
                print("Introduce un número do 0 ao 6.",sep="\n")


if __name__ == "__main__":
    main()