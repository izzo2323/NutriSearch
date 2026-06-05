from chains._generic_table import GenericTableScraper


class KFCScraper(GenericTableScraper):
    name         = "KFC"
    slug         = "kfc"
    website      = "https://www.kfc.com"
    cuisine_type = "Fast Food"
    url          = "https://www.kfc.com/nutrition"
