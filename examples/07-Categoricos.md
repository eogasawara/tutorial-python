# Variáveis Categóricas em Python

Slides: [07-Categoricos.pdf](../07-Categoricos.pdf)

Exemplos de código da aula sobre dados categóricos com `pandas.Categorical`: categorias, códigos internos, ordem e classificação por intervalos com `pd.cut`.

```python
import numpy as np
import pandas as pd
```

## Dados categóricos

Um `Categorical` guarda valores de um conjunto finito de categorias. Por padrão, as categorias ficam em ordem alfabética.

```python
cores = pd.Categorical(["vermelho", "azul", "verde", "azul"])
cores
```

```text
['vermelho', 'azul', 'verde', 'azul']
Categories (3, object): ['azul', 'verde', 'vermelho']
```

## Códigos e categorias

Internamente, cada valor é um código inteiro que aponta para a lista `categories`. Isso economiza memória quando há muitas repetições.

```python
print(cores.codes)
print(cores.categories)
```

```text
[2 0 1 0]
Index(['azul', 'verde', 'vermelho'], dtype='object')
```

## Categorias ordenadas

Com `ordered=True` e uma lista explícita de categorias, a ordem lógica permite comparações e ordenação corretas.

```python
nivel = pd.Categorical(["médio", "baixo", "alto"],
                       categories=["baixo", "médio", "alto"], ordered=True)
print(nivel)
print(nivel < "alto")
```

```text
['médio', 'baixo', 'alto']
Categories (3, object): ['baixo' < 'médio' < 'alto']
[ True  True False]
```

## Escala de dor

```python
pain = [0, 3, 2, 2, 1]
fpain = pd.Categorical(pain, categories=[0, 1, 2, 3], ordered=True)
fpain
```

```text
[0, 3, 2, 2, 1]
Categories (4, int64): [0 < 1 < 2 < 3]
```

## Rótulos descritivos

Um dicionário converte os códigos numéricos em textos; a lista `categories` mantém a ordem lógica.

```python
mapa = {0: "sem", 1: "baixa", 2: "média", 3: "alta"}
pain_txt = [mapa[x] for x in pain]
fpain_lbl = pd.Categorical(pain_txt,
                           categories=["sem", "baixa", "média", "alta"], ordered=True)
fpain_lbl
```

```text
['sem', 'alta', 'média', 'média', 'baixa']
Categories (4, object): ['sem' < 'baixa' < 'média' < 'alta']
```

## Caso prático: alturas

```python
weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
height
```

```text
array([1.75, 1.8 , 1.65, 1.9 , 1.74, 1.91])
```

## Método 1: if / elif / else

Regras: altura < 1,70 m é baixa; de 1,70 m até menos de 1,90 m é média; a partir de 1,90 m é alta.

```python
labels = []
for h in height:
    if h < 1.7:
        labels.append("baixa")
    elif h < 1.9:
        labels.append("média")
    else:
        labels.append("alta")
labels
```

```text
['média', 'média', 'baixa', 'alta', 'média', 'alta']
```

Convertemos a lista em um categórico ordenado:

```python
height_cat = pd.Categorical(labels, categories=["baixa", "média", "alta"], ordered=True)
height_cat
```

```text
['média', 'média', 'baixa', 'alta', 'média', 'alta']
Categories (3, object): ['baixa' < 'média' < 'alta']
```

## Método 2: pd.cut

`pd.cut` classifica todos os valores de uma vez. Por padrão os intervalos são fechados à direita, `(a, b]`; com `right=False` passam a ser `[a, b)`, exatamente as regras do Método 1.

```python
height_cat2 = pd.cut(
    height,
    bins=[0, 1.7, 1.9, np.inf],
    labels=["baixa", "média", "alta"],
    right=False,
)
height_cat2
```

```text
['média', 'média', 'baixa', 'alta', 'média', 'alta']
Categories (3, object): ['baixa' < 'média' < 'alta']
```

Sem `right=False`, a altura 1,90 cairia em `(1.7, 1.9]` e seria classificada como média:

```python
list(pd.cut(height, bins=[0, 1.7, 1.9, np.inf], labels=["baixa", "média", "alta"]))
```

```text
['média', 'média', 'baixa', 'média', 'média', 'alta']
```

## Contagem por categoria

```python
pd.Series(height_cat2).value_counts()
```

```text
média    3
alta     2
baixa    1
Name: count, dtype: int64
```

## Convertendo uma coluna de texto

`astype("category")` converte uma Series existente. Sem lista de categorias, a ordem é alfabética.

```python
s = pd.Series(["baixa", "média", "alta", "média"])
s_cat = s.astype("category")
print(s_cat.cat.categories)
print(s_cat.cat.codes)
```

```text
Index(['alta', 'baixa', 'média'], dtype='object')
0    1
1    2
2    0
3    2
dtype: int8
```

Para impor a ordem lógica, use um `CategoricalDtype`:

```python
tipo = pd.CategoricalDtype(["baixa", "média", "alta"], ordered=True)
s_ord = s.astype(tipo)
print(s_ord.sort_values().tolist())
```

```text
['baixa', 'média', 'média', 'alta']
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
