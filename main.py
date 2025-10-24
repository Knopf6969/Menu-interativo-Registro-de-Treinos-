#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arquivo de configuração do Sistema de Registro de Treinos.
Define constantes e configurações globais do sistema.
"""

import os

# Diretório de dados
DIRETORIO_DADOS = "dados"

# Caminhos dos arquivos
ARQUIVO_TREINOS = os.path.join(DIRETORIO_DADOS, "treinos.csv")
ARQUIVO_LOG = os.path.join(DIRETORIO_DADOS, "log.txt")

# Configurações de formatação
FORMATO_DATA = "%d/%m/%Y"
FORMATO_DATA_HORA = "%d/%m/%Y %H:%M:%S"

# Mensagens do sistema
MENSAGEM_BOAS_VINDAS = "🏋️  SISTEMA DE REGISTRO DE TREINOS"
MENSAGEM_DESPEDIDA = "👋 Até logo!"

# Validações
DURACAO_MINIMA = 0.1  # Duração mínima em minutos
DURACAO_MAXIMA = 1440  # Duração máxima em minutos (24 horas)

# Codificação de arquivos
CODIFICACAO = "utf-8"

# Separador de CSV
SEPARADOR_CSV = ","

