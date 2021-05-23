import scrapy 

class LotterySpider(scrapy.Spider):

    name = "LotterySpider"
    start_urls = [
        'https://www.lotteryusa.com/new-york/win-4/year'
    ]

    def parse(self, response):

        item = {}
        lotteries = response.css(".c-game-table__item")

        for lottery in lotteries:
            date = lottery.css("time.c-game-table__game-date").xpath("@datetime").get()

            lotteryNumber = ''

            numbers = lottery.css(".c-result__ball")
            for number in numbers:
                lotteryNumber+=(number.css(".c-result__ball::text").get())

            winAmount = lottery.css(".c-meta-list__value::text").get()

            winAmount = str(winAmount).replace(" ", "")
            winAmount = winAmount.replace("\n", "")

            if lotteryNumber is not "":
                item['date']         = date
                item['lottey-number'] = lotteryNumber
                item['win-amount']    = winAmount
                yield item


            