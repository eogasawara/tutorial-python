# Ordenação em Python

Slides: [11-Ordenacao.pdf](../11-Ordenacao.pdf)

Exemplos de código da aula sobre ordenação de vetores e tabelas: `np.sort`, `np.argsort` e `DataFrame.sort_values`.

## Dados

```python
import numpy as np
import pandas as pd

weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = ["A", "B", "C", "D", "E", "F"]
d = pd.DataFrame({"weight": weight, "height": height, "subject": subject})
print(d)
```

```text
   weight  height subject
0      60    1.75       A
1      72    1.80       B
2      57    1.65       C
3      90    1.90       D
4      95    1.74       E
5      72    1.91       F
```

## Ordenar valores vs obter a ordem

`np.sort` devolve os valores ordenados. `np.argsort` devolve as posições originais que produzem essa ordem: o menor valor estava na posição 2, o seguinte na 4, e assim por diante.

```python
print(np.sort(height))
idx = np.argsort(height)
print(idx)
```

```text
[1.65 1.74 1.75 1.8  1.9  1.91]
[2 4 0 1 3 5]
```

Os índices de `argsort` servem para reordenar outros vetores na mesma ordem:

```python
print(np.array(subject)[idx])
print(np.argsort(height)[::-1])   # ordem decrescente
```

```text
['C' 'E' 'A' 'B' 'D' 'F']
[5 3 1 0 4 2]
```

## Ordenando uma tabela

`sort_values` reordena as linhas mantendo as colunas alinhadas. O índice original é preservado (a mesma ordem dada por `argsort`); use `reset_index(drop=True)` para renumerar.

```python
ds = d.sort_values("height")
print(ds)
print(ds.reset_index(drop=True))
```

```text
   weight  height subject
2      57    1.65       C
4      95    1.74       E
0      60    1.75       A
1      72    1.80       B
3      90    1.90       D
5      72    1.91       F
   weight  height subject
0      57    1.65       C
1      95    1.74       E
2      60    1.75       A
3      72    1.80       B
4      90    1.90       D
5      72    1.91       F
```

## Crescente e decrescente

```python
print(d.sort_values("height", ascending=False))
```

```text
   weight  height subject
5      72    1.91       F
3      90    1.90       D
1      72    1.80       B
0      60    1.75       A
4      95    1.74       E
2      57    1.65       C
```

## Múltiplas colunas

B e F empatam em 72 kg. Ordenando por peso e, em caso de empate, por altura decrescente, F (mais alto) vem antes de B.

```python
print(d.sort_values(["weight", "height"], ascending=[True, False]))
```

```text
   weight  height subject
2      57    1.65       C
0      60    1.75       A
5      72    1.91       F
1      72    1.80       B
3      90    1.90       D
4      95    1.74       E
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
