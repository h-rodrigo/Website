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
    
    main()
