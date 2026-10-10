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

**A NP já tem a caixa de entrada única: Duotalk** (WhatsApp pela API oficial; a Duotalk também atende Instagram DM, Messenger e WebChat).
Então **não vamos construir canal nenhum**. A IA se pluga na Duotalk, e o time continua usando a mesma tela para assumir conversas.
E-mail (contato@npnatural.com.br) fica para depois, como rascunho que o time aprova.

### Duas formas de plugar a IA na Duotalk (a confirmar com o suporte da Duotalk)
| | A) IA nativa da Duotalk | B) Nosso agente via API/webhook |
|---|---|---|
| Como | Configura a IA da própria Duotalk com o conteúdo do cérebro | A Duotalk avisa nosso servidor a cada mensagem; nosso agente (Claude + cérebro + Shopify) responde pela API |
| Velocidade | Rápido de ligar | Algumas semanas |
| Controle | Limitado ao que a Duotalk permite | Total: regras do NAO-DIZER, consulta de pedido na Shopify, teste no escuro, métricas |
| Consulta "cadê meu pote" | Depende de integração Shopify da Duotalk | Sim, direto na Shopify |

**Recomendação:** perguntar à Duotalk sobre a opção B. Se a API permitir receber e enviar mensagens e transferir para humano, vamos de B. A A serve de plano rápido só se for possível travar bem o que a IA fala.

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
- [x] WhatsApp NP = **API oficial via Duotalk** (10/10/2026)
- [ ] Perguntar à Duotalk: API/webhook para receber e enviar mensagens? transferir para humano? etiquetas? Instagram já conectado?
- [x] Horário humano: **seg–sex 9h–18h, exceto feriados** → o agente cobre **seg–sex 18h–9h + sábado, domingo e feriados inteiros**
- [ ] Exportar 50–100 conversas antigas do WhatsApp da NP (noturnas/fim de semana) para a Fase 0
- [x] Política de envios, trocas e devoluções (`marcas/natural-pure/politicas/`), com 7 lacunas a decidir
- [ ] Quem é o responsável técnico que valida o `NAO-DIZER.md` e as alegações
- [ ] O que o agente pode oferecer: cupom? frete? (padrão: **nada** que não esteja escrito)
