
from helpers import *
import nltk

s="!#$%&()*+,-.:;<=>?@[\]^_`{'~}"
s+='"'
measureList=[
'teaspoon','tablespoon','cup','pint','quart',
'gallon','pinch','dash','lb','pound','cube','head','clove','ounce'
			]

def getName(line):

	text = nltk.word_tokenize(line)
	res=''
	lib=nltk.pos_tag(text)

	for i in range(0,len(lib)):
		marker=0
		for j in measureList:
			if j in lib[i][0]:
				marker=1
				break
		if marker==1:
			continue

		if 'NN' in lib[i][1]:
			res+=lib[i][0] 
			if i+1<len(lib) and ('NN' not in lib[i+1][1]and lib[i+1][1] not in PunctuationList):
				break
			else:
				res+=' '
	if len(res.split())==0:
		res+=GetLatterWord(line,getMeasurement(line)[1])


	return ' '.join(i for i in res.split())

def getQuantity(line):
	temp=getMeasurement(line)
	if temp!='NoItem':
		index=temp[0]
		return line.split()[index-1].replace('(','')
			
	else:
		return line.split()[0]

	return 'NoItem'



def getMeasurement(line):
	for i in range(0,len(line.split()[0:5])):
		for j in measureList:
			if j in line.split()[i]:
				return (i,j)
	return 'NoItem'





def FormIngredientDic(line):
	dic={}
	dic['name']=getName(line)
	dic['quantity']=getQuantity(line)
	temp=getMeasurement(line)
	if temp=='NoItem':
		dic['measurement']='NoItem'
	else:
		dic['measurement']=temp[1]
	print(dic)
	return dic




def FormIngredientList(filepath):
	res=[]
	with open(filepath) as f:
		for line in f.readlines():
			if(line==('Ingredients:'+'\n')):
				continue
			if line==('Directions:'+'\n'):
				break
			if len(line.split())!=0:
				res.append(FormIngredientDic(line))
	print(res)
	return res

def FormIngredientList1(text):
	res=[]

	for line in text:
		if(line==('Ingredients:'+'\n')):
			continue
		if line==('Directions:'+'\n'):
			break
		if len(line.split())!=0:
			res.append(FormIngredientDic(line))
	return res

FormIngredientList('data/white-cheese-chicken-lasagna.txt')





