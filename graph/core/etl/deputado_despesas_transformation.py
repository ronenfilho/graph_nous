import sys
from pathlib import Path
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD
import os

# Adiciona a raiz do projeto ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph.config import RAW_DATA, PROCESSED_DATA, ID_LEGISLATURA
from graph.core.data.io_utils import load_csv
from graph.core.data.rdf.rdf_utils import save_graph_as_nt

# Namespaces
SCHEMA = Namespace("http://schema.org/")
POL = Namespace("http://purl.org/ontology/politico/")
BR = Namespace("https://dadosabertos.camara.leg.br/recurso/")

def create_rdf_graph():
    g = Graph()
    g.bind("schema", SCHEMA)
    g.bind("pol", POL)
    g.bind("br", BR)
    return g

def add_despesa_triples(g, row):
    """
    Cria triplas RDF para uma despesa e relaciona ao deputado.
    """
    deputado_uri = URIRef(f"https://dadosabertos.camara.leg.br/recurso/deputado/{row['deputado_id']}")
    despesa_uri = URIRef(f"https://dadosabertos.camara.leg.br/recurso/despesa/{row['codDocumento']}")

    # Tipo de despesa como recurso (opcional, mas bom para categorizar)
    tipo_despesa_uri = URIRef(f"https://dadosabertos.camara.leg.br/recurso/tipo-despesa/{row['tipoDespesa'].strip().replace(' ', '_')}")

    # Relacionamento entre deputado e despesa
    g.add((deputado_uri, POL.hasExpense, despesa_uri))

    # Despesa
    g.add((despesa_uri, RDF.type, POL.Expense))
    g.add((despesa_uri, SCHEMA.identifier, Literal(row['codDocumento'], datatype=XSD.integer)))
    g.add((despesa_uri, POL.expenseType, tipo_despesa_uri))
    g.add((despesa_uri, POL.expenseDate, Literal(row['dataDocumento'], datatype=XSD.dateTime)))
    g.add((despesa_uri, POL.amount, Literal(row['valorLiquido'], datatype=XSD.decimal)))
    g.add((despesa_uri, SCHEMA.provider, Literal(row['nomeFornecedor'])))

    # Evita erro com valores nulos
    if pd.notna(row.get('urlDocumento')):
        g.add((despesa_uri, SCHEMA.url, URIRef(row['urlDocumento'])))

    if pd.notna(row.get('cnpjCpfFornecedor')):
        g.add((despesa_uri, POL.providerId, Literal(row['cnpjCpfFornecedor'])))

    # Tipo de despesa
    g.add((tipo_despesa_uri, RDF.type, POL.ExpenseCategory))
    g.add((tipo_despesa_uri, SCHEMA.name, Literal(row['tipoDespesa'])))

def build_rdf_graph_from_dataframe(df):
    g = create_rdf_graph()
    for _, row in df.iterrows():
        add_despesa_triples(g, row)
    return g

def main():
    print("##############################")
    print("## Transformação - Despesas ##")
    print("##############################\n")

    csv_path = os.path.join(RAW_DATA, f"deputados_despesas_legisl_{ID_LEGISLATURA}.csv")
    output_path = os.path.join(PROCESSED_DATA, f"deputados_despesas_legisl_{ID_LEGISLATURA}.nt")

    df = load_csv(csv_path)
    g = build_rdf_graph_from_dataframe(df)
    save_graph_as_nt(g, output_path)

if __name__ == "__main__":
    main()
