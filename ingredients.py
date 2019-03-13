
from helpers import *
import nltk
import numpy as np
import pandas as pd
s="!#$%&()*+,-.:;<=>?@[\]^_`{'~}"
s+='"'
measureList=[
'teaspoon','tablespoon','cup','pint','quart',
'gallon','pinch','dash','lb','pound','cube','head','clove','ounce','bunch',
'teaspoons','tablespoons','cups','pints','quarts',
'gallons','pinches','dashes','lbs','pounds','cubes','heads','cloves','ounces','bunches'
			]

#essentials=['beef','lamb','pork','chicken','fish','egg','tofu','tempeh','seitan','buttermilk']
masterdata = loadTransformTable("./dictionary/proteins.csv")
essentials = list(masterdata['protein'])

def get_essentials(line):
	for i in line.split():
		if i.lower() in essentials and len(i)>=3:
			return i
	return None



# def getName(line):

	# text = nltk.word_tokenize(line)
	# res=''
	# lib=nltk.pos_tag(text)

# 	for i in range(0,len(lib)):
# 		marker=0
# 		for j in measureList:
# 			if j in lib[i][0]:
# 				marker=1
# 				break
# 		if marker==1:
# 			continue

# 		if 'NN' in lib[i][1]:
# 			res+=lib[i][0] 
# 			if i+1<len(lib) and ('NN' not in lib[i+1][1]and lib[i+1][1] not in PunctuationList):
# 				break
# 			else:
# 				res+=' '
# 	if len(res.split())==0:
# 		res+=GetLatterWord(line,getMeasurement(line)[1])


# 	return ' '.join(i for i in res.split())

def getName(line):
	text = line.split()
	res=''
	lib=nltk.pos_tag(text)
	temp=getMeasurement(line)
	if temp!='NoItem':
		index=temp[0]+1
		end=temp[0]+1
		for i in range(temp[0]+1,len(line.split())):
			if ',' in line.split()[i]:
				end=i
				res=' '.join(i for i in line.split()[index:end+1])
			if lib[i][1] in ['TO','IN']:
				end=i
				res= ' '.join(i for i in line.split()[index:end])
				break

		if res:
			return RemovePunctuation(res.strip())
		else:
			res=' '.join(i for i in line.split()[index:])
			return RemovePunctuation(res.strip())
	else:
		if getQuantity(line)=='NoItem':
			index=0
			end=0
		elif len(getQuantity(line).split())<2:
			index=1
			end=1
		else:
			index=2
			end=2
		for i in range(index,len(line.split())):
			if ',' in line.split()[i]:
				end=i
				res=' '.join(i for i in line.split()[index:end+1])
			if lib[i][1] in ['TO','IN']:
				end=i
				res=' '.join(i for i in line.split()[index:end])
				break
		res=' '.join(i for i in line.split()[index:])
		return RemovePunctuation(res.strip())

	return None

def getPreparation(line):
	if ',' in line:
		index=line.index(',')

		return line[index+2:].replace('\n','')
	else:
		text = nltk.word_tokenize(line)
		res=''
		lib=nltk.pos_tag(text)
		for i in lib:
			if i[1]=='VBD':
				res+=i[0]
				res+=' '


		if res=='':
			return 'NoItem'
		return res.replace('\n','')







def getQuantity(line):
	temp=getMeasurement(line)
	if temp!='NoItem':
		index=temp[0]
		for i in range(0,len(line.split())):
			if '(' in line.split()[i]:
				res=' '.join(line.split()[i:index])
				return res.replace('(','')	
		if index>=2 and '(' not in line.split()[index-1]:
			for i in '1234567890':
				if i in line.split()[1]:
					return ' '.join(line.split()[0:index])



		return line.split()[0].replace('(','')
			
	else:
		for i in '123456789':
			if '(' in line.split()[1]:
				break 
			if i in line.split()[1]:
				return 	' '.join(line.split()[0:2])
		for i in '123456789':
			if i in line.split()[0]:
				return line.split()[0]
		return 'NoItem'


def convertStrToFloat(str1):
	try:
		res=float(str1)
		return res

	except:
		if len(str1.split())==1:
			l=str1.split('/')
			return float(l[0])/float(l[1])
		else:
			res=0
			l=str1.split()
			res+=float(l[0])
			l1=l[1].split('/')
			res+=float(l1[0])/float(l1[1])
			return res



def getMeasurement(line):
	for i in range(0,len(line.split()[0:5])):
		for j in measureList:
			if j ==RemovePunctuation(line.split()[i].strip()):
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
	dic['Preparation']=getPreparation(line)
	dic['essential']=get_essentials(line)


	return dic







def FormIngredientList1(text):
	res=[]

	for line in text:
		if line==('Directions:'+'\n'):
			return res
		if len(line.split())<=1 or ':'in line:
			continue
		if(line==('Ingredients:'+'\n')):
			continue

		if len(line.split())!=0:
			res.append(FormIngredientDic(line))
	return res







