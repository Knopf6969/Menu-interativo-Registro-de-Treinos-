import csv
import os
from datetime import datetime

# Caminho dos arquivos de dados
ARQUIVO_DADOS = "dados/treinos.csv"
ARQUIVO_LOG = "dados/log.txt"

# Garantir que a pasta dados/ existe
def garantir_pasta_dados():
    """Cria a pasta dados/ se não existir."""
    if not os.path.exists("dados"):
        os.makedirs("dados")

# Inicializar arquivos se não existirem
def inicializar_arquivos():
    """Cria os arquivos de dados e log se não existirem."""
    garantir_pasta_dados()
    
    # Criar arquivo de dados com cabeçalho
    if not os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Exercício", "Duração (min)", "Data"])
        except IOError as e:
            print(f"Erro ao criar arquivo de dados: {e}")
    
    # Criar arquivo de log se não existir
    if not os.path.exists(ARQUIVO_LOG):
        try:
            with open(ARQUIVO_LOG, "w", encoding="utf-8") as f:
                f.write("=== LOG DE EXECUÇÃO - REGISTRO DE TREINOS ===\n")
        except IOError as e:
            print(f"Erro ao criar arquivo de log: {e}")

def registrar_log(acao):
    """Registra uma ação no arquivo de log com data e hora."""
    try:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{data_hora}] {acao}\n")
    except IOError as e:
        print(f"Erro ao registrar log: {e}")

def carregar_dados():
    """Carrega os dados do arquivo CSV e retorna uma lista de dicionários."""
    treinos = []
    try:
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row:
                        treinos.append(row)
    except IOError as e:
        print(f"Erro ao ler arquivo de dados: {e}")
    
    return treinos

def salvar_dados(treinos):
    """Salva os dados em um arquivo CSV."""
    try:
        with open(ARQUIVO_DADOS, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["ID", "Exercício", "Duração (min)", "Data"])
            writer.writeheader()
            writer.writerows(treinos)
    except IOError as e:
        print(f"Erro ao salvar arquivo de dados: {e}")

def gerar_id(treinos):
    """Gera um novo ID único para um treino."""
    if not treinos:
        return "1"
    ids = [int(t["ID"]) for t in treinos if t["ID"].isdigit()]
    return str(max(ids) + 1) if ids else "1"

def cadastrar_treino(treinos):
    """Cadastra um novo treino."""
    print("\n" + "="*50)
    print("📝 CADASTRAR NOVO TREINO")
    print("="*50)
    
    try:
        exercicio = input("Nome do exercício: ").strip()
        if not exercicio:
            print("❌ Erro: O nome do exercício não pode estar vazio.")
            registrar_log("Tentativa de cadastro com exercício vazio - FALHOU")
            return
        
        try:
            duracao = float(input("Duração (em minutos): "))
            if duracao <= 0:
                print("❌ Erro: A duração deve ser um número positivo.")
                registrar_log("Tentativa de cadastro com duração inválida - FALHOU")
                return
        except ValueError:
            print("❌ Erro: A duração deve ser um número válido.")
            registrar_log("Tentativa de cadastro com duração não numérica - FALHOU")
            return
        
        data = input("Data do treino (DD/MM/YYYY): ").strip()
        if not data:
            data = datetime.now().strftime("%d/%m/%Y")
        
        novo_id = gerar_id(treinos)
        novo_treino = {
            "ID": novo_id,
            "Exercício": exercicio,
            "Duração (min)": str(duracao),
            "Data": data
        }
        
        treinos.append(novo_treino)
        salvar_dados(treinos)
        
        print(f"\n✅ Treino cadastrado com sucesso! (ID: {novo_id})")
        registrar_log(f"Cadastro de novo treino - Exercício: {exercicio}, Duração: {duracao} min, Data: {data}")
        
    except Exception as e:
        print(f"❌ Erro inesperado ao cadastrar treino: {e}")
        registrar_log(f"Erro ao cadastrar treino: {e}")

def listar_treinos(treinos):
    """Lista todos os treinos cadastrados."""
    print("\n" + "="*50)
    print("📋 LISTA DE TREINOS")
    print("="*50)
    
    if not treinos:
        print("Nenhum treino cadastrado ainda.")
        registrar_log("Listagem de treinos - Nenhum treino encontrado")
        return
    
    print(f"\n{'ID':<5} {'Exercício':<20} {'Duração (min)':<15} {'Data':<12}")
    print("-" * 52)
    
    for treino in treinos:
        print(f"{treino['ID']:<5} {treino['Exercício']:<20} {treino['Duração (min)']:<15} {treino['Data']:<12}")
    
    print(f"\nTotal de treinos: {len(treinos)}")
    registrar_log(f"Listagem de treinos - Total: {len(treinos)} treino(s)")

def editar_treino(treinos):
    """Edita um treino existente."""
    print("\n" + "="*50)
    print("✏️  EDITAR TREINO")
    print("="*50)
    
    if not treinos:
        print("Nenhum treino cadastrado para editar.")
        registrar_log("Tentativa de edição - Nenhum treino encontrado")
        return
    
    try:
        id_treino = input("Digite o ID do treino a editar: ").strip()
        
        treino_encontrado = None
        indice = -1
        
        for i, treino in enumerate(treinos):
            if treino["ID"] == id_treino:
                treino_encontrado = treino
                indice = i
                break
        
        if not treino_encontrado:
            print(f"❌ Treino com ID {id_treino} não encontrado.")
            registrar_log(f"Tentativa de edição do ID {id_treino} - Não encontrado")
            return
        
        print(f"\nTreino atual:")
        print(f"  Exercício: {treino_encontrado['Exercício']}")
        print(f"  Duração: {treino_encontrado['Duração (min)']} min")
        print(f"  Data: {treino_encontrado['Data']}")
        
        novo_exercicio = input("\nNovo exercício (deixe em branco para manter): ").strip()
        if novo_exercicio:
            treino_encontrado["Exercício"] = novo_exercicio
        
        nova_duracao = input("Nova duração em minutos (deixe em branco para manter): ").strip()
        if nova_duracao:
            try:
                duracao_float = float(nova_duracao)
                if duracao_float <= 0:
                    print("❌ Erro: A duração deve ser um número positivo.")
                    registrar_log(f"Tentativa de edição do ID {id_treino} com duração inválida - FALHOU")
                    return
                treino_encontrado["Duração (min)"] = str(duracao_float)
            except ValueError:
                print("❌ Erro: A duração deve ser um número válido.")
                registrar_log(f"Tentativa de edição do ID {id_treino} com duração não numérica - FALHOU")
                return
        
        nova_data = input("Nova data (DD/MM/YYYY) (deixe em branco para manter): ").strip()
        if nova_data:
            treino_encontrado["Data"] = nova_data
        
        treinos[indice] = treino_encontrado
        salvar_dados(treinos)
        
        print(f"\n✅ Treino {id_treino} editado com sucesso!")
        registrar_log(f"Edição do treino ID {id_treino} - Exercício: {treino_encontrado['Exercício']}, Duração: {treino_encontrado['Duração (min)']} min")
        
    except Exception as e:
        print(f"❌ Erro inesperado ao editar treino: {e}")
        registrar_log(f"Erro ao editar treino: {e}")

def excluir_treino(treinos):
    """Exclui um treino existente."""
    print("\n" + "="*50)
    print("🗑️  EXCLUIR TREINO")
    print("="*50)
    
    if not treinos:
        print("Nenhum treino cadastrado para excluir.")
        registrar_log("Tentativa de exclusão - Nenhum treino encontrado")
        return
    
    try:
        id_treino = input("Digite o ID do treino a excluir: ").strip()
        
        treino_encontrado = None
        indice = -1
        
        for i, treino in enumerate(treinos):
            if treino["ID"] == id_treino:
                treino_encontrado = treino
                indice = i
                break
        
        if not treino_encontrado:
            print(f"❌ Treino com ID {id_treino} não encontrado.")
            registrar_log(f"Tentativa de exclusão do ID {id_treino} - Não encontrado")
            return
        
        print(f"\nTreino a ser excluído:")
        print(f"  Exercício: {treino_encontrado['Exercício']}")
        print(f"  Duração: {treino_encontrado['Duração (min)']} min")
        print(f"  Data: {treino_encontrado['Data']}")
        
        confirmacao = input("\nTem certeza que deseja excluir este treino? (s/n): ").strip().lower()
        
        if confirmacao == "s":
            treinos.pop(indice)
            salvar_dados(treinos)
            print(f"\n✅ Treino {id_treino} excluído com sucesso!")
            registrar_log(f"Exclusão do treino ID {id_treino} - Exercício: {treino_encontrado['Exercício']}")
        else:
            print("❌ Exclusão cancelada.")
            registrar_log(f"Tentativa de exclusão do ID {id_treino} - CANCELADA")
        
    except Exception as e:
        print(f"❌ Erro inesperado ao excluir treino: {e}")
        registrar_log(f"Erro ao excluir treino: {e}")

def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "="*50)
    print("🏋️  SISTEMA DE REGISTRO DE TREINOS")
    print("="*50)
    print("1. Cadastrar Treino")
    print("2. Listar Treinos")
    print("3. Editar Treino")
    print("4. Excluir Treino")
    print("5. Sair")
    print("="*50)
    opcao = input("Escolha uma opção (1-5): ").strip()
    return opcao

