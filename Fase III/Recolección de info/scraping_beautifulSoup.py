from Scraping import Scraping

if __name__ == "__main__":
	url = 'http://www.uanl.mx'
	scraping = Scraping()
	scraping.scrapingImages(url)
	scraping.scrapingPDF(url)
	scraping.scrapingLinks(url)
	#scraping.scrapingBeautifulSoup(url)
