def Potencia(Base: int, Exponente: int) -> int:
    """
    Determina el valor de la potencia de los dos
    parámetros
    Args:
    Base (int) [in] Base
    Exponente (int) [in] Exponente
    Return:
    int Valor de la potencia
    """
    if Exponente % 2 == 0 and Exponente > 0:
        res = Potencia(Base, Exponente // 2) * Potencia(Base, Exponente // 2)
    elif Exponente % 2 == 1 and Exponente > 0:
        res = Base * Potencia(Base, Exponente - 1)
    else:
        res = 1
    return res
        
