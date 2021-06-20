# - *- coding: utf- 8 - *-
import telebot
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

TOKEN = 'YOUR_TOKEN'

bot = telebot.TeleBot(TOKEN)

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('http://www.gatchina.biz/generator')

search_input = driver.find_elements_by_css_selector('input')[0]
search_input.send_keys('Вахрамян')
login_form = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/a")
login_form.click();
sub_menus_html = driver.find_element_by_css_selector('div#text')
res = sub_menus_html.text
result = res[:res.find("А вот «Нямархав»")]
driver.close()
bot.send_message('@vakhramyanko', result)
sys.exit()
