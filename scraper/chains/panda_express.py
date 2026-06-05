from chains._generic_table import GenericTableScraper


class PandaExpressScraper(GenericTableScraper):
    name         = "Panda Express"
    slug         = "panda-express"
    website      = "https://www.pandaexpress.com"
    cuisine_type = "Asian"
    url          = "https://www.pandaexpress.com/menu"
