# Take NSE Code and return the .HTML File
import requests

def htmlMaker(code: str) -> str:
    # Construct the URL as per the actual URL
    if code == "SBILIFE" or code == "BAJAJHFL" or code == "ICICIGI" or code == "IRFC" or code == "BANDHANBNK" or code == "CASTROLIND" or code == "ABBOTINDIA" or code == "MSUMI":
        url = f"https://www.screener.in/company/{code}/"
    else:
        url = f"https://www.screener.in/company/{code}/consolidated/"
    
    # Set headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Send GET request to download HTML
    response = requests.get(url, headers=headers)

    # Store the HTML temporary to read and scrap
    if response.status_code == 200:
        file_path = f"HTML/{code}.html"
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(response.text)
        return file_path
    else:
        raise Exception(f"Failed to retrieve page for {code}. Status code: {response.status_code}")