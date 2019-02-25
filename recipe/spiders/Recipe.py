# -*- coding: utf-8 -*-
import scrapy
from recipe import items


class RecipeItem(scrapy.Item):
	# define the fields for your item here like:
	name = scrapy.Field()


class RecipeSpider(scrapy.Spider):

	name = 'Recipe'
	allowed_domains = ['allrecipes.com']
	#start_urls = ['https://www.allrecipes.com/recipe/270307/moroccan-chicken-thighs/']
	start_urls=[]
	def __init__(self,url=None,*args,**kwargs):
		super(RecipeSpider,self).__init__(*args,**kwargs)
		self.start_urls=[url]


	def parse(self, response):
		sum=1
		ingredients=response.xpath('//*[@id="lst_ingredients_1"]/li')
		for ingredient in ingredients:
			item=RecipeItem()
			# item['name']=ingredient.xpath('//*[@id="lst_ingredients_1"]/li'+'[3]/label/span/text()').extract()
			# item['name'] = ingredient.xpath('//*[@id="lst_ingredients_1"]/li' + '[4]/label/span/text()').extract()
			item['name']=ingredient.xpath('//*[@id="lst_ingredients_1"]/li['+str(sum)+']/label/span/text()').extract()
			sum+=1
			yield item
		ingredients2=response.xpath('//*[@id="lst_ingredients_2"]/li')
		sum=1
		for ingredient in ingredients2:
			item=RecipeItem()
			# item['name']=ingredient.xpath('//*[@id="lst_ingredients_1"]/li'+'[3]/label/span/text()').extract()
			# item['name'] = ingredient.xpath('//*[@id="lst_ingredients_1"]/li' + '[4]/label/span/text()').extract()
			item['name']=ingredient.xpath('//*[@id="lst_ingredients_2"]/li['+str(sum)+']/label/span/text()').extract()
			sum+=1
			yield item

		directions=response.xpath('//*[@id="main-content"]/div[3]/section/section[2]/div/div[1]/ol/li')
		sum=1
		for direction in directions:
			item=RecipeItem()
			item['name']=direction.xpath('//*[@id="main-content"]/div[3]/section/section[2]/div/div[1]/ol/li['+str(sum)+']/span/text()').extract()
			sum+=1
			yield item
