
# import pandas as pd
# import glob 



# all_data = pd.DataFrame()

# for f in glob.glob("*.xlsx"):
#      df = pd.read_excel(f, sheet_name='Table B.13', skiprows=0)
#      all_data = all_data.append(df,ignore_index=True)
     
 
    
# print(all_data)



# # now save the data frame
# writer = pd.ExcelWriter('output.xlsx')
# all_data.to_excel(writer,'sheet1' , index=(False))
# writer.save()    

import pandas as pd
data = pd.read_excel(r'C:\Users\lrmacha\Desktop\Lee_analysis_computing\Data\PRACTICE\output.xlsx')

print(data)
all_data = data.drop_duplicates()
print(data)


# now save the data frame
writer = pd.ExcelWriter('duplicates_removed.xlsx')
all_data.to_excel(writer,'sheet1' , index=(False))
writer.save()    

