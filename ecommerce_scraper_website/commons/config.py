class Config:
    configs = {
        "amazon": "http://www.amazon.com/",
        "ebay": "https://www.ebay.com/sch/i.html?_from=R40&_nkw={0}",
        "walmart": "http://www.walmart.com/"
    }

    headers = {
        "amazon": {
            'Host': 'www.amazon.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; \
                            SM-A520F Build/NRD90M; wv) AppleWebKit/537.36 \
                            (KHTML, like Gecko) Version/4.0 \
                            Chrome/65.0.3325.109 Mobile Safari/537.36',
                                        'Accept': 'text/html,application/xhtml+xml,\
                                                            application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        },
        "walmart": {
            'Host': 'www.walmart.ca',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
    }
