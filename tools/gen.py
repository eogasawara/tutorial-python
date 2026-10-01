"""Gera examples/NN-Nome.md executando cada célula e capturando a saída real.

Uso (na raiz do repositório):
    python tools/gen.py            # todas as aulas
    python tools/gen.py 04 07      # só as aulas indicadas
"""
import ast, contextlib, importlib.util, io, os, sys, tempfile, textwrap, traceback
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
SPECS = os.path.join(TOOLS, "specs")
only = sys.argv[1:]

EX = os.path.join(REPO, "examples")
FIG = os.path.join(EX, "fig")
os.makedirs(FIG, exist_ok=True)


def run_cell(code, ns):
    tree = ast.parse(code)
    last = None
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        last = ast.Expression(tree.body.pop().value)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(tree, "<cell>", "exec"), ns)
        if last is not None:
            val = eval(compile(last, "<cell>", "eval"), ns)
            if val is not None:
                print(repr(val))
    return buf.getvalue()


def build(spec_path):
    spec = importlib.util.spec_from_file_location("spec", spec_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    L = mod.LESSON
    stem = L["file"]
    ns = {"__name__": "__main__"}
    figs = [0]

    def fake_show(*a, **k):
        figs[0] += 1
        name = f"{stem}-{figs[0]}.png"
        plt.gcf().savefig(os.path.join(FIG, name), dpi=80, bbox_inches="tight")
        plt.close("all")
        pending.append(name)

    plt.show = fake_show
    out = [f"# {L['title']}\n", f"Slides: [{stem}.pdf](../{stem}.pdf)\n", L["intro"].strip() + "\n"]
    for c in L["cells"]:
        if "section" in c:
            out.append(f"## {c['section']}\n")
        if c.get("text"):
            out.append(textwrap.dedent(c["text"]).strip() + "\n")
        code = textwrap.dedent(c.get("code", "")).strip("\n")
        if not code:
            continue
        lang = c.get("lang", "python")
        out.append(f"```{lang}\n{code}\n```\n")
        if lang != "python" or c.get("run") is False:
            continue
        pending = []
        try:
            res = run_cell(code, ns)
        except Exception as e:
            if not c.get("error"):
                traceback.print_exc()
                raise SystemExit(f"Falha em {stem}: {code[:60]}")
            res = f"{type(e).__name__}: {e}\n"
        if res.strip():
            out.append("```text\n" + res.rstrip() + "\n```\n")
        for name in pending:
            out.append(f"![{stem}](fig/{name})\n")
        if c.get("after"):
            out.append(textwrap.dedent(c["after"]).strip() + "\n")
    out.append(REFS)
    with open(os.path.join(EX, stem + ".md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print("ok", stem)


REFS = """## Referências

1. Downey, A. *Think Python: How to Think Like a Computer Scientist*. O'Reilly Media.
2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media.
3. Grus, J. *Data Science from Scratch*. O'Reilly Media.
"""

# arquivos gravados pelos exemplos (csv, pkl) vão para uma pasta temporária
os.chdir(tempfile.mkdtemp(prefix="tutorial-python-"))
import pandas as pd
pd.set_option("display.width", 100)
for fn in sorted(os.listdir(SPECS)):
    if fn.endswith(".py") and (not only or fn[:2] in only):
        build(os.path.join(SPECS, fn))
