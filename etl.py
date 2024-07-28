import glob
import os
from pathlib import Path

import pandas as pd


def extrair_dados_consolidar(path_pasta_arquivo: Path) -> pd.DataFrame:
    """
    Função para extrair arquivos .json de um diretório específico
    """
    arquivos_json: Path = glob.glob(os.path.join(path_pasta_arquivo, "*.json"))
    lista_dataframes: list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    dataframe_completo = pd.concat(lista_dataframes, ignore_index=True)

    return dataframe_completo


def calcular_kpi_total_vendas(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Função que calcula a quantidade total de vendas
    """
    dataframe["Total"] = dataframe["Quantidade"] * dataframe["Venda"]

    return dataframe


def carregar_dados(dataframe: pd.DataFrame, formato_saida: list):
    """
    Função para carregar dados de acordo com a necessidade. Pode ser 'csv', 'parquet'
    ou os dois.
    """
    for formato in formato_saida:
        if formato == "csv":
            dataframe.to_csv("dados_agregados.csv", index=False)
        if formato == "parquet":
            dataframe.to_parquet("dados_agregados.parquet", index=False)


def pipeline_calcular_kpi_vendas_consolidado(
    caminho_arquivo: Path, formato_saida: list
):
    """
    Pipeline completa com toda a ETL do arquivo
    """
    dataframe_completo = extrair_dados_consolidar(caminho_arquivo)
    dataframe_completo_calculado = calcular_kpi_total_vendas(dataframe_completo)
    carregar_dados(dataframe_completo_calculado, formato_saida)


if __name__ == "__main__":
    path_pasta_arquivo: Path = "data"
    dataframe_completo = extrair_dados_consolidar(path_pasta_arquivo)
    dataframe_completo_calculado = calcular_kpi_total_vendas(dataframe_completo)
    formato_saida = ["csv", "parquet"]
    carregar_dados(dataframe_completo_calculado, formato_saida)
