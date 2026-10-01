# Indexação de DataFrames em Python

Slides: [04-Indexacao.pdf](../04-Indexacao.pdf)

Exemplos de código da aula sobre acesso e indexação de dados. Construímos um baralho de 52 cartas e o usamos para praticar `iloc`, `loc`, filtros booleanos, visões e cópias.

```python
import numpy as np
import pandas as pd
```

## Construindo o baralho

Percorremos os naipes e, dentro de cada naipe, as 13 faces. A compreensão de lista gera os 52 pares (face, naipe), que viram as linhas do DataFrame.

```python
faces = ["ás", "dois", "três", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "valete", "dama", "rei"]
naipes = ["ouros", "copas", "paus", "espadas"]
baralho = pd.DataFrame(
    [(f, n) for n in naipes for f in faces],
    columns=["face", "naipe"]
)
print(len(baralho))
print(baralho.head())
```

```text
52
     face  naipe
0      ás  ouros
1    dois  ouros
2    três  ouros
3  quatro  ouros
4   cinco  ouros
```

## Nova coluna

`np.tile` repete a sequência de 1 a 13 quatro vezes, uma para cada naipe, atribuindo o valor numérico de cada carta.

```python
baralho["valor"] = np.tile(np.arange(1, 14), 4)
print(baralho.head())
```

```text
     face  naipe  valor
0      ás  ouros      1
1    dois  ouros      2
2    três  ouros      3
3  quatro  ouros      4
4   cinco  ouros      5
```

## Formas de acesso

`iloc` acessa por posição; `loc` acessa por rótulo (índice e nome de coluna); uma expressão booleana filtra linhas.

```python
print(baralho.iloc[0, 1])
print(baralho.loc[0, "naipe"])
print(baralho[baralho["valor"] > 10].head(3))
```

```text
ouros
ouros
      face  naipe  valor
10  valete  ouros     11
11    dama  ouros     12
12     rei  ouros     13
```

## Colunas como Séries

Uma única coluna é uma `Series`: estrutura unidimensional que mantém o índice original.

```python
print(baralho.iloc[0, 0])
print(baralho["face"].iloc[[0, 1]])
```

```text
ás
0      ás
1    dois
Name: face, dtype: object
```

## Sintaxes equivalentes

As três expressões abaixo devolvem a mesma Series (linhas 10 e 13 da coluna `face`).

```python
print(baralho.loc[[10, 13], "face"].tolist())
print(baralho.iloc[[10, 13], 0].tolist())
print(baralho["face"].iloc[[10, 13]].tolist())
```

```text
['valete', 'ás']
['valete', 'ás']
['valete', 'ás']
```

## Várias colunas

Selecionando mais de uma coluna, o resultado é um DataFrame. Note que o fatiamento posicional `10:12` exclui o fim.

```python
print(baralho.iloc[10:12, 0:2])
print(baralho.loc[[10, 13], ["face", "naipe"]])
```

```text
      face  naipe
10  valete  ouros
11    dama  ouros
      face  naipe
10  valete  ouros
13      ás  copas
```

## Series vs DataFrame

Colchetes simples devolvem uma Series; colchetes duplos (uma lista de nomes) preservam a estrutura de tabela.

```python
print(type(baralho["face"]))
print(type(baralho[["face"]]))
```

```text
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
```

## Removendo linhas e colunas

`drop()` remove pelo rótulo e devolve um novo DataFrame; para manter o resultado, reatribua. Atenção: em Python, índices negativos não removem nada, `x[-1]` é o último elemento.

```python
print(baralho.drop(index=range(3)).head(3))
print(baralho.drop(columns=["face"]).head(3))
```

```text
     face  naipe  valor
3  quatro  ouros      4
4   cinco  ouros      5
5    seis  ouros      6
   naipe  valor
0  ouros      1
1  ouros      2
2  ouros      3
```

## Linhas e colunas inteiras

```python
print(baralho.iloc[0])
print(baralho["naipe"].head())
```

```text
face        ás
naipe    ouros
valor        1
Name: 0, dtype: object
0    ouros
1    ouros
2    ouros
3    ouros
4    ouros
Name: naipe, dtype: object
```

## Máscara booleana sobre colunas

Cada `True` indica uma coluna que deve permanecer.

```python
mask = [True, True, False]
print(baralho.loc[:, mask].head())
```

```text
     face  naipe
0      ás  ouros
1    dois  ouros
2    três  ouros
3  quatro  ouros
4   cinco  ouros
```

## Máscara booleana sobre linhas

A forma mais comum de filtrar: a condição gera uma Series de `True`/`False` e só as linhas `True` permanecem.

```python
filtro = baralho["valor"] < 3
print(baralho[filtro])
```

```text
    face    naipe  valor
0     ás    ouros      1
1   dois    ouros      2
13    ás    copas      1
14  dois    copas      2
26    ás     paus      1
27  dois     paus      2
39    ás  espadas      1
40  dois  espadas      2
```

## Embaralhando

`np.random.permutation` gera uma ordem aleatória das posições, aplicada com `iloc`. A semente torna o exemplo reproduzível.

```python
np.random.seed(42)
ordem = np.random.permutation(len(baralho))
cartas = baralho.iloc[ordem]
print(cartas.head())
```

```text
     face    naipe  valor
19   sete    copas      7
41   três  espadas      3
47   nove  espadas      9
12    rei    ouros     13
43  cinco  espadas      5
```

## Encapsulando em uma função

```python
def embaralhar(df):
    ordem = np.random.permutation(len(df))
    return df.iloc[ordem]

print(embaralhar(baralho).head(3))
```

```text
      face  naipe  valor
38     rei   paus     13
10  valete  ouros     11
4    cinco  ouros      5
```

## Tipos de dados (dtype)

```python
a = np.array([1, 2, 3])
b = np.array([1.0, 2.0, 3.0])
print(a.dtype, b.dtype)
print(baralho.dtypes)
```

```text
int64 float64
face     object
naipe    object
valor     int64
dtype: object
```

## Broadcasting

NumPy combina arrays de formas compatíveis: cada dimensão deve ser igual ou valer 1. Um escalar se expande para todo o array; formas incompatíveis geram erro.

```python
x = np.array([1, 2, 3, 4])
x + 10
```

```text
array([11, 12, 13, 14])
```

```python
x + np.array([1, 2])
```

```text
ValueError: operands could not be broadcast together with shapes (4,) (2,)
```

## Visão e cópia

O fatiamento cria uma visão: modificá-la altera o array original. `.copy()` cria dados independentes.

```python
x = np.array([1, 2, 3, 4])
y = x[0:2]          # visão
z = x[0:2].copy()   # cópia
y[0] = 99
x, y, z
```

```text
(array([99,  2,  3,  4]), array([99,  2]), array([1, 2]))
```

## Indexação por lista de índices

Indexar com uma lista de posições sempre cria uma cópia: alterar o resultado não afeta o original.

```python
x = np.array([10, 20, 30, 40, 50])
sel = x[[0, 2, 4]]
sel[0] = -1
print(sel, x)
```

```text
[-1 30 50] [10 20 30 40 50]
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
