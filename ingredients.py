
from helpers import *
import nltk

s="!#$%&()*+,-.:;<=>?@[\]^_`{'~}"
s+='"'
measureList=[
'teaspoon','tablespoon','cup','pint','quart',
'gallon','pinch','dash','lb','pound','cube','head','clove','ounce','bunch'
			]

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
				break
			if lib[i][1] in ['TO','IN']:
				end=i
				res= ' '.join(i for i in line.split()[index:end])
				break

		if res:
			return res
		else:
			return ' '.join(i for i in line.split()[index:])
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
				return ' '.join(i for i in line.split()[index:end+1])
			if lib[i][1] in ['TO','IN']:
				end=i
				return ' '.join(i for i in line.split()[index:end])
		return ' '.join(i for i in line.split()[index:])

	return None
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



def getMeasurement(line):
	for i in range(0,len(line.split()[0:5])):
		for j in measureList:
			if j in line.split()[i]:
				return (i,j)
	return 'NoItem'

print(getQuantity('1 (10 3/4 ounces) MEAT'))



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
			if 'Directions:'in line:
				return res
			if len(line.split())<=1:
				continue
			if(line==('Ingredients:'+'\n')):
				continue

			if len(line.split())!=0:
				res.append(FormIngredientDic(line))
	print(res)
	return res

def FormIngredientList1(text):
	res=[]

	for line in text:
		if line==('Directions:'+'\n'):
			return res
		if len(line.split())<=1:
			continue
		if(line==('Ingredients:'+'\n')):
			continue

		if len(line.split())!=0:
			res.append(FormIngredientDic(line))
	return res

FormIngredientList('data/mardi-gras-king-cake.txt')




