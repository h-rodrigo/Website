# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
Title: Streamlit website                      "
Author: Hiru Rodrigo                          "
"""""""""""""""""""""""""""""""""""""""""""""""

#Import libraries 
import pandas as pd 
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path 

#Create blank webpage 
st.set_page_config( 
        page_icon=":chart_with_upwards_trend:", 
        layout="wide", 
)    

#Hyperlinks     
st.sidebar.header("Sections:") 

cpmi = "https://www.bis.org/cpmi/cross_border.html" 
st.sidebar.write("Research") 

fsb = "https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/" 
st.sidebar.write("Courses") 

fsb_targets = "https://www.fsb.org/wp-content/uploads/P131021-2.pdf" 
st.sidebar.write("Apps and Projects") 

roadmap_update = "https://www.fsb.org/wp-content/uploads/P101022-1.pdf" 
st.sidebar.write("Book Reviews") 

