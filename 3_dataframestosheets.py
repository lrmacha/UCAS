import pandas as pd



import glob

file_list = glob.glob("*.xlsx")

files = []

for filename in file_list:
    df=pd.read_excel(filename)
    files.append(df)
        
writer = pd.ExcelWriter('./MASTERSHEET.xlsx', engine='xlsxwriter')
sheet_names = file_list

for df, sheet_name in zip(files, sheet_names):
    df.to_excel(writer, sheet_name=sheet_name)
writer.save()

