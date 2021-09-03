# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Safari()  # open safari

url = 'https://t.me/NewlearnerChannel'
dr.get(url)

while True:
    try:
        subscriber_line = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]').text
        break
    except:
        pass
subscriber_count = ""
for letter in subscriber_line:
    try:
        int(letter)
        subscriber_count += letter
    except:
        pass
write_in = "{%s, %s}\n"% (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), subscriber_count)
print(write_in)
log = open('./telegramSubscriberCountLog', 'a+')
log.write(write_in)
log.close()
dr.quit()
