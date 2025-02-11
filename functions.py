# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:35:31 2025

@author: AndrewKibirango
"""
import pandas as pd

def Clean(data):
    data.drop(columns=['id'])
    data['name_of_borrower'] = data['name_of_borrower'].str.title()
    data['email_of_borrower'] = data['email_of_borrower'].replace({'no email':'no_email'})
    data['highest_education_level'] = data['highest_education_level'].replace({'not available':'not_available'})
    data['employment_status'] = data['employment_status'].str.replace('Self-employed','self_employed')
    data['Gender'] = data['Gender'].str.replace(' ','')
    data['Loan_amount'] = data['Loan_amount'].str.replace(',','')
    data['Loan_amount'] = pd.to_numeric(data['Loan_amount'])
    data['Loan_amount'] = data['Loan_amount'].astype(int)
    data['Date_of_loan_issue'] = pd.to_datetime(data['Date_of_loan_issue'])
    data['Date_of_repayments_commencement'] = pd.to_datetime(data['Date_of_repayments_commencement'])
    data['Tenure_of_loan']=data['Tenure_of_loan'].str.replace('days','')
    data['Tenure_of_loan']=round(pd.to_numeric(data['Tenure_of_loan'])/30,0)
    data['Tenure_of_loan']=data['Tenure_of_loan'].astype(int)
    data['Interest_rate']=data['Interest_rate']/100
    data['Loan_type']=data['Loan_type'].str.replace(' ','')
    data['Loan_term_value']= 'Months'
    data['Location_of_borrower']=data['Location_of_borrower'].str.title()
    data['Expected_monthly_installment']=pd.to_numeric(data['Expected_monthly_installment'].str.replace(',','')).astype(int)
    data=data.drop(columns = ['created'])
    data['Length_of_time_running']=data['Date_of_loan_issue'] - pd.to_datetime(data['Length_of_time_running'], format ='mixed', errors ='coerce')
    data['Length_of_time_running']=data['Length_of_time_running'].dt.days
    (data['Length_of_time_running']//365).astype('Int64')
    data['Person_with_disabilities']=data['Person_with_disabilities'].str.replace('false','No').str.replace(' ','')
    data['Rural_urban']=data['Rural_urban'].str.replace(' ','')
    data['Number_of_employees_that_are_refugees']=data['Number_of_employees_that_are_refugees'].str.replace(' ','')
    data['Number_of_employees_that_are_refugees']=pd.to_numeric(data['Number_of_employees_that_are_refugees'])
    data['Number_of_employees_with_disabilities']=data['Number_of_employees_with_disabilities'].fillna(0).astype('Int64')
    data['job']=data['Loan_purpose']+data['Line_of_business']
    sector_keywords = {
    'Enterprise':['business'],
    'Agriculture':['agri','GROWING'],
    'Transport':['BODA']}
    data['sector']='None'
    for index, row in data.iterrows():
        activity = row['job']
    for a,b in sector_keywords.items():
        for c in b:
            if c in activity:
                data.at[index,'Sector'] = a
                break
                risk = data['Sector']=='Transport'
                data[risk]
    region_keywords = {
    'Western' : ['Kabale','Ntugamo'],
    'Central' : ['Ntungamo']}
    data['Region'] = 'None'
    for index, row in data.iterrows():
        location = row['Location_of_borrower']
    for a,b in region_keywords.items():
        for c in b:
            if c in location:
                data.at[index,'Region'] = a
                break
    loc = data['Region']=='Western'
    data[loc]

    return data