# -*- coding: utf-8 -*-
"""
Lê a base de conhecimento do Google Drive (pasta "Cérebro"), que é a fonte oficial:
o time edita lá e o agente lê de lá.

Configuração (segredos do servidor):
  GOOGLE_SERVICE_ACCOUNT_JSON  conteúdo do JSON da conta de serviço do Google
  CEREBRO_DRIVE_PASTA_ID       id da pasta "Cérebro" (compartilhada com o e-mail da conta de serviço, como Leitor)

O agente lê da pasta "2. Natural Pure": os documentos da raiz e das subpastas Produtos,
Políticas e Atendimento. NUNCA lê a subpasta "Revisão". Recarrega a cada 10 minutos.
"""
import os
import io
import json
import time

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import conhecimento  # reaproveita os filtros (_sem_interno)

PASTA_MARCA = "2. Natural Pure"
SUBPASTAS = ["Produtos", "Políticas", "Atendimento"]
FOLDER = "application/vnd.google-apps.folder"
DOC = "application/vnd.google-apps.document"
VALIDADE = 600

_cache = {"quando": 0, "texto": None}


def _servico():
    info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
    cred = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/drive.readonly"])
    return build("drive", "v3", credentials=cred, cache_discovery=False)


def _filhos(drive, pasta_id):
    itens, token = [], None
    while True:
        r = drive.files().list(q="'%s' in parents and trashed = false" % pasta_id,
                               fields="nextPageToken, files(id, name, mimeType)", pageSize=200,
                               pageToken=token).execute()
        itens += r.get("files", [])
        token = r.get("nextPageToken")
        if not token:
            return sorted(itens, key=lambda f: f["name"])


def _texto(drive, doc_id):
    buf = io.BytesIO()
    req = drive.files().export_media(fileId=doc_id, mimeType="text/markdown")
    baixar = MediaIoBaseDownload(buf, req)
    feito = False
    while not feito:
        _, feito = baixar.next_chunk()
    return buf.getvalue().decode("utf-8")


def montar():
    if _cache["texto"] and time.time() - _cache["quando"] < VALIDADE:
        return _cache["texto"]
    drive = _servico()
    raiz = os.environ["CEREBRO_DRIVE_PASTA_ID"]
    marca = next(f for f in _filhos(drive, raiz) if f["name"] == PASTA_MARCA and f["mimeType"] == FOLDER)
    partes = []
    pastas = [("", marca["id"])] + [(f["name"], f["id"]) for f in _filhos(drive, marca["id"])
                                    if f["mimeType"] == FOLDER and f["name"] in SUBPASTAS]
    for nome_pasta, pid in pastas:
        for f in _filhos(drive, pid):
            if f["mimeType"] != DOC:
                continue
            texto = conhecimento._sem_interno(_texto(drive, f["id"]))
            partes.append("<documento pasta=\"%s\" nome=\"%s\">\n%s\n</documento>" % (
                nome_pasta or PASTA_MARCA, f["name"], texto.strip()))
    _cache.update(quando=time.time(), texto="\n\n".join(partes))
    return _cache["texto"]
