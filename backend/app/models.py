from datetime import datetime
from sqlalchemy import (
    Boolean, Column, DateTime, Float, ForeignKey,
    Integer, Numeric, String, Text, BigInteger
)
from sqlalchemy.orm import relationship
from geoalchemy2 import Geography
from app.database import Base


class RestaurantChain(Base):
    __tablename__ = "restaurant_chains"

    id           = Column(Integer, primary_key=True)
    name         = Column(String(255), nullable=False)
    slug         = Column(String(255), unique=True, nullable=False)
    website      = Column(String(500))
    logo_url     = Column(String(500))
    cuisine_type = Column(String(100))
    is_chain     = Column(Boolean, default=True)
    created_at   = Column(DateTime, default=datetime.utcnow)
    updated_at   = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    locations        = relationship("RestaurantLocation", back_populates="chain", lazy="selectin")
    menu_categories  = relationship("MenuCategory", back_populates="chain")
    menu_items       = relationship("MenuItem", back_populates="chain")


class RestaurantLocation(Base):
    __tablename__ = "restaurant_locations"

    id         = Column(Integer, primary_key=True)
    chain_id   = Column(Integer, ForeignKey("restaurant_chains.id", ondelete="CASCADE"))
    address    = Column(String(500))
    city       = Column(String(100))
    state      = Column(String(50))
    zip        = Column(String(20))
    country    = Column(String(50), default="US")
    lat        = Column(Numeric(10, 7))
    lon        = Column(Numeric(10, 7))
    geom       = Column(Geography("POINT", srid=4326))
    osm_id     = Column(BigInteger)
    phone      = Column(String(30))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    chain = relationship("RestaurantChain", back_populates="locations")


class MenuCategory(Base):
    __tablename__ = "menu_categories"

    id            = Column(Integer, primary_key=True)
    chain_id      = Column(Integer, ForeignKey("restaurant_chains.id", ondelete="CASCADE"))
    name          = Column(String(255), nullable=False)
    display_order = Column(Integer, default=0)

    chain      = relationship("RestaurantChain", back_populates="menu_categories")
    menu_items = relationship("MenuItem", back_populates="category")


class MenuItem(Base):
    __tablename__ = "menu_items"

    id           = Column(Integer, primary_key=True)
    chain_id     = Column(Integer, ForeignKey("restaurant_chains.id", ondelete="CASCADE"))
    category_id  = Column(Integer, ForeignKey("menu_categories.id", ondelete="SET NULL"), nullable=True)
    name         = Column(String(500), nullable=False)
    description  = Column(Text)
    serving_size = Column(String(100))
    image_url    = Column(String(500))
    is_available = Column(Boolean, default=True)
    created_at   = Column(DateTime, default=datetime.utcnow)
    updated_at   = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    chain     = relationship("RestaurantChain", back_populates="menu_items")
    category  = relationship("MenuCategory", back_populates="menu_items")
    nutrition = relationship("NutritionInfo", back_populates="menu_item", uselist=False, lazy="selectin")


class NutritionInfo(Base):
    __tablename__ = "nutrition_info"

    id                = Column(Integer, primary_key=True)
    menu_item_id      = Column(Integer, ForeignKey("menu_items.id", ondelete="CASCADE"), unique=True)
    calories          = Column(Integer)
    calories_from_fat = Column(Integer)
    total_fat_g       = Column(Numeric(8, 2))
    saturated_fat_g   = Column(Numeric(8, 2))
    trans_fat_g       = Column(Numeric(8, 2))
    cholesterol_mg    = Column(Integer)
    sodium_mg         = Column(Integer)
    total_carbs_g     = Column(Numeric(8, 2))
    dietary_fiber_g   = Column(Numeric(8, 2))
    total_sugars_g    = Column(Numeric(8, 2))
    added_sugars_g    = Column(Numeric(8, 2))
    protein_g         = Column(Numeric(8, 2))
    vitamin_d_mcg     = Column(Numeric(8, 2))
    calcium_mg        = Column(Numeric(8, 2))
    iron_mg           = Column(Numeric(8, 2))
    potassium_mg      = Column(Numeric(8, 2))
    # health_score is a DB-generated column — read-only from SQLAlchemy
    health_score      = Column(Numeric(10, 2))
    created_at        = Column(DateTime, default=datetime.utcnow)
    updated_at        = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    menu_item = relationship("MenuItem", back_populates="nutrition")


class PresetMeal(Base):
    __tablename__ = "preset_meals"

    id            = Column(Integer, primary_key=True)
    chain_id      = Column(Integer, ForeignKey("restaurant_chains.id", ondelete="CASCADE"))
    name          = Column(String(255), nullable=False)
    description   = Column(Text)
    category      = Column(String(50), default="popular")
    display_order = Column(Integer, default=0)
    created_at    = Column(DateTime, default=datetime.utcnow)

    chain = relationship("RestaurantChain")
    items = relationship("PresetMealItem", back_populates="preset_meal", lazy="selectin")


class PresetMealItem(Base):
    __tablename__ = "preset_meal_items"

    id             = Column(Integer, primary_key=True)
    preset_meal_id = Column(Integer, ForeignKey("preset_meals.id", ondelete="CASCADE"))
    menu_item_id   = Column(Integer, ForeignKey("menu_items.id", ondelete="CASCADE"))
    quantity       = Column(Integer, default=1)

    preset_meal = relationship("PresetMeal", back_populates="items")
    menu_item   = relationship("MenuItem", lazy="selectin")
