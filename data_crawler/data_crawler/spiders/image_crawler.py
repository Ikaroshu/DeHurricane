import scrapy as srp
from ..items import DataCrawlerItem

class TCSpider(srp.Spider):
    name = "TC_image"

    def start_requests(self):
        urls = ["https://www.nrlmry.navy.mil/tc-bin/tc_home2.cgi?ACTIVES=19-WPAC-22W.BUALOI,19-CPAC-93C.INVEST,19-IO-97A.INVEST,19-IO-98B.INVEST&PHOT=No&ATCF_BASIN=wp&AGE=Previous&SUB_PROD=1km&SIZE=Thumb&NAV=tc&YR=19&ATCF_YR=2019&YEAR=2019&ATCF_FILE=/SATPRODUCTS/kauai_data/www/atcf_web/public_html/image_archives/2019/wp222019.19102306.gif&CURRENT_ATCF_FILE=/SATPRODUCTS/kauai_data/www/atcf_web/public_html/image_archives/2019/wp222019.19102306.gif&DIR=/SATPRODUCTS/TC/tc19/WPAC/22W.BUALOI/ir/geo/1km&CURRENT_ATCF=wp222019.19102306.gif&ATCF_NAME=wp222019&ATCF_DIR=/SATPRODUCTS/kauai_data/www/atcf_web/public_html/image_archives/2019&ARCHIVE=active&MO=OCT&PROD=ir&BASIN=WPAC&AREA=pacific/southern_hemisphere&STORM_NAME=22W.BUALOI&TYPE=geo&STYLE=tables"]
        for url in urls:
            yield srp.Request(url=url, callback=self.parse)

    def parse(self, response):
        baseurl = "https://www.nrlmry.navy.mil"
        for url in response.xpath("/html/body/table[2]/tr/th[2]/table/tr[2]/td/center[2]/table/tr/th[1]/a/@href").getall():
            yield srp.Request(url=baseurl+url, callback=self.get_image)

    def get_image(self, response):
        baseurl = "https://www.nrlmry.navy.mil"
        item = DataCrawlerItem()
        item['image_urls'] = [baseurl+response.xpath("/html/body/table[2]//tr/th[2]/table/tr[2]/td/center/table/tr[4]/th/a/img/@src").extract_first()]
        return item
