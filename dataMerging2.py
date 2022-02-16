import csv
import pandas as pd

file1 = 'bright_star.csv'
file2 = 'unit_converted_stars.csv'

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

pd1 = d1[1:]
pd2 = d2[1:]

h = h1 + h2

pd = []

for i in pd1:
    pd.append(i)
for i in pd2:
    pd.append(i)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(pd)