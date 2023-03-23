# Data Visualization with ggplot
# Boxplots
# Video 2.5

# Load the dataset as described in Video 1.3
library(tidyverse)
data <- forR <- read_excel("C:/Users/lrmacha/Desktop/Lee_analysis_computing/Data/PRACTICE/FILTERED/TOSINGLESHEET/MASTERSHEET/nozeros.xlsx")
data <- data %>%
  mutate(Course=as.factor(), Applications=as.numeric(Applications))




#THIS WORKS!!!!!!!
boxplot(data, xlab= "Applications", col="orange", notch = FALSE, horizontal = TRUE, las=1, cex=0.5, cex.lab=1, cex.axis=0.5)

m <- apply(data, MARGIN = 2, FUN = median, na.rm = TRUE)
m

o <- order(m, decreasing = FALSE)
o

give.n <- function(x){
  return(c(y = mean(x), label = length(x)))
}

boxplot(data[, o], data, xlab= "Applications", col="orange", notch = FALSE, horizontal = TRUE, las=1, cex=0.5, cex.lab=1, cex.axis=0.5)





