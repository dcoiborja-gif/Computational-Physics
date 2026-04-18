import numpy as np
import matplotlib.pyplot as plt

def gaussiana(x, mu=0, sigma=1, amplitud=1):
    """
    Calcula una distribución gaussiana (normal).
    
    Parámetros:
    -----------
    x : array-like
        Valores en el eje x
    mu : float
        Media (centro) de la gaussiana
    sigma : float
        Desviación estándar (ancho)
    amplitud : float
        Amplitud máxima
    
    Retorna:
    --------
    array
        Valores de la gaussiana
    """
    return amplitud * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))


if __name__ == "__main__":
    # Crear datos
    x = np.linspace(-5, 5, 1000)
    y = gaussiana(x, mu=0, sigma=1, amplitud=1)
    
    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='Gaussiana(μ=0, σ=1)')
    plt.fill_between(x, y, alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución Gaussiana')
    plt.legend()
    plt.tight_layout()
    plt.savefig('gaussiana.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("Gráfica guardada como 'gaussiana.png'")
