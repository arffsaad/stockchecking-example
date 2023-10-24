from playwright.sync_api import sync_playwright
from time import sleep
import requests
from os import system

def main() -> None:
    with sync_playwright() as p:

        # INSERT BOT TOKEN HERE
        botToken = ""
        userId = ""

        count = 0
        checks = 0
        stocked = 0
        refresh = 0
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        while True:
            count = count + 1
            refresh = refresh + 1
            page.goto('https://www.machines.com.my/collections/apple-watch/products/apple-watch-series-8?variant=40979513147503')
            sleep(4)
            page.click('xpath=//*[@id="AddToCartForm-7060617560175"]/div[1]/div[1]/ul/li[2]/span')
            page.click('xpath=//*[@id="AddToCartForm-7060617560175"]/div[1]/div[2]/ul/li[1]/span')
            page.click('xpath=//*[@id="AddToCartForm-7060617560175"]/div[1]/div[3]/ul/li[2]/div')
            sleep(1)
            while count % 10 != 0:
                sleep(2)
                page.click('xpath=//*[@id="AddToCartForm-7060617560175"]/div[1]/div[3]/ul/li[3]/div')
                sleep(1)
                page.click('xpath=//*[@id="AddToCartForm-7060617560175"]/div[1]/div[3]/ul/li[2]/div')
                try:
                    sleep(1)
                    text = page.inner_text('xpath=/html/body/div[1]/div/main/div[1]/div/div/div/div[1]/div[2]/div/form/button[3]')
                    
                    if text == "ADD TO CART":
                        stocked = stocked + 1
                        url = f"https://api.telegram.org/bot" + botToken + "/sendMessage"
                        data = {"chat_id": userId, "text": "Stock is available! (Source: BOT) https://www.machines.com.my/collections/apple-watch/products/apple-watch-series-8?variant=40979513147503"}
                        requests.post(url, data=data)
                    else:
                        continue
                except:
                    continue
                count = count + 1
                checks = checks + 1
                system('cls')
                print("Status\nChecks done: " + str(checks) + "\nRefreshes: " + str(refresh) +  "\nStocked: " + str(stocked) +  "\nNo stock: " + str(checks - stocked) +"\n\n")

if __name__ == '__main__':
    main()
