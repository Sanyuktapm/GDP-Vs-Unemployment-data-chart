# -*- coding: utf-8 -*-
# Author: Sanyunkta Prakash Mudakannavar
# Princeton High School
# GDP Vs Unemployment data analysis
# Takes the CSV GDP and CSV Unemplyment data and makes use of panda Data frame mapes on a
# chart analysis to display correlation 
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

#
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
#
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
#
csv_GDP= links["GDP"]
df_GDP = pd.read_csv(csv_GDP)
#
df_GDP.head()
#
csv_UMP= links["unemployment"]
df_UMP = pd.read_csv(csv_UMP)
#
df_UMP.head()
#
df_UMP.loc[df_UMP['unemployment'] > 8.5]
#
x = df_GDP["date"]
#
gdp_change = df_GDP['change-current']
#
unemployment = df_UMP['unemployment']
#
title = "The relationship between the chanage in GDP vs unemployment rates"
#
file_name = "index.html"
#Fill up the parameters in the following function:
make_dashboard(x, gdp_change , unemployment, title, file_name)

