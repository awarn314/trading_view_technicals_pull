# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:11:51 2019

@author: Alex
"""

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#import pandas as pd
from urllib.request import urlopen

def technicals(se,ticker,p):
    url = 'https://www.tradingview.com/symbols/%s-%s/technicals'%(se,ticker)
    driver = webdriver.Firefox(executable_path=r'C:\Users\Alex\Anaconda3\geckodriver.exe')
    driver.get(url)
    str_period="//*[contains(text(), '"+p+"')]"
    button_element = driver.find_elements_by_xpath(str_period)[0]
    button_element.click()
    sell=[]
    for value in driver.find_elements_by_xpath("//span[@class='counterNumber-3l14ys0C- redColor-Hpg7doOR-']"):
        sell.append(value.text)
    neutral=[]
    for value in driver.find_elements_by_xpath("//span[@class='counterNumber-3l14ys0C- neutralColor-15OoMFX9-']"):
        neutral.append(value.text)
    buy=[]
    for value in driver.find_elements_by_xpath("//span[@class='counterNumber-3l14ys0C- brandColor-1WP1oBmS-']"):
        buy.append(value.text)
    driver.close()
    return sell, neutral, buy

tick='AMD'
stock_exchange='NASDAQ'
period='1 month' #1 minute, 5 minutes, 15 minutes,1 hour, 4 hours, 1 day, 1 week, 1 month

sell,neutral,buy=technicals(stock_exchange,tick,period) #returns values in order of [oscillators, summary, moving average] for sell, buy, neutral