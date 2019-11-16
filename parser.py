from smtplib import SMTP

import requests
from bs4 import BeautifulSoup
import smtplib
import ssl

URL = 'https://egypt.souq.com/eg-en/realme-xt-dual-sim-6-4-inch-128-gb-8-gb-ram-4g-lte-blue-82647700033/u/'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
def price_check():
 page = requests.get(URL, headers=headers )
 soup = BeautifulSoup(page.content, 'html.parser' )
 print(soup.prettify())

 title = soup.find(class_='price is sk-clr1').get_text().strip().replace(',','')
 converted_title = float(title[0:5])

 if(converted_title <= 5390.0):

     send_mail()
     print(converted_title)



def send_mail():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "my@gmail.com"
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()




price_check()

