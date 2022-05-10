#TESTES DE DEF PARA CÓDIGO PROJETO IMC

#Subprograma para apresentar o programa
def apresentacao():
    print("PROGRAMA PARA CALCULAR IMC E QUANTIDADE DE CALORIAS!")
    print("\n  Se desejar sair do programa a qualquer momento é só digitar 'QUIT'")

#Subprograma para solicitar a digitação do Peso e da Altura para calcular o IMC 
def solicitacaoPesoAltura (mensagem, variavel):
    digitouErrado = True
    while digitouErrado:
        try:
            digitar = input("\n>>> " + mensagem).upper()
            if digitar == 'QUIT':
                print("\nObrigado por utilizar o programa!")
                exit()

            digitar = float(digitar)
            if digitar <= 0:
                print(variavel + " não pode ser negativo ou igual a zero. Tente novamente...")

            else:
                digitouErrado = False

        except ValueError:
            print("\n  Somente números podem ser digitados. Tente novamente...")
    
    return digitar


# Subprograma para Calculo do IMC 
def calculoIMC(peso, altura):    
    imc = peso/altura**2
    imc = round(imc, 2)
    print("\n  O seu IMC é ",imc)

    if imc < 16:
        print ("\n  Você está com magreza classe III.")
    elif imc >= 16 and imc <= 16.9:
        print ("\n  Você está com mafreza classe II.")
    elif imc >= 17 and imc < 18.4:
        print ("\n  Você está com magreza classe I")
    elif imc >= 18.5 and imc <= 24.9:
        print ("\n  Você está no peso ideal.")
    elif imc >= 25 and imc <= 29.9:
        print ("\n  Você está com sobrepeso.")
    elif imc >= 30 and imc <= 34.9:
        print ("\n  Você está com obesidade classe I.")
    elif imc >= 35 and imc <= 39.9:
        print ("\n  Você está com obesidade classe II.")
    elif imc >= 40:
        print ("\n  Você está com obesidade classe III.")

    return imc

#Subprograma para solicitar a digitação da idade para o cálculo da Taxa Basal e posterior cálculo das Calorias 
def solicitacaoIdade():
    digitouErrado = True
    while digitouErrado:
        try:
            idade = input("\n>>> Qual sua idade? ")
            if idade == 'QUIT':
                print("\nObrigado por utilizar o programa!")
                exit()
            
            idade = float(idade)
            if idade <= 0:
                print("\n  A idade não pode ser negativa ou igual a zero. Digite novamente...")

            elif  idade < 19 or idade > 60:
                print("\n  ATENÇÃO: Esse programa é indicado para pessoas de faixa etária entre 18 anos e 60 anos.", \
                     "Com a idade inserida os cálculos finais podem dar errado.")
                digitouErrado = False
            else: 
                digitouErrado = False

        except ValueError:
            print("\n  Somente números podem ser digitados. Tente novamente...")

    return idade

#Subprograma para solicitar o sexo do usuário para cálculo da Taxa de Metabolismo Basal e posterior cálculo das Calorias
def solicitacaoSexo():
    digitouErrado = True
    while digitouErrado:
        try:
            sexo = input("\n>>> Qual é seu sexo biológico (Digite M para masculino ou F para feminino)? ").upper()

            if sexo == 'QUIT':
                print("\nObrigado por utilizar esse programa!")
                exit()

            elif sexo == 'F':
                digitouErrado = False
            elif sexo == 'M':
                digitouErrado = False
            else:
                print("\n  Você deve digitar apenas M ou F. Digite novamente...")
                digitouErrado = True
        
        except ValueError:
            print("\n  Somente números podem ser digitados. Tente novamente...")
    
    return sexo

#Subprograma para mostrar as frequências de atividade física possíveis
def frequencias():
    print("\n>> Qual é seu nível de atividade física? ")
    print("\n 1) Sedentário")
    print(" 2) Exercício físico leve ou prática desportiva 1 à 3 dias por semana")
    print(" 3) Exercício físico moderado ou prática desportiva 3 à 5 dias por semana")
    print(" 4) Exercício físico intenso ou prática desportiva 6 à 7 dias por semana")

    return frequencias

#Subprograma para solicitar a frequência de atividade física para cálculo da Taxa de Metabolismo Basal e posterior cálculo das Calorias
def solicitacaoFrequencia():
    digitouErrado = True
    while digitouErrado:
        resposta = input("\n>> Digite a opção a qual você se identifica: ")
        if resposta == 'QUIT' or resposta == 'quit':
            print("\nObrigado por utilizar esse programa!")
            exit()
    
        if resposta == '1':
            freq = 1.2
            digitouErrado = False
        elif resposta == '2':
            freq = 1.375
            digitouErrado = False
        elif resposta == '3':
            freq = 1.550
            digitouErrado = False
        elif resposta == '4':
            freq = 1.725
            digitouErrado = False
        else:
            print ("\n  Você deve digitar o número da opção desejada (de 1 a 4).")
            digitouErrado = True
    
    return freq

#Subprograma para calcular a Taxa de Metabolismo Basal para posterior cálculo das Calorias ideias 
    #TBM = Taxa de Metabolismo Basal
def tbm (sexo, peso, idade, altura, freq):
    if sexo == 'F':
        tbmF= 655.1 + (9.5 * peso) + (1.8 * altura) - (4.7 * idade)
        caloriasDesejadas = tbmF * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)
    if sexo == 'M':
        tbmM = 66.5 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        caloriasDesejadas = tbmM * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)

    print("\n  A quantidade de calorias ideais para você são", caloriasDesejadas, "calorias.")

#Programa
apresentacao()

peso = solicitacaoPesoAltura ("Digite seu peso em quilogramas: ", \
                    "\n  O peso")

altura = solicitacaoPesoAltura ("Digite sua altura em metros: ",\
                    "\n  A altura")

calculoIMC = calculoIMC (peso, altura)

idade = solicitacaoIdade ()

sexo = solicitacaoSexo ()

frequencias()

freq = solicitacaoFrequencia()

tbm (sexo, peso, idade, altura, freq)