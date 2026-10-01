# Classes e Objetos em Python

Slides: [13-Classes.pdf](../13-Classes.pdf)

Exemplos de código da aula sobre classes: atributos, construtor com validação, herança, `__str__`, polimorfismo e sobrescrita de métodos. A classe `Polygon` evolui ao longo da aula; cada versão abaixo é completa, porque redefinir uma classe substitui a anterior.

## Objeto com atributos

Uma classe define como os objetos são criados; `__init__` inicializa os atributos, acessados com `obj.atributo`.

```python
class Polygon:
    def __init__(self, n: int):
        self.n = n

p = Polygon(5)
print(p.n)
```

```text
5
```

## Construtor com validação

O construtor impede estados inválidos lançando uma exceção com mensagem clara.

```python
class Polygon:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("número de vértices deve ser maior que zero")
        self.n = n

print(Polygon(5).n)
```

```text
5
```

```python
Polygon(0)
```

```text
ValueError: número de vértices deve ser maior que zero
```

## Herança

`Rectangle` é um `Polygon` com 4 vértices. `super().__init__(4)` reaproveita o construtor da classe base.

```python
class Rectangle(Polygon):
    def __init__(self, w: float, h: float):
        super().__init__(4)
        self.w = w
        self.h = h

r = Rectangle(3, 10)
print(r.n, r.w, r.h)
```

```text
4 3 10
```

## Impressão com __str__

Sem `__str__`, `print` mostra apenas a classe e o endereço do objeto:

```python
print(r)
```

```text
<__main__.Rectangle object at 0x0000028D694E46E0>
```

Implementando `__str__`, cada classe define sua própria representação textual.

```python
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
```

```text
5
3, 10
```

## Polimorfismo e o método area()

O mesmo comando produz resultados diferentes conforme o tipo do objeto. A classe base define um método padrão; a classe derivada o sobrescreve. Ao chamar `r.area()`, Python procura o método primeiro em `Rectangle` e, se não encontrar, em `Polygon`.

```python
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
```

```text
Polygon 5 0.0
Rectangle 3, 10 30
```

## Descobrindo interfaces

`dir()` lista todos os atributos e métodos, inclusive os especiais (`__init__`, `__str__`...). Filtrando os nomes que começam com `_`, ficam os de uso direto:

```python
[m for m in dir(r) if not m.startswith("_")]
```

```text
['area', 'h', 'n', 'w']
```

## Estendendo: Square e Hexagon

`Square` herda de `Rectangle` (lados iguais) e reaproveita `area()`. `Hexagon` herda de `Polygon` e define sua própria área: (3√3/2)·lado².

```python
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
```

```text
16
10.392304845413264
True
```

## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
