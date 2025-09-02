<!-- web_api_intro.md -->

# WHAT IS A WEB API?

- **API (Application Programming Interface):**  
  A set of rules that allows one software application to interact with another.  

- **Web API:**  
  A type of API accessed over the **internet** using **HTTP requests**.  
  - Typically returns data in **JSON** (sometimes XML).  
  - Common HTTP methods: `GET`, `POST`, `PUT`, `DELETE`.  

---

## Why Learn Web APIs?

✅ **Automate data extraction** from live sources (weather, news, finance, etc.)  
✅ **Integrate Python** with services like **Twitter, Spotify, Google APIs**, etc.  
✅ **Build real-time dashboards** and data-driven applications.  

---

## Example: A Simple Web API Call in Python

```python
import requests

# Example: Fetch public data from a sample API
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if response.status_code == 200:
    data = response.json()
    print("Bitcoin Price in USD:", data["bpi"]["USD"]["rate"])
else:
    print("Error:", response.status_code)
