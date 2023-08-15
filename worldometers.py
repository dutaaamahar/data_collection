import scrapy


class WorldometersSpider(scrapy.Spider):
  name = "worldometers"
  allowed_domains = ["www.worldometers.info"]
  start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

  def parse(self, response):
    rows = response.xpath('//tr')

    for row in rows:
      countries = row.xpath('./td/a/text()').get()
      population = row.xpath('./td[3]/text()').get()
      yearly_change = row.xpath('./td[4]/text()').get()
      net_change = row.xpath('./td[5]/text()').get()
      density = row.xpath('./td[6]/text()').get()
      land_area = row.xpath('./td[7]/text()').get()
      migrants = row.xpath('./td[8]/text()').get()
      fert_rate = row.xpath('./td[9]/text()').get()
      med_age = row.xpath('./td[10]/text()').get()
      urban_pop = row.xpath('./td[11]/text()').get()
      world_share = row.xpath('./td[12]/text()').get()

      yield {
        'countries': countries,
        'population': population,
        'yearly_change': yearly_change,
        'net_change': net_change,
        'density': density,
        'land_area': land_area,
        'migrants': migrants,
        'fert_rate': fert_rate,
        'med_age': med_age,
        'urban_pop': urban_pop,
        'world_share': world_share,
      }

