import requests

# John added this code to get the API, he said it should be
# refactored at some point.
def get_product_from_api(product_id):
    try:
        r = requests.get(f"https://api.provider.ext/products/{product_id}")
        return r.json()
    except Exception:
        print("something bad happened")
    return None

