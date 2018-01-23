from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

sign = input("Please enter your email address: ")

password = getpass.getpass("Enter your password")

driver.get("https://www.office.com/")

get_element_by_xpath('//*[@id="hero-banner-sign-back-in-to-office-365-link"]').click()

get_element_by_xpath('//*[@id="i1668"]').click()

get_element_by_xpath('//*[@id="otherTileText"]').cick()

get_element_by_xpath('//*[@id="i0116"]').sendKeys(Keys.HOME,Keys.chord(Keys.SHIFT,Keys.END),sign)

get_element_by_xpath('//*[@id="idSIButton9"]').click()

get_element_by_xpath('//*[@id="i0118"]').sendKeys(Keys.HOME,Keys.chord(Keys.SHIFT,Keys.END),password)

break
