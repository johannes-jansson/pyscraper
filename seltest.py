from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.fabpedigree.com/james/mathmen.htm')

mathematicians = driver.find_elements_by_xpath('//li')
for i in range(len(mathematicians)):
    print(mathematicians[i].text)

driver.close()
