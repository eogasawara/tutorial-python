# DataFrame em Python (pandas)

Slides: [09-Data-Frames.pdf](../09-Data-Frames.pdf)

Exemplos de código da aula sobre DataFrames: criação, colunas calculadas, leitura e gravação de arquivos, filtros e desempenho de operações vetorizadas.

## Vetores básicos

```python
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
```

## Criando um DataFrame

Cada vetor vira uma coluna com nome. `head()` mostra as primeiras linhas.

```python
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d.head())
```

```text
   weight  height subject
0      60    1.75       A
1      72    1.80       B
2      57    1.65       C
3      90    1.90       D
4      95    1.74       E
```

## Coluna calculada

A fórmula é aplicada a todas as linhas de uma vez (operação vetorizada).

```python
d["bmi"] = d["weight"] / d["height"]**2
print(d.round(2))
```

```text
   weight  height subject    bmi
0      60    1.75       A  19.59
1      72    1.80       B  22.22
2      57    1.65       C  20.94
3      90    1.90       D  24.93
4      95    1.74       E  31.38
5      72    1.91       F  19.74
```

## Removendo uma coluna

```python
d = d.drop(columns=["subject"])
print(d.columns.tolist())
```

```text
['weight', 'height', 'bmi']
```

## Lendo um CSV

O conjunto Wine (UCI) tem 178 vinhos, com a classe e 13 medidas químicas. O arquivo não tem cabeçalho, por isso `header=None`; as colunas recebem os nomes 0, 1, 2...

```python
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(url, header=None)
print(wine.shape)
print(wine.iloc[:3, :6])
```

```text
(178, 14)
   0      1     2     3     4    5
0  1  14.23  1.71  2.43  15.6  127
1  1  13.20  1.78  2.14  11.2  100
2  1  13.16  2.36  2.67  18.6  101
```

## Persistência com pickle

`to_pickle` salva o DataFrame com tipos e índice preservados. Só abra arquivos pickle que você mesmo gerou: carregar um pickle de origem desconhecida pode executar código malicioso. Para compartilhar, prefira CSV ou Parquet.

```python
wine.to_pickle("wine.pkl")
del wine
wine = pd.read_pickle("wine.pkl")
print(wine.shape)
```

```text
(178, 14)
```

## Exportando para CSV

```python
wine.to_csv("wine.csv", index=False)
```

## Filtro com máscara booleana

```python
mask = d["height"] > 1.7
print(mask)
print(d[mask].round(2))
```

```text
0     True
1     True
2    False
3     True
4     True
5     True
Name: height, dtype: bool
   weight  height    bmi
0      60    1.75  19.59
1      72    1.80  22.22
3      90    1.90  24.93
4      95    1.74  31.38
5      72    1.91  19.74
```

## Desempenho: vetorizado

Geramos 100.000 pessoas aleatórias e calculamos o IMC sobre colunas inteiras. Os tempos abaixo foram medidos na geração deste documento e variam de máquina para máquina.

```python
from time import perf_counter
np.random.seed(42)
rheight = np.random.normal(1.8, 0.2, 100_000)
rweight = np.random.normal(72, 15, 100_000)

t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hw["bmi"] = hw["weight"] / hw["height"]**2
t_vet = perf_counter() - t0
print(f"Tempo vetorizado: {t_vet:.4f} s")
```

```text
Tempo vetorizado: 0.0015 s
```

## Tipos das colunas

`float64` é ponto flutuante de dupla precisão (~15–16 dígitos); `int64`, inteiro; `object`, texto ou dados mistos; `bool`, verdadeiro/falso.

```python
print(hw.dtypes)
```

```text
height    float64
weight    float64
bmi       float64
dtype: object
```

## Antipadrão: laço sobre o DataFrame

Atribuir linha a linha com `loc` é muito mais lento.

```python
t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hw["bmi"] = np.nan
for i in range(len(hw)):
    hw.loc[i, "bmi"] = hw.loc[i, "weight"] / hw.loc[i, "height"]**2
t_loop = perf_counter() - t0
print(f"Tempo com loop: {t_loop:.2f} s ({t_loop / t_vet:.0f}x mais lento)")
```

```text
Tempo com loop: 8.79 s (5960x mais lento)
```

## Laço sobre NumPy

Converter para NumPy antes do laço é intermediário: mais rápido que o laço no DataFrame, mais lento que a vetorização.

```python
t0 = perf_counter()
hw = pd.DataFrame({"height": rheight, "weight": rweight})
hwm = hw.to_numpy()
bmi = np.empty(len(hwm))
for i in range(len(hwm)):
    bmi[i] = hwm[i, 1] / hwm[i, 0]**2
hw["bmi"] = bmi
print(f"Tempo NumPy + loop: {perf_counter() - t0:.3f} s")
```

```text
Tempo NumPy + loop: 0.032 s
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
