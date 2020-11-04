import sys
import time
import datetime

import Log
import Database

import requests
from bs4 import BeautifulSoup

class Loan:

	lid = None
	b_name = None
	b_description = None
	b_type = None
	b_sector = None
	b_employees = None
	date_approved = None
	loan_amount = None
	lender = None

def run():

	log = Log.Log()	
	log.makeDirectories()

	dbh = Database.Database()

	total_pages = list(range(6613))
	total = len(total_pages)
	start_from = 0

	for page in total_pages:
		print("Current: {0}/{1}".format(page,total))

		if start_from > page:
			continue

		try:
			
			url = "https://www.cnn.com/projects/ppp-business-loans/loans?page=" + str(page) + "&limit=100"
			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')

			# Get elements where needed data is
			wrapper = soup.find('div', class_='table-wrapper').find('tbody')
			table_rows = wrapper.find_all('tr')
			
			rows = ""
			for row in table_rows:

				tds = []
				try:
					tds = row.find_all('td')
				except Exception as e:
					continue

				c = {}
				c['lid'] = None
				c['b_name'] = tds[1].text.strip().replace('  ','').replace('\n\n',' ').replace('\n','')
				c['b_description'] = tds[0].text.strip()
				c['b_type'] = tds[2].text.strip()
				c['b_sector'] = tds[3].text.strip().replace('  ','').replace('\n\n',' ').replace('\n','')
				c['b_employees'] = tds[4].text.strip()
				c['date_approved'] = tds[5].text.strip()
				c['loan_amount'] = tds[6].text.strip()
				c['lender'] = tds[7].text.strip()

				date = c['date_approved']
				date = datetime.datetime.strptime(date, '%B %d, %Y')
				c['date_approved'] = date

				rows +=  "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}\n".format(c['b_name'], c['b_description'], c['b_type'], c['b_sector'], c['b_employees'], c['date_approved'], c['loan_amount'], c['lender'])

			if rows != "":
				with open('tmp_data.txt','w') as f:
					f.write(rows)
					
				sql = "LOAD DATA LOCAL INFILE 'tmp_data.txt' INTO TABLE loans FIELDS TERMINATED BY '|' (loans.name,loans.description,loans.type,loans.sector,loans.employees,loans.date_approved,loans.loan_amount,loans.lender) SET id=NULL"
				dbh.cursor = dbh.connection.cursor()
				dbh.cursor.execute(sql)

		except Exception as e:
			Log.Log().logError("Error Processing: {0} - {1}".format(page, str(e)))

	dbh.closeConnection()


if __name__ == '__main__':
	run()
