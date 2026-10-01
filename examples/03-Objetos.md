# Objetos em Python

Slides: [03-Objetos.pdf](../03-Objetos.pdf)

Exemplos de código da aula sobre objetos, tipos e valores. Em Python, todo valor é um objeto e possui um tipo, que define as operações permitidas.

```python
import numpy as np
import pandas as pd
```

## Variáveis

Uma variável é um nome associado a um valor. Ao reatribuir, o nome passa a apontar para o novo valor.

```python
idade = 30
idade = idade + 1
idade
```

```text
31
```

## Objetos, tipos e valores

`type()` mostra o tipo de um objeto. Operações produzem novos objetos.

```python
a = 5
b = 2
c = a * b
type(c)
```

```text
<class 'int'>
```

## DataFrames

Um DataFrame do pandas organiza dados em linhas (registros) e colunas (atributos). Cada coluna pode ter um tipo diferente.

```python
df = pd.DataFrame({
    "face": ["ás", "dois", "quatro"],
    "naipe": ["ouros", "copas", "paus"],
    "valor": [1, 2, 4],
})
print(df)
```

```text
     face  naipe  valor
0      ás  ouros      1
1    dois  copas      2
2  quatro   paus      4
```

## Salvando e lendo CSV

`to_csv` grava a tabela em texto; `index=False` evita gravar a coluna de índice. `read_csv` lê o arquivo de volta.

```python
df.to_csv("cartas.csv", index=False)
cartas = pd.read_csv("cartas.csv")
print(cartas)
```

```text
     face  naipe  valor
0      ás  ouros      1
1    dois  copas      2
2  quatro   paus      4
```

## Valores ausentes

`None` indica ausência de um objeto qualquer; `np.nan` representa um número ausente e é usado em cálculos numéricos. Funções comuns retornam `nan` quando há ausentes; as versões com prefixo `nan` os ignoram.

```python
y = np.array([1.0, np.nan, 3.0])
print(np.mean(y))
print(np.nanmean(y))
print(np.isnan(y))
```

```text
nan
2.0
[False  True False]
```

Em tabelas pandas, `dropna()` remove e `fillna()` preenche valores ausentes.

```python
s = pd.Series(y)
print(s.dropna().tolist(), s.fillna(0).tolist())
```

```text
[1.0, 3.0] [1.0, 0.0, 3.0]
```

## Tipos simples e estruturas

Números e textos representam valores únicos; listas e dicionários agrupam vários valores. Cada tipo tem métodos próprios.

```python
print(type(10), type([1, 2, 3]))
"dados".upper()
```

```text
<class 'int'> <class 'list'>
'DADOS'
```

## Arrays do NumPy

Arrays armazenam vários valores do mesmo tipo de forma eficiente.

```python
dado = np.array([1, 2, 3, 4, 5, 6])
dado
```

```text
array([1, 2, 3, 4, 5, 6])
```

## Escalar vs array de tamanho 1

Um número solto é um escalar e não tem tamanho; já `np.array([5])` é um vetor com um elemento.

```python
len(5)
```

```text
TypeError: object of type 'int' has no len()
```

```python
vetor = np.array([5])
print(len(vetor), len(dado))
```

```text
1 6
```

## Inteiros e textos

```python
print(type(1), type("ás"))
```

```text
<class 'int'> <class 'str'>
```

## Funções sobre sequências

Funções agregadoras resumem uma sequência numérica. Textos também podem ser comparados: a ordem segue os códigos Unicode, e letras acentuadas, como `á`, vêm depois de `z`. Por isso o maior elemento é `'ás'`.

```python
cartas = np.arange(1, 14)
print(np.sum(cartas))
faces = ["ás", "dois", "três", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "valete", "dama", "rei"]
print(max(faces))
print(sorted(faces)[:3])
```

```text
91
ás
['cinco', 'dama', 'dez']
```

## Ponto flutuante (float)

Números decimais usam ponto flutuante de dupla precisão (`float64`, cerca de 15 a 16 dígitos significativos).

```python
dado = np.array([1, 2, 3, 4, 5, 6], dtype=float)
print(dado, dado.dtype)
```

```text
[1. 2. 3. 4. 5. 6.] float64
```

O float binário tem erros de arredondamento. Para valores monetários, use `decimal.Decimal`.

```python
from decimal import Decimal
print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
```

```text
False
True
```

## Booleanos

Comparações produzem `True` ou `False`, usados em decisões e filtros.

```python
logico = np.array([True, False, 3 >= 4, 3 < 4, 3 != 4, 4 == 4])
logico
```

```text
array([ True, False, False,  True,  True,  True])
```

## Números complexos

Python suporta números complexos nativamente; a parte imaginária usa o sufixo `j`.

```python
comp = np.array([1+1j, 1+2j, 1+3j])
print(comp, comp.dtype)
```

```text
[1.+1.j 1.+2.j 1.+3.j] complex128
```

## Bytes

Cada byte guarda um valor de 0 a 255. Valores fora do intervalo geram erro e precisam ser convertidos explicitamente.

```python
r = bytearray(3)
r[1] = 255
r[2] = 1024 % 256   # conversão explícita: 0
r
```

```text
bytearray(b'\x00\xff\x00')
```

```python
r[2] = 1024
```

```text
ValueError: byte must be in range(0, 256)
```

## Rótulos e atributos

Para dar nome a cada valor, usamos uma `pd.Series` com índice. Já os atributos (acessados com ponto) descrevem o próprio objeto.

```python
dado = np.array([1, 2, 3, 4, 5, 6])
nomes = ["um", "dois", "três", "quatro", "cinco", "seis"]
rotulado = pd.Series(dado, index=nomes)
print(rotulado["três"])
print(dado.dtype, dado.shape, dado.ndim)
```

```text
3
int64 (6,) 1
```

## Matrizes

`reshape` reorganiza os dados em outra forma. O padrão (`order="C"`) preenche linha por linha; `order="F"` preenche coluna por coluna.

```python
dado = np.arange(1, 7)
print(dado.reshape((2, 3), order="C"))
print(dado.reshape((2, 3), order="F"))
```

```text
[[1 2 3]
 [4 5 6]]
[[1 3 5]
 [2 4 6]]
```

## Tipo e forma

```python
dado = np.arange(1, 7).reshape((2, 3))
print(type(dado))
print(dado.shape)
```

```text
<class 'numpy.ndarray'>
(2, 3)
```

## Data e hora

O módulo `datetime` representa datas e horas. Aqui usamos uma data fixa para que a saída seja sempre a mesma; `datetime.now()` devolve o instante atual.

```python
from datetime import datetime
d = datetime(2024, 1, 15, 14, 30)
print(d, type(d))
print(d.year, d.strftime("%d/%m/%Y"))
```

```text
2024-01-15 14:30:00 <class 'datetime.datetime'>
2024 15/01/2024
```

## Dados categóricos

`pd.Categorical` representa grupos fixos e armazena cada categoria uma única vez.

```python
genero = pd.Categorical(["feminino", "masculino", "feminino", "masculino"])
genero
```

```text
['feminino', 'masculino', 'feminino', 'masculino']
Categories (2, object): ['feminino', 'masculino']
```

## Conversões de tipo

```python
print(int(True), int(False))
print(float(True), float(False))
print(bool(1), bool(0))
print(repr(str(1)), repr(str(True)))
```

```text
1 0
1.0 0.0
True False
'1' 'True'
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
