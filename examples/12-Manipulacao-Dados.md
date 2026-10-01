# Manipulação de Dados com Pandas

Slides: [12-Manipulacao-Dados.pdf](../12-Manipulacao-Dados.pdf)

Exemplos de código da aula sobre transformação de dados: junção de tabelas, filtragem, seleção, ordenação e agregação por grupos.

## Tabela principal

```python
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d.dtypes)
```

```text
weight       int64
height     float64
subject     object
dtype: object
```

## Tabela auxiliar

Uma segunda tabela associa cada sujeito a um estado. A coluna `subject` é a chave comum.

```python
state = np.array(["RJ", "SP", "MG", "RJ", "SP", "MG"])
ds = pd.DataFrame({"subject": subject, "state": state})
print(ds)
```

```text
  subject state
0       A    RJ
1       B    SP
2       C    MG
3       D    RJ
4       E    SP
5       F    MG
```

## Junção

Por padrão, `merge` faz junção interna (`how="inner"`): só ficam as chaves presentes nas duas tabelas. Use `how="left"` para manter todas as linhas da tabela principal.

```python
dsm = pd.merge(d, ds, on="subject")
print(dsm)
```

```text
   weight  height subject state
0      60    1.75       A    RJ
1      72    1.80       B    SP
2      57    1.65       C    MG
3      90    1.90       D    RJ
4      95    1.74       E    SP
5      72    1.91       F    MG
```

## Filtragem

```python
filtered = dsm[dsm["height"] > 1.7]
print(filtered)
```

```text
   weight  height subject state
0      60    1.75       A    RJ
1      72    1.80       B    SP
3      90    1.90       D    RJ
4      95    1.74       E    SP
5      72    1.91       F    MG
```

## Seleção de colunas

```python
selected = filtered[["subject", "weight", "height"]]
print(selected)
```

```text
  subject  weight  height
0       A      60    1.75
1       B      72    1.80
3       D      90    1.90
4       E      95    1.74
5       F      72    1.91
```

## Ordenação

```python
ordered = selected.sort_values(by="height")
print(ordered)
```

```text
  subject  weight  height
4       E      95    1.74
0       A      60    1.75
1       B      72    1.80
3       D      90    1.90
5       F      72    1.91
```

## Encadeamento

As três etapas anteriores podem ser escritas como um único pipeline. Os parênteses externos permitem quebrar a expressão em várias linhas.

```python
resultado = (
    dsm[dsm["height"] > 1.7]
    [["subject", "weight", "height"]]
    .sort_values("height")
)
print(resultado)
```

```text
  subject  weight  height
4       E      95    1.74
0       A      60    1.75
1       B      72    1.80
3       D      90    1.90
5       F      72    1.91
```

## Agregação por grupos

`groupby` divide as linhas por estado e `agg` calcula, para cada grupo, a contagem de sujeitos e a altura média.

```python
grouped = dsm.groupby("state").agg(
    count=("subject", "count"),
    height=("height", "mean"),
)
print(grouped)
```

```text
       count  height
state               
MG         2   1.780
RJ         2   1.825
SP         2   1.770
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
