LESSON = {
"file": "01-Introducao",
"title": "Introdução à Linguagem Python",
"intro": """
Exemplos de código da primeira aula. Python é uma linguagem interpretada: o interpretador traduz cada trecho para bytecode e o executa imediatamente, o que favorece a experimentação. Os exemplos podem ser digitados no console (`python` no terminal) ou salvos em um script `.py`.
""",
"cells": [
{"section": "Primeiros comandos",
 "text": "No console, o símbolo `>>>` indica que o interpretador está pronto. Uma expressão digitada é avaliada e o resultado aparece logo abaixo.",
 "code": "2 + 2"},
{"section": "Variáveis e execução sequencial",
 "text": "Uma variável associa um nome a um valor. Os comandos são executados na ordem em que aparecem, e cada linha usa o estado criado pelas anteriores.",
 "code": """
x = 10
y = 3
x + y
"""},
{"section": "Um programa simples",
 "text": "Um conjunto de comandos forma um programa. Em um script `.py`, use `print()` para exibir resultados: digitar apenas o nome da variável só mostra o valor no console interativo.",
 "code": """
x = 10
y = 20
z = x + y
print(z)
"""},
{"section": "Operações aritméticas",
 "text": "A divisão `/` sempre retorna um número de ponto flutuante (`float`). Para a divisão inteira use `//`, e para o resto, `%`.",
 "code": """
print(2 + 3, 10 - 4)
print(5 * 6, 8 / 2)
print(2 ** 3)
print(7 // 2, 7 % 2)
"""},
{"section": "Sequências de valores",
 "text": "Listas são a sequência nativa do Python. Para computação científica usamos arrays do NumPy, que permitem operações matemáticas sobre todos os elementos de uma vez.",
 "code": """
v = [10, 20, 30, 40]
v
"""},
{"code": """
import numpy as np
x = np.array([10, 20, 30, 40])
x * 2
""",
 "after": "Observe a diferença: `v * 2` repetiria a lista (`[10, 20, 30, 40, 10, 20, 30, 40]`), enquanto `x * 2` multiplica cada elemento."},
{"section": "Funções",
 "text": "Funções encapsulam um algoritmo para que possa ser reutilizado. `def` define a função e `return` devolve o resultado.",
 "code": """
def soma(a, b):
    return a + b

soma(3, 5)
"""},
{"section": "Parâmetros e argumentos",
 "text": "Parâmetros são os nomes declarados na definição (`x` e `y`); argumentos são os valores passados na chamada (`10` e `20`).",
 "code": """
def media(x, y):
    return (x + y) / 2

media(10, 20)
"""},
{"section": "Instalação e verificação",
 "text": "Depois de instalar o Python (https://www.python.org), verifique a versão no terminal. No Windows, marque a opção *Add python.exe to PATH* durante a instalação; em macOS e Linux o comando costuma ser `python3`.",
 "lang": "bash",
 "code": """
python --version    # Windows
python3 --version   # macOS/Linux
"""},
{"section": "Ambientes virtuais",
 "text": "Um ambiente virtual isola as bibliotecas de cada projeto. Crie-o uma vez na pasta do projeto e ative-o sempre que for trabalhar. No VS Code, selecione esse interpretador em *Python: Select Interpreter*.",
 "lang": "bash",
 "code": """
python -m venv .venv
.venv\\Scripts\\Activate.ps1     # Windows (PowerShell)
source .venv/bin/activate      # macOS/Linux
"""},
{"section": "Erros comuns",
 "text": "Ler a mensagem de erro é parte do aprendizado. Usar um nome que não foi definido (ou uma biblioteca não importada) gera `NameError`:",
 "error": True,
 "code": "print(total)"},
]}
