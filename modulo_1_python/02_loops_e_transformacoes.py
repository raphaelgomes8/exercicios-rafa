# ============================================================
# Módulo 1 - Exercício 2: Loops e Transformações
# Dataset: dados/imoveis_df.csv
# ============================================================
# Como rodar: python modulo_1_python/02_loops_e_transformacoes.py
# Dica: use csv.DictReader, sem bibliotecas externas (só stdlib).
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

# Atenção: valores lidos do CSV são strings; converta quando precisar de números.

# ----------------------------------------------------------
# FÁCIL 1
# Crie uma lista com todos os preços convertidos para reais em formato
# string: "R$ 350.000" (ponto como separador de milhar, sem centavos).
# Considere apenas imóveis cujo campo preco não está vazio.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f1 = None  # lista de strings


# ----------------------------------------------------------
# FÁCIL 2
# Normalize os nomes dos bairros para maiúsculas.
# Retorne uma lista na mesma ordem dos imóveis em `dados`.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f2 = None  # lista de strings


# ----------------------------------------------------------
# FÁCIL 3
# Crie uma lista com o campo quartos convertido para int.
# Ignore imóveis em que quartos está vazio (não inclua na lista).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f3 = None  # lista de int


# ----------------------------------------------------------
# FÁCIL 4
# Para cada imóvel, adicione um campo preco_mil = preço dividido por 1000
# (float). Retorne uma NOVA lista de dicionários (não altere `dados` in-place
# se quiser reutilizá-lo depois).
# Imóveis sem preço podem ficar sem a chave preco_mil ou com None — seja
# consistente; os testes só exigem preco_mil onde preco existe.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f4 = None  # lista de dicts


# ----------------------------------------------------------
# FÁCIL 5
# Crie lista com strings "id:bairro" para todos os imóveis (ex.: "42:Asa Norte").
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_f5 = None  # lista de strings


# ----------------------------------------------------------
# MÉDIO 1
# Crie lista com preços normalizados entre 0 e 1 (min-max scaling) usando
# apenas imóveis com preco válido, na ordem em que aparecem em `dados`.
# Fórmula: (preco - min) / (max - min). Se max == min, use 0.0 para todos.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m1 = None  # lista de floats (mesmo comprimento que há preços válidos em ordem)


# ----------------------------------------------------------
# MÉDIO 2
# Acumule a soma de preços percorrendo a lista e imprima o total a cada 100 imóveis.
# Use `resultado_m2` como lista dos totais acumulados nesses marcos (100º, 200º, …),
# na ordem — os testes conferem essa lista.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m2 = None  # lista de floats (totais após 100, 200, … imóveis)


# ----------------------------------------------------------
# MÉDIO 3
# Crie dicionário contando quantos imóveis têm 1, 2, 3 e 4 quartos.
# Chaves: inteiros 1, 2, 3, 4. Só conte imóveis com quartos válido (1 a 4).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m3 = None  # dict[int, int]


# ----------------------------------------------------------
# MÉDIO 4
# Transforme a lista em dicionário indexado por id: {1: {...}, 2: {...}, ...}
# (chaves int, valores cópia ou referência ao dict do imóvel).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m4 = None  # dict[int, dict]


# ----------------------------------------------------------
# MÉDIO 5
# Crie lista de dicionários com apenas 3 campos: id, bairro, preco
# (valores como no CSV, strings).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_m5 = None  # lista de dicts


# ----------------------------------------------------------
# DIFÍCIL 1
# Pipeline: filtrar só apartamentos → converter area_m2 para float (ignore
# linhas onde não for possível) → ordenar por área decrescente → pegar top 10.
# Retorne lista de até 10 dicionários (cópias com área já como float nos
# registros retornados, se quiser).
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_d1 = None  # lista de dicts, len <= 10


# ----------------------------------------------------------
# DIFÍCIL 2
# Ordene os imóveis pelo id (numérico crescente). Calcule a variação percentual
# de preço entre cada par de imóveis consecutivos nessa ordem:
# (preco_atual - preco_anterior) / preco_anterior * 100
# Ignore pares em que algum dos dois não tem preco válido.
# Retorne lista de floats, um valor por par válido consecutivo.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_d2 = None  # lista de floats


# ----------------------------------------------------------
# DIFÍCIL 3
# Crie função transformar(dados, funcoes) que aplica cada função de `funcoes`
# em sequência ao resultado da anterior. A primeira recebe `dados`.
# ----------------------------------------------------------
# TODO: implemente transformar
def transformar(dados, funcoes):
    pass  # substitua pelo seu código


# ----------------------------------------------------------
# DIFÍCIL 4
# Normalize preços por bairro (z-score): (x - média do bairro) / desvio padrão
# do bairro. Se o desvio for 0, use 0.0 para os preços desse bairro.
# Retorne lista na mesma ordem de `dados`, com float ou None onde não houver preço.
# ----------------------------------------------------------
# TODO: seu código aqui
resultado_d4 = None  # lista alinhada a `dados`


# ----------------------------------------------------------
# DIFÍCIL 5
# Crie função agrupar_e_agregar(dados, campo_grupo, campo_valor, funcao) onde
# `funcao` recebe a lista dos valores (float) daquele grupo e retorna um único
# resultado (ex.: sum, max, min, len).
# Retorne dicionário {valor_campo_grupo: resultado_da_funcao}.
# Ignore entradas sem campo_valor numérico válido no grupo.
# ----------------------------------------------------------
# TODO: implemente agrupar_e_agregar
def agrupar_e_agregar(dados, campo_grupo, campo_valor, funcao):
    pass  # substitua pelo seu código


if __name__ == "__main__":
    from tests.modulo_1.test_02_loops_e_transformacoes import rodar_todos_os_testes

    rodar_todos_os_testes(sys.modules[__name__])
