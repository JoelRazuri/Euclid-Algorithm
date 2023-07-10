"""
Algoritmo de Euclides
    
    a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
    números 𝑛 y 𝑚, dado por los siguientes pasos.
    
        1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
        2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
        3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.
    
    b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de números:
    (15, 9); (9, 15); (10, 8); (12, 6).
"""

def algoritmo_Euclides(m1,n1):

    n=n1
    m=m1
    r = m%n

    while r!=0:
        m=n
        n=r
        r = m%n
    
    print(f"El mcd entre {m1} y {n1} es: {n}")

algoritmo_Euclides(15, 9)
algoritmo_Euclides(9, 15)
algoritmo_Euclides(10, 8)
algoritmo_Euclides(12, 6)
