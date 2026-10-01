# Iteração Implícita em Python

Slides: [10-Vetorizacao.pdf](../10-Vetorizacao.pdf)

Exemplos de código da aula sobre iteração implícita: funções aplicadas a colunas, linhas e elementos sem laços explícitos, com NumPy e pandas.

## Estruturas vetorizadas

```python
import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4])
np.mean(x)
```

```text
np.float64(2.5)
```

## Tabela de exemplo

```python
df = pd.DataFrame({
    "weight": [60, 72, 57, 90, 95, 72],
    "height": [1.75, 1.80, 1.65, 1.90, 1.74, 1.91],
    "subject": ["A", "B", "C", "D", "E", "F"],
})
df.shape
```

```text
(6, 3)
```

## Colunas numéricas

`select_dtypes` separa as colunas numéricas, evitando erros ao calcular estatísticas sobre texto.

```python
num_cols = df.select_dtypes(include="number")
num_cols.mean()
```

```text
weight    74.333333
height     1.791667
dtype: float64
```

## O parâmetro axis

Em uma matriz, `axis=0` percorre as linhas e produz um resultado por coluna; `axis=1` percorre as colunas e produz um resultado por linha.

```python
m = num_cols.to_numpy()
print(np.min(m, axis=1))
print(np.min(m, axis=0))
```

```text
[1.75 1.8  1.65 1.9  1.74 1.91]
[57.    1.65]
```

## Operações elemento a elemento

O expoente 2 (escalar) é aplicado a cada elemento. Entre duas colunas, o pandas alinha os valores pelo índice.

```python
df["height"] ** 2
```

```text
0    3.0625
1    3.2400
2    2.7225
3    3.6100
4    3.0276
5    3.6481
Name: height, dtype: float64
```

## Cálculo derivado sem laço

```python
df["bmi"] = df["weight"] / df["height"]**2
print(df.round(2))
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

## apply por coluna

`apply` aplica uma função a cada coluna (padrão) e devolve um resultado por coluna.

```python
cols = ["weight", "height"]
df[cols].apply(np.mean)
```

```text
weight    74.333333
height     1.791667
dtype: float64
```

## apply por linha

Com `axis=1`, a função recebe uma linha por vez. Funciona para qualquer lógica, mas é mais lento que a operação vetorizada.

```python
df.apply(lambda r: r["weight"] / r["height"]**2, axis=1).round(2)
```

```text
0    19.59
1    22.22
2    20.94
3    24.93
4    31.38
5    19.74
dtype: float64
```

## map por elemento

```python
df["subject"].map(str.lower)
```

```text
0    a
1    b
2    c
3    d
4    e
5    f
Name: subject, dtype: object
```

## Compreensão de dicionário

Outra forma de aplicar a mesma operação a várias colunas, guardando o resultado por nome.

```python
means = {col: round(df[col].mean(), 2) for col in cols}
means
```

```text
{'weight': np.float64(74.33), 'height': np.float64(1.79)}
```

Use `apply`/`map` quando não existir uma operação vetorizada pronta. Quando ela existir, como no IMC, a vetorização é sempre mais rápida.

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
