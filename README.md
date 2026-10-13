# Mi calculadora de préstamos

Un programa educativo en español para calcular la cuota mensual de un préstamo o una hipoteca a interés fijo, con importes en euros.

## Requisitos

Python 3.10 o posterior. Solo usa la biblioteca estándar: no hay que instalar paquetes, no pide claves y no usa internet.

## Cómo ejecutarlo

Abre PowerShell en la carpeta donde está `main.py` y escribe:

```powershell
python main.py
```

Introduce el capital sin separadores de miles, el interés nominal anual (TIN) y el plazo en meses. Puedes usar coma o punto decimal. Para 25 años, escribe 300 meses.

## Ejemplo

- Capital: `150000`
- TIN anual: `3`
- Meses: `300`
- Cuota: **711,32 € al mes**
- Total teórico: **213.395,09 €**
- Intereses: **63.395,09 €**

## Qué calcula y qué no

Usa el sistema francés de cuota constante, con tipo mensual igual al TIN anual dividido entre 12. Admite el 0 % de interés. El total se calcula antes de redondear la cuota a céntimos, por lo que puede diferir de multiplicar la cuota mostrada por los meses.

No incluye comisiones, seguros, impuestos ni cambios de tipo. No calcula la TAE. Es una estimación educativa, no una oferta bancaria ni asesoramiento financiero.

## Límites

Importes entre 0,01 y 100.000.000 €, TIN entre 0 y 100 % y plazo de 1 a 600 meses enteros. Pulsa Ctrl+C para salir en cualquier momento.

## Sobre este proyecto

Primer ejercicio para practicar Python y subir archivos a GitHub. Código preparado con ayuda de IA.
