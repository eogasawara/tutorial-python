# Modificação de Valores em Python

Slides: [05-Modificacao-Valores.pdf](../05-Modificacao-Valores.pdf)

Exemplos de código da aula sobre atribuição, estado do programa e modificação de valores em tabelas. O baralho é carregado de `examples/baralho.csv`, neste repositório.

```python
import numpy as np
import pandas as pd
```

## Atribuição e estado

Cada atribuição substitui o valor anterior; o valor antigo não é lembrado.

```python
x = 10
x = x + 5
print(x)
```

```text
15
```

## Execução sequencial

`b` é calculado quando `a` vale 5. Mudar `a` depois não recalcula `b`.

```python
a = 5
b = a * 2
a = 10
print(b)
```

```text
10
```

## Carregando dados de uma URL

`read_csv` aceita uma URL e converte o arquivo remoto em DataFrame.

```python
url = "https://raw.githubusercontent.com/eogasawara/tutorial-python/main/examples/baralho.csv"
baralho = pd.read_csv(url)
print(baralho.shape)
print(baralho.head())
```

```text
(52, 2)
     face  naipe
0      ás  ouros
1    dois  ouros
2    três  ouros
3  quatro  ouros
4   cinco  ouros
```

## Salvando e recarregando

`del` apaga o nome `baralho`; a memória é liberada quando não há outras referências ao objeto. O arquivo continua no disco e pode ser lido de novo.

```python
baralho.to_csv("baralho.csv", index=False)
del baralho
baralho = pd.read_csv("baralho.csv")
print(baralho.head(3))
```

```text
   face  naipe
0    ás  ouros
1  dois  ouros
2  três  ouros
```

## Adicionando colunas

O tamanho do vetor atribuído deve ser igual ao número de linhas.

```python
baralho["idx"] = np.arange(1, len(baralho) + 1)
print(baralho.head())
```

```text
     face  naipe  idx
0      ás  ouros    1
1    dois  ouros    2
2    três  ouros    3
3  quatro  ouros    4
4   cinco  ouros    5
```

## Alterando valores por índice

```python
baralho.loc[[0, 2, 4], "idx"] = 1
print(baralho.head())
```

```text
     face  naipe  idx
0      ás  ouros    1
1    dois  ouros    2
2    três  ouros    1
3  quatro  ouros    4
4   cinco  ouros    1
```

## Alterando valores por intervalo

Com `loc`, o intervalo `3:5` inclui o último rótulo (diferente do fatiamento padrão do Python).

```python
baralho.loc[3:5, "idx"] = baralho.loc[3:5, "idx"] + 1
print(baralho.loc[0:6, ["idx"]])
```

```text
   idx
0    1
1    2
2    1
3    5
4    2
5    7
6    7
```

## Vetores lógicos

`% 2 == 1` identifica valores ímpares e gera um vetor de `True`/`False`.

```python
vec = baralho["idx"] % 2 == 1
print(baralho.loc[vec, "idx"].head())
```

```text
0    1
2    1
3    5
5    7
6    7
Name: idx, dtype: int64
```

## Aplicando filtros

```python
cartas = baralho[vec]
print(cartas.head())
```

```text
     face  naipe  idx
0      ás  ouros    1
2    três  ouros    1
3  quatro  ouros    5
5    seis  ouros    7
6    sete  ouros    7
```

## Operações de comparação

Comparações entre escalares produzem um booleano; entre arrays, funcionam elemento a elemento. `np.isin` testa pertinência a um conjunto.

```python
print(1 > 2)
print(np.array([1, 2, 3]) == np.array([3, 2, 1]))
print(np.isin([1, 2, 3], [3, 4, 5]))
```

```text
False
[False  True False]
[False False  True]
```

## Operadores lógicos

Em pandas e NumPy, use `&` (E) e `|` (OU), com cada condição entre parênteses.

```python
x = (baralho["face"] == "dama") & (baralho["naipe"] == "espadas")
print(baralho[x])
y = (baralho["face"] == "dama") | (baralho["naipe"] == "espadas")
print(baralho[y].head())
```

```text
    face    naipe  idx
50  dama  espadas   51
    face    naipe  idx
11  dama    ouros   12
24  dama    copas   25
37  dama     paus   38
39    ás  espadas   40
40  dois  espadas   41
```

## Valores ausentes

```python
v = np.array([np.nan] + list(range(1, 51)))
print(np.mean(v))
print(np.nanmean(v))
```

```text
nan
25.5
```

## Filtrando com dados ausentes

Comparar `NaN` com qualquer número resulta em `False`, então linhas com ausentes somem do filtro sem aviso. Use `isna()` para encontrá-los e `dropna()`/`fillna()` para tratá-los.

```python
ordem = ["ás", "dois", "três", "quatro", "cinco", "seis", "sete",
         "oito", "nove", "dez", "valete", "dama", "rei"]
mapa = {face: i + 1 for i, face in enumerate(ordem)}
baralho["valor"] = baralho["face"].map(mapa)
baralho.loc[[0, 13, 26, 39], "valor"] = np.nan   # um ás por naipe
print(baralho[baralho["valor"] < 3])
print(baralho["valor"].isna().sum())
```

```text
    face    naipe  idx  valor
1   dois    ouros    2    2.0
14  dois    copas   15    2.0
27  dois     paus   28    2.0
40  dois  espadas   41    2.0
4
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
