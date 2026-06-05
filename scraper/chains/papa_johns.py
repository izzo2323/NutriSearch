from chains._generic_table import GenericTableScraper


class PapaJohnsScraper(GenericTableScraper):
    name         = "Papa John's"
    slug         = "papa-johns"
    website      = "https://www.papajohns.com"
    cuisine_type = "Pizza"
    url          = "https://www.papajohns.com/order/menu"
