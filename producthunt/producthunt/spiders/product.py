#import selectors
import scrapy
from scrapy_playwright.page import PageMethod
from scrapy import Request, Selector
from scrapy.utils.response import open_in_browser
from producthunt.items import ProducthuntItem
from scrapy.loader import ItemLoader



class ProductSpider(scrapy.Spider):
    name = "product"
    #allowed_domains = ['producthunt.com']
    def start_requests(self):
        url = "https://www.producthunt.com/"
        yield scrapy.Request(url,
        meta=dict(
            playwright= True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector','[data-test="homepage-section-0"]'),
                PageMethod('evaluate' , 'window.scrollBy(0,document.body.scrollHeight)'),
            ],
            
        ))
    async def parse(self, response):
        page = response.meta["playwright_page"]
        for i in range(1,30): 
            await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')
            await page.wait_for_selector(f'[data-test="homepage-section-{i}"]')
        html = await page.content()
        await page.close()
        s = Selector(text = html)
        #open_in_browser(response)
        #page.goto("https://www.producthunt.com/", timeout = 0)
        for links in s.css('a.styles_title__jWi91::attr(href)'):
            url = links.get()
            yield Request(response.urljoin(url),
                        meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector','div.flex.direction-column.flex-1')
                ]
                        ) , callback=self.parse_item)
        errback=self.errback,

    async def parse_item(self, response):
        page = response.meta["playwright_page"]
        await page.close()
        l = ItemLoader(item=ProducthuntItem() , selector=response )

        l.add_css('name' , '.styles_title__vct6Q')
        l.add_css('free' , '[data-test="pricing-type"]')
        l.add_css('genre' , 'a.hover-blue.color-lighter-grey.fontSize-16.fontWeight-400.noOfLines-undefined')

        yield l.load_item()
        
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()