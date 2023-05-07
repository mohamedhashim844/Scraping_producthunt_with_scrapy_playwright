# Scrapy settings for producthunt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scraper_helper as sh

BOT_NAME = "producthunt"

SPIDER_MODULES = ["producthunt.spiders"]
NEWSPIDER_MODULE = "producthunt.spiders"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DEFAULT_REQUEST_HEADERS = sh.get_dict (
    '''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,ar;q=0.8
cache-control: max-age=0
cookie: first_visit=1677008715; first_referer=; visitor_id=f3ad29e9-5a58-4e03-bfde-018bdd1b3ec4; track_code=e10117e2e9; _delighted_web={%2271AaKmxD4TpPsjYW%22:{%22_delighted_fst%22:{%22t%22:%221677008715992%22}}}; ajs_anonymous_id=ef788039-1fde-440e-95cf-3d9fe3ab7792; intercom-id-fe4ce68d4a8352909f553b276994db414d33a55c=ffcffa7e-9194-4065-b00b-dab074c00c98; intercom-session-fe4ce68d4a8352909f553b276994db414d33a55c=; intercom-device-id-fe4ce68d4a8352909f553b276994db414d33a55c=7e6e4a31-96cb-4181-9602-3231d9646853; _ga=GA1.1.78326386.1677008720; _ga_WZ46833KH9=GS1.1.1677498464.1.1.1677499003.0.0.0; g_state={"i_p":1677585409724,"i_l":2}; csrf_token=JVAF1v8RnV7CUZXXnZEmMQ2g3VYu8jDBBaDDW02shH2NgoD7lql2AbSuPNbL1VSY579fW1QlEV4b63YvPfLsgw; _producthunt_session_production=1zYKrX6TVJgpU0KLLcvsiu1IwoOfGYGDRmlgxSdoRQR%2BRXjFhc6Fw%2Bhl%2Bo28EGsyyuc0oDEa1XX07U6DIH1r1OpByp6r%2B4KCRaevcEL6%2F71Ui%2F1V5fjuSf6fauMEJ6jRBe7SL6AC%2BAX4of%2FRAQb%2F1f%2FLuFW1fOoX%2FismRe9Ag4XrzOB7IXd1kX8WG7CDwt8at%2FGvsG2VF1njrw0041ubq2UzlplvNSRjyU96Jb9FFfi%2BQ%2F5rQE1Me6xYrkIEIkrymW2GwXdaco%2BpKR6tXMsTiUTXC685wI35uIwtherDJgcO5kxTooDFz%2Bkd4ZO1U8obLXnQbOzBExvZYQuDz6gVmFCbbvoWW13Q6RbSH1rSs31lu178CmCnCAR8KrCXrXyZ14hEMzuQOh7DBmKuOFgA%2FoXrpq2zGaobBAnpRdB30bp%2B--WbMnShxHoK9%2FSIp8--f4mSHBEYhJmxcVMlo80xxQ%3D%3D
sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36
    '''
)


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "producthunt (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "producthunt.middlewares.ProducthuntSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "producthunt.middlewares.ProducthuntDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "producthunt.pipelines.ProducthuntPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
