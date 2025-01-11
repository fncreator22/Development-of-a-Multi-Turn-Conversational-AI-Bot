import httpx

def make_api_call(url, payload, headers=None):
    try:
        response = httpx.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        return {"error": str(e)}
