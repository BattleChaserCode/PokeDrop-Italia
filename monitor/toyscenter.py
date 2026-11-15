import requests
from bs4 import BeautifulSoup

URL = "https://www.toyscenter.it/brands/pokemon/"

def check_toyscenter():
    print("Checking Toys Center Pokémon products...")

    headers = {
        "User-Agent": "PokeDropItalia/1.0 (product availability checker)"
    }

    response = requests.get(
        URL,
        headers=headers,
        timeout=30
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select("li.product, .product")
    found = set()

    for product in products:
        link = product.select_one('a[href*="/prodotto/"]')

        if not link:
            continue

        url = link.get("href", "")
        title = (
            product.select_one(
                ".woocommerce-loop-product__title"
            )
            or product.select_one("h2")
            or product.select_one("h3")
        )

        if not url or url in found:
            continue

        found.add(url)

        name = title.get_text(strip=True) if title else link.get_text(strip=True)
        price = product.select_one(".price")

        print("Product:", name or "Name unavailable")
        print("URL:", url)

        if price:
            print("Price:", price.get_text(" ", strip=True))

        print("-" * 40)

    print("Products found:", len(found))

if __name__ == "__main__":
    check_toyscenter()
