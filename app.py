import streamlit as st 
from subprocess import call
import pandas as pd
import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("<div><img src='https://pngimg.com/d/tiktok_PNG9.png' width=200 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("Este cuadro de mandos permite analizar las tendencias de tiktoks 📈 utilizando Python y Streamlit.")
st.sidebar.markdown("Para empezar <ol><li>Ingresa el <i>hashtag</i> que deseas analizar</li> <li>Presiona el boton <i>Obtener Data</i>.</li> <li>Visualiza los graficos</li></ol>",unsafe_allow_html=True)


st.write('La API de Tiktok requiere de subscripcion, por lo que el ultimo hashtag a utilizar fue el de "ai". ')
hashtag = st.text_input('Ingresa el Hashtag a buscar aqui', value="")



if st.button('Obtener data'):
    # Comando para activar el entorno virtual y ejecutar el script
    command = f'tiktokproject\\Scripts\\activate && python tiktok_2.py {hashtag}'
    call(command, shell=True)
    # call(['python ', 'tiktok_2.py ', hashtag])


    # df = pd.read_csv('data_final_inmuebles_hashtag.csv')
    df = pd.read_csv('data_final_ai_hashtag.csv')
    # df = pd.read_csv('data_final.csv')

    
    
    # Plot viz here
    fig = px.histogram(df, x='desc', y='statsV2_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)

    # Splits columns 
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_playCount', y='statsV2_commentCount', size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart - video stats
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heart', size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)
    
    # Show tabular dataframe in streamit
    df  

    