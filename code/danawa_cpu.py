# pip install selenium
# pip install webdriver-manager
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
def main():
    ws.append(['제품명','순위','가격'])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.danawa.com/")
    search_tag = driver.find_element(By.CLASS_NAME,"search__input")
    search_tag.send_keys("CPU")
    search_tag.send_keys(Keys.ENTER)

    count = 1
    PageNo = 2
    for i in range(count,PageNo):
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_layer")
        for item in itemList:
            if item.get_attribute("id") != "":
                name = item.find_element(By.CLASS_NAME, "prod_name").text
                priceList = item.find_element(By.CLASS_NAME,"prod_pricelist ")
                for price in priceList.find_elements(By.TAG_NAME,"li"):
                    price_result = price.find_element(By.CLASS_NAME,"price_sect")\
                        .find_element(By.TAG_NAME,"a").text
                    ranking = price.find_element(By.CLASS_NAME,"over_preview").text
                    print(name,"/",ranking,price_result)
                    ws.append([name,ranking,price_result])
    wb.save("cpu.xlsx")




if __name__ == '__main__':
    main()