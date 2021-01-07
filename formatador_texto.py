txt = str(input('Digite o texto que será formatado: '))
print('''Escolha o formatação desejada:
[ 1 ] - TODO EM CAIXA ALTA
[ 2 ] - todo em caixa baixa
[ 3 ] - Primeira Letra de Cada Palavra Captalizada
[ 4 ] - Apenas a primeira letra da frase Captalizada''')
opcao = int(input('Opção: '))
if opcao == 1:
	print(txt.upper())
elif opcao == 2:
	print(txt.lower())
elif opcao == 3:
	print(txt.capitalize())
elif opcao == 4:
	print(txt.title())
else:
	print('Você escolheu uma opção inválida')
