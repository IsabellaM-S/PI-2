print ("PROGRAMA PARA CALCULAR IMC DE PESSOAS ADULTAS :)")

continuar = True
while continuar:

    # Informações para calculo IMC
    digitouErradoPeso = True
    while digitouErradoPeso:
    
        try:
            peso = float (input("\n>> Digite seu peso em quilogramas: "))
            if peso <= 0:
                print("\n  O peso não pode ser negativo ou igual a zero. Tente novamente...")
                digitouErradoPeso = True
            else:
                digitouErradoPeso = False
                   
        except ValueError:
            print ("\n  Somente números podem ser digitados. Tente novamente...")
            digitouErradoPeso = True

    digitouErradoAltura = True
    while digitouErradoAltura:

        try:
            altura = float (input("\n>> Digite sua altura em metros:  "))
            if altura <= 0:
                print("\n  A altura não pode ser negativa ou igual a zero. Tente novamente...")
                digitouErradoAltura = True

            else:
                digitouErradoAltura = False

        except ValueError:
            print("\n  Somente números podem ser digitados. Tente novamente...")
            digitouErradoAltura = True

    # Calculo IMC      
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

    # Informações para calculo de calorias
    digitouErradoIdade = True
    while digitouErradoIdade:

        try:
            idade = int (input("\n>> Qual a sua idade? "))
            if idade <= 0:
                print("\n  A idade não pode ser neagtiva ou igual a zero. Digite novamente...")
                digitouErradoIdade = True
            
            else:
                if idade < 18 or idade >60:
                    print("  ATENÇÃO: esse programa é indicado para pessoas de faixa etária entre 18 anos e 60 anos. Com essa idade os cálculos finais podem dar errado.")
                    digitouErradoIdade = False
                else:
                    digitouErradoIdade = False

        except ValueError:
            print("\n  Somente números podem ser digitados. Tente novamente...")

    digitouErradoSexo = True
    while digitouErradoSexo:

        sexo = input("\n>> Qual é seu sexo biológico (Digite M para masculino ou F para feminino)? ").upper()
        
        if sexo == 'M':
            digitouErradoSexo = False
        elif sexo == 'F':
            digitouErradoSexo = False
        else:
            digitouErradoSexo = True
            print ("\n  A resposta deve ser M ou F. Digite novamente...")
    
    
    print("\n>> Qual é seu nível de atividade física? ")
    print("\n 1) Sedentário")
    print(" 2) Exercício físico leve ou prática desportiva 1 à 3 dias por semana")
    print(" 3) Exercício físico moderado ou prática desportiva 3 à 5 dias por semana")
    print(" 4) Exercício físico intenso ou prática desportiva 6 à 7 dias por semana")

    digitouErradoFreq = True
    while digitouErradoFreq:
        resposta = input("\n>> Digite a opção a qual você se identifica: ")

        if resposta == '1':
            freq = 1.2
            digitouErradoFreq = False
        elif resposta == '2':
            freq = 1.375
            digitouErradoFreq = False
        elif resposta == '3':
            freq = 1.550
            digitouErradoFreq = False
        elif resposta == '4':
            freq = 1.725
            digitouErradoFreq = False
        else:
            print ("\n  Você deve digitar o número da opção desejada (de 1 a 4).")
            digitouErradoFreq = True
    
    #Calculo de calorias ideias por dia
        # TBM = Taxa de Metabolismo Basal
    if sexo == 'F':
        tbmF= 655.1 + (9.5 * peso) + (1.8 * altura) - (4.7 * idade)
        caloriasDesejadas = tbmF * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)
    else:
        tbmM = 66.5 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        caloriasDesejadas = tbmM * freq
        caloriasDesejadas = round(caloriasDesejadas, 2)

    print("\n  A quantidade de calorias ideais para você são", caloriasDesejadas, "calorias.")

    # Calculo quantas calorias a mais ou a menos deveria ingerir
    digitouErradoCalorias = True
    while digitouErradoCalorias:
        try:
            caloriasIngeridas = float(input("\n>> Quantas calorias você ingeriu hoje? "))
            digitouErradoCalorias = False
        
        except ValueError:
            print ("\n  Apenas números podem ser digitados. Tente novamente...")
            digitouErradoCalorias = True
    
    diferenca = caloriasDesejadas - caloriasIngeridas 
    diferenca = round(diferenca, 2)

    if diferenca == 0:
        print ("\n  Você ingeriu a quantidade adequada de calorias hoje. Continue assim!!")
    elif diferenca > 1:
        print ("\n  Você ingeriu", diferenca, "calorias à menos do que deveria.")
    elif diferenca < -1:
        print ("\n  Você ingeriu", -diferenca, "calorias à mais do que deveria.")

    # Pergunta se o usuário quer calcular outro IMC
    querContinuar = True
    while querContinuar:
       
        resposta = input("\n>> Você deseja continuar utilizando o programa (S/N)? ").upper()
       
        if resposta == 'S':
            querContinuar = False
            continuar = True
        elif resposta == 'N':
            querContinuar = False
            continuar = False
        else:
            print ("\nVocê deve digitar S ou N. Tente novamente...")
            querContinuar = True

print ("\n  Obrigado por utilizar esse programa!")
