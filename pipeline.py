from pathlib import Path

from etl import pipeline_calcular_kpi_vendas_consolidado

path_pasta_arquivo: Path = "data"
formato = ["csv"]
pipeline_calcular_kpi_vendas_consolidado(path_pasta_arquivo, formato)
