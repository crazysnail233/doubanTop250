# -*- coding: utf-8 -*-
import scrapy


class SdSpSpider(scrapy.Spider):
    name = 'sd_sp'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html']

    # 省级行政区域
    def parse(self, response):
        selectors = response.xpath("//tr[@class='provincetr']//a")
        for selector in selectors:
            suffix_url = selector.xpath("@href").get()
            # 市级行政区域url
            city_url = response.urljoin(suffix_url)
            # 省级行政区域名称
            province_name = selector.xpath("text()").get()

            yield scrapy.Request(url=city_url,callback=self.parse_city,
                 meta={'province_name':province_name})

    def parse_city(self,response):
        province_name = response.meta.get('province_name',None)

        selectors = response.xpath("//tr[@class='citytr']/td[2]/a")
        for selector in selectors:
            suffix_url = selector.xpath("@href").get()
            # 县级行政区区域的url
            county_url = response.urljoin(suffix_url)
            # 市级行政区域名称
            city_name = selector.xpath("text()").get()

            yield scrapy.Request(url=county_url,callback=self.parse_county,
meta={
                'province_name':province_name,
                'city_name':city_name
           })

    # 县级行政区域
    def parse_county(self,response):
        province_name = response.meta.get('province_name',None)
        city_name = response.meta.get('city_name',None)

        selectors = response.xpath("//tr[@class='countytr']/td[2]/a")
        for selector in selectors:
            suffix_url = selector.xpath("@href").get()
            # 镇级行政区域url
            town_url = response.urljoin(suffix_url)

            # 县级行政区域名称
            county_name = selector.xpath("text()").get()

            yield scrapy.Request(url=town,callback=self.parse_town,
meta={

                'province_name':province_name,
                'city_name':city_name,
                'county_name':county_name
            })

    # 镇级行政区域
    def parse_town(self,response):
        province_name = response.meta.get('province_name', None)
        city_name = response.meta.get('city_name', None)
        county_name = response.meta.get('country_name',None)

        selectors = response.xpath("//tr[@class='towntr']/td[2]/a")
        for selector in selectors:
            suffix_url = response.xpath("@href").get()
            # 村级行政区域url
            village_url = response.urljoin(suffix_url)

            # 镇级行政区域名称
            town_name = selector.xpath("text()").get()

            yield scrapy.Request(url=village_url,callback=self.parse_town,
meta={
                'province_name': province_name,
                'city_name': city_name,
                'county_name': county_name,
                'town_name':town_name
            })

    # 村级行政区域
    def parse_village(self,response):
        province_name = response.meta.get('province_name', None)
        city_name = response.meta.get('city_name', None)
        county_name = response.meta.get('country_name', None)
        town_name = response.meta.get('town_name',None)

        village_name_list = response.xpath("//tr[@class='villagetr']//td[3]/text()").getall()
        for village_name in village_name_list:
            item = {
                '省级行政区域': province_name,
                '市级行政区域': city_name,
                '县级行政区域': county_name,
                '镇级行政区域': town_name,
                '村级行政区域': village_name
            }
            yield item



