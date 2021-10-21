import time

def menu():
    print("Welcome to the BMW M3 Webscraper v0.1 \n\n 1: BMW Seattle \n 2: BMW Bellevue \n 3: BMW Northwest")
    option = input("\nPlease enter your choice > ")

    if option == "1":
        print("Seattle selected...\nScraping website for M3 listings...")
        time.sleep(2)
        scraper()

    if option == "2":
        print("Bellevue selected...\nScraping website for M3 listings...")
        time.sleep(2)
        scraper()

    if option == "3":
        print("Northwest selected...\nScraping website for M3 listings...")
        time.sleep(2)
        scraper()

    else:
        print("Invalid selection, returning to main menu...")
        time.sleep(2)
        menu()
menu()
