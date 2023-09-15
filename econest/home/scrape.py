from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()


def get_house_links(driver,city,bhk,locality):
            driver.get(
                "https://magicbricks.com/property-for-rent/residential-real-estate?bedroom="+bhk+"&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&page1=&Locality="+locality+"&cityName="+city)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            avg = 0.0
            c = 0
            prop = soup.find_all('div', class_='mb-srp__card__price--amount')
            for i in prop:
                a = i.prettify()
                b = a.split("\n")
                if float(b[4].split()[0].replace(",", "")) < 100:
                    avg = avg + float(b[4].split()[0].replace(",", ""))
                    c = c + 1
                else:
                    avg = avg + float(b[4].split()[0].replace(",", ""))
                    c = c + 1
            return int(avg / c)
