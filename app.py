# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:37:53 2022

@author: jahop_fz60h0
"""

import streamlit as st
import pandas as pd

st.title("Indicadores de compresión")


data = pd.read_csv("compresion-ipnp.csv")
data = data.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para IPNP")
col1.write(data)

col2.subheader("Gráfica para IPNP")
col2.bar_chart(data)

################################################

data1 = pd.read_csv("compresion-mtbf.csv")
data1 = data1.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTBF")
col1.write(data1)

col2.subheader("Gráfica para MTBF")
col2.bar_chart(data1)

#################################################

data2 = pd.read_csv("compresion-mttr.csv")
data2 = data2.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTTR")
col1.write(data2)

col2.subheader("Gráfica para MTTR")
col2.bar_chart(data2)

#################################################

data3 = pd.read_csv("compresion-dm.csv")
data3 = data3.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para DM")
col1.write(data3)

col2.subheader("Gráfica para DM")
col2.bar_chart(data3)



#BOMBEO+++++++++++++++++++++++++++++++++++++++++++++++++++

st.title("Indicadores de bombeo")

data4 = pd.read_csv("bombeo-ipnp.csv")
data4 = data4.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para IPNP")
col1.write(data4)

col2.subheader("Gráfica para IPNP")
col2.bar_chart(data4)

################################################

data5 = pd.read_csv("bombeo-mtbf.csv")
data5 = data5.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTBF")
col1.write(data5)

col2.subheader("Gráfica para MTBF")
col2.bar_chart(data5)

#################################################

data6 = pd.read_csv("bombeo-mttr.csv")
data6 = data6.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTTR")
col1.write(data6)

col2.subheader("Gráfica para MTTR")
col2.bar_chart(data6)

#################################################

data7 = pd.read_csv("bombeo-dm.csv")
data7 = data7.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para DM")
col1.write(data7)

col2.subheader("Gráfica para DM")
col2.bar_chart(data7)

#GENERACIÓN#################################################################################################

st.title("Indicadores de generación")

data8 = pd.read_csv("generacion-ipnp.csv")
data8 = data8.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para IPNP")
col1.write(data8)

col2.subheader("Gráfica para IPNP")
col2.bar_chart(data8)

################################################

data9 = pd.read_csv("generacion-mtbf.csv")
data9 = data9.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTBF")
col1.write(data9)

col2.subheader("Gráfica para MTBF")
col2.bar_chart(data9)

#################################################

data10 = pd.read_csv("generacion-mttr.csv")
data10 = data10.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para MTTR")
col1.write(data10)

col2.subheader("Gráfica para MTTR")
col2.bar_chart(data10)

#################################################

data11 = pd.read_csv("generacion-dm.csv")
data11 = data11.set_index('mes')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([20, 40])

col1.subheader("Tabla para DM")
col1.write(data11)

col2.subheader("Gráfica para DM")
col2.bar_chart(data11)

########################################################
st.subheader('')
st.subheader('')
st.subheader('Página creada por:')
st.header('Javier Horacio Pérez Ricárdez')
