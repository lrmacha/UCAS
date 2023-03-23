library(readxl)

#read in the UCAs data file
df1 <- read_excel("C:/Users/lrmacha/Desktop/Lee_analysis_computing/Data/PRACTICE/duplicates_removed.xlsx", 
                  col_types = c("numeric", "text", "text", 
                                "text", "text", "text", "numeric", 
                                "numeric", "numeric"))
#rename to ir
ir = df1

##do k-means clustering (3 clusters) on application, offers and acceptances columns
km3= kmeans(ir[,7:9],3,iter.max=100)
km3
ir$KM3= km3$cluster # add a km3 column to ir

####print out ir dataframe as excel
write_xlsx(ir, "C:/Users/lrmacha/Desktop/Lee_analysis_computing//k_means_UCAS.xlsx")





