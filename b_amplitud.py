from collections import defaultdict

# Crear grafo


def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList


# Nodo padre con nodo vecino -> Ej: Padre Medellín con vecinos: Pereira, Manizales y Pto Berrío
edges = [["Medellin", "Pereira"], ["Medellin", "Manizales"], ["Medellin", "Puerto Berrio"], ["Pereira", "Ibague"],
         ["Manizales", "Honda"], ["Puerto Berrio", "Tunja"], [
             "Ibague", "Melgar"], ["Honda", "Facatativa"],
         ["Tunja", "Bogota"], ["Melgar", "Bogota"], ["Facatativa", "Bogota"]]
adjacencyList = generateAdjacencyLst(edges)
# print(adjacencyList)

# Nodo a buscar
valueToFind = "Bogota"


def bfs(adjacencyList, vertex):
    visitedSet = set()
    queue = []
    visitedSet.add(vertex)
    queue.append(vertex)

    result = []
    while queue:
        v = queue[0]
        result.append(v)
        queue = queue[1:]
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                visitedSet.add(neighbor)
                queue.append(neighbor)
        if v == valueToFind:
            break
    print("")
    return result


print(bfs(adjacencyList, "Medellin"))
