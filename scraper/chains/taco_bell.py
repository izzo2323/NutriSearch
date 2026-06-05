from chains._generic_table import GenericTableScraper


class TacoBellScraper(GenericTableScraper):
    name         = "Taco Bell"
    slug         = "taco-bell"
    website      = "https://www.tacobell.com"
    cuisine_type = "Mexican"
    url          = "https://www.tacobell.com/nutrition/info"
