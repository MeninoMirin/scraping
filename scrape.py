from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def verificar_estrategia(lista):
    for numero in lista[:4]:
        if numero >= 2:
            return False
    return True

def execute_scraping():
    options = Options()
    options.add_argument('--headless')  # Execute o Chrome em modo headless
    options.add_argument('--disable-logging')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get('https://estrelabet.com/ptb/bet/main')
        sleep(10)
        driver.refresh()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cookies-bottom-modal"]/div/div[1]/a'))
        )
        sleep(10)
        driver.find_element(By.XPATH, '//*[@id="cookies-bottom-modal"]/div/div[1]/a').click()
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('mario@tmpeml.com')
        driver.find_element(By.XPATH, '//*[@id="password-login"]').send_keys('Aviator102030!')
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div/div[2]/app-login/form/div/div/div[2]/button').click()
        sleep(5)
        driver.get('https://estrelabet.com/ptb/games/detail/casino/normal/7787')
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'gm-frm'))
        )
        sleep(5)
        iframe = driver.find_element(By.ID, 'gm-frm')
        driver.switch_to.frame(iframe)
        sleep(5)
        resultados = [float(n) for n in driver.find_element(By.CLASS_NAME, 'result-history').text.replace('x', '').split('\n')][:10]
        if verificar_estrategia(resultados):
            print(f'estrategia ok -> {resultados[:4]}')
        return resultados
    finally:
        driver.quit()
