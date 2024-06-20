import requests
from bs4 import BeautifulSoup

url = "https://badesaba.ir"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    divs_with_box_class = soup.find_all('div', class_='card')
    print(divs_with_box_class)
    for div in divs_with_box_class:
        # Here you can access elements within each div and process them
        # For example, to get the text within each div:
        print(divs_with_box_class.contents[0])
else:
    print("Failed to retrieve the webpage")

