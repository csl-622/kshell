import csv


f = open('./12/RO_edges.csv','rb')
fw = open('./12/dataset12.txt','w+')
reader = csv.reader(f)
for row in reader:
	fw.write(row[0]+"\t"+row[1]+"\n")

f.close()
fw.close()