from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import restaurants, menu_items, locations, meal, preset_meals, builder

app = FastAPI(title="Restaurant Nutrition API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurants.router, prefix="/api")
app.include_router(menu_items.router, prefix="/api")
app.include_router(locations.router, prefix="/api")
app.include_router(meal.router, prefix="/api")
app.include_router(preset_meals.router, prefix="/api")
app.include_router(builder.router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}
