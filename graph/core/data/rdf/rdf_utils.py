from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD
import pandas as pd

# Namespaces
SCHEMA = Namespace("http://schema.org/")
POL = Namespace("http://purl.org/ontology/politico/")
BR = Namespace("https://dadosabertos.camara.leg.br/recurso/")

def create_rdf_graph():
    """
    Inicializa e retorna um grafo RDF com prefixos.
    """
    g = Graph()
    g.bind("schema", SCHEMA)
    g.bind("pol", POL)
    g.bind("foaf", FOAF)
    g.bind("br", BR)
    return g

def build_rdf_graph_from_dataframe(df):
    """
    Cria e retorna o grafo RDF completo a partir do DataFrame.
    """
    g = create_rdf_graph()
    for _, row in df.iterrows():
        add_deputado_triples(g, row)
    return g

def save_graph_as_nt(g, output_path):
    """
    Salva o grafo RDF em formato N-Triples.
    """
    g.serialize(destination=output_path, format="nt")
    print(f"[INFO] Arquivo N-Triples '{output_path}' salvo com sucesso!")

def load_rdf_graph(nt_file):
    """
    Carrega o arquivo N-Triples em um grafo RDFLib.
    """
    g = Graph()
    g.parse(nt_file, format="nt")
    print(f"[INFO] Grafo RDF carregado com {len(g)} triplas.")
    return g    