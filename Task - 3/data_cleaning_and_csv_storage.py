import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for item in soup.find_all('div', class_= 'data-item'):
        title = item.find('h2').text.strip()
        description = item.find('p').text.strip()
        data.append({'Title': title, 'Description': description})

    return data


def clean_data(data):
    df = pd.DataFrame(data)
    df.drop_duplicates(inplace=True)
    return df


def save_to_csv(df, filename):
    df.to_csv(filename, index=False)


url = 'https://www.amazon.in/'

scraped_data = scrape_data(url)

cleaned_data = clean_data(scraped_data)

csv_filename = 'scraped_data.csv'
save_to_csv(cleaned_data, csv_filename)

print(f"Data saved to {csv_filename}")
