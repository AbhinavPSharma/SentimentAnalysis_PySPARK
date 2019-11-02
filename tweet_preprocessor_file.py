import csv
import preprocessor as p
with open('D:/HPC-proj/datasetcombined.csv','rt', encoding="utf-8")as f:
  data = csv.reader(f)
  c=0
  for row in data:
  	if not row:
  		continue;
  	t=p.clean(row[1])
  	i=row[0]
  	with open('D:/HPC-proj/datasetfinal.csv', mode='a', encoding="utf-8", newline='') as file:
  		writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  		writer.writerow([i,t])
  	c+=1
  	print(c)