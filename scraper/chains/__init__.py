from chains.mcdonalds import McDonaldsScraper
from chains.chipotle import ChipotleScraper
from chains.starbucks import StarbucksScraper
from chains.subway import SubwayScraper
from chains.taco_bell import TacoBellScraper
from chains.burger_king import BurgerKingScraper
from chains.wendys import WendysScraper
from chains.panera import PaneraScraper
from chains.chick_fil_a import ChickFilAScraper
from chains.kfc import KFCScraper
from chains.popeyes import PopeyesScraper
from chains.sonic import SonicScraper
from chains.panda_express import PandaExpressScraper
from chains.dominos import DominosScraper
from chains.pizza_hut import PizzaHutScraper
from chains.five_guys import FiveGuysScraper
from chains.arbys import ArbysScraper
from chains.dairy_queen import DairyQueenScraper
from chains.jimmy_johns import JimmyJohnsScraper
from chains.culvers import CulversScraper
from chains.wingstop import WingstopScraper
from chains.raising_canes import RaisingCanesScraper
from chains.applebees import AppleBeesScraper
from chains.chilis import ChilisScraper
from chains.olive_garden import OliveGardenScraper
from chains.texas_roadhouse import TexasRoadhouseScraper
from chains.red_robin import RedRobinScraper
from chains.buffalo_wild_wings import BuffaloWildWingsScraper
from chains.little_caesars import LittleCaesarsScraper
from chains.papa_johns import PapaJohnsScraper
from chains.dunkin import DunkinScraper
from chains.ihop import IHOPScraper
from chains.dennys import DennysScraper
from chains.cracker_barrel import CrackerBarrelScraper
from chains.outback import OutbackScraper
from chains.red_lobster import RedLobsterScraper
from chains.shake_shack import ShakeShackScraper
from chains.jersey_mikes import JerseyMikesScraper
from chains.firehouse_subs import FirehouseSubsScraper
from chains.noodles import NoodlesScraper
from chains.qdoba import QdobaScraper
from chains.jack_in_the_box import JackInTheBoxScraper
from chains.whataburger import WhataburgerScraper
from chains.zaxbys import ZaxbysScraper
from chains.bob_evans import BobEvansScraper
from chains.hardees import HardeesScraper
from chains.del_taco import DelTacoScraper
from chains.el_pollo_loco import ElPolloLocoScraper
from chains.longhorn import LongHornScraper
from chains.in_n_out import InNOutScraper

ALL_SCRAPERS = [
    McDonaldsScraper,
    ChipotleScraper,
    StarbucksScraper,
    SubwayScraper,
    TacoBellScraper,
    BurgerKingScraper,
    WendysScraper,
    PaneraScraper,
    ChickFilAScraper,
    KFCScraper,
    PopeyesScraper,
    SonicScraper,
    PandaExpressScraper,
    DominosScraper,
    PizzaHutScraper,
    FiveGuysScraper,
    ArbysScraper,
    DairyQueenScraper,
    JimmyJohnsScraper,
    CulversScraper,
    WingstopScraper,
    RaisingCanesScraper,
    AppleBeesScraper,
    ChilisScraper,
    OliveGardenScraper,
    TexasRoadhouseScraper,
    RedRobinScraper,
    BuffaloWildWingsScraper,
    LittleCaesarsScraper,
    PapaJohnsScraper,
    DunkinScraper,
    IHOPScraper,
    DennysScraper,
    CrackerBarrelScraper,
    OutbackScraper,
    RedLobsterScraper,
    ShakeShackScraper,
    JerseyMikesScraper,
    FirehouseSubsScraper,
    NoodlesScraper,
    QdobaScraper,
    JackInTheBoxScraper,
    WhataburgerScraper,
    ZaxbysScraper,
    BobEvansScraper,
    HardeesScraper,
    DelTacoScraper,
    ElPolloLocoScraper,
    LongHornScraper,
    InNOutScraper,
]

SCRAPER_MAP = {s.slug: s for s in ALL_SCRAPERS}
