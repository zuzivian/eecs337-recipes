import sys
def RemovePunctuation(line):
    s = "[]'"
    for x in s:
        line = line.replace(x, '')
        line=line.replace(r'\n','')
    return line


def txt_parser(filepath,recipe):
    with open(filepath, 'r') as f:
        sum=0
        with open(recipe+".txt",'w')as fp:
            fp.write('Ingredients:'+'\n')
            for i in f.readlines():
                i=RemovePunctuation(i)
                i=i.replace(r'\n','')
                if 'Add all ingredients'in i:
                    fp.write('\n')
                    fp.write('Directions:'+'\n')
                else:
                    fp.write(i)

