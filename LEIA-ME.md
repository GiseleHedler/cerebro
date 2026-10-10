# 🧠 Cérebro — Grupo Saúde Avançada

Fonte única da verdade da empresa. Todo agente (atendimento, criativos, financeiro, Central de Comando)
e toda pessoa do time consulta **daqui**. Se uma informação está em dois lugares, um deles está errado.

## As 3 camadas

| Camada | Pasta | O que é | Quem altera |
|---|---|---|---|
| **Contexto** | `empresa/`, `marcas/`, `setores/` | Quem somos, produtos, políticas, tom de voz. Muda pouco. | Dono da pasta, com aprovação |
| **Memória** | `memoria/` | Decisões, aprendizados, mudanças de rumo. Muda sempre. | Qualquer um propõe; humano aprova |
| **Ação** | `skills/`, `projetos/` | Como fazer as coisas + agentes em construção. | Gisele + Claude |

## Regras de ouro

1. **Cada pasta tem um DONO** (ver `LEIA-ME.md` de cada pasta). Sem dono, a pasta apodrece.
2. **Nada que um agente fala com CLIENTE muda sem aprovação humana.** Agentes podem *propor*, nunca publicar sozinhos.
3. **Marcas não se misturam.** NP e FSA são empresas (CNPJs) diferentes. O agente da NP só lê `marcas/natural-pure/` + `empresa/`.
4. **Nenhum dado pessoal de cliente aqui.** Nada de nome, telefone, conversa, exame. Padrões sim ("20 pessoas perguntaram X"), pessoas não. (LGPD — dado de saúde é sensível.)
5. **Status em todo documento de cliente:** `✅ aprovado`, `🟡 rascunho`, `🔴 em revisão — NÃO USAR`. Agente só usa `✅`.

## Quem lê o quê

| Consumidor | Lê |
|---|---|
| Agente de atendimento NP | `empresa/`, `marcas/natural-pure/` (só `✅`) |
| Agente de atendimento FSA | `empresa/`, `marcas/fsa/` (só `✅`) |
| Central de Comando (financeiro) | `empresa/metas.md`, `setores/financeiro/`, `memoria/` |
| Agente de criativos | `marcas/*/`, `skills/`, `memoria/aprendizados/` |
| Time (via Projeto no Claude) | tudo |

## Como adicionar um setor novo
1. Preencher `setores/<setor>/LEIA-ME.md` (dono, o que contém, quem lê).
2. Colocar o conteúdo **que algum agente ou pessoa vai usar de fato** — não o que "seria bom ter".
3. Registrar em `memoria/decisoes/` que o setor entrou.
