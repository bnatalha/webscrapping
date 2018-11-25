import urllib2
import time
from bs4 import BeautifulSoup as bs

MAX_VOLUME_ID = 10
MAX_BOOK_ID = 100
MAX_PUZZLE_ID = 8

for book in range(1,MAX_BOOK_ID+1):
	for vol in range(1,MAX_VOLUME_ID+1):
		for puzzle in range(1,MAX_PUZZLE_ID+1):	

			# url
			u0 = "https://krazydad.com/tablet/killer/?kind=IM&" 
			u1 = "volumeNumber=" + str(vol)
			u2 = "&bookNumber=" + str(book)
			u3 = "&puzzleNumber=" + str(puzzle)
			url = u0 + u1 + u2 + u3

			# Download html
			response = urllib2.urlopen(url)
			webContent = response.read()

			# path
			p0 = 'ks-crazy/' + 'ks-'
			p1 = str(vol) + '-'
			p2 = str(book) + '-'
			p3 = str(puzzle) + '.html'
			path = p0 + p1 + p2 + p3

			# Save page
			f = open(path, 'w')
			f.write(webContent)
			f.close()

			print('saved: ' + path)
			time.sleep(.5)