LESSON = {
"file": "08-Listas",
"title": "Listas em Python",
"intro": """
Exemplos de código da aula sobre listas, dicionários, `dataclass` e mutabilidade.
""",
"cells": [
{"section": "O que são listas",
 "text": "Uma lista é uma coleção ordenada, acessada por índice a partir de zero. Os elementos podem ter tipos diferentes.",
 "code": """
my_list = [1, "a", 3.5, True]
my_list
"""},
{"section": "Criando listas",
 "text": "Uma lista pode guardar arrays, outras listas, números e textos ao mesmo tempo.",
 "code": """
import numpy as np
weight = np.array([60, 72, 57, 90, 95, 72])
height = np.array([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])
subject = ["A", "B", "C", "D", "E", "F"]
mybag = [weight, height, subject, 0, "a"]
len(mybag), type(mybag)
"""},
{"section": "Conteúdo da lista",
 "text": "Cada posição mantém o tipo do objeto armazenado. `enumerate` devolve a posição e o elemento.",
 "code": """
for i, item in enumerate(mybag):
    print(i, type(item))
"""},
{"section": "Fatiamento",
 "text": "O início é incluído e o fim é excluído: `[0:3]` devolve as posições 0, 1 e 2.",
 "code": """
print(len(mybag[0:3]), len(mybag[:2]))
"""},
{"section": "Elemento vs sublista",
 "text": "Um índice único devolve o próprio objeto; um intervalo devolve uma nova lista.",
 "code": """
print(type(mybag[0:1]), mybag[0:1])
print(type(mybag[0]), mybag[0])
"""},
{"section": "Dicionários",
 "text": "Um `dict` associa chaves a valores. Use lista quando a posição importa e dicionário quando o nome importa.",
 "code": """
bag = {"weight": weight, "height": height, "subject": subject}
print(bag["weight"])
bag["nome"] = "a"
print(list(bag.keys()))
"""},
{"section": "Registros com dataclass",
 "text": "Quando os campos são fixos, uma `dataclass` dá nome e tipo a cada um, acessados por ponto. Campos opcionais recebem valor padrão.",
 "code": """
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
"""},
{"section": "Campos opcionais",
 "text": "Como `bmi` foi declarado na classe, ele aparece na representação do objeto. Um atributo criado fora da classe não apareceria.",
 "code": """
mybag.bmi = (mybag.weight / mybag.height**2).round(2)
mybag
"""},
{"section": "Mutabilidade e cópias",
 "text": "Atribuir (`a = lista`) não copia: os dois nomes apontam para o mesmo objeto. `.copy()` faz uma cópia rasa: a lista é nova, mas os objetos internos são compartilhados. Por isso alterar `a[0][0]` muda também `b` e o próprio `weight`.",
 "code": """
mybag_list = [weight, height, subject]
a = mybag_list
b = mybag_list.copy()
a[0][0] = 999
print(a[0][0], b[0][0], weight[0])
"""},
{"text": "`copy.deepcopy` copia também os objetos internos, gerando uma estrutura independente.",
 "code": """
import copy
c = copy.deepcopy(mybag_list)
a[0][0] = 60
print(c[0][0], weight[0])
"""},
]}
