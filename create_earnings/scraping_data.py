class ScrapingData :
    
    date = ''
    name = ''
    price = ''
    commission = ''
    customer = ''
    postcode = ''
    address = ''
    code = ''
    
    @staticmethod
    def setScrapingData(date, name, price, commission, customer, postcode, address, code):
        ScrapingData.date = date
        ScrapingData.name = name
        ScrapingData.price = price
        ScrapingData.commission = commission
        ScrapingData.customer = customer
        ScrapingData.postcode = postcode
        ScrapingData.address = address
        ScrapingData.code = code