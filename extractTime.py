#/usr/env/python
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


""" 
Export the TimeSpent2022 Google Sheet to a csv file. 
The exported cvs file has the ProjectID as an integer. 
On the other hand, the exported xlsx leads to the ProjectIDs being exported as reals.
"""

df = pd.read_csv('/Users/blaine/6003TimeTracking/data/TimeSpent-Oct2022.csv')

# The next command converts the ProjectID to an integer.
df['ProjectID'] = df['ProjectID'].dropna().astype(int)

# Extract the time spent on all COBRE related projects
COBREadmin = df.loc[df['ProjectID'].isin([211,4514,
                                          7551,
                                          7552,
                                          7553,
                                          7554,
                                          7561,
                                          7571,
                                          7601,
                                          7602, 
                                          7603,
                                          7630,
                                          7631,
                                          7632,
                                          7633,
                                          7634,
                                          7635,
                                          7636,
                                          7637,
                                          7638,
                                          7639,
                                          7640,
                                          7641,
                                          7642,
                                          7643,
                                          7644,
                                          7645,
                                          7646,
                                          7647,
                                          7648,
                                          7648,
                                          7649,
                                          7651,
                                          7652,
                                          7653,
                                          7801,
                                          7654])]

# Print total effort
print(COBREadmin['DecimalTime'].sum())

# Now write out an Excel sheet. 
# I sort by Project ID and get the project subtotals in Excel.
# I need to add more pandas code to automate this step.
writer = ExcelWriter('COBREoctober2022.xlsx')
COBREadmin.to_excel(writer,'Sheet1',index=False)
writer.save()