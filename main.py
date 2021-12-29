
import requests
from bs4 import BeautifulSoup




def twabSpider():

    keyWord = input("Enter the keyword you would like to search the twabs for: ")
    print(keyWord)
    max_pages = 20
    page = 0
    while page <= max_pages:
        print("On Page:",page)
        url = 'https://www.bungie.net/en/News/Index?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.find_all('a', {'class': 'news-item'}):
            href = 'https://www.bungie.net/' + link.get('href')

            findKeyWord(href, keyWord)
        page += 1



def findKeyWord(twabUrl, keyWord):
    symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
    source_code = requests.get(twabUrl)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")

    for paragraph in soup.findAll('div', {'class': 'content'}):

        content = paragraph.text
        res = content.split()

        for word in res:
            keyWord = keyWord.lower()
            word = word.lower()
            for i in range(len(symbols)): #cleaning up the word
                word = word.replace(symbols[i], ' ')

            if(word == keyWord):
                print(twabUrl)
                break



if __name__ == '__main__':

    twabSpider()


