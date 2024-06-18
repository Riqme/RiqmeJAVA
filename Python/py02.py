notas_aluno = []

for i in range(4):
    notas = float(input('Qual sua nota {}?:'.format(i + 1)))
    notas_aluno.append(notas)

soma_notas = sum(notas_aluno)
média = sum(notas_aluno) / len(notas_aluno)

print('A média das notas {} é {:.1f}'. format(notas_aluno, média))
nova_nota = float(input('Qual foi a sua última nota?'))
notas_aluno.append(nova_nota)
print('A sua média final das notas {} é {:.1f}'.format(notas_aluno, média))

remover_nota1 = input('Deseja remover uma de suas notas (sim/não)?')
if remover_nota1.lower() == 'sim':
    nota_remover = int(input('Qual das 5 notas {}, você deseja remover?'.format(notas_aluno)))
    if nota_remover in notas_aluno:
        notas_aluno.remove(nota_remover)
    print('Nota removida. Novas notas:{}'.format(notas_aluno))
    print('Sua nova média é: {}'.format(média))
else: 
    print('A sua média final de notas {} permanecerá {}'.format(notas_aluno, média))
    