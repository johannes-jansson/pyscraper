from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.blocket.se/hela_sverige?q=magic%20trackpad&st=s&l=0&ca=11&sp=1&w=3')

price = driver.find_elements_by_xpath('//p[@class="list_price font-large"]')
for i in range(len(price)):
    print(price[i].text)

driver.close()
