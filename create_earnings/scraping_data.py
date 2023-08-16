class ScrapingData :
    
    date = ''
    name = ''
    price = ''
    commission = ''
    customer = ''
    address = ''
    code = ''
    
    @staticmethod
    def setScrapingData(date, name, price, commission, customer, address, code):
        ScrapingData.date = date
        ScrapingData.name = name
        ScrapingData.price = price
        ScrapingData.commission = commission
        ScrapingData.customer = customer
        ScrapingData.address = address
        ScrapingData.code = code