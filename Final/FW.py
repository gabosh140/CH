












































import heapq as hq
import math
from random import *
import networkx as nx
INF = float("inf")



def generarGrafoConPesos(n,m):
    mat = [[] for i in range(n)]
    for j in range(m):
        v1 = randint(0, n - 1)
        v2 = randint(0, n - 1)
        w = randint(1, 10)
        adyacentes = [x[0] for x in mat[v1]]
        adyacentes2 = [x[0] for x in mat[v2]]
        while(v2 in adyacentes or v2 == v1 or v1 in adyacentes2):
            v1 = randint(0, n - 1)
            v2 = randint(0, n - 1)
        mat[v1] += [(v2,w)]
    return mat



def FloydWarshall(g):
    distancia = [[INF] * len(g) for i in range(len(g))]
    predecesor = [[(-1,-1)] * len(g) for i in range(len(g))]
    for i in range(len(g)):
        distancia[i][i] = 0
        for u,v in g[i]:
            distancia[i][u] = v
            predecesor[i][u] = (i,v)
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                if distancia[i][j] > distancia[i][k] + distancia[k][j]: 
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
                    predecesor[i][j] = (k,distancia[k][j])
    return distancia,predecesor




def hacerRecorridosFloydWarshall(g):
    d, p = FloydWarshall(g)
    recorrido = [[]]
    for u in range(len(p)):
        recorrido += [[]]
        for v in range(len(p)):
            if p[u][v][0] > -1:
                recorrido[u] += [(p[u][v][0],v,p[u][v][1])]
    return recorrido


FloydWarshall(g)
hacerRecorridosFloydWarshall(g)
