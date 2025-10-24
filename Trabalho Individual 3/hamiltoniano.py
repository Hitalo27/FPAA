from typing import List, Set, Optional
from grafo import Grafo

def hamiltoniano_backtracking(g: Grafo, inicio: Optional[int] = None) -> Optional[List[int]]:
    n = g.n

    def bt(v: int, visitados: Set[int], caminho: List[int]) -> Optional[List[int]]:
        if len(caminho) == n:
            return caminho[:] 
        for w in g.adj[v]:
            if w in visitados:
                continue
            visitados.add(w)
            caminho.append(w)
            resp = bt(w, visitados, caminho)
            if resp is not None:
                return resp
            caminho.pop()
            visitados.remove(w)
        return None

    iniciais = [inicio] if inicio is not None else list(range(n))
    for s in iniciais:
        visitados = {s}
        caminho = [s]
        resp = bt(s, visitados, caminho)
        if resp:
            return resp
    return None
