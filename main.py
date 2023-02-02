import datetime
import streamlit as st

st.title('Tarefas da House')

st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Selecione uma opção',['Inserir Tarefa', 'Todas as Tarefas'])

if pagSelecionada == 'Inserir Tarefa':
    st.header('Inserir Tarefa')

    with st.form(key='icluirTarefa'):
        tarefa = st.text_input(label='Tarefa: ')
        data = st.time_input('Data')
        hora = st.number_input('Hora')


elif pagSelecionada == 'Todas as Tarefas':
    st.header('Tarefas')
