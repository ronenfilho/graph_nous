import os
from rdflib import Graph
import networkx as nx
import sys
from pathlib import Path
from graph.core.data.neo4j.neo4j_utils import save_graph_to_neo4j
from graph.core.data.utils import convert_to_networkx, plot_graph
from graph.core.data.rdf.rdf_utils import load_rdf_graph
from rdflib import URIRef

# Adiciona a raiz do projeto ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph.config import PROCESSED_DATA, ID_LEGISLATURA, ID_DEPUTADO


def filter_graph_for_deputado_despesas(rdf_graph, deputado_id):
    """
    Filtra o grafo RDF para incluir apenas triplas de despesas relacionadas a um deputado específico.
    Retorna o nome do deputado (se encontrado) e o grafo filtrado.
    """
    filtered_graph = Graph()

    for s, p, o in rdf_graph:
        # Filtra apenas recursos que contenham o ID do deputado como parte do URI (útil para despesas)
        if str(deputado_id) in str(s):
            filtered_graph.add((s, p, o))
            print(f"[INFO] Tripla adicionada: {s} {p} {o}")

    print(f"[INFO] Grafo de despesas filtrado com {len(filtered_graph)} triplas.")
    return filtered_graph

def main():
    print("##############################")
    print("## Carga - Despesas Deputado ##")
    print("##############################")

    nt_file = os.path.join(PROCESSED_DATA, f"deputados_despesas_legisl_{ID_LEGISLATURA}.nt")

    rdf_graph = load_rdf_graph(nt_file)

    filtered_graph = filter_graph_for_deputado_despesas(rdf_graph, ID_DEPUTADO)
    nx_graph = convert_to_networkx(filtered_graph)
    plot_graph(nx_graph, title=f"Despesas - Deputado: {ID_DEPUTADO}", file_name=f"despesas_{ID_DEPUTADO}_graph.png")

    # Salva no Neo4j
    save_graph_to_neo4j(rdf_graph)

if __name__ == "__main__":
    main()
