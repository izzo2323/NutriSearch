from chains._generic_table import GenericTableScraper


class PizzaHutScraper(GenericTableScraper):
    name         = "Pizza Hut"
    slug         = "pizza-hut"
    website      = "https://www.pizzahut.com"
    cuisine_type = "Pizza"
    url          = "https://www.pizzahut.com/nutrition"
