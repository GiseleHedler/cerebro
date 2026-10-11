#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conversa com o agente pelo terminal, como se fosse o WhatsApp.  python3 simulador.py"""
import agente

historico = []
print("Simulador Natural Pure — digite 'sair' para encerrar.\n")
while True:
    msg = input("Cliente: ").strip()
    if msg.lower() == "sair":
        break
    historico.append({"role": "user", "content": msg})
    r = agente.responder(historico)
    historico.append({"role": "assistant", "content": r["texto"]})
    print("\nAgente: %s\n" % r["texto"])
    for t in r["transferencias"]:
        print("   [→ time: %s] %s\n" % (t["etiqueta"], t["resumo"]))
