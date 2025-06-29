from graph.core.etl.deputado_extraction import main as deputado_extraction_main
from graph.core.etl.deputado_transformation import main as deputado_transformation_main
from graph.core.etl.deputado_loading import main as deputado_loading_main
from graph.core.etl.deputado_despesas_extraction import main as deputado_despesas_extraction_main
from graph.core.etl.deputado_despesas_transformation import main as deputado_despesas_transformation_main
from graph.core.etl.deputado_despesas_loading import main as deputado_despesas_loading_main


def main():
    print("##############################")
    print("## Semantic ETL Pipilines - ##")
    print("##############################")
    print("\n")

    print("Iniciando extração dos deputados...")
    deputado_extraction_main()
    print("Extração dos deputados concluída!")    
    print("\n")    

    print("Iniciando transformação dos deputados...")
    deputado_transformation_main()
    print("Transformação dos deputados concluída!")
    print("\n")

    print("Iniciando carga dos deputados...")
    deputado_loading_main()
    print("Carga dos deputados concluída!")
    print("\n")

    print("Iniciando extração das despesas dos deputados...")
    deputado_despesas_extraction_main()
    print("Extração das despesas dos deputados concluída!")    
    print("\n")    

    print("Iniciando transformação das despesas dos deputados...")
    deputado_despesas_transformation_main()
    print("Transformação das despesas dos deputados concluída!")
    print("\n")

    print("Iniciando carga das despesas dos deputados...")
    deputado_despesas_loading_main()
    print("Carga das despesas dos deputados concluída!")
    print("\n")     

if __name__ == "__main__":
    main()