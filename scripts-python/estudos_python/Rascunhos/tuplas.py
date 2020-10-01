print("Tuplas!")
uma_tupla = ('a', 'b', 'pelegrino', 'z', 'exemplo')
print(uma_tupla)
print(uma_tupla[0])
print(uma_tupla[-1])
print(uma_tupla[1:3])
print("Uma tupla é definida da mesma maneira que uma lista, exceto que todo o conjunto de elementos é colocado ebtre "
      "parênteses em vez de colchetes.")
print(''' Os elementos de uma tupla tem uma ordem definida, assim como uma lista. Os índices de tupla são baseados em zero, assim como uma lista, então
o primeiro elemento de uma tupla não vazia é sempre uma_tupla[0].
índices negativos contam a partir do final da tupla, assim como uma lista.
fatiar também funciona, como uma lista. Quando você fatia uma lista, obtém uma nova lista; quando você corta uma tupla, obtém uma nova tupla.''')
print("Importante!")
print('''Você não pode adicionar elementos a uma tupla. Tuplas não tem os métodos append() ou extend().
 Não podemos remover elementos de uma tupla. Tuplas não tem os métodos remove() ou pop().
 Podemos encontrar elementos em uma tupla, pois isso não altera a tupla.
 Podemos também usar o operador in para verificar se um elemento existe na tupla''')
encontrou = 'a' in uma_tupla
print(encontrou)
print('''Para que serve as Tuplas?
Tuplas são mais rápidas que listas. Se você está definindo um conjunto constante de valores e tudo o que vai fazer com ele é iterar por ele, use
uma tupla em vez de lista.
Isso torna seu código mais seguro se você "proteger contra gravação" os dados que não precisam ser alterados.''')

print('''Aqui temos um atalho: no python, podemos usar uma tupla para atribuir vários valores de uma vez''')
v = ('a', 2, True)
(x, y, z) = v
print(x)
print(y)
print(z)
