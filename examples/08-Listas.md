# Listas em Python

Slides: [08-Listas.pdf](../08-Listas.pdf)

Exemplos de código da aula sobre listas, dicionários, `dataclass` e mutabilidade.

## O que são listas

Uma lista é uma coleção ordenada, acessada por índice a partir de zero. Os elementos podem ter tipos diferentes.

```python
my_list = [1, "a", 3.5, True]
my_list
```

```text
[1, 'a', 3.5, True]
```

## Criando listas

Uma lista pode guardar arrays, outras listas, números e textos ao mesmo tempo.

```python
import numpy as np
weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = ["A", "B", "C", "D", "E", "F"]
mybag = [weight, height, subject, 0, "a"]
len(mybag), type(mybag)
```

```text
(5, <class 'list'>)
```

## Conteúdo da lista

Cada posição mantém o tipo do objeto armazenado. `enumerate` devolve a posição e o elemento.

```python
for i, item in enumerate(mybag):
    print(i, type(item))
```

```text
0 <class 'numpy.ndarray'>
1 <class 'numpy.ndarray'>
2 <class 'list'>
3 <class 'int'>
4 <class 'str'>
```

## Fatiamento

O início é incluído e o fim é excluído: `[0:3]` devolve as posições 0, 1 e 2.

```python
print(len(mybag[0:3]), len(mybag[:2]))
```

```text
3 2
```

## Elemento vs sublista

Um índice único devolve o próprio objeto; um intervalo devolve uma nova lista.

```python
print(type(mybag[0:1]), mybag[0:1])
print(type(mybag[0]), mybag[0])
```

```text
<class 'list'> [array([60, 72, 57, 90, 95, 72])]
<class 'numpy.ndarray'> [60 72 57 90 95 72]
```

## Dicionários

Um `dict` associa chaves a valores. Use lista quando a posição importa e dicionário quando o nome importa.

```python
bag = {"weight": weight, "height": height, "subject": subject}
print(bag["weight"])
bag["nome"] = "a"
print(list(bag.keys()))
```

```text
[60 72 57 90 95 72]
['weight', 'height', 'subject', 'nome']
```

## Registros com dataclass

Quando os campos são fixos, uma `dataclass` dá nome e tipo a cada um, acessados por ponto. Campos opcionais recebem valor padrão.

```python
from dataclasses import dataclass

@dataclass
class Bag:
    weight: np.ndarray
    height: np.ndarray
    subject: list
    valor: int | None = None
    nome: str | None = None
    bmi: np.ndarray | None = None

mybag = Bag(weight, height, subject)
mybag.weight
```

```text
array([60, 72, 57, 90, 95, 72])
```

## Campos opcionais

Como `bmi` foi declarado na classe, ele aparece na representação do objeto. Um atributo criado fora da classe não apareceria.

```python
mybag.bmi = (mybag.weight / mybag.height**2).round(2)
mybag
```

```text
Bag(weight=array([60, 72, 57, 90, 95, 72]), height=array([1.75, 1.8 , 1.65, 1.9 , 1.74, 1.91]), subject=['A', 'B', 'C', 'D', 'E', 'F'], valor=None, nome=None, bmi=array([19.59, 22.22, 20.94, 24.93, 31.38, 19.74]))
```

## Mutabilidade e cópias

Atribuir (`a = lista`) não copia: os dois nomes apontam para o mesmo objeto. `.copy()` faz uma cópia rasa: a lista é nova, mas os objetos internos são compartilhados. Por isso alterar `a[0][0]` muda também `b` e o próprio `weight`.

```python
mybag_list = [weight, height, subject]
a = mybag_list
b = mybag_list.copy()
a[0][0] = 999
print(a[0][0], b[0][0], weight[0])
```

```text
999 999 999
```

`copy.deepcopy` copia também os objetos internos, gerando uma estrutura independente.

```python
import copy
c = copy.deepcopy(mybag_list)
a[0][0] = 60
print(c[0][0], weight[0])
```

```text
999 60
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
