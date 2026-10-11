# Agente de atendimento Natural Pure — código

O "cérebro de conversa" do agente, **independente de canal**. A Duotalk (WhatsApp, Instagram, chat do site) vai chamar `responder()`.

| Arquivo | O que faz |
|---|---|
| `agente.py` | Recebe a conversa, consulta a base do cérebro, usa ferramentas e devolve a resposta + transferências para o time |
| `conhecimento.py` | Monta a base a partir de `marcas/natural-pure/` (NÃO lê `revisao/` nem trechos "Interno") |
| `ferramentas.py` | `consultar_pedido` (Shopify; exige nº do pedido + e-mail batendo) e `transferir_para_humano` (etiquetas) |
| `horario.py` | Horário do time (seg–sex 9h–18h, feriados) |
| `teste_no_escuro.py` | Roda os casos de teste e uma segunda IA dá nota a cada resposta → `../resultados/` |
| `casos_teste.json` | 25 casos (pedido, frete, saúde, avaria, cupom, tentativa de manipulação…) |
| `simulador.py` | Conversar com o agente pelo terminal |

## Como rodar o teste
Automático: a cada mudança no agente ou no conhecimento da NP, o GitHub roda `teste-agente.yml` e salva o relatório.
**Precisa do segredo `ANTHROPIC_API_KEY` neste repositório** (Settings → Secrets and variables → Actions).

## Critério para ir ao ar
Nota média ≥ 4,5 · **zero** violações do NAO-DIZER · **zero** informações inventadas, primeiro nos 25 casos e depois nas conversas reais exportadas da Duotalk.

## Falta para ligar no canal
- Resposta da Duotalk sobre API/webhook → escrever o adaptador `duotalk.py` e hospedar (servidor que recebe a mensagem e responde).
- Segredos de produção: `ANTHROPIC_API_KEY`, `SHOPIFY_NP_*` (consulta de pedido) e o token da Duotalk.
