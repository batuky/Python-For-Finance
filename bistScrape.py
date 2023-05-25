from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import json


def setup_webdriver():
    # Setup webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

stock_data = {}

def scrape_BIST_data_page1(driver):
    driver.get("https://www.bloomberght.com/borsa/hisseler")
    time.sleep(15)  # wait for page to load
   
    rows = driver.find_elements(By.XPATH, '/html/body/div[3]/section/div/div/div[1]/div[4]/div/div/table[2]/tbody/tr')
    for row in rows[1:]:
        columns = row.find_elements(By.TAG_NAME, 'td')
        stock_name = columns[0].text.strip()
        stock_value = columns[1].text.strip()
        stock_data[stock_name] = stock_value

    print(f"Page 1 scraped successfully.")
    print(json.dumps(stock_data, indent=4, ensure_ascii=False))


def scrape_BIST_data(driver):
    for i in range(2,33):
        driver.get(f"https://www.bloomberght.com/borsa/hisseler/{i}")
        time.sleep(15)  # wait for page to load because of advertisement
        rows = driver.find_elements(By.XPATH, '/html/body/div[3]/section/div/div/div[1]/div[4]/div/div/table[2]/tbody/tr')
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            stock_name = columns[0].text.strip()
            stock_value = columns[2].text.strip()
            stock_data[stock_name] = stock_value

        print(f"Page {i} scraped successfully.")
        print(json.dumps(stock_data, indent=4, ensure_ascii=False))


# Run every 10 mins
while True:
    
    start_time = time.time() #start timer before the script
    driver = setup_webdriver()
    scrape_BIST_data_page1(driver)
    scrape_BIST_data(driver)
    driver.quit()  # Close the driver after finishing
    end_time = time.time()#end timer after the script
    execution_time = end_time - start_time
    print("Scriptin çalışma süresi: {} saniye".format(execution_time))
    time.sleep(120)  # Sleep before starting a new iteration
