from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import re
from time import sleep

# Set options
o = Options()
o.add_argument("--headless")

# Initialize Driver
driver = webdriver.Chrome(options=o)

def get_player_data(code):
    url = "https://slippi.gg/user/" + code
    driver.get(url)

    # jss7  - Username, Code, Rank, ELO
    # jss8  - Region, Support Tier
    # jss18 - Wins, Losses, Total Sets
    data1 = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME,"jss7"))
    data2 = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME,"jss8"))
    data3 = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME,"jss18"))

    return (data1.text, data2.text, data3.text)

def parse_data(d1, d2, d3):
    tag = d1[0]
    code = d1[1]
    rank = d1[2]
    elo = float(d1[3].split()[0])

    region = d2[1]

    wins = int(d3[4])
    losses = int(d3[6])
    total_sets = int(d3[8])

    print(wins, losses, total_sets, elo)


if __name__ == "__main__":
    (data1, data2, data3) = get_player_data("pete-235")
    parse_data(data1.splitlines(), data2.splitlines(), data3.splitlines())
    driver.quit()
    