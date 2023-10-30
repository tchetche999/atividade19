# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
nota1 = float(input('primeira nota'))
nota2 = float(input('segunda nota'))
media = (nota1 + nota2) / 2
print('media:',media)
if media<7.0:
    print('reprovado melhore na próxima')
elif media<10:
    print('aprovado')
else:
    print('aprovado bom aluno')