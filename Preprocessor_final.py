import csv
import re
with open('D:/HPC-proj/datasetf.csv','rt', encoding="utf-8")as f:
  data = csv.reader(f)
  c=0
  for row in data:
    sentiment=row[0]
    tweet=row[1]
    tweet.strip()
    #remove url from the tweet
    tweet=re.sub(r"http\S+", "", tweet)
    #remove other characters from the tweet
    tweet=re.sub("[^a-zA-z]", " ", tweet)
    tweet=tweet.lower()
    #convert tweet in to list of words
    words_list=tweet.split()
    if "".join(words_list)=="" or "".join(words_list)==" ":
        continue;
    with open('D:/HPC-proj/datasetfinal.csv', mode='a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([sentiment, " ".join(words_list)])
    c+=1
    print(c)
