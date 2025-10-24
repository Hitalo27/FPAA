from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Grafo:
    n: int
    adj: Dict[int, List[int]]
    direcionado: bool = True

    @staticmethod
    def vazio(n: int, direcionado: bool = True) -> "Grafo":
        return Grafo(n=n, adj={i: [] for i in range(n)}, direcionado=direcionado)

    def adiciona_aresta(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        if not self.direcionado:
            self.adj[v].append(u)
