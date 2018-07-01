from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://zealpc.net/collections/switches/products/zilents')

price = driver.find_elements_by_xpath('//*[@id="price-preview"]')
for i in range(len(price)):
    print(price[i].text)

driver.close()
