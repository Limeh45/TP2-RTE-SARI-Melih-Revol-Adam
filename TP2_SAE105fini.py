from math import *
import csv
import matplotlib.pyplot as plt
import numpy
tdc = []
with open ('RTE_2022.csv' , newline="")as csvfile :
	reader = csv.reader (csvfile, delimiter = ',')
	csvfile.readline()
	for row in reader :
		tdc.append(row)
date = []
consommation = []		
for row in tdc :
	date.append(row[2])
	consommation.append(row[4])

date_unique = []
for k in date :
  if k not in date_unique :
    date_unique.append(k)

for row in tdc :
	for i in range(len(row)):
		if row[i]=='':
			row[i] = 0

for i in range(len(consommation)) :
	if consommation[i] == '' :
		consommation[i] = 0
L=[]
for d in date_unique:
	total=0
	for row in tdc:
		if row[2]==d :
			total += int(row[4])
	L=L+[total]
trop = 365
del L[trop]
del date_unique[trop]


plt.title("consommation journalier a l'année")
plt.plot(date_unique, L)
plt.xlabel('jour')
plt.ylabel('consommation')
plt.show()


