LESSON = {
"file": "06-Estrutura-Repeticao",
"title": "Estrutura de Repetição em Python",
"intro": """
Exemplos de código da aula sobre decisões (`if`), repetições (`for`, `while`) e vetorização. O exemplo condutor é o cálculo do Índice de Massa Corporal (IMC = peso / altura²).
""",
"cells": [
{"code": "import numpy as np"},
{"section": "Tomada de decisão",
 "text": "O bloco do `if` executa quando a condição é verdadeira; caso contrário, executa o `else`. Em Python, a indentação (4 espaços) delimita os blocos.",
 "code": """
x = 10
if x > 5:
    print("Maior que 5")
else:
    print("5 ou menos")
"""},
{"section": "Um indivíduo",
 "code": """
weight = 60
height = 1.75
bmi = weight / height**2
bmi
"""},
{"section": "Vários indivíduos",
 "text": "Com várias pessoas, guardamos os valores em arrays. Podemos processá-los com laços ou, como veremos no final, com operações vetorizadas.",
 "code": """
weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = np.array(["A", "B", "C", "D", "E", "F"])
weight
"""},
{"section": "Múltiplas condições (if / elif / else)",
 "text": "As condições são testadas de cima para baixo; a primeira verdadeira é executada e o `else` trata os casos restantes.",
 "code": """
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
"""},
{"section": "Condições em vetores",
 "text": "O `if` espera um único booleano. Com um array, a condição gera vários booleanos e o Python não sabe qual usar:",
 "error": True,
 "code": """
alturas = np.array([1.65, 1.80, 1.55])
if alturas < 1.70:
    print("baixa")
"""},
{"text": "`np.where` aplica a condição a cada elemento e escolhe o valor correspondente.",
 "code": """
classe = np.where(alturas < 1.70, "baixa", "alta")
classe
"""},
{"section": "Vetorização",
 "text": "Quando possível, operações vetorizadas processam todos os elementos de uma vez, sem laço explícito.",
 "code": """
x = np.array([1, 2, 3, 4])
x**2
"""},
{"section": "Condição dentro de repetição",
 "code": """
i = 1
while i <= 5:
    if i % 2 == 0:
        print(i, "é par")
    i += 1
"""},
{"section": "Laço for",
 "text": "`for` percorre uma sequência; `range(1, 6)` gera 1, 2, 3, 4, 5.",
 "code": """
for i in range(1, 6):
    print(i)
"""},
{"section": "IMC com for e zip",
 "text": "`zip` percorre dois vetores em paralelo, sem gerenciar índices.",
 "code": """
bmi = []
for w, h in zip(weight, height):
    bmi.append(w / h**2)
bmi = np.array(bmi)
bmi.round(2)
"""},
{"section": "Inspecionando o laço",
 "text": "Imprimir dentro do laço mostra cada passo: o vetor começa com zeros e é preenchido uma posição por vez.",
 "code": """
bmi = np.zeros(len(weight))
for i in range(len(weight)):
    bmi[i] = weight[i] / height[i]**2
    print(bmi.round(2))
"""},
{"section": "Depuração no VS Code",
 "text": "Clique à esquerda do número da linha para criar um *breakpoint* e execute com F5. A cada parada, o painel *Variables* mostra `w`, `h` e `bmi_val`.",
 "code": """
for w, h in zip(weight, height):
    bmi_val = w / h**2   # breakpoint aqui
    print(w, h, round(bmi_val, 2))
"""},
{"section": "Escopo",
 "text": "Variáveis criadas dentro de uma função são locais a ela. Blocos `if`, `for` e `while` não criam escopo: o que é definido dentro deles continua existindo depois.",
 "code": """
def compute():
    x_local = 10
    return x_local * 2

print(compute())
for k in range(3):
    pass
print(k)
"""},
{"error": True, "code": "print(x_local)"},
{"section": "Laço while",
 "text": "`while` repete enquanto a condição for verdadeira. A variável de controle precisa mudar dentro do laço, senão ele nunca termina.",
 "code": """
i = 1
while i <= 5:
    print(i)
    i += 1
"""},
{"section": "IMC com while",
 "code": """
i = 0
bmi = np.zeros(len(weight))
while i < len(weight):
    bmi[i] = weight[i] / height[i]**2
    i += 1
bmi.round(2)
"""},
{"section": "Encapsulando em uma função",
 "code": """
def compute_bmi(weight, height):
    i = 0
    bmi = np.zeros(len(weight))
    while i < len(weight):
        bmi[i] = weight[i] / height[i]**2
        i += 1
    return bmi

compute_bmi(weight, height).round(2)
"""},
{"section": "Versão vetorizada",
 "text": "Sem laço: o NumPy divide os arrays elemento a elemento. A mesma função serve para escalares e vetores.",
 "code": """
def compute_bmi(weight, height):
    return weight / height**2

print(round(compute_bmi(80, 1.79), 2))
print(compute_bmi(weight, height).round(2))
"""},
]}
