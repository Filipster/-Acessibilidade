import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import pytz as pytz
import matplotlib.pyplot as plt
import numpy as np
import datetime
from dateutil.relativedelta import *


from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder



@st.cache(allow_output_mutation=True)
def button_states():
    return {"pressed": None}

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
#timezone-handling
import streamlit as st
from datetime import datetime
import pytz


#Header
st.title('Descubre páginas preservadas👨‍💻')

st.sidebar.image("\\Users\\filip\\Downloads\\arquivo.pt+.png", use_column_width=True)

add_selectbox = st.sidebar.selectbox(
    "Exporte o resultado  da sua pesquisa",
    ("PDF", "XLSX", "JSON")
)

st.sidebar.write('Está com algum problema?')
help = st.sidebar.button(label = 'Peça ajuda agora 🔎')


with st.expander("O que é o arquivo.pt +acessibilidade?"):
     st.write("""
        É uma ferramenta do arquivo.pt projetada e
          desenvolvida para que pessoas com deficiência possam usá-las. Aqui nos importamos
          com a inclusão 👩‍🦼👨‍🦽👩‍🦯👭 🧑‍🤝‍🧑
     """)

tag = st.selectbox('Escolha a palavra para pesquisar', ['filmes','acessibilidade', 'finanças', 'desenvolvimento'])

slider = st.slider('Selecione o período de tempo da pesquisa',1996,2022)

#data loading
def data_upload():
    df = pd.read_csv("\\Users\\filip\\Downloads\\movie_metadata.csv")
    return df

df = data_upload()
st.dataframe(data=df)

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)


st.title('Pesquisa avançada')

sel_mode = st.radio('Tipo de seleção', options=['único', 'múltiplo'])
gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
gridoptions = gd.build()
AgGrid(df, gridOptions=gridoptions)

sitioweb = st.text_input('Sítio web. ex: www.arquivo.pt')
number = st.number_input('Número de resultados', min_value=10, step=10)

import plotly.figure_factory as ff
import numpy as np

st.write('Frequência de uso da palavra em artigos científicos')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Brasil', 'Portugal', 'Outro'])
st.area_chart(chart_data)
