# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    #
    job_name = scrapy.Field()
    #
    company_name = scrapy.Field()
    #
    providesalary_text = scrapy.Field()
    #
    workarea_text = scrapy.Field()
    #
    companytype_text = scrapy.Field()
    #
    jobwelf = scrapy.Field()
    #
    attribute_text = scrapy.Field()
    #
    companysize_text = scrapy.Field()
    #
    companyind_text = scrapy.Field()
    #
    job_word = scrapy.Field()
