from txtParser import *
import os


def AutoCrawl(url):

	if os.path.exists('recipe.txt'):
		os.remove('recipe.txt')
	command="scrapy crawl Recipe -a url="+url
	os.system(command)
	txt_parser('recipe.txt',"data/new")
	with open("data/new"+".txt",'r')as fp:
		return fp.readlines()
	print('crawling error, things wrong with the url')
	return None



#AutoCrawl("https://www.allrecipes.com/recipe/229931/marinated-mushrooms/")
# AutoCrawl("https://www.allrecipes.com/recipe/246628/spaghetti-cacio-e-pepe/")
# AutoCrawl("https://www.allrecipes.com/recipe/255633/cheesy-cauliflower-pizza-crust/")
