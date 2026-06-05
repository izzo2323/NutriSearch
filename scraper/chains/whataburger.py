from chains._generic_table import GenericTableScraper


class WhataburgerScraper(GenericTableScraper):
    name         = "Whataburger"
    slug         = "whataburger"
    website      = "https://whataburger.com"
    cuisine_type = "Fast Food"
    url          = "https://whataburger.com/menu"
