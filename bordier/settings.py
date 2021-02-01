BOT_NAME = 'bordier'
SPIDER_MODULES = ['bordier.spiders']
NEWSPIDER_MODULE = 'bordier.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'bordier.pipelines.DatabasePipeline': 300,
}
