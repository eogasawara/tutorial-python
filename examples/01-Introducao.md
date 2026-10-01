# Introdução à Linguagem Python

Slides: [01-Introducao.pdf](../01-Introducao.pdf)

Exemplos de código da primeira aula. Python é uma linguagem interpretada: o interpretador traduz cada trecho para bytecode e o executa imediatamente, o que favorece a experimentação. Os exemplos podem ser digitados no console (`python` no terminal) ou salvos em um script `.py`.

## Primeiros comandos

No console, o símbolo `>>>` indica que o interpretador está pronto. Uma expressão digitada é avaliada e o resultado aparece logo abaixo.

```python
2 + 2
```

```text
4
```

## Variáveis e execução sequencial

Uma variável associa um nome a um valor. Os comandos são executados na ordem em que aparecem, e cada linha usa o estado criado pelas anteriores.

```python
x = 10
y = 3
x + y
```

```text
13
```

## Um programa simples

Um conjunto de comandos forma um programa. Em um script `.py`, use `print()` para exibir resultados: digitar apenas o nome da variável só mostra o valor no console interativo.

```python
x = 10
y = 20
z = x + y
print(z)
```

```text
30
```

## Operações aritméticas

A divisão `/` sempre retorna um número de ponto flutuante (`float`). Para a divisão inteira use `//`, e para o resto, `%`.

```python
print(2 + 3, 10 - 4)
print(5 * 6, 8 / 2)
print(2 ** 3)
print(7 // 2, 7 % 2)
```

```text
5 6
30 4.0
8
3 1
```

## Sequências de valores

Listas são a sequência nativa do Python. Para computação científica usamos arrays do NumPy, que permitem operações matemáticas sobre todos os elementos de uma vez.

```python
v = [10, 20, 30, 40]
v
```

```text
[10, 20, 30, 40]
```

```python
import numpy as np
x = np.array([10, 20, 30, 40])
x * 2
```

```text
array([20, 40, 60, 80])
```

Observe a diferença: `v * 2` repetiria a lista (`[10, 20, 30, 40, 10, 20, 30, 40]`), enquanto `x * 2` multiplica cada elemento.

## Funções

Funções encapsulam um algoritmo para que possa ser reutilizado. `def` define a função e `return` devolve o resultado.

```python
def soma(a, b):
    return a + b

soma(3, 5)
```

```text
8
```

## Parâmetros e argumentos

Parâmetros são os nomes declarados na definição (`x` e `y`); argumentos são os valores passados na chamada (`10` e `20`).

```python
def media(x, y):
    return (x + y) / 2

media(10, 20)
```

```text
15.0
```

## Instalação e verificação

Depois de instalar o Python (https://www.python.org), verifique a versão no terminal. No Windows, marque a opção *Add python.exe to PATH* durante a instalação; em macOS e Linux o comando costuma ser `python3`.

```bash
python --version    # Windows
python3 --version   # macOS/Linux
```

## Ambientes virtuais

Um ambiente virtual isola as bibliotecas de cada projeto. Crie-o uma vez na pasta do projeto e ative-o sempre que for trabalhar. No VS Code, selecione esse interpretador em *Python: Select Interpreter*.

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1     # Windows (PowerShell)
source .venv/bin/activate      # macOS/Linux
```

## Erros comuns

Ler a mensagem de erro é parte do aprendizado. Usar um nome que não foi definido (ou uma biblioteca não importada) gera `NameError`:

```python
print(total)
```

```text
NameError: name 'total' is not defined
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
