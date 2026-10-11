# -*- coding: utf-8 -*-
"""Horário de atendimento humano da Natural Pure (seg–sex 9h–18h, exceto feriados)."""
import datetime
from zoneinfo import ZoneInfo

FUSO = ZoneInfo("America/Sao_Paulo")
ABRE, FECHA = 9, 18

# Feriados nacionais fixos (MM-DD). Móveis (Carnaval, Sexta Santa, Corpus Christi) entram por ano.
FERIADOS_FIXOS = {"01-01", "04-21", "05-01", "09-07", "10-12", "11-02", "11-15", "11-20", "12-25"}
FERIADOS_MOVEIS = {"2026-02-16", "2026-02-17", "2026-04-03", "2026-06-04",
                   "2027-02-08", "2027-02-09", "2027-03-26", "2027-05-27"}


def agora():
    return datetime.datetime.now(FUSO)


def eh_feriado(d):
    return d.strftime("%m-%d") in FERIADOS_FIXOS or d.strftime("%Y-%m-%d") in FERIADOS_MOVEIS


def time_humano_disponivel(momento=None):
    """True quando o time humano está atendendo; nesse horário o agente não responde."""
    m = momento or agora()
    return m.weekday() < 5 and not eh_feriado(m) and ABRE <= m.hour < FECHA


def proximo_atendimento(momento=None):
    """Texto curto com o próximo horário do time, ex.: 'segunda-feira a partir das 9h'."""
    m = momento or agora()
    if time_humano_disponivel(m):
        return "agora mesmo"
    dia = m if m.hour < ABRE else m + datetime.timedelta(days=1)
    while dia.weekday() >= 5 or eh_feriado(dia):
        dia += datetime.timedelta(days=1)
    if dia.date() == m.date():
        return "hoje a partir das 9h"
    if dia.date() == (m + datetime.timedelta(days=1)).date():
        return "amanhã a partir das 9h"
    nomes = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
    return "%s a partir das 9h" % nomes[dia.weekday()]
