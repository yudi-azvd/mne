def ea(x: float, x_prev: float)-> float:
    '''Erro aproximado relativo'''
    return (x - x_prev)/x


def ea_alt(x1: float, x2: float):
    '''Erro aproximado relativo percentual. Forma alternativa: x1 < x2
    
    ea = | (x2 - x1) / (x2 + x1) | * 100 %
    '''
    return abs((x2 - x1) / (x2 + x1))*100

