import função_01
import streamlit as st 

st.title("calculadora de media dos alunos")

nome = st.text_input("Digite o nome do aluno: ")
nota1 = st.number_input("Digite a primeira nota: ", min_value=0.0, max_value=10.0)
nota2 = st.number_input("Digite a segunda nota: ", min_value=0.0, max_value=10.0)
nota3 = st.number_input("Digite a terceira nota: ", min_value=0.0, max_value=10.0)
nota4 = st.number_input("Digite a quarta nota: ", min_value=0.0, max_value=10.0)





botao_imc = st.button("calcular media")
if botao_imc:
    media = função_01.calcula_media(nota3,nota2,nota1,nota4)
    situacao = função_01.situacao_media(media)
    texto = f"O aluno: {nome}, esta {situacao}, com media: {media}"
    if situacao == "Aprovado": 
        st.success(texto)
    elif situacao == "Recuperação":
        st.warning(texto)
    else:
        st.error(texto)