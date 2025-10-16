import matplotlib.pyplot as plt
import random

def simular_maquina_galton(num_canicas=3000, niveles=12):
    """
    Simula una máquina de Galton con el número especificado de canicas y niveles.
    
    Args:
        num_canicas (int): Número de canicas a simular (por defecto 3000)
        niveles (int): Número de niveles de obstáculos (por defecto 12)
    
    Returns:
        list: Lista con la cantidad de canicas en cada contenedor
    """
    
    contenedores = [0] * (niveles + 1)
    
    for canica in range(num_canicas):
        
        posicion = 0
        
        
        for nivel in range(niveles):
            
            direccion = random.choice([-0.5, 0.5])
            posicion += direccion
        
        
        indice = int(posicion + niveles/2)
        contenedores[indice] += 1
    
    return contenedores

def graficar_histograma(contenedores):
    """
    Crea un histograma con los resultados de la máquina de Galton.
    
    Args:
        contenedores (list): Lista con la cantidad de canicas en cada contenedor
    """
    
    plt.figure(figsize=(12, 6))
    
    
    contenedor_nums = list(range(len(contenedores)))
    
    
    plt.bar(contenedor_nums, contenedores, color='skyblue', edgecolor='black', alpha=0.7)
    
    
    plt.title('Distribución de Canicas en la Máquina de Galton', fontsize=16, fontweight='bold')
    plt.xlabel('Contenedores', fontsize=12)
    plt.ylabel('Número de Canicas', fontsize=12)
    
    
    plt.grid(axis='y', alpha=0.3)
    
    
    for i, valor in enumerate(contenedores):
        plt.text(i, valor + 10, str(valor), ha='center', va='bottom')
    
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Simulando máquina de Galton con 3000 canicas y 12 niveles...")
    
    
    resultados = simular_maquina_galton(3000, 12)
    
    
    print("\nResultados por contenedor:")
    for i, cantidad in enumerate(resultados):
        print(f"Contenedor {i}: {cantidad} canicas")
    
    
    graficar_histograma(resultados)