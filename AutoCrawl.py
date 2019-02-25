from txtParser import *
import os

def AutoCrawl(url):
	command="scrapy crawl Recipe -a url="+url
	os.system(command)
	if os.path.exists('recipe.txt'):
		txt_parser('recipe.txt',"data/"+url.split('/')[-2])
		print('Successfully Loading.....')
		os.remove('recipe.txt')
		with open("data/"+url.split('/')[-2]+".txt",'r')as fp:
			return fp.readlines()
	else:
		print('no recipe.txt existed....')
		return None


# AutoCrawl("https://www.allrecipes.com/recipe/270307/moroccan-chicken-thighs/")
# AutoCrawl("https://www.allrecipes.com/recipe/246628/spaghetti-cacio-e-pepe/")
# AutoCrawl("https://www.allrecipes.com/recipe/255633/cheesy-cauliflower-pizza-crust/")