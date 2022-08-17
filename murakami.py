import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from os import environ
import win32clipboard as wcb
import win32con as wc
import pyautogui
import random
import names
import requests
from json import load
import imaplib
import email

def murakami():
    init()
    password = create_password()
    executable_path = "/webdrivers"
    os.environ["webdriver.chrome.driver"] = executable_path
    options = Options()
    options.add_extension('anticaptcha.crx')
    options.add_extension('extension.crx')
    use_email = create_catchall_email()
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
        print("creating Metamask account...")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//*[@id='app-content']/div/div[3]/div/div/div/button")), ).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button')), ).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//*[@id='app-content']/div/div[3]/div/div/div/div[5]/div[1]/footer/button[2]")), ).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="create-password"]')), )
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="confirm-password"]')), )
        driver.find_element_by_xpath(
            '//*[@id="create-password"]').send_keys('')
        driver.find_element_by_xpath(
            "//*[@id='confirm-password']").send_keys('')

        driver.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div/div[2]/form/div[3]/div').click()
        driver.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div/div[2]/form/button').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[4]/div[2]')), ).click()
        passcode = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[4]/div').text
        print(f'wallet word is :{passcode}')
        time.sleep(3)
        with open('accounts.txt', 'a') as account:
            account.write(
                "{}\n".format(passcode))
        driver.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div[2]/button[1]').click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[1]/div/div[4]/div/div/div/div[1]/div/div/div/button')), ).click()

        wcb.OpenClipboard()
        time.sleep(2)
        address = wcb.GetClipboardData(wc.CF_TEXT)
        time.sleep(2)
        address.decode("gbk")
        print(f'wallet address is : {address.decode("gbk")}')
        waddress = address.decode("gbk")
        time.sleep(3)

        first = pyautogui.locateOnScreen(image='1.png', grayscale=True, confidence=0.9)
        x, y = pyautogui.center(first)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        time.sleep(1)
        pyautogui.click(x=x - 194, y=y + 239, clicks=1, button='left')
        time.sleep(1)
        pyautogui.click(x=x - 418, y=y + 165, clicks=1, button='left')
        time.sleep(1)
        pyautogui.write('key')
        time.sleep(1)
        pyautogui.click(x=x - 536, y=y + 216, clicks=1, button='left')
        time.sleep(1)
        pyautogui.click(x=x - 362, y=y + 75, clicks=1, button='left')
        time.sleep(1)
        pyautogui.click(x=x , y=y -20 , clicks=1, button='left')
        time.sleep(1)
        try:
            driver.get('https://murakamiflowers.kaikaikiki.com/register/new')
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                            '/html/body/div[4]/section/div[2]/form/div[1]/div/div/div[2]/input')), ).click()
        except:
            try:
                driver.get('https://murakamiflowers.kaikaikiki.com/register/new')
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                               '/html/body/div[4]/section/div[2]/form/div[1]/div/div/div[2]/input')), ).click()
            except:
                driver.get('https://murakamiflowers.kaikaikiki.com/register/new')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/section/div[2]/form/div[1]/div/div/div[2]/input')), ).click()
        driver.find_element_by_xpath('/html/body/div[4]/section/div[2]/form/div[1]/div/div/div[2]/input').send_keys(
            use_email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/section/div/h2')), )

        print('Congrats! succesful getting email!')
        time.sleep(5)

        while True:
            try:
                read_email_from_gmail(use_email)
                if 'https' in finallink:

                    break
                time.sleep(5)
                print('checking email..')
            except:
                pass

        driver.get(finallink)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/section/div/h2')), )
        except:
            try:
                driver.get(finallink)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                '/html/body/div[4]/section/div/h2')), )
            except:
                try:
                    driver.get(finallink)
                except:
                    with open('linkcollect.txt', 'a') as account:
                        account.write(
                            "{}\n".format(
                                finallink))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                       '/html/body/div[4]/section/div/h2')), )
        warn_info = {
            'username': 'maybe murakamiflowers',
            'avatar_url': 'https://lh3.googleusercontent.com/WGlA-JoX4kCsOKhT9V353C_B-D-zSw196-DBdDUxCqU71BnUvtDtYYf2umGH_zMK0SLoh8RivV-QDNwX4DEvSk0GYGFgq9ssw7NLLw=s0',
            "embeds": [
                {"title": "**maybe murakamiflowers entered**",
                 "color": 16711935,
                 "footer": {
                     "text": "maybe murakamiflowers enter bot",
                     "icon_url": "https://lh3.googleusercontent.com/WGlA-JoX4kCsOKhT9V353C_B-D-zSw196-DBdDUxCqU71BnUvtDtYYf2umGH_zMK0SLoh8RivV-QDNwX4DEvSk0GYGFgq9ssw7NLLw=s0"
                 },
                 "fields": [
                     {"name": "use_link", "value": "||{}||".format(finallink),
                      "inline": False},
                     {"name": "use_email", "value": "||{}||".format(use_email),
                      "inline": False},
                     {"name": "use_wallet", "value": "||{}||".format(waddress),
                      "inline": False},
                     {"name": "walletkeyword", "value": "||{}||".format(passcode),
                      "inline": False},
                     {"name": "Status", "value": "Done", "inline": False}]}]}
        requests.post(
            'webhook',
            json=warn_info)
        driver.find_element_by_xpath('/html/body/div[4]/section/div/form/div[1]/div/div[2]/div[2]/input').send_keys(names.get_first_name().lower())
        driver.find_element_by_xpath('/html/body/div[4]/section/div/form/div[1]/div/div[3]/div[2]/input').send_keys(waddress)
        driver.find_element_by_xpath('/html/body/div[4]/section/div/form/div[1]/div/div[4]/div[2]/input').send_keys('')
        driver.find_element_by_xpath('/html/body/div[4]/section/div/form/div[1]/div/div[5]/div[2]/input').send_keys('')

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/section/div/div/div/a')), )
            driver.find_element_by_xpath('/html/body/div[4]/section/div/div/div/a')
            warn_info = {
                'username': 'murakamiflowers',
                'avatar_url': 'https://lh3.googleusercontent.com/WGlA-JoX4kCsOKhT9V353C_B-D-zSw196-DBdDUxCqU71BnUvtDtYYf2umGH_zMK0SLoh8RivV-QDNwX4DEvSk0GYGFgq9ssw7NLLw=s0',
                "embeds": [
                    {"title": "**murakamiflowers entered**",
                     "color": 16777215,
                     "footer": {
                         "text": "murakamiflowers enter bot",
                         "icon_url": "https://lh3.googleusercontent.com/WGlA-JoX4kCsOKhT9V353C_B-D-zSw196-DBdDUxCqU71BnUvtDtYYf2umGH_zMK0SLoh8RivV-QDNwX4DEvSk0GYGFgq9ssw7NLLw=s0"
                     },
                     "fields": [
                         {"name": "use_email", "value": "||{}||".format(use_email),
                          "inline": False},
                         {"name": "use_wallet", "value": "||{}||".format(waddress),
                          "inline": False},
                         {"name": "walletkeyword", "value": "||{}||".format(passcode),
                          "inline": False},
                         {"name": "Status", "value": "Done", "inline": False}]}]}
            requests.post(
                '',
                json=warn_info)
            print('Congrats! succesful registered!')
            time.sleep(4)
        except:
            with open('linkcollect.txt', 'a') as account:
                account.write(
                    "{}\n".format(
                        finallink))
        time.sleep(4)
        driver.close()
        driver.quit
    except:
        driver.close()
        driver.quit
        pass

if __name__ == '__main__':
    print('Welcome using Murakami Register bot, type yes to start: ')
    choise = input()
    if choise.lower() == 'yes':
        n = 0
        while n < 10000:
            profie = load_profile()
            murakami()
            from ctypes import windll
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            n += 1
            if n == 10000:
                break


