import webbrowser, requests
from bs4 import BeautifulSoup

def fetchResults(companyName):
    #result = requests.get('https://google.com/');
    #print(result.raise_for_status())
    url = "https://google.com/";
    webbrowser.open(url);
    
    #webbrowser.open('https://google.com' + companyName);
#webbrowser.open('https://www.zenken.co.jp/business/')
companyList = ['Sony','Fujitsu','Nec']
for company in companyList:
    company = company+" Japan";
    fetchResults(company);




page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content,'html.parser')
print(soup.find_all('p',class_="outer-text"))

print(soup.find_all(class_="outer-text"))
