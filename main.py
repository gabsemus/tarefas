import streamlit as st

#st.title('Lista de Tarefas')

st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Selecione uma opção',['Inserir Tarefa', 'Todas as Tarefas'])

if pagSelecionada == 'Inserir Tarefa':
    st.title('Inserir Tarefa')

elif pagSelecionada == 'Todas as Tarefas':
    st.title('Tarefas')
