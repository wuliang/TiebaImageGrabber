# Scrapy settings for ImageGrabber project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME    = 'TiebaImageGrabber'
BOT_VERSION = '0.1'

# Random interval between 0.5 and 1.5 * DOWNLOAD_DELAY
DOWNLOAD_DELAY     = 0.25 

SPIDER_MODULES     = ['TiebaImageGrabber.spiders']
NEWSPIDER_MODULE   = 'TiebaImageGrabber.spiders'
DEFAULT_ITEM_CLASS = 'TiebaImageGrabber.items.ImageItem'

USER_AGENT   = "Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.19) Gecko/20110430 Iceweasel/3.5.19 (like Firefox/3.5.19)"
ITEM_PIPELINES = ['TiebaImageGrabber.pipelines.TiebaFileDownload']
STORE_DIR = '/mnt/fat2/webcrawler/mine/TiebaImageGrabber/TiebaImageStore'


DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-cn,zh;q=0.5',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Charset' :'GBK,utf-8;q=0.7,*;q=0.7',
#    'Keep-Alive': 300,
    'Connection': 'keep-alive'
}
