# Estrutura de Repetição em Python

Slides: [06-Estrutura-Repeticao.pdf](../06-Estrutura-Repeticao.pdf)

Exemplos de código da aula sobre decisões (`if`), repetições (`for`, `while`) e vetorização. O exemplo condutor é o cálculo do Índice de Massa Corporal (IMC = peso / altura²).

```python
import numpy as np
```

## Tomada de decisão

O bloco do `if` executa quando a condição é verdadeira; caso contrário, executa o `else`. Em Python, a indentação (4 espaços) delimita os blocos.

```python
x = 10
if x > 5:
    print("Maior que 5")
else:
    print("5 ou menos")
```

```text
Maior que 5
```

## Um indivíduo

```python
weight = 60
height = 1.75
bmi = weight / height**2
bmi
```

```text
19.591836734693878
```

## Vários indivíduos

Com várias pessoas, guardamos os valores em arrays. Podemos processá-los com laços ou, como veremos no final, com operações vetorizadas.

```python
weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
weight
```

```text
array([60, 72, 57, 90, 95, 72])
```

## Múltiplas condições (if / elif / else)

As condições são testadas de cima para baixo; a primeira verdadeira é executada e o `else` trata os casos restantes.

```python
nota = 7
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 6:
    conceito = "C"
else:
    conceito = "D"
conceito
```

```text
'B'
```

## Condições em vetores

O `if` espera um único booleano. Com um array, a condição gera vários booleanos e o Python não sabe qual usar:

```python
alturas = np.array([1.65, 1.80, 1.55])
if alturas < 1.70:
    print("baixa")
```

```text
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```

`np.where` aplica a condição a cada elemento e escolhe o valor correspondente.

```python
classe = np.where(alturas < 1.70, "baixa", "alta")
classe
```

```text
array(['baixa', 'alta', 'baixa'], dtype='<U5')
```

## Vetorização

Quando possível, operações vetorizadas processam todos os elementos de uma vez, sem laço explícito.

```python
x = np.array([1, 2, 3, 4])
x**2
```

```text
array([ 1,  4,  9, 16])
```

## Condição dentro de repetição

```python
i = 1
while i <= 5:
    if i % 2 == 0:
        print(i, "é par")
    i += 1
```

```text
2 é par
4 é par
```

## Laço for

`for` percorre uma sequência; `range(1, 6)` gera 1, 2, 3, 4, 5.

```python
for i in range(1, 6):
    print(i)
```

```text
1
2
3
4
5
```

## IMC com for e zip

`zip` percorre dois vetores em paralelo, sem gerenciar índices.

```python
bmi = []
for w, h in zip(weight, height):
    bmi.append(w / h**2)
bmi = np.array(bmi)
bmi.round(2)
```

```text
array([19.59, 22.22, 20.94, 24.93, 31.38, 19.74])
```

## Inspecionando o laço

Imprimir dentro do laço mostra cada passo: o vetor começa com zeros e é preenchido uma posição por vez.

```python
bmi = np.zeros(len(weight))
for i in range(len(weight)):
    bmi[i] = weight[i] / height[i]**2
    print(bmi.round(2))
```

```text
[19.59  0.    0.    0.    0.    0.  ]
[19.59 22.22  0.    0.    0.    0.  ]
[19.59 22.22 20.94  0.    0.    0.  ]
[19.59 22.22 20.94 24.93  0.    0.  ]
[19.59 22.22 20.94 24.93 31.38  0.  ]
[19.59 22.22 20.94 24.93 31.38 19.74]
```

## Depuração no VS Code

Clique à esquerda do número da linha para criar um *breakpoint* e execute com F5. A cada parada, o painel *Variables* mostra `w`, `h` e `bmi_val`.

```python
for w, h in zip(weight, height):
    bmi_val = w / h**2   # breakpoint aqui
    print(w, h, round(bmi_val, 2))
```

```text
60 1.75 19.59
72 1.8 22.22
57 1.65 20.94
90 1.9 24.93
95 1.74 31.38
72 1.91 19.74
```

## Escopo

Variáveis criadas dentro de uma função são locais a ela. Blocos `if`, `for` e `while` não criam escopo: o que é definido dentro deles continua existindo depois.

```python
def compute():
    x_local = 10
    return x_local * 2

print(compute())
for k in range(3):
    pass
print(k)
```

```text
20
2
```

```python
print(x_local)
```

```text
NameError: name 'x_local' is not defined
```

## Laço while

`while` repete enquanto a condição for verdadeira. A variável de controle precisa mudar dentro do laço, senão ele nunca termina.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

```text
1
2
3
4
5
```

## IMC com while

```python
i = 0
bmi = np.zeros(len(weight))
while i < len(weight):
    bmi[i] = weight[i] / height[i]**2
    i += 1
bmi.round(2)
```

```text
array([19.59, 22.22, 20.94, 24.93, 31.38, 19.74])
```

## Encapsulando em uma função

```python
def compute_bmi(weight, height):
    i = 0
    bmi = np.zeros(len(weight))
    while i < len(weight):
        bmi[i] = weight[i] / height[i]**2
        i += 1
    return bmi

compute_bmi(weight, height).round(2)
```

```text
array([19.59, 22.22, 20.94, 24.93, 31.38, 19.74])
```

## Versão vetorizada

Sem laço: o NumPy divide os arrays elemento a elemento. A mesma função serve para escalares e vetores.

```python
def compute_bmi(weight, height):
    return weight / height**2

print(round(compute_bmi(80, 1.79), 2))
print(compute_bmi(weight, height).round(2))
```

```text
24.97
[19.59 22.22 20.94 24.93 31.38 19.74]
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
