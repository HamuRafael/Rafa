def imc(a,p):
    a= float(a)
    p= float(p)
    calculo = p/(a**2)
    calculo = round(calculo,2)
    if calculo < 18.6:
        return(f'Abaixo do peso,IMC = {calculo}')
    elif calculo > 18.6 and calculo < 24.9:
         return(f'Peso Normal, IMC = {calculo}')
    elif calculo >= 25 and calculo <= 29.9:
         return(f'Sobrepeso, IMC = {calculo}')
    elif calculo> 29.9:
        return('Obesidade, IMC = {calculo}')

    
    
