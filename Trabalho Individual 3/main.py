# main.py
import argparse
from grafo import Grafo
from hamiltoniano import hamiltoniano_backtracking

def parse_arestas(n: int, s: str, direcionado: bool) -> Grafo:
    g = Grafo.vazio(n, direcionado)
    if not s:
        return g
    for aresta in s.split(','):
        aresta = aresta.strip()
        if direcionado:
            u, v = map(int, aresta.split('>'))
        else:
            u, v = map(int, aresta.split('-'))
        g.adiciona_aresta(u, v)
    return g

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int)
    parser.add_argument('--arestas', type=str, default='')
    parser.add_argument('--direcionado', action='store_true')
    parser.add_argument('--nao-direcionado', action='store_true')
    parser.add_argument('--inicio', type=int, default=None)
    args = parser.parse_args()

    if args.n is None:
        print("Erro: use --n e --arestas.")
        return

    direc = args.direcionado and not args.nao_direcionado
    grafo = parse_arestas(args.n, args.arestas, direc)

    caminho = hamiltoniano_backtracking(grafo, args.inicio)
    if caminho:
        print("Existe Caminho Hamiltoniano:", caminho)
    else:
        print("Não existe Caminho Hamiltoniano.")

if __name__ == "__main__":
    main()
