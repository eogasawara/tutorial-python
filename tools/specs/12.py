LESSON = {
"file": "12-Manipulacao-Dados",
"title": "Manipulação de Dados com Pandas",
"intro": """
Exemplos de código da aula sobre transformação de dados: junção de tabelas, filtragem, seleção, ordenação e agregação por grupos.
""",
"cells": [
{"section": "Tabela principal",
 "code": """
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d.dtypes)
"""},
{"section": "Tabela auxiliar",
 "text": "Uma segunda tabela associa cada sujeito a um estado. A coluna `subject` é a chave comum.",
 "code": """
state = np.array(["RJ", "SP", "MG", "RJ", "SP", "MG"])
ds = pd.DataFrame({"subject": subject, "state": state})
print(ds)
"""},
{"section": "Junção",
 "text": "Por padrão, `merge` faz junção interna (`how=\"inner\"`): só ficam as chaves presentes nas duas tabelas. Use `how=\"left\"` para manter todas as linhas da tabela principal.",
 "code": """
dsm = pd.merge(d, ds, on="subject")
print(dsm)
"""},
{"section": "Filtragem",
 "code": """
filtered = dsm[dsm["height"] > 1.7]
print(filtered)
"""},
{"section": "Seleção de colunas",
 "code": """
selected = filtered[["subject", "weight", "height"]]
print(selected)
"""},
{"section": "Ordenação",
 "code": """
ordered = selected.sort_values(by="height")
print(ordered)
"""},
{"section": "Encadeamento",
 "text": "As três etapas anteriores podem ser escritas como um único pipeline. Os parênteses externos permitem quebrar a expressão em várias linhas.",
 "code": """
resultado = (
    dsm[dsm["height"] > 1.7]
    [["subject", "weight", "height"]]
    .sort_values("height")
)
print(resultado)
"""},
{"section": "Agregação por grupos",
 "text": "`groupby` divide as linhas por estado e `agg` calcula, para cada grupo, a contagem de sujeitos e a altura média.",
 "code": """
grouped = dsm.groupby("state").agg(
    count=("subject", "count"),
    height=("height", "mean"),
)
print(grouped)
"""},
]}
