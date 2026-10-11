# O que falta para ligar o agente da Natural Pure

Atualizado em 11/10/2026. Cada bloco vai para uma pessoa. Quando algo ficar pronto, avise o Claude.

## 1. Quem fala com a Duotalk ✅ respondido em 11/10/2026
Respostas: tem API; WhatsApp e Instagram caem no mesmo lugar; dá para transferir e colocar etiquetas por API; a transferência avisa o time com som e mostra há quanto tempo a pessoa espera; o WhatsApp de suporte e o Instagram da NP já estão conectados.
- [ ] **Falta:** a documentação da API e o token de acesso
- [ ] **Falta confirmar:** o chat do site (WebChat) também está na Duotalk?

Perguntas originais:
Mandar ao suporte da Duotalk:
1. A Duotalk tem **API ou webhook** para um sistema externo **receber as mensagens** que chegam (WhatsApp e Instagram) e **enviar respostas** pela mesma conversa?
2. Por API, dá para **transferir a conversa para um atendente humano** e **colocar etiquetas**?
3. Quando o robô transfere, a conversa aparece numa **fila para o time, com aviso**? Dá para ver **há quanto tempo** ela está esperando?
4. O **Instagram** e o **chat do site (WebChat)** da Natural Pure já estão conectados na nossa conta?
5. Onde fica a **documentação técnica da API**, e como geramos o **token de acesso**?
- [x] Exportar o histórico de conversas (já pedido; chega na terça)

## 2. Quem cuida do GitHub 🔴 (2 minutos)
- [ ] Em github.com/GiseleHedler/cerebro → Settings → Secrets and variables → Actions → **New repository secret**: nome `ANTHROPIC_API_KEY`, valor = a mesma chave da Anthropic do cofre do Central (começa com `sk-ant-`).

## 3. Responsável técnico (nutricionista) 🟠
- [ ] Ler `marcas/natural-pure/NAO-DIZER.md` e `marcas/natural-pure/atendimento/GUIA-DE-LINGUAGEM.md` (~20 min). **Mínimo para ir ao ar.**
- [ ] Conferir no rótulo:
  - Magnésio 4X: a quantidade total (451 mg?) e se a forma é citrato ou treonato
  - Trio Sonus: a quantidade de cálcio (250 mg?)
  - Dekka: a vitamina A por porção
  - Pure B Balance: a B12 por cápsula
  - A origem dos colágenos e dos aminoácidos
- [ ] Depois, com calma: `marcas/natural-pure/revisao/REVISAO-RESPONSAVEL-TECNICO.md` (fichas, FAQ e frases do site)

## 4. Quem mexe no site / Shopify 🟠
- [ ] **FAQ do site:** trocar pelas respostas novas de `revisao/faq-site-reescrito.md`. Mais urgente: o **Dekka ainda diz 4.000 UI** (o certo é 2.000) e há "cálculo renal pode tomar? Pode, sim".
- [ ] Política de envios: "48horas" → "até 2 dias úteis"; "sem sinais de uso" → "com o lacre intacto"; incluir que o **frete da devolução é por conta da NP**, o **reembolso pelo mesmo meio de pagamento** e a **regra de produto com problema** (até 30 dias, sem custo).
- [ ] Contador "FRETE GRÁTIS por tempo limitado — 00:00:00" está zerado: corrigir ou tirar.
- [ ] Página de Amino Limonada Rosa traz o texto dos colágenos colado; sabores trocados nas listas de ingredientes dos colágenos.
- [ ] Shopify (opcional, ajuda o agente): no app do Central, adicionar as permissões `read_products` e `read_inventory`, para o agente ver estoque e preço ao vivo.

## 5. Jurídico 🟡 (sem pressa)
- [ ] Na devolução por arrependimento, pode exigir nota fiscal?
- [ ] A frase do site "o prazo de entrega não é de nossa responsabilidade (Correios)" pode ficar?

## 6. Decisões da Gisele 🟡
- [ ] O horário de atendimento é **8h ou 9h**? (o topo do site diz 8h; as páginas dizem 9h)
- [ ] Assinatura: como o cliente **cancela ou altera**, e o que acontece se o **cartão recusar**?
- [ ] O agente começa **só fora do horário** (recomendado nas 2 primeiras semanas) ou já **24h**?
- [ ] Quem do time é **dono** da pasta da Natural Pure no cérebro (mantém as informações em dia)?
