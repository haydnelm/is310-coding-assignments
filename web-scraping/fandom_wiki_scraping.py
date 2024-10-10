from bs4 import *
import requests

url = "https://oldschool.runescape.wiki/w/Boss"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

boss_table = soup.find('table', {'class': 'wikitable'})
boss_rows = boss_table.find_all('tr')[1:]  # Skip the header row

for row in boss_rows:
    columns = row.find_all('td')
    boss_data = [col.get_text(strip=True) for col in columns]
    print(boss_data)