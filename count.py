import csv
import preprocessor as p
with open('D:/HPC-proj/datasetcombined.csv','rt',  encoding="utf8")as f:
  data = csv.reader(f)
  c=0
  for row in data:
  	c+=1
print(c)