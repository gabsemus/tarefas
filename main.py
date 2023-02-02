import datetime
import streamlit as st

st.title('Tarefas da House')

st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Selecione uma opção',['Inserir Tarefa', 'Todas as Tarefas'])

if pagSelecionada == 'Inserir Tarefa':
    st.header('Inserir Tarefa')

    with st.form(key='icluirTarefa'):
        tarefa = st.text_input(label='Tarefa: ')
        data = st.date_input('Data')
        hora = st.time_input('Hora')
        botao = st.form_submit_button('Inserir')
    
    


elif pagSelecionada == 'Todas as Tarefas':
    st.header('Tarefas')
