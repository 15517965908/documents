from txt2 import outt
import os


x=[]
y=[]
for flie_name in os.listdir('1'):
	if flie_name[-4:]=='.txt':
		x.append(flie_name)
for flie_name in os.listdir('2'):
	if flie_name[-4:]=='.txt':
		y.append(flie_name)
for _ in x:
	if _ in y:
		outt('1/'+_,'2/'+_,'3/'+_)