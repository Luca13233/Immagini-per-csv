import os
import time
from Scraper import GoogleImageScraper
from patch import webdriver_executable
from Scraper import bcolors


if __name__ == "__main__":
	
	input_filename = 'input.csv'			# The .csv input file
	headless = True                     # True = No Chrome GUI
	min_resolution = (0, 0)             # Minimum desired image resolution
	max_resolution = (9999, 9999)       # Maximum desired image resolution
	load_time = 0.25							# Image load time (program sleeps, program execution takes longer but chance of saving a link is higher)
													# Should implement in a different way (wait until element loaded etc...)
	
	webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))

	dir = os.path.join(os.getcwd(), "webdriver")
	if not os.path.exists(dir):
		os.mkdir(dir)

	# Selects the second column of a csv file and limits the maximum amount of words allowed
	import csv
	search_keys=[]  # an empty list to store the second column
	with open(input_filename, 'r') as rf:
		reader = csv.reader(rf, delimiter=',')
		for row in reader:
			s = row[1].split()
			del s[8:len(s)]
			s = " ".join(s)
			search_keys.append(s)
	
	image_scraper = GoogleImageScraper(webdriver_path, search_keys, headless, min_resolution, max_resolution)

	idx = 0
	for key in search_keys:
		print(bcolors.BOLD + "[INFO] Loop number " + str(idx) + bcolors.ENDC)
		start_time = time.time()
		myFile = open("output.csv", mode="a")
		myFile.write(image_scraper.find_image_urls(key, load_time))
		myFile.close()
		print("--- %.2f seconds ---" % (time.time() - start_time))
		idx += 1

	del image_scraper