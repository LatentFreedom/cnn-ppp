import datetime
import os
import pathlib

class Log:
	
	def __init__(self):
		self.directory = str(pathlib.Path(__file__).parent.absolute()) + "/logs"

	def makeDirectories(self):
		if not os.path.isdir(self.directory):
			os.makedirs(self.directory)
			os.makedirs(self.directory+"/errors")
			os.makedirs(self.directory+"/running")
		else:
			if not os.path.isdir(self.directory+"/errors"):
				os.makedirs(self.directory+"/errors")
			if not os.path.isdir(self.directory+"/running"):
				os.makedirs(self.directory+"/running")

	def logError(self, error):
		now = datetime.datetime.now()
		date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
		logLocation = self.directory+'/errors/' + date + '.log'
		f = open(logLocation, 'a+')
		f.write(str(datetime.datetime.now().strftime('%m%d%y %H:%M:%S')) + " " + error + '\n')
		f.close()

	def logAction(self, action):
		now = datetime.datetime.now()
		date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
		logLocation = self.directory+'/running/' + date + '.log'
		f = open(logLocation, 'a+')
		f.write(str(datetime.datetime.now().strftime('%m%d%y %H:%M:%S')) + " " + action + '\n')
		f.close()
