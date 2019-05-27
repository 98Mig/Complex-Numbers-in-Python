#Complexos
#Construtor - Real -> Complexo
def cria_complexo(a,b): #Cria os complexos, que serão representados por um dicionário.
    if isinstance(a,int) and isinstance(b,int):
        return {'r': a, 'i': b}
    else:
        raise ValueError ('cria_complexo: argumento errado')

#Seletores - Complexo -> Real
def parte_real(c): #Seleciona a parte real - r - do complexo.
    return c['r']

def parte_imaginaria(c): #Seleciona a parte imaginaria - i - do complexo.
    return c['i']

#Testes - Universal -> Lógico e Complexos -> Lógico
def e_complexo(arg): #Verifica se o argumento dado é mesmo um complexo.
    if len(arg)==2 and isinstance(arg,dict) and isinstance(parte_real(c),int) and isinstance(parte_imaginaria(c),int):
        return True
    else:
        return False

def e_imaginario_puro(c): #Verifica se o número é um imaginário puro.
    if parte_real(c)==0:
        return True
    else:
        return False

def e_real(c): #Verifica se o número é um real.
    if parte_imaginaria(c)==0:
        return True
    else:
        return Falsereal

def complexos_iguais(c1,c2): #Verifica se dois complexos são iguais.
    if parte_real(c1)==parte_real(c2) and parte_imaginaria(c1)==parte_imaginaria(c2):
        return True
    else:
        return False

#Representação do complexo
def representa_complexo(c): #Faz a representação do complexo na sua aparição normal do nosso dia-a-dia.
    if e_real(c):
        print(c['r'])
    elif e_imaginario_puro(c):
        print(c['i'],'i')
    else:
        print(c['r'],'+',c['i'],'i')

#Operações com complexos
def conjugado(c): #Faz o conjugado de um complexo.
    return {'r': parte_real(c), 'i': -parte_imaginaria(c)}

def soma_complexos(c1,c2,a): #Faz a soma entre dois complexos.
    if a==0: #O valor de a corresponde a uma flag que, se for 0, irá fazer uma soma, e se for 1, faz uma subtração.
        real_c3=c1['r']+c2['r']
        imag_c3=c1['i']+c2['i']
        return {'r': real_c3, 'i': imag_c3}
    elif a==1: #O valor de a corresponde a uma flag que, se for 0, irá fazer uma soma, e se for 1, faz uma subtração.
        real_c3=c1['r']-c2['r']
        imag_c3=c1['i']-c2['i']
        return {'r': real_c3, 'i': imag_c3}

def multiplica_complexos(c1,c2): #Faz a multiplicação de dois complexos. 
    if parte_imaginaria(c2)==-(parte_imaginaria(c1)) or parte_imaginaria(c1)==-(parte_imaginaria(c2)): #Verifica se um dos complexos é o conjugado do outro - se for, aplica a fórmula a**2+b**2.
        a=(parte_real(c1)**2)
        b=(parte_imaginaria(c1)**2)
        return a+b
    else: #Se um dos complexos não for o conjugador do outro, aplica a fórmula (ac-bd)+(ad+db)i.
        real_c3=(parte_real(c1)*parte_real(c2))-(parte_imaginaria(c1)*parte_imaginaria(c2))
        imag_c3=(parte_real(c1)*parte_imaginaria(c2))+(parte_imaginaria(c1)*parte_real(c2))
    return {'r': real_c3, 'i': imag_c3}

def divisao_complexos(c1,c2): #Efetua a divisão de complexos, aplica a fórmula z1/z2=(z1*conjugado(z2))/(z2*conjugado(z2))
    denominador=multiplica_complexos(c1,conjugado(c2)) #Multiplicação entre z1 e o conjugado de z2.
    numerador=multiplica_complexos(c2,conjugado(c2)) #Multiplicação entre z2 e o seu conjugador.
    p_real=denominador['r']/numerador #Divisão entre o real que resultou da multiplicação do denominador pelo numerador.
    p_imag=denominador['i']/numerador #Divisão entre o imaginario que resultou da multiplicação do denominador pelo numerador.
    return {'r': p_real, 'i': p_imag}
