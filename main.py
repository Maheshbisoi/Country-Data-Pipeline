
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import CountryDatabaseManager

app = FastAPI(title="Country Data Pipeline API")

db = CountryDatabaseManager()


class Country(BaseModel):
    name: str = Field(min_length=1)
    capital: str
    population: int = Field(ge=0)
    area: float = Field(ge=0)


@app.get("/")
def home():
    return {"message": "Country Data Pipeline API is running"}


@app.get("/countries")
def get_all_countries():
    return db.get_all_countries()


@app.get("/countries/{country_name}")
def get_country(country_name: str):
    country = db.get_country(country_name)

    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")

    return country


@app.post("/countries", status_code=201)
def create_country(country: Country):
    if db.get_country(country.name):
        raise HTTPException(status_code=409, detail="Country already exists")

    db.insert_country(country.model_dump())

    return {
        "message": "Country created successfully",
        "country": country.model_dump()
    }


@app.put("/countries/{country_name}")
def update_country(country_name: str, country: Country):
    existing_country = db.get_country(country_name)

    if existing_country is None:
        raise HTTPException(status_code=404, detail="Country not found")

    if country.name != country_name:
        raise HTTPException(
            status_code=400,
            detail="Country name in the body must match the URL"
        )

    db.update_country(
        country_name,
        country.capital,
        country.population,
        country.area
    )

    return {
        "message": "Country updated successfully",
        "country": db.get_country(country_name)
    }


@app.delete("/countries/{country_name}")
def delete_country(country_name: str):
    deleted = db.delete_country(country_name)

    if not deleted:
        raise HTTPException(status_code=404, detail="Country not found")

    return {"message": f"{country_name} deleted successfully"}
