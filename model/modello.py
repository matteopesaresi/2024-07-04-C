from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._DAO = DAO
        self._years = self._DAO.get_all_years()
        self._all_sightnings= {s.id : s for s in self._DAO.get_all_sightings()}
        self._graph = nx.DiGraph()
    def getYears(self):
        return self._years
    def getShapes(self,anno):
        return self._DAO.get_all_shapes(anno)
    def buildGraph(self,anno,shape):
        self._graph.clear()
        for s in self._all_sightnings.values():
            year = s.datetime.year
            if  year == int(anno):
                if s.shape == shape:
                    sight= self._all_sightnings.get(s.id)
                    self._graph.add_node(sight)
        for a in self._graph.nodes:
            for b in self._graph.nodes:
                if a.state == b.state:
                    if a.longitude < b.longitude:
                        peso = b.longitude - a.longitude
                        self._graph.add_edge(a,b,weight=peso)
                    if a.longitude > b.longitude:
                        peso =a.longitude - b.longitude
                        self._graph.add_edge(b,a,weight=peso)

    def details(self):
        return len(self._graph.nodes()), len(self._graph.edges())

    def get_top5_archi(self):
        lista_archi = []

        # grafo.edges(data=True) restituisce una tupla di 3 elementi per ogni arco:
        # (nodo_partenza, nodo_arrivo, dizionario_degli_attributi)
        # Esempio: ('A', 'B', {'weight': 15})
        for u, v, dati in self._graph.edges(data=True):
            # Estraiamo il peso dal dizionario (se non c'è, diciamo che vale 0 di default)
            peso = dati.get('weight', 0)

            # Salviamo in una nostra lista una tupla personalizzata
            lista_archi.append((u, v, peso))

        # Ordiniamo la lista in base al peso.
        # Il peso si trova all'indice 2 della nostra tupla (u=0, v=1, peso=2)
        # reverse=True serve per avere i pesi più alti per primi (ordine decrescente)
        lista_archi.sort(key=lambda x: x[2], reverse=True)

        # Ritorniamo solo i primi 5 elementi
        return lista_archi[:5]


