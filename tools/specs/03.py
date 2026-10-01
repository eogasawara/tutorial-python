LESSON = {
"file": "03-Objetos",
"title": "Objetos em Python",
"intro": """
Exemplos de código da aula sobre objetos, tipos e valores. Em Python, todo valor é um objeto e possui um tipo, que define as operações permitidas.
""",
"cells": [
{"code": """
import numpy as np
import pandas as pd
"""},
{"section": "Variáveis",
 "text": "Uma variável é um nome associado a um valor. Ao reatribuir, o nome passa a apontar para o novo valor.",
 "code": """
idade = 30
idade = idade + 1
idade
"""},
{"section": "Objetos, tipos e valores",
 "text": "`type()` mostra o tipo de um objeto. Operações produzem novos objetos.",
 "code": """
a = 5
b = 2
c = a * b
type(c)
"""},
{"section": "DataFrames",
 "text": "Um DataFrame do pandas organiza dados em linhas (registros) e colunas (atributos). Cada coluna pode ter um tipo diferente.",
 "code": """
df = pd.DataFrame({
    "face": ["ás", "dois", "quatro"],
    "naipe": ["ouros", "copas", "paus"],
    "valor": [1, 2, 4],
})
print(df)
"""},
{"section": "Salvando e lendo CSV",
 "text": "`to_csv` grava a tabela em texto; `index=False` evita gravar a coluna de índice. `read_csv` lê o arquivo de volta.",
 "code": """
df.to_csv("cartas.csv", index=False)
cartas = pd.read_csv("cartas.csv")
print(cartas)
"""},
{"section": "Valores ausentes",
 "text": "`None` indica ausência de um objeto qualquer; `np.nan` representa um número ausente e é usado em cálculos numéricos. Funções comuns retornam `nan` quando há ausentes; as versões com prefixo `nan` os ignoram.",
 "code": """
y = np.array([1.0, np.nan, 3.0])
print(np.mean(y))
print(np.nanmean(y))
print(np.isnan(y))
"""},
{"text": "Em tabelas pandas, `dropna()` remove e `fillna()` preenche valores ausentes.",
 "code": """
s = pd.Series(y)
print(s.dropna().tolist(), s.fillna(0).tolist())
"""},
{"section": "Tipos simples e estruturas",
 "text": "Números e textos representam valores únicos; listas e dicionários agrupam vários valores. Cada tipo tem métodos próprios.",
 "code": """
print(type(10), type([1, 2, 3]))
"dados".upper()
"""},
{"section": "Arrays do NumPy",
 "text": "Arrays armazenam vários valores do mesmo tipo de forma eficiente.",
 "code": """
dado = np.array([1, 2, 3, 4, 5, 6])
dado
"""},
{"section": "Escalar vs array de tamanho 1",
 "text": "Um número solto é um escalar e não tem tamanho; já `np.array([5])` é um vetor com um elemento.",
 "error": True,
 "code": "len(5)"},
{"code": """
vetor = np.array([5])
print(len(vetor), len(dado))
"""},
{"section": "Inteiros e textos",
 "code": """
print(type(1), type("ás"))
"""},
{"section": "Funções sobre sequências",
 "text": "Funções agregadoras resumem uma sequência numérica. Textos também podem ser comparados: a ordem segue os códigos Unicode, e letras acentuadas, como `á`, vêm depois de `z`. Por isso o maior elemento é `'ás'`.",
 "code": """
cartas = np.arange(1, 14)
print(np.sum(cartas))
faces = ["ás", "dois", "três", "quatro", "cinco", "seis",
         "sete", "oito", "nove", "dez", "valete", "dama", "rei"]
print(max(faces))
print(sorted(faces)[:3])
"""},
{"section": "Ponto flutuante (float)",
 "text": "Números decimais usam ponto flutuante de dupla precisão (`float64`, cerca de 15 a 16 dígitos significativos).",
 "code": """
dado = np.array([1, 2, 3, 4, 5, 6], dtype=float)
print(dado, dado.dtype)
"""},
{"text": "O float binário tem erros de arredondamento. Para valores monetários, use `decimal.Decimal`.",
 "code": """
from decimal import Decimal
print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
"""},
{"section": "Booleanos",
 "text": "Comparações produzem `True` ou `False`, usados em decisões e filtros.",
 "code": """
logico = np.array([True, False, 3 >= 4, 3 < 4, 3 != 4, 4 == 4])
logico
"""},
{"section": "Números complexos",
 "text": "Python suporta números complexos nativamente; a parte imaginária usa o sufixo `j`.",
 "code": """
comp = np.array([1+1j, 1+2j, 1+3j])
print(comp, comp.dtype)
"""},
{"section": "Bytes",
 "text": "Cada byte guarda um valor de 0 a 255. Valores fora do intervalo geram erro e precisam ser convertidos explicitamente.",
 "code": """
r = bytearray(3)
r[1] = 255
r[2] = 1024 % 256   # conversão explícita: 0
r
"""},
{"error": True, "code": "r[2] = 1024"},
{"section": "Rótulos e atributos",
 "text": "Para dar nome a cada valor, usamos uma `pd.Series` com índice. Já os atributos (acessados com ponto) descrevem o próprio objeto.",
 "code": """
dado = np.array([1, 2, 3, 4, 5, 6])
nomes = ["um", "dois", "três", "quatro", "cinco", "seis"]
rotulado = pd.Series(dado, index=nomes)
print(rotulado["três"])
print(dado.dtype, dado.shape, dado.ndim)
"""},
{"section": "Matrizes",
 "text": "`reshape` reorganiza os dados em outra forma. O padrão (`order=\"C\"`) preenche linha por linha; `order=\"F\"` preenche coluna por coluna.",
 "code": """
dado = np.arange(1, 7)
print(dado.reshape((2, 3), order="C"))
print(dado.reshape((2, 3), order="F"))
"""},
{"section": "Tipo e forma",
 "code": """
dado = np.arange(1, 7).reshape((2, 3))
print(type(dado))
print(dado.shape)
"""},
{"section": "Data e hora",
 "text": "O módulo `datetime` representa datas e horas. Aqui usamos uma data fixa para que a saída seja sempre a mesma; `datetime.now()` devolve o instante atual.",
 "code": """
from datetime import datetime
d = datetime(2024, 1, 15, 14, 30)
print(d, type(d))
print(d.year, d.strftime("%d/%m/%Y"))
"""},
{"section": "Dados categóricos",
 "text": "`pd.Categorical` representa grupos fixos e armazena cada categoria uma única vez.",
 "code": """
genero = pd.Categorical(["feminino", "masculino", "feminino", "masculino"])
genero
"""},
{"section": "Conversões de tipo",
 "code": """
print(int(True), int(False))
print(float(True), float(False))
print(bool(1), bool(0))
print(repr(str(1)), repr(str(True)))
"""},
]}
