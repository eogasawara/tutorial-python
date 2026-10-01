LESSON = {
"file": "09-Data-Frames",
"title": "DataFrame em Python (pandas)",
"intro": """
Exemplos de código da aula sobre DataFrames: criação, colunas calculadas, leitura e gravação de arquivos, filtros e desempenho de operações vetorizadas.
""",
"cells": [
{"section": "Vetores básicos",
 "code": """
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
"""},
{"section": "Criando um DataFrame",
 "text": "Cada vetor vira uma coluna com nome. `head()` mostra as primeiras linhas.",
 "code": """
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d.head())
"""},
{"section": "Coluna calculada",
 "text": "A fórmula é aplicada a todas as linhas de uma vez (operação vetorizada).",
 "code": """
d["bmi"] = d["weight"] / d["height"]**2
print(d.round(2))
"""},
{"section": "Removendo uma coluna",
 "code": """
d = d.drop(columns=["subject"])
print(d.columns.tolist())
"""},
{"section": "Lendo um CSV",
 "text": "O conjunto Wine (UCI) tem 178 vinhos, com a classe e 13 medidas químicas. O arquivo não tem cabeçalho, por isso `header=None`; as colunas recebem os nomes 0, 1, 2...",
 "code": """
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(url, header=None)
print(wine.shape)
print(wine.iloc[:3, :6])
"""},
{"section": "Persistência com pickle",
 "text": "`to_pickle` salva o DataFrame com tipos e índice preservados. Só abra arquivos pickle que você mesmo gerou: carregar um pickle de origem desconhecida pode executar código malicioso. Para compartilhar, prefira CSV ou Parquet.",
 "code": """
wine.to_pickle("wine.pkl")
del wine
wine = pd.read_pickle("wine.pkl")
print(wine.shape)
"""},
{"section": "Exportando para CSV",
 "code": """
wine.to_csv("wine.csv", index=False)
"""},
{"section": "Filtro com máscara booleana",
 "code": """
mask = d["height"] > 1.7
print(mask)
print(d[mask].round(2))
"""},
{"section": "Desempenho: vetorizado",
 "text": "Geramos 100.000 pessoas aleatórias e calculamos o IMC sobre colunas inteiras. Os tempos abaixo foram medidos na geração deste documento e variam de máquina para máquina.",
 "code": """
from time import perf_counter
np.random.seed(42)
rheight = np.random.normal(1.8, 0.2, 100_000)
rweight = np.random.normal(72, 15, 100_000)

t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hw["bmi"] = hw["weight"] / hw["height"]**2
t_vet = perf_counter() - t0
print(f"Tempo vetorizado: {t_vet:.4f} s")
"""},
{"section": "Tipos das colunas",
 "text": "`float64` é ponto flutuante de dupla precisão (~15–16 dígitos); `int64`, inteiro; `object`, texto ou dados mistos; `bool`, verdadeiro/falso.",
 "code": "print(hw.dtypes)"},
{"section": "Antipadrão: laço sobre o DataFrame",
 "text": "Atribuir linha a linha com `loc` é muito mais lento.",
 "code": """
t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hw["bmi"] = np.nan
for i in range(len(hw)):
    hw.loc[i, "bmi"] = hw.loc[i, "weight"] / hw.loc[i, "height"]**2
t_loop = perf_counter() - t0
print(f"Tempo com loop: {t_loop:.2f} s ({t_loop / t_vet:.0f}x mais lento)")
"""},
{"section": "Laço sobre NumPy",
 "text": "Converter para NumPy antes do laço é intermediário: mais rápido que o laço no DataFrame, mais lento que a vetorização.",
 "code": """
t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hwm = hw.to_numpy()
bmi = np.empty(len(hwm))
for i in range(len(hwm)):
    bmi[i] = hwm[i, 1] / hwm[i, 0]**2
hw["bmi"] = bmi
print(f"Tempo NumPy + loop: {perf_counter() - t0:.3f} s")
"""},
]}
