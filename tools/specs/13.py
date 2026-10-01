LESSON = {
"file": "13-Classes",
"title": "Classes e Objetos em Python",
"intro": """
Exemplos de código da aula sobre classes: atributos, construtor com validação, herança, `__str__`, polimorfismo e sobrescrita de métodos. A classe `Polygon` evolui ao longo da aula; cada versão abaixo é completa, porque redefinir uma classe substitui a anterior.
""",
"cells": [
{"section": "Objeto com atributos",
 "text": "Uma classe define como os objetos são criados; `__init__` inicializa os atributos, acessados com `obj.atributo`.",
 "code": """
class Polygon:
    def __init__(self, n: int):
        self.n = n

p = Polygon(5)
print(p.n)
"""},
{"section": "Construtor com validação",
 "text": "O construtor impede estados inválidos lançando uma exceção com mensagem clara.",
 "code": """
class Polygon:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("número de vértices deve ser maior que zero")
        self.n = n

print(Polygon(5).n)
"""},
{"error": True, "code": "Polygon(0)"},
{"section": "Herança",
 "text": "`Rectangle` é um `Polygon` com 4 vértices. `super().__init__(4)` reaproveita o construtor da classe base.",
 "code": """
class Rectangle(Polygon):
    def __init__(self, w: float, h: float):
        super().__init__(4)
        self.w = w
        self.h = h

r = Rectangle(3, 10)
print(r.n, r.w, r.h)
"""},
{"section": "Impressão com __str__",
 "text": "Sem `__str__`, `print` mostra apenas a classe e o endereço do objeto:",
 "code": "print(r)",
 "after": "Implementando `__str__`, cada classe define sua própria representação textual."},
{"code": """
class Polygon:
    def __init__(self, n: int):
        self.n = n

    def __str__(self) -> str:
        return f"{self.n}"

class Rectangle(Polygon):
    def __init__(self, w: float, h: float):
        super().__init__(4)
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return f"{self.w}, {self.h}"

print(Polygon(5))
print(Rectangle(3, 10))
"""},
{"section": "Polimorfismo e o método area()",
 "text": "O mesmo comando produz resultados diferentes conforme o tipo do objeto. A classe base define um método padrão; a classe derivada o sobrescreve. Ao chamar `r.area()`, Python procura o método primeiro em `Rectangle` e, se não encontrar, em `Polygon`.",
 "code": """
class Polygon:
    def __init__(self, n: int):
        self.n = n

    def __str__(self) -> str:
        return f"{self.n}"

    def area(self) -> float:
        return 0.0   # área genérica desconhecida

class Rectangle(Polygon):
    def __init__(self, w: float, h: float):
        super().__init__(4)
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return f"{self.w}, {self.h}"

    def area(self) -> float:
        return self.w * self.h

p = Polygon(5)
r = Rectangle(3, 10)
for obj in [p, r]:
    print(type(obj).__name__, obj, obj.area())
"""},
{"section": "Descobrindo interfaces",
 "text": "`dir()` lista todos os atributos e métodos, inclusive os especiais (`__init__`, `__str__`...). Filtrando os nomes que começam com `_`, ficam os de uso direto:",
 "code": """
[m for m in dir(r) if not m.startswith("_")]
"""},
{"section": "Estendendo: Square e Hexagon",
 "text": "`Square` herda de `Rectangle` (lados iguais) e reaproveita `area()`. `Hexagon` herda de `Polygon` e define sua própria área: (3√3/2)·lado².",
 "code": """
import math

class Square(Rectangle):
    def __init__(self, lado: float):
        super().__init__(lado, lado)

class Hexagon(Polygon):
    def __init__(self, lado: float):
        super().__init__(6)
        self.lado = lado

    def area(self) -> float:
        return (3 * math.sqrt(3) / 2) * self.lado ** 2

s = Square(4)
h = Hexagon(2)
print(s.area())
print(h.area())
print(isinstance(s, Polygon))
"""},
]}
