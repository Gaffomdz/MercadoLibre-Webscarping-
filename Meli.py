import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://moto.mercadolibre.com.ar/MLA-866956589-mondial-rv-125-_JM#position=21&type=item&tracking_id=5594e2c6-3b74-430e-a922-f5e764b721b2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="item-title__primary").get_text()
    price = soup.find(class_="price-tag-fraction").get_text()
    num_price = float(price[0:3])
    print(num_price)
    
    
    
    if(num_price =! 540):
        send_mail()


def send_mail(): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('giorgiogirardelli@gmail.com', 'ufqcgmsuetfoyxnn')

    subjet = "El precio ha bajado"
    body = "Checkea este link: https://moto.mercadolibre.com.ar/MLA-866956589-mondial-rv-125-_JM#position=21&type=item&tracking_id=5594e2c6-3b74-430e-a922-f5e764b721b2"     
    msg = f"Subjet: {subjet}\n\n{body}"

    server.sendmail(
        'giorgiogirardelli@gmail.com',
        'giorgiogirardelli@gmail.com',
        msg
    )
    print ("El email se mando")
        
    server.quit()

check_price()

#while(True):
    #check_price()
    #time.sleep(60 * 60)


