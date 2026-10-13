"""Calculadora educativa de préstamos a tipo fijo. Solo usa Python estándar."""

import math


def leer_numero(pregunta, minimo, maximo):
    """Acepta punto o coma decimal, pero no separadores de miles."""
    while True:
        texto = input(pregunta).strip().replace(",", ".")
        try:
            valor = float(texto)
            if math.isfinite(valor) and minimo <= valor <= maximo:
                return valor
        except ValueError:
            pass
        print(f"Escribe un número entre {minimo:g} y {maximo:g}, sin miles.")


def calcular(capital, interes_anual, meses):
    """Sistema francés: cuota mensual constante; TIN anual / 12."""
    if not math.isfinite(capital) or not 0 < capital <= 100_000_000:
        raise ValueError("Capital fuera de rango.")
    if not math.isfinite(interes_anual) or not 0 <= interes_anual <= 100:
        raise ValueError("Interés fuera de rango.")
    if not isinstance(meses, int) or not 1 <= meses <= 600:
        raise ValueError("El plazo debe ser de 1 a 600 meses enteros.")
    tasa = interes_anual / 100 / 12
    if tasa == 0:
        cuota = capital / meses
    else:
        # log1p y expm1 evitan perder precisión con intereses muy pequeños.
        divisor = -math.expm1(-meses * math.log1p(tasa))
        cuota = capital * tasa / divisor
    total = cuota * meses
    intereses = max(0.0, total - capital)
    return cuota, total, intereses


def euros(cantidad):
    texto = f"{cantidad:,.2f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".") + " €"


def main():
    print("\nMI CALCULADORA DE PRÉSTAMOS")
    print("Cuota mensual con interés fijo. No necesita instalar paquetes.")
    print("Sin comisiones, seguros ni otros gastos; no calcula la TAE.")
    print("Escribe 150000, no 150.000. Para decimales: 3,5 o 3.5.\n")
    while True:
        capital = leer_numero("Importe del préstamo (€): ", 0.01, 100_000_000)
        interes = leer_numero("Interés anual fijo, TIN (%): ", 0, 100)
        while True:
            plazo = leer_numero("Plazo en meses (25 años = 300): ", 1, 600)
            if plazo.is_integer():
                meses = int(plazo)
                break
            print("El plazo debe ser un número entero de meses.")
        cuota, total, intereses = calcular(capital, interes, meses)
        print("\nRESULTADO ORIENTATIVO")
        print(f"Cuota mensual:     {euros(cuota)}")
        print(f"Total a pagar:     {euros(total)}")
        print(f"Intereses totales: {euros(intereses)}")
        print("Total calculado con la cuota sin redondear.")
        print("El banco puede ajustar los céntimos y la última cuota.\n")
        if input("¿Otro cálculo? (s/n): ").strip().lower() != "s":
            print("¡Hasta la próxima!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma cerrado.")
