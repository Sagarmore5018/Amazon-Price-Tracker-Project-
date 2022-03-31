# import requests
#
# # import lxml
# from bs4 import BeautifulSoup
# # from unidecode import unidecode
# # price = "$\xa0999"
# # price = unidecode(price) # $ 999
#
# url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
#
# response = requests.get(url, headers=header)
#
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())
#
#
# # price = float(soup.find_all(name="span", class_="a-size-medium a-color-price")[4].getText().split("$")[1])
# price = soup.find(name="span",id="priceblock_ourprice").get_text()
# price_without_currency = price.split("$")[1]
# # price_without_currrency = float(soup.find_all(name="span", class_="a-size-medium a-color-price")[4].getText().split("$")[1])
# price_as_float = float(price_without_currency)
# print(price_as_float)

from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.in/BenQ-23-8-inch-Monitor-Built/dp/B073NTCT4Q/ref=sr_1_5?dchild=1&keywords=monitor&qid=1631012056&sr=8-5"
params = {
"Accept-Language": "en-US,en;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
response = requests.get(URL, headers=params)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
price = soup.find(name="span", id="priceblock_ourprice").getText()
split_price_symbol = price.split("₹")[1]
remove_price_comma = split_price_symbol.replace(",", "")
price_conversion = float(remove_price_comma)