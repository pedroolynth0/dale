from selenium import webdriver
import time
from discord_webhooks import DiscordWebhooks



class SnkrsBot:

    def __init__(self, sneaker_url):
        self.sneaker_url =  sneaker_url
        self.driver = webdriver.Chrome('./chromedriver.exe')
    
    def get_price(self):
        self.driver.get(self.sneaker_url)
        price = self.driver.find_element_by_class_name('tem-estoque')
        return (price.get_attribute('innerHTML').strip(''))
    
def main():
    WEBHOOK_URL ='https://discord.com/api/webhooks/729041837922451517/ayzmz_BvfiL6xT9cFgM5aGKgk5GmSX1s40g8hZjsCK2weym23sQGaTBPErjLQmBVmMC8'

    webhook = DiscordWebhooks(WEBHOOK_URL)

    webhook.set_content(content='https://www.nike.com.br/Snkrs/Produto/Nike-x-Cactus-Jack-Air-Max-270-Infantil-26-33/67-80-445-209011')
    url = 'https://www.nike.com.br/Snkrs/Produto/Nike-x-Cactus-Jack-Air-Max-270-Infantil-26-33/67-80-445-209011'
    bot = SnkrsBot(url)

    last_price = None
    while 1:
        price = bot.get_price()
        if last_price:
            if price != last_price:
                webhook.send()
            else:
                print(f"PRODUTO: {price}")
        last_price = price
        time.sleep(3)

if __name__ == "__main__":
    main()



  


