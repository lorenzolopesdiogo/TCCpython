import json
import os

ARQUIVO = "contas.json" #nome do arquivo onde salva as contas 

#carrega as contas do arquivo se existir 

def carregar_contas():
    if os.path.exists(ARQUIVO):    # vai verifica se o arquivo vai existir 
        with open(ARQUIVO)