# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class RecipePipeline(object):
	def substring(self,template):
		rule=r'title="(.*?)"'
		slotList=re.findall(rule,template)
		return slotList

	def process_item(self, item, spider):
		with open("recipe.txt",'a')as fp:
			fp.write(str(item['name'])+'\n')
			# initial=str(item['name'])
			# res=self.substring(initial)
			# for i in res:
			# 	fp.write(i+ '\n')
			return item
