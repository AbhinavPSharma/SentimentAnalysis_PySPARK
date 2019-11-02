import csv
import preprocessor as p
with open('D:/HPC-proj/dataset1.csv','rt')as f:
  data = csv.reader(f)
  c=0
  for row in data:
  	t=row[1]
  	i=row[0]
  	with open('D:/HPC-proj/datasetcombine.csv', mode='a') as file:
  		writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  		writer.writerow([i,t])
  	print(c)
  	c+=1