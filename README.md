
# Conversor de Bases Numéricas

## Descripción

Este programa es un conversor de bases numéricas construido con Python utilizando la biblioteca Tkinter para la interfaz gráfica. El programa permite convertir un número de una base original a otra base deseada. Soporta bases numéricas desde la base 2 (binario) hasta la base 36 (alfanumérico).

## Fórmulas Utilizadas

Para la conversión de la parte entera del número se utiliza la fórmula de división sucesiva:

\[
\text{Resultado} = \left( \text{Parte entera del cociente} \right)_{\text{base destino}}
\]

Para la conversión de la parte decimal se utiliza la fórmula de multiplicación sucesiva:

\[
\text{Resultado} = \left( \text{Parte entera del producto} \right)_{\text{base destino}}
\]

## Requisitos

- Python 3.x
- Tkinter (Normalmente viene preinstalado con Python)

## Cómo Usar

1. **Clonar el Repositorio**: Primero, clona el repositorio a tu máquina local usando `git clone`.

2. **Ejecutar el Programa**: Abre una terminal y navega hasta el directorio donde se encuentra el archivo del programa. Ejecuta el programa usando `python nombre_del_archivo.py`.

3. **Interfaz Gráfica**: Se abrirá una ventana con la interfaz gráfica del programa.

4. **Ingresar Datos**: 
    - **Número**: Ingresa el número que deseas convertir.
    - **Base Original**: Ingresa la base numérica del número que has introducido.
    - **Base a Convertir**: Ingresa la base numérica a la que deseas convertir el número.

5. **Convertir**: Haz clic en el botón "Convertir".

6. **Resultado**: El resultado se mostrará en la parte inferior de la ventana.

## Ejemplo

Si deseas convertir el número `101.101` de base 2 a base 10:

- **Número**: 101.101
- **Base Original**: 2
- **Base a Convertir**: 10

Haz clic en "Convertir" y obtendrás el resultado `5.625`.


