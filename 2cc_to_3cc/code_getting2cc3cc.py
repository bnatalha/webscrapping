# creating a .csv file from a html table
# data source: https://www.worldatlas.com/aatlas/ctycodes.htm

import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request as url_lib

# getting html page
response = url_lib.urlopen('https://www.worldatlas.com/aatlas/ctycodes.htm')
data = response.read() 
text = data.decode('utf-8')

# getting table tag
soup = bs(text, 'html.parser')


# dict for the dataframe
code_dict = {}
# table lines
rows = soup.body.tbody.find_all('tr')

# table header
# ['COUNTRY', 'A2 (ISO)', 'A3 (UN)', 'NUM (UN)', 'DIALING CODE']
cols = [i.get_text() for i in rows[0].find_all('td')]

# filling every dict key with empty lists and setting the indexing names
for c in cols:
  code_dict[c] = []

# filling dict entries
for l in rows[1:]:
  for dict_idx, item in enumerate(l.find_all('td')):
    code_dict[cols[dict_idx]].append(item.get_text())

# creating dataframe
df_codes = pd.DataFrame(code_dict, columns=cols)

# saving dataframe
df_codes.to_csv('country_code.csv')

