# Gerador dos exemplos

Os arquivos `examples/NN-Nome.md` são gerados a partir de `tools/specs/NN.py`. O script executa cada trecho de código e grava no `.md` a saída real. Os gráficos (`plt.show()`) são salvos em `examples/fig/`.

## Uso

Na raiz do repositório, com `numpy`, `pandas` e `matplotlib` instalados:

```bash
python tools/gen.py          # todas as aulas
python tools/gen.py 04 07    # só as aulas indicadas
```

As aulas 05 e 09 leem dados pela internet (GitHub e UCI). Os arquivos que os exemplos gravam (`.csv`, `.pkl`) vão para uma pasta temporária e não para o repositório.

## Formato de uma aula

Cada `specs/NN.py` define um dicionário `LESSON`:

```python
LESSON = {
    "file": "07-Categoricos",          # nome do PDF e do .md
    "title": "Variáveis Categóricas em Python",
    "intro": "Texto de abertura.",
    "cells": [
        {"section": "Título da seção",  # opcional: cria um "## Título"
         "text": "Explicação antes do código.",
         "code": "x = 1\nx + 1",
         "after": "Explicação depois da saída."},  # opcional
    ],
}
```

Chaves opcionais de uma célula:

- `"lang": "bash"`: mostra o código sem executá-lo (comandos de terminal).
- `"run": False`: mostra código Python sem executá-lo.
- `"error": True`: a célula deve gerar uma exceção, e a mensagem vai para a saída.

Como em um notebook, a última expressão de cada célula é exibida automaticamente. As células de uma mesma aula compartilham as variáveis. Qualquer exceção não marcada com `"error": True` interrompe a geração.
