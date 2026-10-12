
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("exported_countries.csv")

    print("Country Data Analytics")
    print("----------------------")
    print("Total countries:", len(df))
    print("Average population:", round(df["population"].mean(), 2))
    print("Average area:", round(df["area"].mean(), 2))

    plt.figure(figsize=(10, 6))

    plt.scatter(df["population"], df["area"])

    plt.xlabel("Population")
    plt.ylabel("Area (sq. km)")
    plt.title("Country Population vs Area")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("population_vs_area.png")

    print("\nChart saved as population_vs_area.png")

    plt.show()


if __name__ == "__main__":
    main()
