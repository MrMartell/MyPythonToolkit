import requests

def VuldbLookup(product, version=None):
    url = "https://vuldb.com/?api"
    query = {
        "apikey": "YOUR_API_KEY",
        "advancedsearch": f"product:{product}{',version:{version}' if version else ''}"
    }
    results = requests.post(url, query)
    j = results.json()
    if "result" in j:
        return [result["source"] for result in j["result"] if "source" in result]
    else:
        return []
