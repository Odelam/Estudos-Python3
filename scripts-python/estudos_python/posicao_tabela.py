tabela_colocacao = ('Palmeiras', 'Corinthians', 'Santos', 'São Paulo', 'Cruzeiro', 'Chapecoense', 'Treze da Paraíba', 'Fortaleza', 'Ceará', 'Atlético -MG')

print(f"Os cinco primeiros colocados:")
for posicao, times in enumerate(tabela_colocacao):
   if posicao >= 5:
       break
   print(f"- {posicao + 1} {times}")

print()
print("Os quatro últimos colocados")
for posicao_ultimo, times in enumerate(tabela_colocacao):
    if posicao_ultimo > 5:
        print(f'- {posicao_ultimo} {times}.')

print()
print('Em ordem alfabética.')
tabela_ordem = sorted(tabela_colocacao)
for times in range(0, len(tabela_ordem)):
    print(tabela_ordem[times])

print()
print("Posição:")
print(f"Chapecoense está na posição: {tabela_colocacao.index('Chapecoense')}")
