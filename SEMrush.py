from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def pesquisa(links):
    #login no SEMrush
    EMAIL = 'maruquesso@gmail.com'
    SENHA = 'ICMarket01'

    PATH = '/home/lucas/Documentos/chromedriver-linux64/chromedriver'

    driver = webdriver.Chrome()
    driver.get("https://pt.semrush.com/projects/")
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "srf-login-btn")))
    login.click()
    wait = WebDriverWait(driver, 10)
    email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    email.send_keys(EMAIL)
    senha = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    senha.send_keys(SENHA)
    fazer_login = wait.until(EC.element_to_be_clickable((By.ID, "loginForm"))) 
    fazer_login.click()
    #IMPOSSÍVEL CONCLUIR POS TEM CAPTCHA NO LOGIN


    #driver.close()