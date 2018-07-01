from selenium import webdriver

with open('results.csv', 'w') as f:
    f.write("Company; Change; Price \n")

driver = webdriver.Chrome()
driver.get('https://www.di.se/')

winner = driver.find_elements_by_xpath('//a[@class="di_winner-loser__name"]')
value = driver.find_elements_by_xpath('//div[@class="di_winner-loser__value"]')
last_price = driver.find_elements_by_xpath('//div[@class="di_winner-loser__last-price"]')

for i in range(len(winner)):
    if len(winner[i].text) > 0:
        print(winner[i].text + ' changed ' +
              value[i].text + ', the price is now ' +
              last_price[i].text + ' sek.')
        with open('results.csv', 'a') as f:
            f.write(winner[i].text + '; ' +
              value[i].text + '; ' +
              last_price[i].text + ' \n')

print('Results exported to results.csv')
driver.close()
