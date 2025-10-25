import funcoes

treinos = []

def main():
    funcoes.registrar_log("Carregando dados")
    funcoes.carregar_dados(treinos)

    while True:
         print("""
               ========== REGISTRO DE TREINOS ==========
               1- Adicionar treino
               2- Exibir treinos 
               3- Alterar treinos
               4- Deletar treino
               5- Log out""")
         escolha_do_usuario = int(input("Informe uma opção:"))

         funcoes.limpar_terminal()
         print("Opção desejada: ", escolha_do_usuario)