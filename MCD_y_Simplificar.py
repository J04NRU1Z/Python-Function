def CalculoDelMCD(a: int, b: int)-> int:

    """
    Determina el valor máximo común divisor de los dos
    parámetros a y b
    Args:
    a (int) [in] Primer valor
    b (int) [in] Segundo valor
    Return:
    int Valor del máximo común divisor
    """
    while a != 0:
        aux = a
        a = b % a
        b = aux
    return b 

def Simplificar(a: int, b: int) -> (int, int):
    """
    Simplifica numerador y denominador por su máximo común divisor, hasta que este sea 1
    
    Args:
    a (int) [in] Numerador
    b (int) [in] Denominador
    
    Return:
    int Numerador (simplificado si es posible)
    int Denominador (simplificado si es posible)
    """
    
    div = CalculoDelMCD(a, b)
    
    while div != 1:
        print(a, b)
        a = a // div
        b = b // div
        div = CalculoDelMCD(a, b)
        
    return a, b

