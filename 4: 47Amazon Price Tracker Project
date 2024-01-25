import requests
import smtplib
from bs4 import BeautifulSoup

SENDING_ADDRESS = "YOUR OWN EMAIL"
RECEIVING_ADDRESS = "YOUR OWN EMAIL"
PASSWORD = "YOUR OWN PASSWORD"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
no_currency = price.split("$")[1]
float_price = float(no_currency)

if float_price <= 99.99:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(SENDING_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=SENDING_ADDRESS,
            to_addrs=RECEIVING_ADDRESS,
            msg=f"Subject: YOUR OWN SUBJECT\n\nYOUR OWN TEXT"
        )
    print("Email send succesfully")
