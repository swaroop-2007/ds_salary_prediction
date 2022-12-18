# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:48:46 2022

@author: Swaroop
"""

import pandas as pd
import numpy as np

df = pd.read_csv('glassdoor_jobs.csv')
df

#We need: Salary parsing, company name, state field, age of company, parsing of job description

df = df.drop(['Unnamed: 0'], axis=1  )
#Salary Cleaning
df['hoursalary'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour'in x.lower() else 0) # Salary mentioned in hour in salary estimate
df['employeerprovided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:'in x.lower() else 0) # Salary mentioned in as employer provided  in salary estimate


df = df[df['Salary Estimate']!='-1']  # Removing the salary field where -1 is mentioned

sal = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) # Removed Glassdoor est
salary = sal.apply(lambda x: x.replace('K', '').replace('$', '')) # Removed $ and k from salary
salary = salary.apply(lambda x: x.replace('Per Hour','').replace('Employer Provided Salary:',''))

df['minsalary'] = salary.apply(lambda x: int(x.split('-')[0]))
df['maxsalary'] = salary.apply(lambda x: int(x.split('-')[1]))

df['averagesalary'] = (df.minsalary+df.maxsalary)/2

#Company Name
df['Company'] = df.apply(lambda x: x['Company Name']if x['Rating']<0 else x['Company Name'][:-3], axis=1) #Removed Company Ratings from Company Name

#State: Taking only state from the location column
df['state'] = df['Location'].apply(lambda x: x.split(',')[1])
#print(df.state.value_counts())

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1) #To check whether the company is located in the same state as its headquarters

#Years of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2022-x)  #Calculating the age of the company

#Parsing Job description
#Checking if Python is there in Job Description
df['python y/n'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#Checking if spark is there in Job Description
df['spark y/n'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#Checking if Excel is there in Job Description
df['excel y/n'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#Checking if aws is there in Job Description
df['aws y/n'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

df.to_csv('Cleaned_data.csv', index= False)
#df2 = pd.read_csv('Cleaned_data.csv')
