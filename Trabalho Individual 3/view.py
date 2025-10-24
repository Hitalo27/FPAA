import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(n, arestas, direcionado, caminho=None):
    G = nx.DiGraph() if direcionado else nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(arestas)

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=800)
    if caminho:
        edges = list(zip(caminho[:-1], caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3)

    plt.show()

if __name__ == "__main__":
    desenhar_grafo(5, [(0,1),(1,2),(2,3),(3,4),(0,4)], False, [0,1,2,3,4])
