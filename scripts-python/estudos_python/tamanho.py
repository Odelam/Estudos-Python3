sufixos = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def tamanho_aprox(tamanho, kylobyte_eh_1024_bytes=True):
    ''' converta um tamanho de arquivo em um formato legível por humanos
        palavras-chave:
        tamanho = tamanho do arquivo em bytes
        kylobyte_eh_1024_bytes = if True (default), use múltiplos de 1024
                                 if False, use múltiplos de 1000
    '''
    if tamanho < 0:
        raise ValueError('Número não pode ser negativo!')

    multiplo = 1024 if kylobyte_eh_1024_bytes else 1000
    for sufix in sufixos[multiplo]:
        tamanho /= multiplo
        if tamanho < multiplo:
            return f'{tamanho:.1f}, {sufix}'

    raise ValueError("Número muito grande!")


if __name__ == '__main__':
    print(tamanho_aprox(1000000000000, False))
    print(tamanho_aprox(1000000000000))
