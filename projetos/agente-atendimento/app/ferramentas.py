# -*- coding: utf-8 -*-
"""
Ferramentas que o agente pode usar.
- consultar_pedido: status e rastreio na Shopify. Exige nº do pedido + e-mail da compra
  (os dois precisam bater), e devolve só status, itens e rastreio, nada de endereço ou CPF.
- transferir_para_humano: marca a conversa para o time, com etiqueta e resumo.
"""
import os
import json
import urllib.parse
import urllib.request
import urllib.error

API_VERSION = "2026-01"

FERRAMENTAS = [
    {
        "name": "consultar_pedido",
        "description": (
            "Consulta status, itens e código de rastreio de um pedido da loja Natural Pure. "
            "Use quando o cliente perguntar sobre o pedido, entrega ou rastreio. Precisa do número do "
            "pedido E do e-mail usado na compra; se o cliente não informou os dois, peça antes de chamar."
        ),
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "numero_pedido": {"type": "string", "description": "Número do pedido, ex.: 1234 ou #1234"},
                "email": {"type": "string", "description": "E-mail usado na compra"},
            },
            "required": ["numero_pedido", "email"],
            "additionalProperties": False,
        },
    },
    {
        "name": "transferir_para_humano",
        "description": (
            "Marca a conversa para o time humano responder no próximo horário de atendimento. "
            "Use sempre que: o cliente citar doença, gestação, criança ou remédio; houver produto com problema; "
            "pedido de troca, devolução, reembolso ou cancelamento; reclamação; pedido atrasado; assunto que não está "
            "na base; ou o cliente pedir para falar com uma pessoa. Também para 'venda-quente' (cliente quer comprar e "
            "precisa de ajuda que você não consegue dar). Depois de chamar, escreva a mensagem final ao cliente."
        ),
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "etiqueta": {
                    "type": "string",
                    "enum": ["saude", "problema-produto", "troca-devolucao", "reembolso-cancelamento",
                             "reclamacao", "pedido-atrasado", "venda-quente", "fora-da-base", "pediu-humano"],
                },
                "resumo": {"type": "string", "description": "Resumo em 1-3 frases para o time, sem dados sensíveis desnecessários"},
            },
            "required": ["etiqueta", "resumo"],
            "additionalProperties": False,
        },
    },
]


def _shopify_token(store, cid, csec):
    body = urllib.parse.urlencode({"client_id": cid, "client_secret": csec,
                                   "grant_type": "client_credentials"}).encode()
    req = urllib.request.Request("https://%s/admin/oauth/access_token" % store, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())["access_token"]


def consultar_pedido(numero_pedido, email):
    store = os.environ.get("SHOPIFY_NP_STORE", "").replace("https://", "").strip("/")
    cid, csec = os.environ.get("SHOPIFY_NP_CLIENT_ID", ""), os.environ.get("SHOPIFY_NP_CLIENT_SECRET", "")
    if not (store and cid and csec):
        return {"erro": "consulta de pedidos indisponível no momento"}
    numero = "#" + numero_pedido.strip().lstrip("#")
    try:
        token = _shopify_token(store, cid, csec)
        url = "https://%s/admin/api/%s/orders.json?%s" % (store, API_VERSION, urllib.parse.urlencode(
            {"name": numero, "status": "any",
             "fields": "name,email,created_at,financial_status,fulfillment_status,cancelled_at,line_items,fulfillments"}))
        req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": token})
        with urllib.request.urlopen(req, timeout=20) as r:
            pedidos = json.loads(r.read().decode()).get("orders", [])
    except (urllib.error.URLError, KeyError, ValueError):
        return {"erro": "consulta de pedidos indisponível no momento"}
    p = next((o for o in pedidos if (o.get("email") or "").strip().lower() == email.strip().lower()), None)
    if not p:
        return {"encontrado": False, "mensagem": "nenhum pedido com esse número e esse e-mail"}
    rastreios = [{"codigo": f.get("tracking_number"), "link": f.get("tracking_url"), "transportadora": f.get("tracking_company")}
                 for f in p.get("fulfillments") or [] if f.get("tracking_number")]
    return {
        "encontrado": True,
        "pedido": p["name"],
        "feito_em": (p.get("created_at") or "")[:10],
        "pagamento": p.get("financial_status"),
        "envio": p.get("fulfillment_status") or "ainda não enviado",
        "cancelado": bool(p.get("cancelled_at")),
        "itens": ["%sx %s" % (i.get("quantity"), i.get("title")) for i in p.get("line_items") or []],
        "rastreio": rastreios,
    }


def executar(nome, entrada, estado):
    """Executa a ferramenta. `estado` acumula transferências para o canal (Duotalk) agir."""
    if nome == "consultar_pedido":
        return consultar_pedido(entrada["numero_pedido"], entrada["email"])
    if nome == "transferir_para_humano":
        estado.setdefault("transferencias", []).append(entrada)
        return {"ok": True, "mensagem": "conversa marcada para o time"}
    return {"erro": "ferramenta desconhecida"}
