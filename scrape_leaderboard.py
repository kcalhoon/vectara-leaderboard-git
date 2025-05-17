import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://github.com/vectara/hallucination-leaderboard"
table_selector = "markdown-accessibility-table > table"
output_filename = "leaderboard_data.csv"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.select_one(table_selector)

    if table:
        data = []
        header_row = table.find('thead').find('tr') if table.find('thead') else None
        if header_row:
            headers = [th.text.strip() for th in header_row.find_all('th')]
            data.append(headers)

        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                row_data = [td.text.strip() for td in row.find_all('td')]
                data.append(row_data)

        if data:
            with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            print(f"Data successfully written to {output_filename}")
        else:
            print("No data found in the table.")
    else:
        print(f"Table with selector '{table_selector}' not found.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
