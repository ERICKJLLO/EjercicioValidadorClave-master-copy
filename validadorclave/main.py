# main.py

from validador import Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto
from errores import (
    NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,
    NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError
)

def main():
    # Crear instancias del validador con diferentes reglas
    validador_ganimedes = Validador(ReglaValidacionGanimedes())
    validador_calisto = Validador(ReglaValidacionCalisto())

    clave = input("Introduce una clave para validar: ")

    # Validar con regla Ganimedes
    try:
        if validador_ganimedes.es_valida(clave):
            print("La clave es válida según la regla de Ganimedes.")
    except (NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,
            NoTieneNumeroError, NoTieneCaracterEspecialError) as e:
        print(f"Error de validación con la regla de Ganimedes: {str(e)}")

    # Validar con regla Calisto
    try:
        if validador_calisto.es_valida(clave):
            print("La clave es válida según la regla de Calisto.")
    except (NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,
            NoTieneNumeroError, NoTienePalabraSecretaError) as e:
        print(f"Error de validación con la regla de Calisto: {str(e)}")

if __name__ == "__main__":
    main()
