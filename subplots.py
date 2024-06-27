import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return None

def graficar_distribuciones(df):
    # Calcular porcentajes para las distribuciones
    porcentaje_anemicos = [53.1, 46.9]
    porcentaje_diabeticos = [58.0, 42.0]
    porcentaje_fumadores = [69.9, 30.1]
    porcentaje_muertos = [72.8, 27.2]

    # Configurar los subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Distribuciones', fontsize=16)

    # Graficar la distribución de anémicos
    axs[0, 0].pie(porcentaje_anemicos, labels=['No anémicos', 'Anémicos'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'], startangle=140)
    axs[0, 0].set_title('Distribución de Anémicos')

    # Graficar la distribución de diabéticos
    axs[0, 1].pie(porcentaje_diabeticos, labels=['No diabéticos', 'Diabéticos'], autopct='%1.1f%%', colors=['lightgreen', 'gold'], startangle=140)
    axs[0, 1].set_title('Distribución de Diabéticos')

    # Graficar la distribución de fumadores
    axs[1, 0].pie(porcentaje_fumadores, labels=['No fumadores', 'Fumadores'], autopct='%1.1f%%', colors=['lightsalmon', 'lightseagreen'], startangle=140)
    axs[1, 0].set_title('Distribución de Fumadores')

    # Graficar la distribución de muertos
    axs[1, 1].pie(porcentaje_muertos, labels=['Vivos', 'Muertos'], autopct='%1.1f%%', colors=['lightpink', 'lightgrey'], startangle=140)
    axs[1, 1].set_title('Distribución de Muertos')

    plt.tight_layout()
    plt.show()

def main():
    nombre_archivo = 'categorias.csv'
    
    # Cargar datos desde el archivo CSV
    df = cargar_datos(nombre_archivo)
    
    if df is not None:
        # Graficar distribuciones
        graficar_distribuciones(df)

if __name__ == '__main__':
    main()
