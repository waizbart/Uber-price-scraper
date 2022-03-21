from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome(options=chrome_options)
# d = webdriver.Edge()

d.get('https://auth.uber.com/login/social/?next_url=https%3A%2F%2Fm.uber.com%2F%3Fuclick_id%3Da3c57bc3-f239-4bfb-9062-23751a9afd58&privileged_op_url=https%3A%2F%2Fm.uber.com%2F%3Fuclick_id%3Da3c57bc3-f239-4bfb-9062-23751a9afd58&uber_client_name=m2')
sleep(3)

entrar_face = d.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div/div/a[1]/div')
entrar_face.click()
sleep(3)

email = d.find_element_by_xpath('//*[@id="email"]')
email.send_keys("[EMAIL]")
sleep(1)
password = d.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("[SENHA]")
sleep(1)

avancar = d.find_element_by_xpath('//*[@id="loginbutton"]')
avancar.submit()
sleep(5)


while True:
    try:
        file = open('data.csv', 'a+', newline='', encoding='utf-8')
        write = csv.writer(file)
        d.get('https://m.uber.com/looking?drop%5B0%5D=%7B%22latitude%22%3A-23.528191%2C%22longitude%22%3A-47.4651676%2C%22addressLine1%22%3A%22Mind%20Consulting%20-%20Desenvolvimento%20de%20aplicativos%2C%20desenvolvimento%20web%20%2C%20empresa%20de%20ti%2C%20desenvolvimento%20de%20software%22%2C%22addressLine2%22%3A%22Terceiriza%C3%A7%C3%A3o%20de%20ti%20empresa%20ti%20desenvolvimento%20web%20agencia%20de%20aplicativos%20-%20Avenida%20Ant%C3%B4nio%20Carlos%20Comitre%20-%20Parque%20Campolim%2C%20Sorocaba%20-%20SP%2C%20Brasil%22%2C%22id%22%3A%22ChIJoVHgBOCKxZQRp1yAFrNU65s%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D&pickup=%7B%22latitude%22%3A-23.4679109%2C%22longitude%22%3A-47.4389241%2C%22addressLine1%22%3A%22Rua%20Canan%C3%A9ia%2C%20100%22%2C%22addressLine2%22%3A%22Jardim%20Leocadia%2C%20Sorocaba%20-%20SP%2C%20Brasil%22%2C%22id%22%3A%22ChIJ64HS-O9fz5QRRHKli5jG5v4%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D&vehicle=10000382')
        sleep(60)
        uberx_price = d.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div')
        comfort_price = d.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div')
        time = datetime.now()
        print(float(uberx_price.text.replace("R$", "").replace(",", ".")))
        print(float(comfort_price.text.replace("R$", "").replace(",", ".")))
        print(time)
        write.writerow([time, float(uberx_price.text.replace("R$", "").replace(",", ".")), float(comfort_price.text.replace("R$", "").replace(",", "."))])
        file.close() 
    except KeyboardInterrupt:
        file.close() 
        d.close()
        d.quit()
        sleep(2)

    

