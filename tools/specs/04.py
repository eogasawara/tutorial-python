LESSON = {
"file": "04-Indexacao",
"title": "Indexação de DataFrames em Python",
"intro": """
Exemplos de código da aula sobre acesso e indexação de dados. Construímos um baralho de 52 cartas e o usamos para praticar `iloc`, `loc`, filtros booleanos, visões e cópias.
""",
"cells": [
{"code": """
import numpy as np
import pandas as pd
"""},
{"section": "Construindo o baralho",
 "text": "Percorremos os naipes e, dentro de cada naipe, as 13 faces. A compreensão de lista gera os 52 pares (face, naipe), que viram as linhas do DataFrame.",
 "code": """
faces = ["ás", "dois", "três", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "valete", "dama", "rei"]
naipes = ["ouros", "copas", "paus", "espadas"]
baralho = pd.DataFrame(
    [(f, n) for n in naipes for f in faces],
    columns=["face", "naipe"]
)
print(len(baralho))
print(baralho.head())
"""},
{"section": "Nova coluna",
 "text": "`np.tile` repete a sequência de 1 a 13 quatro vezes, uma para cada naipe, atribuindo o valor numérico de cada carta.",
 "code": """
baralho["valor"] = np.tile(np.arange(1, 14), 4)
print(baralho.head())
"""},
{"section": "Formas de acesso",
 "text": "`iloc` acessa por posição; `loc` acessa por rótulo (índice e nome de coluna); uma expressão booleana filtra linhas.",
 "code": """
print(baralho.iloc[0, 1])
print(baralho.loc[0, "naipe"])
print(baralho[baralho["valor"] > 10].head(3))
"""},
{"section": "Colunas como Séries",
 "text": "Uma única coluna é uma `Series`: estrutura unidimensional que mantém o índice original.",
 "code": """
print(baralho.iloc[0, 0])
print(baralho["face"].iloc[[0, 1]])
"""},
{"section": "Sintaxes equivalentes",
 "text": "As três expressões abaixo devolvem a mesma Series (linhas 10 e 13 da coluna `face`).",
 "code": """
print(baralho.loc[[10, 13], "face"].tolist())
print(baralho.iloc[[10, 13], 0].tolist())
print(baralho["face"].iloc[[10, 13]].tolist())
"""},
{"section": "Várias colunas",
 "text": "Selecionando mais de uma coluna, o resultado é um DataFrame. Note que o fatiamento posicional `10:12` exclui o fim.",
 "code": """
print(baralho.iloc[10:12, 0:2])
print(baralho.loc[[10, 13], ["face", "naipe"]])
"""},
{"section": "Series vs DataFrame",
 "text": "Colchetes simples devolvem uma Series; colchetes duplos (uma lista de nomes) preservam a estrutura de tabela.",
 "code": """
print(type(baralho["face"]))
print(type(baralho[["face"]]))
"""},
{"section": "Removendo linhas e colunas",
 "text": "`drop()` remove pelo rótulo e devolve um novo DataFrame; para manter o resultado, reatribua. Atenção: em Python, índices negativos não removem nada, `x[-1]` é o último elemento.",
 "code": """
print(baralho.drop(index=range(3)).head(3))
print(baralho.drop(columns=["face"]).head(3))
"""},
{"section": "Linhas e colunas inteiras",
 "code": """
print(baralho.iloc[0])
print(baralho["naipe"].head())
"""},
{"section": "Máscara booleana sobre colunas",
 "text": "Cada `True` indica uma coluna que deve permanecer.",
 "code": """
mask = [True, True, False]
print(baralho.loc[:, mask].head())
"""},
{"section": "Máscara booleana sobre linhas",
 "text": "A forma mais comum de filtrar: a condição gera uma Series de `True`/`False` e só as linhas `True` permanecem.",
 "code": """
filtro = baralho["valor"] < 3
print(baralho[filtro])
"""},
{"section": "Embaralhando",
 "text": "`np.random.permutation` gera uma ordem aleatória das posições, aplicada com `iloc`. A semente torna o exemplo reproduzível.",
 "code": """
np.random.seed(42)
ordem = np.random.permutation(len(baralho))
cartas = baralho.iloc[ordem]
print(cartas.head())
"""},
{"section": "Encapsulando em uma função",
 "code": """
def embaralhar(df):
    ordem = np.random.permutation(len(df))
    return df.iloc[ordem]

print(embaralhar(baralho).head(3))
"""},
{"section": "Tipos de dados (dtype)",
 "code": """
a = np.array([1, 2, 3])
b = np.array([1.0, 2.0, 3.0])
print(a.dtype, b.dtype)
print(baralho.dtypes)
"""},
{"section": "Broadcasting",
 "text": "NumPy combina arrays de formas compatíveis: cada dimensão deve ser igual ou valer 1. Um escalar se expande para todo o array; formas incompatíveis geram erro.",
 "code": """
x = np.array([1, 2, 3, 4])
x + 10
"""},
{"error": True, "code": "x + np.array([1, 2])"},
{"section": "Visão e cópia",
 "text": "O fatiamento cria uma visão: modificá-la altera o array original. `.copy()` cria dados independentes.",
 "code": """
x = np.array([1, 2, 3, 4])
y = x[0:2]          # visão
z = x[0:2].copy()   # cópia
y[0] = 99
x, y, z
"""},
{"section": "Indexação por lista de índices",
 "text": "Indexar com uma lista de posições sempre cria uma cópia: alterar o resultado não afeta o original.",
 "code": """
x = np.array([10, 20, 30, 40, 50])
sel = x[[0, 2, 4]]
sel[0] = -1
print(sel, x)
"""},
]}
