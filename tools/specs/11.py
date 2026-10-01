LESSON = {
"file": "11-Ordenacao",
"title": "Ordenação em Python",
"intro": """
Exemplos de código da aula sobre ordenação de vetores e tabelas: `np.sort`, `np.argsort` e `DataFrame.sort_values`.
""",
"cells": [
{"section": "Dados",
 "code": """
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = ["A", "B", "C", "D", "E", "F"]
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d)
"""},
{"section": "Ordenar valores vs obter a ordem",
 "text": "`np.sort` devolve os valores ordenados. `np.argsort` devolve as posições originais que produzem essa ordem: o menor valor estava na posição 2, o seguinte na 4, e assim por diante.",
 "code": """
print(np.sort(height))
idx = np.argsort(height)
print(idx)
"""},
{"text": "Os índices de `argsort` servem para reordenar outros vetores na mesma ordem:",
 "code": """
print(np.array(subject)[idx])
print(np.argsort(height)[::-1])   # ordem decrescente
"""},
{"section": "Ordenando uma tabela",
 "text": "`sort_values` reordena as linhas mantendo as colunas alinhadas. O índice original é preservado (a mesma ordem dada por `argsort`); use `reset_index(drop=True)` para renumerar.",
 "code": """
ds = d.sort_values("height")
print(ds)
print(ds.reset_index(drop=True))
"""},
{"section": "Crescente e decrescente",
 "code": """
print(d.sort_values("height", ascending=False))
"""},
{"section": "Múltiplas colunas",
 "text": "B e F empatam em 72 kg. Ordenando por peso e, em caso de empate, por altura decrescente, F (mais alto) vem antes de B.",
 "code": """
print(d.sort_values(["weight", "height"], ascending=[True, False]))
"""},
]}
