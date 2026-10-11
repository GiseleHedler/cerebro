# -*- coding: utf-8 -*-
"""
Monta a base de conhecimento do agente a partir do cérebro.
Lê só o que o agente pode usar: nada de revisao/, nada de trechos "Interno".
A ordem é fixa para o texto sair idêntico a cada chamada (cache do prompt).
"""
import re
from pathlib import Path

CEREBRO = Path(__file__).resolve().parents[3]
NP = CEREBRO / "marcas" / "natural-pure"

ARQUIVOS_FIXOS = [
    NP / "NAO-DIZER.md",
    NP / "atendimento" / "GUIA-DE-LINGUAGEM.md",
    NP / "politicas" / "envios-trocas-devolucoes.md",
    NP / "politicas" / "produto-com-problema.md",
    NP / "politicas" / "pagamento.md",
    NP / "politicas" / "assinatura-e-descontos.md",
    NP / "produtos" / "catalogo.md",
    NP / "atendimento" / "faq-por-objetivo.md",
]


def _sem_interno(texto):
    # remove seções "## Interno ..." até o próximo título de mesmo nível
    return re.sub(r"(?ms)^## Interno.*?(?=^## |\Z)", "", texto)


def _ficha_produto(caminho):
    t = caminho.read_text(encoding="utf-8")
    m = re.search(r"(?ms)^## Versão para o agente.*?(?=^---\s*$|\Z)", t)
    titulo = t.splitlines()[0]
    if m:
        return "%s\n%s" % (titulo, m.group(0).strip())
    # sem versão revisada: só o texto do site, marcado para usar apenas composição/modo de uso
    corpo = t.split("\n---\n", 1)[-1]
    return "%s\n(Texto do site — use SOMENTE composição, modo de uso, rendimento e sabor.)\n%s" % (titulo, corpo.strip())


def montar():
    partes = []
    for arq in ARQUIVOS_FIXOS:
        if arq.exists():
            partes.append("<documento nome=\"%s\">\n%s\n</documento>" % (
                arq.relative_to(CEREBRO), _sem_interno(arq.read_text(encoding="utf-8")).strip()))
    for arq in sorted((NP / "produtos").glob("*.md")):
        if arq.name == "catalogo.md":
            continue
        partes.append("<produto arquivo=\"%s\">\n%s\n</produto>" % (arq.name, _ficha_produto(arq)))
    return "\n\n".join(partes)
