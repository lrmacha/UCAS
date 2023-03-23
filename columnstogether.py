import pandas as pd



all_dfs = pd.read_excel('Applicationsonly.xlsx', sheet_name=None)

print (all_dfs)

writer = pd.ExcelWriter('forR.xlsx', engine='xlsxwriter')

df = pd.concat(all_dfs, ignore_index=False, axis=1)

df.to_excel(writer)


writer.save()