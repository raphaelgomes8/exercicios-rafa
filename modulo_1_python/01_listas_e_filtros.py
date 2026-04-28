# ============================================================
# Módulo 1 - Exercício 1: Listas e Filtros
# Dataset: dados/imoveis_df.csv
# ============================================================
# Como rodar: python modulo_1_python/01_listas_e_filtros.py
# Dica: os dados são carregados como lista de dicionários.
#       Cada dicionário tem as chaves: id, bairro, tipo, quartos,
#       banheiros, area_m2, garagens, andar, novo, preco
# ============================================================

import csv
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

with open("dados/imoveis_df.csv", encoding="utf-8") as f:
    dados = list(csv.DictReader(f))

# Atenção: todos os valores lidos do CSV são strings!
# Para comparar números, converta: int(imovel["quartos"])

# ----------------------------------------------------------
# FÁCIL 1
# Quantos imóveis têm mais de 3 quartos?
# Dica: percorra a lista com um for e conte usando uma variável.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f1 = None # deve ser um int


# ----------------------------------------------------------
# FÁCIL 2
# Quais são os bairros únicos presentes no dataset?
# Retorne uma lista (sem repetições, qualquer ordem).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f2 = None  # deve ser uma lista de strings


# ----------------------------------------------------------
# FÁCIL 3
# Filtre apenas os imóveis do tipo "apartamento".
# Retorne a lista de dicionários filtrada.
# ----------------------------------------------------------
Respostas:
ls = []

for apt in dados:
    apt_tipo = apt["tipo"]
    if apt_tipo == "apartamento":
        ls.append(apt)
resultado_f3 = ls


# ----------------------------------------------------------
# FÁCIL 4
# Qual é o imóvel mais caro do dataset?
# Retorne o dicionário completo do imóvel.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f4 = None  # deve ser um dicionário


# ----------------------------------------------------------
# FÁCIL 5
# Quantas garagens existem no total somando todos os imóveis?
# Ignore imóveis com o campo garagens vazio.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f5 = None  # deve ser um int


# ----------------------------------------------------------
# MÉDIO 1
# Filtre imóveis com área maior que 80 m² E preço menor que
# R$ 500.000. Retorne a lista de dicionários.
# Ignore imóveis com area_m2 que contenha letras (ex: "75 m²").
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m1 = None


# ----------------------------------------------------------
# MÉDIO 2
# Agrupe os imóveis por tipo em um dicionário.
# Resultado esperado: {"apartamento": [...], "casa": [...], "cobertura": [...]}
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m2 = None


# ----------------------------------------------------------
# MÉDIO 3
# Ordene a lista de imóveis pelo preço do menor para o maior.
# NÃO use o método .sort() nem sorted() — implemente você mesmo
# a lógica de ordenação (ex: selection sort ou bubble sort).
# Retorne a lista ordenada.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m3 = None


# ----------------------------------------------------------
# MÉDIO 4
# Conte quantos imóveis existem em cada bairro.
# Retorne um dicionário: {"Asa Norte": 42, "Ceilândia": 31, ...}
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m4 = None


# ----------------------------------------------------------
# MÉDIO 5
# Calcule o preço por m² de cada imóvel (preco / area_m2).
# Retorne os 5 imóveis mais BARATOS por m².
# Ignore imóveis com area_m2 que contenha letras.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m5 = None  # lista de 5 dicionários


# ----------------------------------------------------------
# DIFÍCIL 1
# Calcule a média de preço por bairro.
# Retorne um dicionário: {"Asa Norte": 950000.0, ...}
# Não use numpy nem pandas.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_d1 = None


# ----------------------------------------------------------
# DIFÍCIL 2
# Implemente uma busca binária para encontrar, em uma lista
# de preços ordenada, o primeiro preço >= ao valor buscado.
# Função: busca_binaria(precos_ordenados, valor) -> índice
# Teste com: busca_binaria(precos, 300_000)
# Não use bisect nem sorted() dentro da função.
# ----------------------------------------------------------
# TODO: implemente a função busca_binaria
def busca_binaria(precos_ordenados, valor):
    pass  # substitua pelo seu código


# ----------------------------------------------------------
# DIFÍCIL 3
# Separe os imóveis em duas listas usando uma regra de preço:
#   - lista_baratos: preço < regra
#   - lista_caros:   preço >= regra
# Faça isso para CADA valor de regra de 100k até 900k (passo 50k).
# Para cada regra, calcule o desvio padrão da lista original e
# a média ponderada dos desvios das duas sublistas resultantes.
# Retorne o valor de regra que minimiza essa média ponderada.
# (Essa é a ideia por trás do ganho de informação em árvores!)
# ----------------------------------------------------------
# TODO: seu código aqui
melhor_regra = None  # deve ser um número (int ou float)


# ----------------------------------------------------------
# DIFÍCIL 4
# Para cada bairro, calcule o preço médio por m².
# Retorne um dicionário ordenado do mais barato ao mais caro,
# mostrando apenas os 5 primeiros e os 5 últimos.
# Resultado: {"ranking": [("Planaltina", 1200.5), ...]}
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_d4 = None


# ----------------------------------------------------------
# DIFÍCIL 5
# Dado o imóvel abaixo, encontre os 3 imóveis mais similares
# do dataset usando distância euclidiana no espaço (area_m2, quartos).
# Ignore imóveis com area_m2 malformada.
# Retorne lista de 3 dicionários.
# ----------------------------------------------------------
imovel_referencia = {"area_m2": 85.0, "quartos": 3}

# TODO: seu código aqui
resultado_d5 = None


if __name__ == "__main__":
    from tests.modulo_1.test_01_listas_e_filtros import rodar_todos_os_testes

    rodar_todos_os_testes(sys.modules[__name__])
