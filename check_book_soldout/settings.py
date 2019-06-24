BOT_NAME = 'check_book_soldout'

LOG_LEVEL='ERROR'
#
SPIDER_MODULES = ['check_book_soldout.spiders']
NEWSPIDER_MODULE = 'check_book_soldout.spiders'

ROBOTSTXT_OBEY = True

# 기사 내용 크롤링시 MongoDBPipeline 설정
ITEM_PIPELINES = {'check_book_soldout.pipelines.SimplePipeline': 300,}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "books_crawl"
MONGODB_COLLECTION = "books"
