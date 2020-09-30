# capitais = {'Amazonas': 'Manaus', 'Paraná': 'Curitiba', 'Ceará': 'Fortaleza'}
# print(capitais['Amazonas'])
# capitais['Minas Gerais'] = 'Belo Horizonte'
# print(capitais)
# capitais['Bahia'] = 'Salvador'
# print(len(capitais))
# for c in capitais:
#     print(capitais[c], "é a capital de [a/o] ", c)

ramal = {'Daniel': '1410', 'Adriana': '1194', 'Odelam': '1122'}
print(ramal)
print("Retorna as chaves do dicionário em um objeto dict_keys: ", ramal.keys())
print("Retorna os valores do dicionário em um objeto dict_values: ", ramal.values())
print("Retorna todos os itens com suas respectivas chaves: ", ramal.items())
print("Transformando um dicionário em um opbjeto do tipo list: ", list(ramal.items()))
print("Retorna o valor associado a (), e retorna None caso contrário", ramal.get("Pedro"))
print("Retorna o valor associado a (), 'SEM RAMAL' caso contrário", ramal.get("Pedro", "SEM RAMAL"))

