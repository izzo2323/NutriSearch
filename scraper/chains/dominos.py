from chains._generic_table import GenericTableScraper


class DominosScraper(GenericTableScraper):
    name         = "Domino's"
    slug         = "dominos"
    website      = "https://www.dominos.com"
    cuisine_type = "Pizza"
    url          = "https://www.dominos.com/en/pages/content/localized/nutritioninfo.html"
