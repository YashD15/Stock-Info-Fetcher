# Take NSE Code and return the HTML File
import requests

def htmlMaker(code: str) -> str:
    # Construct the URL
    if code == "SBILIFE" or code == "BAJAJHFL" or code == "ICICIGI" or code == "IRFC" or code == "BANDHANBNK" or code == "CASTROLIND" or code == "ABBOTINDIA":
        url = f"https://www.screener.in/company/{code}/"
    else:
        url = f"https://www.screener.in/company/{code}/consolidated/"
    
    # Set headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Send GET request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_path = f"HTML/{code}.html"
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(response.text)
        # print(f"HTML saved successfully as '{file_path}'")
        return file_path
    else:
        raise Exception(f"Failed to retrieve page for {code}. Status code: {response.status_code}")