import requests
import bs4

base_url = "https://www.jjfoodservice.com/product/Birmingham-Aston/{}/" ### Base URL with formating for product code
running = True 
while running:
	print("--- JJ PRICE SCRAPER ---") ## Title
	try: ## Try get user input equal to a competitors product code

		stock_code = input("Product code? ") ### User input for product code

		result = requests.get(base_url.format(stock_code)) ## Fetch URL and format with product code
		soup = bs4.BeautifulSoup(result.text,"lxml") ## Parse html into readable format

		prices = soup.select(".Productstyle__PriceText-sc-1ssfvqo-33.fJbipF") ## Select class which contains price
		title = soup.select(".ProductDetailPagestyle__Title-sc-16cjnig-16.kqPDBW") ## Select class which contains title

		product_name = title[0].text ## Filter to show just price contained within class
		product_price = prices[0].text ## Filter to show just title contained within class

		print(product_name) ## Print product name
		print("Collection Price:" + " " + product_price) ## Print product price
		search_again = input("Search again? y/n: ")
		if search_again.lower() == "y":
			continue
		else:
			running = False ## Break loop
	except: ###  If no product code found
		print("Sorry no product code found")
