# Python code to filter and save the
# data with different file names
import pandas
import numpy as np


data = pandas.read_excel("duplicates_removed.xlsx")

dataset = np.array([  'Gaming & Animation ',	'Illustration with Animation',	'Animation Production',	'Visual Effects (VFX) For Film & TV',	'Animation',	'Digital Animation with FY',	'Visual Effects',	'Animation & Illustration',	'VFX with Animation ',	'Computer Animation with Art & Design  ',	'Computer Animation with Technical Arts',	'Animation DL',	'Games Animation',	'Game Animation',	'2D digital Animation',	'3D Digital Animation and Visual Effects ',	'Illustration Animation',	'Animation & Visual Effects',	'Illustration & Animation',	'3D Animation with Games',	'Animation with VFX',	'Animation with FY',	'Animation with Games Art',	'Computer animation',	'Games, Design & Animation',	'Animation with Illustration',	'Animation with Film Production',
]) #spits out excel files with these search terms
#make case sensitive for search terms

for i in dataset:
 	a = data[data["Course"].str.contains(i)]
 	a.to_excel(i+".xlsx")


