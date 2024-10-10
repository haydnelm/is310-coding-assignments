from bs4 import *
import requests

url = 'https://oldschool.runescape.wiki/w/Boss'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_tables = soup.find_all('table', {'class': 'wikitable'})
all_bosses = []

for table in all_tables:
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if columns:
            boss_name = columns[0].get_text(strip=True).replace(' ', '_')
            all_bosses.append(boss_name)

all_bosses = list(set(all_bosses))
separated_bosses = []
for boss in all_bosses:
    if '&' in boss:
        separated_bosses.extend(boss.split('&'))
    else:
        separated_bosses.append(boss)

# Remove any leading/trailing whitespace from the separated names
separated_bosses = [boss.strip() for boss in separated_bosses]
boss_unique_items = []

for boss in separated_bosses:
    boss_url = f'https://oldschool.runescape.wiki/w/{boss}#Uniques'
    boss_response = requests.get(boss_url)
    boss_soup = BeautifulSoup(boss_response.content, 'html.parser')
    
    unique_items_section = boss_soup.find(id='Uniques')
    if unique_items_section:
        unique_items_list = unique_items_section.find_next('ul')
        if unique_items_list:
            unique_items = [item.get_text(strip=True) for item in unique_items_list.find_all('li')]
            boss_unique_items.append([boss, unique_items])

current_boss = None
for boss, items in boss_unique_items:
    if boss in separated_bosses:
        if boss != current_boss:
            if current_boss is not None:
                print()
            current_boss = boss
        print(f"{boss}: {', '.join(items)}")
print()