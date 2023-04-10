for id in range(120):
    with open(f'{id}.out', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)  # Volto pra linha 0 do arquivo pra releitura
        linhas = file.read().split('\n')  # Separo em uma lista as linhas
        print(f"\nArquivo {id}")
        for i in linhas:
            print(i)
