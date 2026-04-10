# Estudos Rafa — Trilha de Data Science

Exercícios práticos de Python para Dados, Estatística e Ciência de Dados.
Todos os exercícios usam um dataset fictício de imóveis no Distrito Federal.

## Como começar

### 1. Instalar dependências

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### 2. Gerar o dataset

```bash
python gerar_dados.py
```

Isso cria o arquivo `dados/imoveis_df.csv` com 500 imóveis.

## Estrutura

```
modulo_1_python/      → Python puro para dados (sem bibliotecas)
modulo_2_estatistica/ → Estatística descritiva e inferencial
modulo_3_ciencia_de_dados/ → Limpeza, EDA, visualização, ML
tests/                → Testes automáticos (por módulo), importados pelos exercícios
```

## Testes automáticos

Os checks ficam em `tests/` (por exemplo `tests/modulo_1/`), separados dos arquivos
do aluno em `modulo_1_python/`. Você não precisa alterar essa pasta: implemente
só o que está indicado com `TODO` no exercício e rode o `.py` correspondente.
Execute sempre a partir da **raiz do repositório** (onde está `gerar_dados.py`),
para o Python encontrar o pacote `tests` e o arquivo `dados/imoveis_df.csv`.

## Como resolver os exercícios

Abra o arquivo do exercício, leia o enunciado e substitua o `TODO` pela sua
solução. Depois rode o arquivo para disparar os testes importados de `tests/` (exemplo abaixo):

```bash
python modulo_1_python/01_listas_e_filtros.py
```

## Progressão recomendada

1. Módulo 1 completo (6 arquivos)
2. Módulo 2 completo (5 arquivos)
3. Módulo 3 completo (5 arquivos)
