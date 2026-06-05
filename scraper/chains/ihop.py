from chains._generic_table import GenericTableScraper


class IHOPScraper(GenericTableScraper):
    name         = "IHOP"
    slug         = "ihop"
    website      = "https://www.ihop.com"
    cuisine_type = "Breakfast"
    url          = "https://www.ihop.com/en/menu"
