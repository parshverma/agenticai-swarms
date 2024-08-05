import requests

def fetch_cat_fact():
    """
    Fetch a random cat fact from the Cat Facts API.

    Returns:
        str: A random cat fact.
    """
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            fact = response.json().get("fact", "No fact found")
            return fact
        else:
            return f"Error: Received status code {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the API
cat_fact = fetch_cat_fact()
print(f"Cat Fact: {cat_fact}")
