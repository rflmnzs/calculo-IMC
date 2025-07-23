#ESTE É UM EXERCICIO PARTICULAR PARA PRATICAR MEU RECENTE APRENDIZADO EM PYTHON

'''
Criei um programa simples que lê os dados do usuário (nome, idade, altura, peso)
e exibe o IMC (Índice de massa corporal)
'''

#OPCIONAL

'''
Nessa parte do desafio, pesquisei sobre os dados e adicionei ao meu programa
as classificações do IMC segundo a OMS (organização mundial da saúde):

Até 18,5 → Abaixo do peso

18,5 a 24,9 → Peso normal

25,0 a 29,9 → Sobrepeso

30,0 a 34,9 → Obesidade grau I

35,0 a 39,9 → Obesidade grau II

40,0 ou mais → Obesidade grau III (obesidade mórbida) 
'''

#Início

nome = (input('Digite seu nome: '))
idade = int(input('Ótimo! Agora digite sua idade: '))
altura = float(input('Digite aqui sua altura: '))
peso = float(input('E por fim, digite aqui seu peso: '))

IMC = (peso / (altura * altura))

print(f'\n{nome}, sua massa corporal está em: {IMC:.2f}')

vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m' 
reset = '\033[0m'

if IMC < 18.5:
    print(f'{vermelho}Alerta:{reset} Você está abaixo do peso. ')
elif IMC < 25.0:
    print('Peso normal')
elif IMC < 30.0:
    print(f'{amarelo}Aviso:{reset} sobrepeso')
elif IMC < 35.0:
    print(f'{vermelho}Alerta{reset} obesidade grau I')
elif IMC < 40.0:
    print(f'{vermelho}Alerta:{reset} Obesidade grau II')
else:
    print(f'{vermelho}CUIDADO!{reset} Obesidade grau III (mórbida)')

print('-------------------------------------------')

nomeNutri = 'Anita Celedon Couto Vegas'
CRN = 2234
telefone = '(11) 9 1763-3040'

print(f"""{verde}Para o bem da sua saúde, entre em contato com nossa nutricionista:{reset}
      {azul}{nomeNutri}{reset}
      CRN: {azul}{CRN}{reset}
        Telefone: {azul}{telefone}{reset}""")
