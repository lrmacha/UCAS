import pandas as pd


writer = pd.ExcelWriter('Applicationsonly.xlsx', engine='xlsxwriter')

all_dfs = pd.read_excel('MASTERSHEET.xlsx', usecols='I', sheet_name=None, header=0)

for sheet, all_dfs in  all_dfs.items(): # .use .items for python 3.X
    all_dfs.to_excel(writer, sheet_name = sheet, index=0)


writer.save()


