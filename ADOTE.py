import streamlit as st
import sqlite3
import requests

# Função para carregar e exibir uma imagem no canto esquerdo da tela
def carregar_imagem_canto_esquerdo_base64(imagem_base64):
    html_str = f"""
    <style>
    .img-container {{
        position: fixed;
        top: 0;
        left: 0;
    }}
    .img-container img {{
        max-height: 400px;
        max-width: 400px;
    }}
    </style>
    <div class="img-container">
        <img src="data:image/png;base64,{imagem_base64}">
    </div>
    """
    st.markdown(html_str, unsafe_allow_html=True)

# Função para salvar os dados do cadastro no banco de dados
def salvar_cadastro(conexao, nome, email, cpf, telefone, endereco, animal_preferido, razao_adocao, opcoes):
    cursor = conexao.cursor()
    query = """
    INSERT INTO cadastros (nome, email, cpf, telefone, endereco, animal_preferido, razao_adocao, opcoes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (nome, email, cpf, telefone, endereco, animal_preferido, razao_adocao, str(opcoes)))
    conexao.commit()

# Função para a tela de cadastro
def tela_cadastro():
    conexao = sqlite3.connect('caminho_para_seu_banco_de_dados.db')
    st.title("Cadastro para Adoção")
    
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        nasc = st.text_input("Data de nascimento")
        email = st.text_input("Email")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        endereco = st.text_input("Endereço")
        animal_preferido = st.selectbox("Animal de Preferência", ["Cachorro", "Gato"])
        razao_adocao = st.text_area("Por que você quer adotar um animal?")
        opcoes = [
            st.checkbox('Quero divulgar bichinhos fofos para adoção'),
            st.checkbox('Quero adotar um cachorro ou gato'),
            st.checkbox('Quero receber dicas de cuidados com meu pet'),
            st.checkbox('Marque esta caixa')
        ]
        
        enviado = st.form_submit_button("Enviar Cadastro")
        
        if enviado:
            salvar_cadastro(conexao, nome, email, cpf, telefone, endereco, animal_preferido, razao_adocao, opcoes)
    conexao.close()

# Função para a tela inicial
def tela_inicial():
    st.title("Bem-vindo ao Sistema de Adoção de Animais")
    st.write("Aqui você pode adotar seu novo melhor amigo!")
    if st.button("Quero Adotar"):
        tela_cadastro()

# Função para a tela "Sobre Nós"
def tela_sobre_nos():
    st.title("Sobre Nós")
    st.write("Somos uma organização comprometida com o bem-estar animal. Nosso objetivo é encontrar lares amorosos para animais abandonados ou em situação de risco. Acreditamos que cada animal merece uma segunda chance e trabalhamos incansavelmente para tornar isso possível.")
    carregar_imagem_canto_esquerdo_base64("sua_string_base64_aqui")

# Função para a tela "Quero Ajudar"
def tela_quero_ajudar():
    st.title("Quero Ajudar")
    st.write("Se você quer ajudar, entre em contato conosco e faça uma doação. Você pode fazer uma doação de qualquer valor, desde que você acredite em nossa causa.")
    st.write("Entre em contato conosco através do email: contato@adote.com.br")
    st.write("Ou ligue para: 11 99999-9999")

# Função para a tela "Notícias"
def tela_noticias():
    st.title("Notícias sobre Animais Desaparecidos")
    st.write("Aqui você encontra as últimas notícias sobre animais desaparecidos. Nos ajude a encontrá-los!")
    url_da_api = 
