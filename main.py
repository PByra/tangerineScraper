import requests
from bs4 import BeautifulSoup

# Step 1: Make an HTTP request to the website
url = 'https://blog.python.org/'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 2: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract information from the parsed HTML
    articles = soup.find_all('div', class_='date-outer')

    for article in articles:
        title = article.find('h3', class_='post-title').text
        date = article.find('h2', class_='date-header').text
        content = article.find('div', class_='post-body').text

        print(f'Title: {title}\nDate: {date}\nContent: {content}\n---')
else:
    print(f'Error: Unable to fetch the page. Status code: {response.status_code}')
