import time


# Função - exibe a tabuada do número solicitado
def tabuada(x):
    y = 1
    while y <= 10:
        print(f'{x}*{y}={x * y}')
        time.sleep(0.5)
        y += 1


# Apresentação do programa
print('Seja bem-vindo(a) ao exibidor de tabuada!')
time.sleep(1.5)
print('Escolha um número e em seguida veja a mágica!')
time.sleep(1.5)

# Solicitação da tabuada desejada
while True:
    num = int(input('Qual tabuada deseja? '))
    print('')
    tabuada(num)
    time.sleep(1)
    print('')
    print('Aqui está sua tabuada')
    time.sleep(1.5)
    replay = input('Deseja outra tabuada? (s/n) ').lower()
    while replay not in ['s', 'n']:
        print('Opção inválida!')
        replay = input('Deseja outra tabuada? (s/n) ').lower()
    if replay == 's':
        print('')
    if replay == 'n':
        print('')
        break

# Finalização do programa
print('Obrigado por utilizar o programa. Volta sempre!')
