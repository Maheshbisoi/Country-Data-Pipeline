
import sqlite3


class CountryDatabaseManager:
    def __init__(self, db_name="countries.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS countries (
                    name TEXT PRIMARY KEY,
                    capital TEXT NOT NULL,
                    population INTEGER NOT NULL,
                    area REAL NOT NULL
                )
            """)

    def insert_country(self, country):
        with self.connect() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO countries
                (name, capital, population, area)
                VALUES (?, ?, ?, ?)
            """, (
                country["name"],
                country["capital"],
                country["population"],
                country["area"]
            ))

    def insert_many(self, countries):
        with self.connect() as conn:
            conn.executemany("""
                INSERT OR REPLACE INTO countries
                (name, capital, population, area)
                VALUES (?, ?, ?, ?)
            """, [
                (c["name"], c["capital"], c["population"], c["area"])
                for c in countries
            ])

    def get_all_countries(self):
        with self.connect() as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                "SELECT * FROM countries ORDER BY name"
            ).fetchall()
            return [dict(row) for row in rows]

    def get_country(self, name):
        with self.connect() as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM countries WHERE name = ?",
                (name,)
            ).fetchone()
            return dict(row) if row else None

    def update_country(self, name, capital, population, area):
        with self.connect() as conn:
            cursor = conn.execute("""
                UPDATE countries
                SET capital = ?, population = ?, area = ?
                WHERE name = ?
            """, (capital, population, area, name))
            return cursor.rowcount > 0

    def delete_country(self, name):
        with self.connect() as conn:
            cursor = conn.execute(
                "DELETE FROM countries WHERE name = ?", (name,)
            )
            return cursor.rowcount > 0


if __name__ == "__main__":
    db = CountryDatabaseManager()

    print("Database created successfully!")

    countries = db.get_all_countries()
    print("Total countries in database:", len(countries))

    print("Database check completed successfully!")
