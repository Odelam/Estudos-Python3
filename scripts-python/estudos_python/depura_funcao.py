def h(n):
    print('Start h')
    if n == 0:
        print(f"Encerrado pois o n deu: {n}.")
    else:
        print(1/n)
        print(n)
def g(n):
    print('Start g')
    h(n - 1)
    print(n)
def f(n):
    print('Start f')
    g(n -1)
    print(n)
f(2)
