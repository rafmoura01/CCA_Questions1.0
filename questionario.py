import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Simulador de Questionário")

# Instruções
st.write("Por favor, responda às perguntas de múltipla escolha a seguir. Apenas uma alternativa é correta para cada pergunta.")

# Função para carregar o arquivo CSV com as perguntas
def carregar_perguntas(arquivo_csv):
    try:
        # Forçar encoding e verificar o separador
        df = pd.read_csv(arquivo_csv, encoding='utf-8', sep=';')
        # Remover espaços em branco dos nomes das colunas
        df.columns = df.columns.str.strip()
        #st.write("Colunas detectadas no CSV:", df.columns)  # Exibe as colunas para verificação
        #st.write(df.head())  # Exibe as primeiras linhas para garantir que os dados estão corretos
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo CSV: {e}")
        return None

# Carregar as perguntas do arquivo perguntas.csv
perguntas_df = carregar_perguntas("perguntas.csv")

if perguntas_df is not None:
    # Dicionário para armazenar as respostas do usuário
    respostas_usuario = {}

    # Loop para gerar as perguntas e alternativas a partir do DataFrame
    for index, row in perguntas_df.iterrows():
        pergunta = row['pergunta']
        alternativas = [row['alternativa1'], row['alternativa2'], row['alternativa3'], row['alternativa4']]
        respostas_usuario[pergunta] = st.radio(pergunta, alternativas)

    # Botão para enviar respostas
    if st.button('Enviar'):
        # Variável para contar acertos
        acertos = 0
        
        # Verificando as respostas
        for index, row in perguntas_df.iterrows():
            pergunta = row['pergunta']
            correta = row['correta']
            if respostas_usuario[pergunta] == correta:
                acertos += 1
        
        # Exibindo o resultado total sem mostrar as respostas corretas diretamente
        st.write(f"Você acertou {acertos} de {len(perguntas_df)} perguntas.")
        
        # Mostrando feedback individual para cada pergunta
        for index, row in perguntas_df.iterrows():
            pergunta = row['pergunta']
            correta = row['correta']
            if respostas_usuario[pergunta] == correta:
                st.write(f"{pergunta} - Correto! ✅")
            else:
                st.write(f"{pergunta} - Incorreto ❌")
