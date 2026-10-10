# Agente de Suporte e Vendas — fora do horário comercial

**Dona:** Gisele · **Status:** 🟡 planejamento · **Começou:** 10/10/2026

## O problema (palavras da Gisele)
O time humano atende WhatsApp, Instagram e e-mail, mas **as pessoas chamam fora do expediente e no fim de semana, quando não tem ninguém**. Ali se perde venda e o cliente fica sem suporte.

## O que o agente é (e não é)
- ✅ **Cobre o buraco**: noites, madrugadas, sábados, domingos e feriados.
- ✅ Resolve o que é objetivo e **entrega o resto organizado** pro time de manhã.
- ❌ Não substitui o time no horário comercial (fase 1).
- ❌ Não fala de doença, dose para criança/gestante, nem promete resultado (`marcas/natural-pure/NAO-DIZER.md`).

## Canais (todos possíveis)
| Canal | Como liga | Observação |
|---|---|---|
| WhatsApp | API oficial do WhatsApp Business (Meta), direta ou via provedor | Janela de 24h: depois disso só template pago. **Nunca API não oficial** (risco de banir o número). |
| Instagram DM | API do Meta (mesmo ecossistema do token que o Central já usa) | Conta profissional; janela de 24h. |
| Chat do site | Widget no site/Shopify | O mais fácil e seguro para testar primeiro. |
| E-mail | Caixa de suporte (Gmail/Google Workspace) | Pode começar como **rascunho** que o time aprova. |

Recomendação: **uma "caixa de entrada" única** (plataforma de atendimento) que junta os 4 canais, onde a IA responde e o time assume quando precisa. Construir isso do zero não vale a pena; o sob medida é a IA + o cérebro + a ligação com Shopify/Hotmart.

## Fases
| Fase | Marca | O agente faz | Critério para avançar |
|---|---|---|---|
| **0. Teste no escuro** | NP | Responde 50–100 conversas reais antigas (exportadas), sem cliente ver. Comparamos com o que o time respondeu. | ≥ 90% respostas corretas e **0** violações do NAO-DIZER |
| **1. Noite/fim de semana — suporte** | NP | "Cadê meu pote" (Shopify), composição, modo de uso, políticas. Resto → humano de manhã. | 2 semanas estável |
| **2. Noite — vendas** | NP | Recomenda por objetivo (só alegações aprovadas), manda link de checkout. | conversão medida |
| **3. FSA** | FSA | Suporte de aluno ("onde acesso") + dúvidas da pós + captação de lead para o comercial. | — |
| **4. Horário comercial** | todas | IA sugere resposta, humano aprova e envia. | — |

## Passagem para humano (sempre)
Doença / gestação / criança / remédio · reclamação ou cliente irritado · pedido de reembolso · qualquer coisa que não esteja no cérebro · pedido explícito ("quero falar com uma pessoa").
De manhã o time recebe: **resolvidas · pendentes (com resumo) · leads quentes**.

## Métricas (para saber se valeu)
- Conversas fora do horário / semana (hoje: _medir_)
- % resolvidas sem humano
- Vendas atribuídas a conversas noturnas (link com UTM)
- Erros graves (meta: zero)

## Pendências — decisões da Gisele
- [ ] Hoje o WhatsApp da NP é o **app WhatsApp Business** ou já é a **API oficial** (com alguma plataforma)? Qual?
- [ ] Horário comercial exato (início/fim, sábado?)
- [ ] Exportar 50–100 conversas antigas do WhatsApp da NP (noturnas/fim de semana) para a Fase 0
- [ ] Documentos de política (entrega, troca, frete) — `marcas/natural-pure/politicas/`
- [ ] Quem é o responsável técnico que valida o `NAO-DIZER.md` e as alegações
- [ ] O que o agente pode oferecer: cupom? frete? (padrão: **nada** que não esteja escrito)
