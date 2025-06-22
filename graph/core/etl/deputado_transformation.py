import sys
from pathlib import Path
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD
import os
from graph.core.data.rdf.rdf_utils import save_graph_as_nt
from graph.core.data.io_utils import load_csv

# Adiciona a raiz do projeto ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph.config import RAW_DATA, PROCESSED_DATA, ID_LEGISLATURA


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

def add_deputado_triples(g, row):
    """
    Adiciona as triplas RDF de um deputado ao grafo,
    representando partido e UF como nós (recursos).
    """
    deputado_uri = URIRef(f"https://dadosabertos.camara.leg.br/recurso/deputado/{row['id']}")
    partido_uri = URIRef(row['uriPartido'])
    uf_uri = URIRef(f"https://dadosabertos.camara.leg.br/recurso/uf/{row['siglaUf']}")

    # Deputado
    g.add((deputado_uri, RDF.type, SCHEMA.Person))
    g.add((deputado_uri, SCHEMA.name, Literal(row['nome'])))
    g.add((deputado_uri, SCHEMA.memberOf, partido_uri))
    g.add((deputado_uri, SCHEMA.addressRegion, uf_uri))
    g.add((deputado_uri, SCHEMA.identifier, Literal(row['id'], datatype=XSD.integer)))
    g.add((deputado_uri, FOAF.page, URIRef(row['uri'])))
    g.add((deputado_uri, SCHEMA.image, URIRef(row['urlFoto'])))
    g.add((deputado_uri, POL.legislatura, Literal(row['idLegislatura'], datatype=XSD.integer)))

    if pd.notna(row.get('email')):
        g.add((deputado_uri, SCHEMA.email, Literal(row['email'])))

    # Nó Partido
    g.add((partido_uri, RDF.type, SCHEMA.Organization))
    g.add((partido_uri, SCHEMA.name, Literal(row['siglaPartido'])))

    # Nó UF
    g.add((uf_uri, RDF.type, SCHEMA.Place))
    g.add((uf_uri, SCHEMA.name, Literal(row['siglaUf'])))

def build_rdf_graph_from_dataframe(df):
    """
    Cria e retorna o grafo RDF completo a partir do DataFrame.
    """
    g = create_rdf_graph()
    for _, row in df.iterrows():
        add_deputado_triples(g, row)
    return g

def main():
    """
    Fluxo completo: carrega CSV, cria grafo RDF e salva N-Triples.
    """

    print("########################")
    print("## Transformação - Deputados ##")
    print("########################")
    print("\n")

    csv_path = os.path.join(RAW_DATA, f"deputados_legisl_{ID_LEGISLATURA}.csv")
    output_path = os.path.join(PROCESSED_DATA, f"deputados_legisl_{ID_LEGISLATURA}.nt")

    df = load_csv(csv_path)
    g = build_rdf_graph_from_dataframe(df)

    # Salva como .nt
    save_graph_as_nt(g, output_path)

if __name__ == "__main__":
    main()
