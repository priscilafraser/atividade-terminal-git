aluno = dict()
aluno['Aluno'] = str(input('Digite nome do aluno: '))
aluno['Média'] = float(input('Digite a nota: '))

print(aluno)

if aluno['Média'] >= 7:
    print('O aluno está APROVADO')
elif aluno['Média'] >= 5 and aluno['Média'] <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')
