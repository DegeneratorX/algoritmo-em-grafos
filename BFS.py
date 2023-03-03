visitados = []
fila = []
lista_adj = [[1,8],
             [0],
             [3,4,5,8],
             [2],
             [2,7],
             [2,6],
             [7,8],
             [0,7],]

for i in range(len(lista_adj)):
    if i not in visitados:
        visitados.append(i)
    for j in lista_adj[i]:
        fila.append(lista_adj[i][j])
        if j not in visitados:
            visitados.append(j)

for 
