import requests
from bs4 import BeautifulSoup

def main():
    try:
        print("1")
        soup = BeautifulSoup(page.text, "html.parser")
        print(soup)
        print("2")
        company = soup.find('h1', {'class': 'D(ib) Fz(18px'}).text
        #company = soup.select('h1.D(ib) Fz(18px)')[0].text.strip()
        print("3")
        print(f"\nCompany: {company}")
        #<div class="D(ib) "><h1 class="D(ib) Fz(18px)">Invesco QQQ Trust (QQQ)</h1></div>
    except:
        print(f"Error with URL[i]")
"""
if __name__ == '__main__':
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    s = requests.Session()
    s.headers.update(headers)
    for i in range(len(URL)):
        page = s.get(URL[i])
        main()
"""  
if __name__ =='main': 
    try:
        file = open(r'urls.txt','r')
        main.py
        URL = file.readlines()
    finally:
        file.close()
    for line in URL:
        print(URL)
        page = requests.get(URL[line])
        main()
 