from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.economist.com/latest-updates')

price = driver.find_elements_by_xpath('//span[@class="flytitle-and-title__title"]')
for i in range(len(price)):
    print(price[i].text)

driver.close()
