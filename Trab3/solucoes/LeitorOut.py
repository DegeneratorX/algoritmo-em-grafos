for id in range(13):
    with open(f'Trab3/solucoes/{id}.out', 'r') as file:
        while (True):
            if file.read() == '':  # Se arquivo vazio
                exit(1)
            else:
                break
        file.seek(0, 0)  # Volto pra linha 0 do arquivo pra releitura
        linhas = file.read().split('\n')  # Separo em uma lista as linhas
        print(f"Arquivo {id}:")
        for i in linhas:
            print(i)
#n = max(max(x[0], x[1]) for x in self._lista_de_arestas) + 1