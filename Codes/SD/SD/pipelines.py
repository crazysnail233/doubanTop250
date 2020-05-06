# -*- coding: utf-8 -*-
import csv


class SdPipeline(object):
    def __init__(self):
        columns = ['省级行政区域','市级行政区域','县级行政区域','镇级行政区域','村级行政区域']

        file_name= 'sdsp.csv'

        self.file = open(file_name,'a',newline='',encoding='utf-8')
        self.writer = csv.DictWriter(self.file,columns)

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self,spider):
        self.file.close()

