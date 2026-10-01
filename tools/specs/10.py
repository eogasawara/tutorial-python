LESSON = {
"file": "10-Vetorizacao",
"title": "Iteração Implícita em Python",
"intro": """
Exemplos de código da aula sobre iteração implícita: funções aplicadas a colunas, linhas e elementos sem laços explícitos, com NumPy e pandas.
""",
"cells": [
{"section": "Estruturas vetorizadas",
 "code": """
import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4])
np.mean(x)
"""},
{"section": "Tabela de exemplo",
 "code": """
df = pd.DataFrame({
    "weight": [60, 72, 57, 90, 95, 72],
    "height": [1.75, 1.80, 1.65, 1.90, 1.74, 1.91],
    "subject": ["A", "B", "C", "D", "E", "F"],
})
df.shape
"""},
{"section": "Colunas numéricas",
 "text": "`select_dtypes` separa as colunas numéricas, evitando erros ao calcular estatísticas sobre texto.",
 "code": """
num_cols = df.select_dtypes(include="number")
num_cols.mean()
"""},
{"section": "O parâmetro axis",
 "text": "Em uma matriz, `axis=0` percorre as linhas e produz um resultado por coluna; `axis=1` percorre as colunas e produz um resultado por linha.",
 "code": """
m = num_cols.to_numpy()
print(np.min(m, axis=1))
print(np.min(m, axis=0))
"""},
{"section": "Operações elemento a elemento",
 "text": "O expoente 2 (escalar) é aplicado a cada elemento. Entre duas colunas, o pandas alinha os valores pelo índice.",
 "code": 'df["height"] ** 2'},
{"section": "Cálculo derivado sem laço",
 "code": """
df["bmi"] = df["weight"] / df["height"]**2
print(df.round(2))
"""},
{"section": "apply por coluna",
 "text": "`apply` aplica uma função a cada coluna (padrão) e devolve um resultado por coluna.",
 "code": """
cols = ["weight", "height"]
df[cols].apply(np.mean)
"""},
{"section": "apply por linha",
 "text": "Com `axis=1`, a função recebe uma linha por vez. Funciona para qualquer lógica, mas é mais lento que a operação vetorizada.",
 "code": """
df.apply(lambda r: r["weight"] / r["height"]**2, axis=1).round(2)
"""},
{"section": "map por elemento",
 "code": """
df["subject"].map(str.lower)
"""},
{"section": "Compreensão de dicionário",
 "text": "Outra forma de aplicar a mesma operação a várias colunas, guardando o resultado por nome.",
 "code": """
means = {col: round(df[col].mean(), 2) for col in cols}
means
""",
 "after": "Use `apply`/`map` quando não existir uma operação vetorizada pronta. Quando ela existir, como no IMC, a vetorização é sempre mais rápida."},
]}
