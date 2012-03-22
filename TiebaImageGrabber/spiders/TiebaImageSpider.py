from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.utils.url import urljoin_rfc, url_query_cleaner 

from scrapy.item import Item
from TiebaImageGrabber.items import ImageItem

#url = urljoin_rfc(response.url, url)

class ImageSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ["tieba.baidu.com"]
    # start_urls = ['http://tieba.baidu.com/p/1403955308']
    start_urls = ['http://tieba.baidu.com/gift/f/dir?id=4']

    #start_urls = ['http://tieba.baidu.com/gift/f/dir?id=4', 
    #              'http://tieba.baidu.com/gift/f/dir?id=3']

#Forum- http://tieba.baidu.com/f?kw=XXX   
#Post - http://tieba.baidu.com/p/1403955308

    rules = (
        Rule(SgmlLinkExtractor(allow='tieba.baidu.com/gift/f/dir[?]id=[0-9]+$')),
        Rule(SgmlLinkExtractor(allow='tieba.baidu.com/f[?]kw[a-zA-Z0-9.:\/=_?&-]+$')),
        Rule(SgmlLinkExtractor(allow='tieba.baidu.com/p/[0-9]+$'),
            callback='parse_post')

      )

    
    def parse_post(self, response):
        image_urls = []
        hxs = HtmlXPathSelector(response)
          
        # scrap each row in the table
        posts = hxs.select('//div[@class="l_post"]')

        for post in posts:
            # only one image at most in fact 
            images = post.select('.//div[@class="p_content"]/img/@src')
            for image in images:               
                url = image.extract() 
                url = urljoin_rfc(response.url, url)
                url = url_query_cleaner(url, [])
                print 'url is %s' % url
                image_urls.append(url)
            # End of For
        #End of For
        item = ImageItem()
        item['image_urls'] = image_urls
        yield item



