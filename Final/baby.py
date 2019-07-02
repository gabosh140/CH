






















































from collections import defaultdict 
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


def minimaDistancia(distancia, visitado):   
    (minimo, minVertice) = (INF, 0) 
    for v in range(len(distancia)): 
        if minimo > distancia[v] and not visitado[v]:
            (minimo, minVertice) = (distancia[v], v)   
    return minVertice

def BellmanFord(aristas, numeroVertices):
    distancia = [INF] * (numeroVertices + 1)
    distancia[numeroVertices] = 0
    for i in range(numeroVertices):
        aristas += [[numeroVertices, i, 0]]
    for i in range(numeroVertices):
        for (u, v, w) in aristas:
            if((distancia[u] != INF) and (distancia[u] + w < distancia[v])):
                distancia[v] = distancia[u] + w 
    return distancia[:numeroVertices]

def Dijkstra(g, gModificado, s): 
    visitado = defaultdict(lambda : False)
    distancia = [INF] * len(g)
    distancia[s] = 0
    predecesor = [-1] * len(g)
    for c in range(len(g)):
        minVertice = minimaDistancia(distancia, visitado)
        visitado[minVertice] = True
        for v in range(len(g)):
            adyacentes = [i for i,_ in g[minVertice]]
            if ((not visitado[v]) and
                (v in adyacentes) and
                (distancia[v] > (distancia[minVertice] + gModificado[minVertice][adyacentes.index(v)][1]))):
                distancia[v] = (distancia[minVertice] + gModificado[minVertice][adyacentes.index(v)][1])
                predecesor[v] = minVertice
    return distancia,predecesor

def Johnson(g):
    aristas = []
    for u in range(len(g)):
        for v,w in g[u]:
            aristas += [[u, v, w]]
    pesoModificado = BellmanFord(aristas, len(g))
    gModificado = [[] for i in range(len(g))]
    for u in range(len(g)):
        for v,w in g[u]:
            gModificado[u] += [(v, w + pesoModificado[u] - pesoModificado[v])]
    recorrido = []
    predecesor = []
    for u in range(len(g)):
        distancia,p = Dijkstra(g, gModificado, u)
        recorrido += [[]]
        for v in range(len(distancia)):
            if p[v] != -1:
                recorrido[-1] += [(p[v],v,distancia[v] - distancia[p[v]])]
    print(recorrido)

g = generarGrafoConPesos(10,28)
print(g)
print("//////////////")
Johnson(g) 


####def guardardatosdetexto(f2):
####   linea= f2.readlines()
####   arr=[]
####    arr2=[]
####    s=str()
####    x=float()
####    for i in linea:
####        for j in i:
####            if(j is not "\n")and(j is not " "):
####                s+=j
####            else:
####                arr.append(s)
####                s=str()
####        arr.pop()
####        arr=[float(i) for i in arr]
####        arr2.append(arr)
####        arr=[]
####    f2.close()
####    return arr2
