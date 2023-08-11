import requests
from bs4 import BeautifulSoup
import pandas as pd


# Sites are in format: https://thehimalayantimes.com/morearticles/[catagories]?pgno=[page number]
site = 'https://thehimalayantimes.com/'
catagories = ['Nepal', 'world', 'opinion', 'business', 'sports', 'entertainment', 'lifestyle', 'science-and-tech', 'environment', 'health']
No_pages_per_catagory = 10


def scrape_links():
    meta_data = []
    for item in catagories:
        for i in range(1,No_pages_per_catagory+1):
            link = site + 'morearticles/' + item + '?pgno=' + str(i)
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            soup = soup.find('div',class_ = "post_list")
            soups = soup.find_all('a', class_ = "ratio")
            # print(f"pgno= {i}")
            for soup in soups:
                meta_data.append([item, soup['title'], soup['href']])
        print(f"catagory= {item} done")
    
    return meta_data

def scrape_contents(meta_data):
    contents = []
    for catagory, title, link in meta_data:
        print(link)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        date = soup.find('div', class_ = "article_date").text
        soup = soup.find('div', class_ = "dropcap")
        soups = soup.find_all('p')
        text = ''.join(soup.text for soup in soups if not soup.find('strong'))
        contents.append([catagory, title, date, link, text])           
    return contents
    
if __name__ == "__main__":
    ## Uncomment to scrape meta data (Complete execution once)
    
    # meta_data = scrape_links()
    # df = pd.DataFrame(meta_data, columns = ['catagory', 'title', 'link'])
    # df.to_csv('scraped_data/meta_data.csv', index = False)
    
    
    ## Uncomment to use previously scraped meta data
    df = pd.read_csv('scraped_data/meta_data.csv')
    meta_data  = df.values.tolist()
    
    
    ## scrape actual contents going through each link
    contents = scrape_contents(meta_data)
    pd.DataFrame(contents, columns = ['catagory', 'title', 'date', 'link', 'text']).to_csv('scraped_data/contents.csv', index = False)
    