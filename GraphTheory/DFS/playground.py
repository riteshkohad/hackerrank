import random
import networkx as nx
import string
import matplotlib.pyplot as plt


def generate_random_graph(n=None, p=None):
    if n is None:
        n = random.randint(8, 25)
    if p is None:
        p = random.random()/4 + 0.25
    graph = nx.Graph()
    vertices = string.ascii_uppercase[:n]
    graph.add_nodes_from(vertices)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                graph.add_edge(vertices[i], vertices[j])
    return graph



if __name__ == "__main__":
    gph = generate_random_graph()
    print(gph)
    nx.draw(gph)
    plt.show()  