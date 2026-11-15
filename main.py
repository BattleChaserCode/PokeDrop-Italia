
import json
from datetime import datetime, timezone

PROJECT_NAME = "PokeDrop Italia"

RETAILERS = [
    "Comet",
    "Mondadori Store",
    "Esselunga",
    "Conad",
    "Euronics",
    "MediaWorld",
    "GameStop Italy",
    "Unieuro",
    "Carrefour",
    "Coop",
    "Toys Center",
    "Il Covo del Nerd",
    "Iperbimbo",
    "Federicstore",
    "NerdStore Italia",
    "Goldstar Shop",
    "PyrosTCG",
    "Temple Games",
    "OroCardS",
    "TCG-Store",
    "TimeTwister Games",
    "CarteMagic"
]
PRODUCT_CATEGORIES = [
    "Booster Packs",
    "Booster Boxes",
    "Elite Trainer Boxes",
    "Collection Boxes",
    "Special Sets",
    "Pokémon Tins",
    "Blister Packs",
    "30th Anniversary"
]

def main():
    print("=" * 40)
    print(PROJECT_NAME)
    print("Italian Pokémon TCG Tracker")
    print("=" * 40)

    print("\nRetailers configured:")

    for store in RETAILERS:
        print(f"[PENDING] {store}")

    print("\nProducts to monitor:")

    for category in PRODUCT_CATEGORIES:
        print(f"- {category}")

    report = {
        "project": PROJECT_NAME,
        "checked_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "retailers": RETAILERS,
        "categories": PRODUCT_CATEGORIES,
        "status": "Initial setup"
    }

    with open("status.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nSetup report saved to status.json")
    print("PokeDrop Italia initialized!")

if __name__ == "__main__":
    main()
  
