import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# ------- Configuracion -------------
page_title ="Example of Dashboard"
page_icon = ":bar_chart:"
layout = "wide"
#-------------------------------

# Nota: Para poner los iconos pueden acceder el código:
# https://www.webfx.com/tools/emoji-cheat-sheet/ ó
# https://icons.getbootstrap.com/

# Aqui se establece la configuración de la página
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

#------- Carga de los Datos ------
df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
df_states = pd.read_csv("https://raw.githubusercontent.com/jeaggo/datasets/master/States_USA.csv")
#-------------------------------

#-------- Adecuación de datos para controles-------
state_options = df['State'].unique().tolist()
#--------------------------------

#---- Se genera una tabla con las ventas por estado ----
sales_df = df.pivot_table('Sales', 'State', aggfunc=np.sum)
#----------------------

#------ Integración de las bases de datos para la generación ----
#------ de un mapa ---------------------------------
df_state_sales = pd.merge(sales_df, df_states, on="State")
#-----------------------------------------

#------- Menu de Navegación ----------
selected = option_menu(
	menu_title=None,
	options=["Análisis General", "Hallazgos", "Modelo"],
	icons=["activity", "binoculars", "bezier2"],
	orientation="horizontal",
)

#----- Sección: Análisis General ------------
if selected == "Análisis General":
	# Un subencabezado de esta sección
	st.subheader("Descripción de la situación de la empresa")
	st.write('''
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
		Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. 
		Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed.
	''')
	with st.form("state_form"):
		state = st.multiselect('Which state would like to see', state_options, ['Texas'])
		submitted = st.form_submit_button("Submit")
		if submitted:
			state_option = df[df['State'].isin(state)]
			fig1 = px.histogram(state_option, x="Category", y="Profit", color="Category")
			fig1.update_layout(width=400)
			st.write(fig1)
#--------------------------

#----- Sección: Hallazgos ------------
if selected == "Hallazgos":
	# Aquí va un subencabezado
	st.header("Mapa con los hallazgos más sobresalientes")
	st.write('''
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
		Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. 
		Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed.
	''')
	fig2 = px.choropleth(df_state_sales, locations="Abbreviation", locationmode="USA-states", color="Sales", scope="usa")
	st.write(fig2)

#----- Sección: Modelo ------------
if selected == "Modelo":
	# Aquí va un encabezado
	st.header("Modelo 1")
	st.write('''
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
		Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. 
		Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed.
	''')
	fig3 = px.sunburst(df, path=['Segment', 'Region', 'Category'], values='Quantity')
	st.write(fig3)
	# Aquí va un encabezado
	st.header("Modelo 2")
	st.write('''
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
		Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. 
		Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed.
	''')
	colorscales = px.colors.named_colorscales()
	color = st.selectbox('Which color would like to see', colorscales)
	fig4 = px.parallel_categories(df, dimensions=['Region', 'Category', 'Quantity'], 
		color="Quantity", color_continuous_scale=color,
        labels={'Region':'Regions in USA','Category':'Categories','Quantity':'Quantity per month'})
	st.write(fig4)

