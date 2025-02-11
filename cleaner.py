# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:37:32 2025

@author: AndrewKibirango
"""

import streamlit as st
import pandas as pd
import numpy as np
import functions as fx


st.subheader('Wazzzzaaaa')

file = st.file_uploader("Select a file", type='xlsx')

if file is not None:

    data = pd.read_excel(file)
    
    df = fx.Clean(data)
    
    st.write(df.shape)
    st.write(df.head())
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        #show loan amount
        st.write('Loan Amount')
        amount = df['Loan_amount'].sum()
        st.metric('The loan amount is:',amount)
    
    with col2:
        #Show number of loans
        st.write('Number of loans')
        number = df['Borrower_ID'].count()
        st.metric('The loana:',number)
    
    with col3:
        #NUMBER OF YOUTH
        mask = df['Age']<=35
        st.write('Number of youths')
        youths = df[mask]['Borrower_ID'].count()
        st.metric('Number of youth:',youths)
    
    with col1:
        #Number of women
        mask = df['Gender']=='Female'
        st.write('Number of women')
        women = df[mask]['Borrower_ID'].count()
        st.metric('Number of women:',women)
    
    with col2:
        #Number of young women
        mask = (df['Gender']=='Female') & (df['Age']<=35)
        st.write('Number of Young women')
        youngwomen = df[mask]['Borrower_ID'].count()
        st.metric('Number of young women:',youngwomen)
    
    with col3:
        #Interest rate
        rate = df['Interest_rate'].mean()
        st.metric('The interest rate is:',rate)
    
    df.to_excel('data.xlsx', index = False)
    
    #add download button
    st.download_button(
        label = 'Click to download',
        data = df.to_csv(index = False),
        file_name = 'Cleaner_data.csv' 
        )