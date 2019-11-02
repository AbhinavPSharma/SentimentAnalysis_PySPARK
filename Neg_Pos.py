import csv
import preprocessor as p
file1 = open("neg.txt","a")
file2 = open("pos.txt","a")
with open('D:/HPC-proj/datasetfinal.csv','rt', encoding="utf-8")as f:
  data = csv.reader(f)
  c=0
  for row in data:
    c+=1
    if c==1:
      continue;
    if not row:
      continue;
    i=row[0]
    if i=='0':
      file1.write(row[1]+"\n")
    else:
      file2.write(row[1]+"\n")
    print(c)