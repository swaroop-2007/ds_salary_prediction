# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:32:56 2022

@author: Swaroop
"""

import glassdoorscraping as gls
import pandas as pd

path = "C:/Users/Swaroop/programming/ds_salary_prediction/chromedriver"
df = gls.get_jobs('data scientist', 15, False, path, 15)