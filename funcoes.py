import os
from datetime import datetime

def limpar_terminal():
    os.system("cls")

def registrar_log(acesso_do_usuario):
    arquivo_de_log = open("./dados/logs.sistema", "a", encoding="utf-8")
    arquivo_de_log.write(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] {acesso_do_usuario} \n")
    arquivo_de_log.close()

def carregar_dados(treinos):
    arquivo_de_treinos = open("./dados/treinos.sistema", "r", encoding="utf-8")
    linhas = arquivo_de_treinos.readlines()
    
    
    for linha in linhas:
        dia_da_semana, grupo_muscular, nome_do_exercicio, repetiçoes, observacoes = linha.strip().split(";")
        treinos = {"dia_da_semana": dia_da_semana, "grupo_muscular": grupo_muscular, "nome_do_exercicio": nome_do_exercicio, "repeticoes": repetiçoes, "observaçoes": observacoes}
        treinos.append(treinos)
    
