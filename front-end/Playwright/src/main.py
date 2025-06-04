import os
import time

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
driver = browser.new_page()
load_dotenv()

def initial_page():

    driver.goto("https://pt.anotepad.com/")

    TITLE_BROWSER = os.getenv("TITULO")
    TEXT_BROWSER = os.getenv("TEXTO")

    
    insert_header = driver.locator('//*[@id="edit_title"]')
    insert_header.click()
    insert_header.fill(TITLE_BROWSER)
    time.sleep(2)

    insert_text = driver.locator('//*[@id="edit_textarea"]')
    insert_text.click()
    insert_text.fill(TEXT_BROWSER)
    time.sleep(2)

def ending_broser():

    driver.close()

def main():
    
    initial_page()
    ending_broser()

if __name__ == "__main__":
    main()