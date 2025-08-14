#SCRAPPING DATA FUNCTIONS SET 1

# Title of webpage
def title(soup):
    title_tag = soup.title
    return title_tag.string.strip() if title_tag and title_tag.string else "No title found"

# NSE Code
def nse(soup):
    # Find span with text starting with 'NSE:'
    nse_span = soup.find("span", string=lambda text: text and "NSE:" in text)
    if nse_span:
        return nse_span.get_text(strip=True).replace("NSE:", "").strip()
    return None

# BSE Code
def bse(soup):    
    # Find span with class that contains BSE: code
    bse_span = soup.find("span", string=lambda text: text and "BSE:" in text)
    if bse_span:
        # Split and clean to extract just the code
        return bse_span.get_text(strip=True).replace("BSE:", "").strip()
    return None

# Market Cap
def marketCap(soup):
    try:
        # Find the list item that contains "Market Cap"
        market_cap_item = soup.find("li", class_="flex flex-space-between", attrs={"data-source": "default"})
        name_tag = market_cap_item.find("span", class_="name")
        if name_tag and "Market Cap" in name_tag.get_text():
            number_span = market_cap_item.find("span", class_="number")
            if number_span:
                raw_value = number_span.get_text(strip=True)
                digits_only = ''.join(filter(str.isdigit, raw_value))
                return digits_only
        return None
    except Exception as e:
        print(f"Error extracting market cap: {e}")
        return None
    
# Stock PE
def stockPE(soup):
    try:
        # Find all <li> items with this class and data-source
        items = soup.find_all("li", class_="flex flex-space-between", attrs={"data-source": "default"})
        for item in items:
            label = item.find("span", class_="name")
            if label and "Stock P/E" in label.get_text(strip=True):
                number = item.find("span", class_="number")
                return number.get_text(strip=True) if number else None
        return None  # Not found
    except Exception as e:
        print(f"Error extracting stock P/E: {e}")
        return None
    
# Comapny Name
def companyName(soup):
    try:
        container = soup.find("div", class_="flex-row flex-wrap flex-align-center flex-grow")
        company_name = container.find("h1").get_text(strip=True)
        return company_name
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
    
# Last Price
def lPrice(soup):
    try:
        container = soup.find("div", class_="font-size-18 strong line-height-14")
        span = container.find("span")
        if span:
            raw_text = span.get_text(strip=True)
            numeric_value = ''.join(filter(str.isdigit, raw_text))
            return numeric_value
        return None
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Last Price Change Percent
def lpChange(soup):
    try:
        container = soup.find("div", class_="flex-row flex-wrap flex-align-center flex-grow")
        change_percent = None
        for direction in ["down", "up"]:
            span = container.find("span", class_=["font-size-12", direction, "margin-left-4"])
            if span:
                raw_text = span.get_text(strip=True).replace('%', '')
                change_percent = float(raw_text)
                break
        return change_percent
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Last Price Date
def lpDate(soup):
    try:
        container = soup.find("div", class_="flex-row flex-wrap flex-align-center flex-grow")
        date_info = container.find("div", class_="ink-600 font-size-11 font-weight-500") \
                             .get_text(strip=True)
        # Split on newline or hyphen and return the first part
        clean_date = date_info.split("\n")[0].split("-")[0].strip()
        return clean_date
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Dividend Yeild
def dividend(soup):
    try:
        # Find all relevant <li> blocks
        items = soup.find_all("li", class_="flex flex-space-between", attrs={"data-source": "default"})
        for item in items:
            label = item.find("span", class_="name")
            if label and "Dividend Yield" in label.get_text(strip=True):
                number = item.find("span", class_="number")
                return number.get_text(strip=True) if number else None
        return None  # If not found
    except Exception as e:
        print(f"Error extracting dividend yield: {e}")
        return None
    
# ROE
def roe(soup):
    try:
        items = soup.find_all("li", class_="flex flex-space-between", attrs={"data-source": "default"})
        for item in items:
            label = item.find("span", class_="name")
            if label and "ROE" in label.get_text(strip=True):
                number = item.find("span", class_="number")
                return number.get_text(strip=True) if number else None
        return None  # If ROE not found
    except Exception as e:
        print(f"Error extracting ROE: {e}")
        return None

# ROCE
def roce(soup):
    try:
        items = soup.find_all("li", class_="flex flex-space-between", attrs={"data-source": "default"})
        for item in items:
            label = item.find("span", class_="name")
            if label and "ROCE" in label.get_text(strip=True):
                number = item.find("span", class_="number")
                return number.get_text(strip=True) if number else None
        return None  # If not found
    except Exception as e:
        print(f"Error extracting ROCE: {e}")
        return None