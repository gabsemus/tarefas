import streamlit as st

st.title('Tarefas da House')

st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Selecione uma opção',['Inserir Tarefa', 'Todas as Tarefas'])

if pagSelecionada == 'Inserir Tarefa':
    st.header('Inserir Tarefa')

elif pagSelecionada == 'Todas as Tarefas':
    st.header('Tarefas')
