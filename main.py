from app.io import (
    mostrar_menu,
    pedir_opcion,
    rexistrar_repostaxe_desde_input,
    mostrar_historial,
    mostrar_gasto_total,
    mostrar_consumo_medio,
    cargar_repostaxes,
    gardar_repostaxes
)


def main():
    repostaxes = cargar_repostaxes()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            rexistrar_repostaxe_desde_input(repostaxes)
        elif opcion == 2:
            mostrar_historial(repostaxes)
        elif opcion == 3:
            mostrar_gasto_total(repostaxes)
        elif opcion == 4:
            mostrar_consumo_medio(repostaxes)
        elif opcion == 5:
            gardar_repostaxes(repostaxes)
            print("Datos gardados.")
        elif opcion == 6:
            print("Saíndo...")
            break
        else:
            print("Opción non válida.")


if __name__ == "__main__":
    main()
