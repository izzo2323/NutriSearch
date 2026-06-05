from chains._generic_table import GenericTableScraper


class SubwayScraper(GenericTableScraper):
    name         = "Subway"
    slug         = "subway"
    website      = "https://www.subway.com"
    cuisine_type = "Sandwiches"
    url          = "https://www.subway.com/en-US/MenuNutrition/Menu/NutritionLanding"
