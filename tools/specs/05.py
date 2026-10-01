LESSON = {
"file": "05-Modificacao-Valores",
"title": "Modificação de Valores em Python",
"intro": """
Exemplos de código da aula sobre atribuição, estado do programa e modificação de valores em tabelas. O baralho é carregado de `examples/baralho.csv`, neste repositório.
""",
"cells": [
{"code": """
import numpy as np
import pandas as pd
"""},
{"section": "Atribuição e estado",
 "text": "Cada atribuição substitui o valor anterior; o valor antigo não é lembrado.",
 "code": """
x = 10
x = x + 5
print(x)
"""},
{"section": "Execução sequencial",
 "text": "`b` é calculado quando `a` vale 5. Mudar `a` depois não recalcula `b`.",
 "code": """
a = 5
b = a * 2
a = 10
print(b)
"""},
{"section": "Carregando dados de uma URL",
 "text": "`read_csv` aceita uma URL e converte o arquivo remoto em DataFrame.",
 "code": """
url = "https://raw.githubusercontent.com/eogasawara/tutorial-python/main/examples/baralho.csv"
baralho = pd.read_csv(url)
print(baralho.shape)
print(baralho.head())
"""},
{"section": "Salvando e recarregando",
 "text": "`del` apaga o nome `baralho`; a memória é liberada quando não há outras referências ao objeto. O arquivo continua no disco e pode ser lido de novo.",
 "code": """
baralho.to_csv("baralho.csv", index=False)
del baralho
baralho = pd.read_csv("baralho.csv")
print(baralho.head(3))
"""},
{"section": "Adicionando colunas",
 "text": "O tamanho do vetor atribuído deve ser igual ao número de linhas.",
 "code": """
baralho["idx"] = np.arange(1, len(baralho) + 1)
print(baralho.head())
"""},
{"section": "Alterando valores por índice",
 "code": """
baralho.loc[[0, 2, 4], "idx"] = 1
print(baralho.head())
"""},
{"section": "Alterando valores por intervalo",
 "text": "Com `loc`, o intervalo `3:5` inclui o último rótulo (diferente do fatiamento padrão do Python).",
 "code": """
baralho.loc[3:5, "idx"] = baralho.loc[3:5, "idx"] + 1
print(baralho.loc[0:6, ["idx"]])
"""},
{"section": "Vetores lógicos",
 "text": "`% 2 == 1` identifica valores ímpares e gera um vetor de `True`/`False`.",
 "code": """
vec = baralho["idx"] % 2 == 1
print(baralho.loc[vec, "idx"].head())
"""},
{"section": "Aplicando filtros",
 "code": """
cartas = baralho[vec]
print(cartas.head())
"""},
{"section": "Operações de comparação",
 "text": "Comparações entre escalares produzem um booleano; entre arrays, funcionam elemento a elemento. `np.isin` testa pertinência a um conjunto.",
 "code": """
print(1 > 2)
print(np.array([1, 2, 3]) == np.array([3, 2, 1]))
print(np.isin([1, 2, 3], [3, 4, 5]))
"""},
{"section": "Operadores lógicos",
 "text": "Em pandas e NumPy, use `&` (E) e `|` (OU), com cada condição entre parênteses.",
 "code": """
x = (baralho["face"] == "dama") & (baralho["naipe"] == "espadas")
print(baralho[x])
y = (baralho["face"] == "dama") | (baralho["naipe"] == "espadas")
print(baralho[y].head())
"""},
{"section": "Valores ausentes",
 "code": """
v = np.array([np.nan] + list(range(1, 51)))
print(np.mean(v))
print(np.nanmean(v))
"""},
{"section": "Filtrando com dados ausentes",
 "text": "Comparar `NaN` com qualquer número resulta em `False`, então linhas com ausentes somem do filtro sem aviso. Use `isna()` para encontrá-los e `dropna()`/`fillna()` para tratá-los.",
 "code": """
ordem = ["ás", "dois", "três", "quatro", "cinco", "seis", "sete",
         "oito", "nove", "dez", "valete", "dama", "rei"]
mapa = {face: i + 1 for i, face in enumerate(ordem)}
baralho["valor"] = baralho["face"].map(mapa)
baralho.loc[[0, 13, 26, 39], "valor"] = np.nan   # um ás por naipe
print(baralho[baralho["valor"] < 3])
print(baralho["valor"].isna().sum())
"""},
]}
