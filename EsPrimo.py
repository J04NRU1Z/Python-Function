def EsPrimo(numero: int)-> bool:
    """
    Determina si un número es primo o no basandose en si se puede dividir por
    los números más bajos que él
    Args:
        numero (int) [in] número a comprobar
    Return:
        bool Respuesta a la pregunta si es primo o no
    """
    div = 2
    primo = True
    while div < numero:
        if numero % div == 0 or numero < 2:
            primo = False
        div += 1
    return primo
        
