#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:54:22 2020

@author: imclumsypanda
"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

file=st.file_uploader('选择要上传的文件',type='csv')
if file is not None:
    df=pd.read_csv(file)
    
    xaxis=st.multiselect('选择x轴变量',options=df.columns,key=1)
    yaxis=st.multiselect('选择x轴变量',options=df.columns,key=2)
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df[xaxis],y=df[yaxis]))
    st.plotly_chart(fig, use_container_width=True)
    
