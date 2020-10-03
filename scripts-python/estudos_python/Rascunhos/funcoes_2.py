import random


# def raiz_quadrada(n):
#     return n ** 2
#
#
# print(raiz_quadrada(3))
#
#
# def raizquadrada(n):
#     root = n / 2
#     for c in range(20):
#         root = (1 / 2) * (root + (n / root))
#     return root
#
#
# print(f"{raizquadrada(12):.2f}")

# def mostrar_resposta(num_resposta):
#     if num_resposta == 1:
#         return 'É certo!'
#     elif num_resposta == 2:
#         return 'Você está quase lá!'
#     elif num_resposta == 3:
#         return 'Não desista!'
#     elif num_resposta == 4:
#         return 'Não pense em parar agora!'
#
#
# num_resposta = random.randint(1, 4)
# mensagem = mostrar_resposta(num_resposta)
#
# print(mensagem)
# # print(mostrar_resposta(random.randint(1, 4)))
#

def a():
    print(f"a() começa.")
    b()
    d()
    print('a() retorna')


def b():
    print("b() começa")
    c()
    print("b() retorna")


def c():
    print("c() retorna")
    print('c() retorna')


def d():
    print("d() começa")
    print('d() retorna')


print(a())
