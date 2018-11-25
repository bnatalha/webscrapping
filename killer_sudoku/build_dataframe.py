from bs4 import BeautifulSoup as bs
import re
import json
import pandas as pd

MAX_VOLUME_ID = 10
MAX_BOOK_ID = 100
MAX_PUZZLE_ID = 8

# path
PATHDIR = 'ks-crazy/' + 'ks-'

ks_dict = {'ptitle':[], 'vol':[], 'book':[], 'puzzle':[], 'puzz_color':[], 'puzz_hint':[], 'solved':[], 'sOrder':[]}

pattern_var = re.compile(r'var pRec = (\{.*\});')
pattern_ptitle = re.compile(r'IM(\d+)-B(\d+)-P(\d+)')

# Building dict with puzzles
for book in range(1,MAX_BOOK_ID+1):
	for vol in range(1,MAX_VOLUME_ID+1):
		for puzzle in range(1,MAX_PUZZLE_ID+1):

			# Building path
			path_v = str(vol) + '-'
			path_b = str(book) + '-'
			path_p = str(puzzle) + '.html'
			path = PATHDIR + path_v + path_b + path_p

			# Opening html file
			f = open(path,'r')
			webContent = f.read()

			# Getting the right script tag
			soup = bs(webContent,'html.parser')
			scripts = soup.head.find_all("script")
			js_content = scripts[4].get_text()

			# Fiding var pRec content
			found = re.findall(pattern_var,str(js_content))

			if found != []:

				# Deserializing JSON
				puzzle = json.loads(found[0])

				# Saving puzzle on dict
				for k,v in ks_dict.items():
					if k in puzzle['puzzle_data']:
						ks_dict[k].append(puzzle['puzzle_data'][k])

				# Separeting cages from hints
				puzz = puzzle['puzzle_data']['puzz'].split(';')
				ks_dict['puzz_color'].append(puzz[0])
				ks_dict['puzz_hint'].append(puzz[1])

				# Getting vol, book and puzzle numbers from 'ptitle'
				re_ptitle = re.findall(pattern_ptitle, puzzle['puzzle_data']['ptitle'])
				ks_dict['vol'].append(re_ptitle[0][0])
				ks_dict['book'].append(re_ptitle[0][1])
				ks_dict['puzzle'].append(re_ptitle[0][2])

				# Closing file handler
				f.close()

	print("Book " + str(book) + " done.")

# Building dataframe
ks_df = pd.DataFrame(ks_dict, columns=['ptitle', 'vol', 'book', 'puzzle', 'puzz_color', 'puzz_hint', 'solved', 'sOrder']) 

# Save csv
ks_df.to_csv('dataset_killer_sudoku.csv')

print("Done.")