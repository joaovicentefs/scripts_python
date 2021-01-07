from validate_docbr import CPF
pessoafisica = CPF()
if pessoafisica.validate(input('Informe o CPF: ')) == True:
	print('CPF Válido')
else:
	print('CPF Inválido!')