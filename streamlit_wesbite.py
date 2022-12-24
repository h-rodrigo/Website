# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
Title: Streamlit website                      "
Author: Hiru Rodrigo                          "
"""""""""""""""""""""""""""""""""""""""""""""""

#Import libraries 
import pandas as pd 
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
import streamlit_authenticator as stauth 
import pickle
from pathlib import Path 

def main(): 
      
    #Hyperlinks     
    st.sidebar.header("Useful Links:") 

    cpmi = "https://www.bis.org/cpmi/cross_border.htm" 
    st.sidebar.write("Research" % cpmi) 

    fsb = "https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/" 
    st.sidebar.write("Courses" % fsb) 

    fsb_targets = "https://www.fsb.org/wp-content/uploads/P131021-2.pdf" 
    st.sidebar.write("Apps and Projects" % fsb_targets) 

    roadmap_update = "https://www.fsb.org/wp-content/uploads/P101022-1.pdf" 
    st.sidebar.write("Book Reviews" % roadmap_update) 

    st.markdown(
    """
    <style>
    span[data-baseweb="tag"] {background-color: #7E7F7A !important;}  
    span[data-baseweb="tag"]>span{font-size: 13px}  
    </style>
    """,
    unsafe_allow_html=True,) 

    #Plots
    #Reading Main CB Dashboard tab from workbook 
    xls = (r'https://github.com/bocrodh/21eB6-WCN-Ao-v-JK-yRpRT0e-qp/blob/main/wb_remittance_data.xlsx?raw=true')

    cost = pd.read_excel(xls, 'Cost of sending $200', header=0)
    times = pd.read_excel(xls, '<1 Hour Options', header=0)
    provider = pd.read_excel(xls, 'Proportion of MT', header=0)
    banked = pd.read_excel(xls, 'Banked', header=0)
      
    st.header('Trends in XB Payment')
    st.subheader('Remittances')

    
    fig = px.line(cost, x="Year", y='%', color="Country", title="Remittance Fee as % of $200 <br><sup>Source: https://remittanceprices.worldbank.org/</sup>")
    fig.update_traces(mode="lines")
    fig.update_layout(hovermode="x unified") 
    fig.update_xaxes(tickangle= -90, nticks=4)
    fig.update_traces(patch={"line": {"color": "purple", "width": 6}}, selector={"legendgroup": "Canada"})
    fig.update_traces(patch={"line": {"color": "MidnightBlue", "width": 6, "dash": 'dot'}}, selector={"legendgroup": "G8"}) 
    fig.show() 
    #st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(times, x="Year", y='Number of Service Providers', color="Country", title="Access to <1 Hour Remittance Services (by corridor)<br><sup>Source: https://remittanceprices.worldbank.org/</sup>")
    fig2.update_traces(mode="lines")
    fig2.update_layout(hovermode="x unified") 
    fig2.update_xaxes(tickangle= -90, nticks=4)
    fig2.show() 
    #st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.line(banked, x='Year', y='% Banked', color="Country", title="% of Banked Population <br><sup>Source: https://databank.worldbank.org/source/global-financial-inclusion/</sup>")
    fig3.update_traces(mode="lines")
    fig3.update_layout(hovermode="x unified") 
    fig3.update_xaxes(tickangle= -90)
    fig3.update_traces(patch={"line": {"color": "purple", "width": 6}}, selector={"legendgroup": "Canada"})
    fig3.update_traces(patch={"line": {"color": "MidnightBlue", "width": 6, "dash": 'dot'}}, selector={"legendgroup": "G8"}) 
    fig3.show() 
    
    fig4 = px.line(provider, x='Year', y='%', color="Country", title="% of Remittances Completed Money Transfer Services (by corridor) <br><sup>Source: https://remittanceprices.worldbank.org/</sup>")
    fig4.update_traces(mode="lines")
    fig4.update_layout(hovermode="x unified") 
    fig4.update_xaxes(tickangle= -90, nticks=4)
    fig4.show() 
    
    plot1, plot2 = st.columns(2,gap='small')
    plot1.plotly_chart(fig, use_container_width=True)    
    plot2.plotly_chart(fig2, use_container_width=True)    
    
    plot3, plot4 = st.columns(2,gap='small')
    plot3.plotly_chart(fig3, use_container_width=True)    
    plot4.plotly_chart(fig4, use_container_width=True)
    
    main()
