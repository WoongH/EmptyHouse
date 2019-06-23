BOT_NAME = 'booksbot'

LOG_LEVEL='ERROR'
#
SPIDER_MODULES = ['booksbot.spiders']
NEWSPIDER_MODULE = 'booksbot.spiders'

ROBOTSTXT_OBEY = True

# 기사 내용 크롤링시 MongoDBPipeline 설정
ITEM_PIPELINES = {'booksbot.pipelines.MongoDBPipeline': 300,}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "books_crawl"
MONGODB_COLLECTION = "books"
