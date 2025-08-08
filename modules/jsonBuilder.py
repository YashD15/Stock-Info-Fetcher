import os
import json

# Create Dictionary
def jsonDict(title,cn,link,nse,bse,ac,mc,pe,roe,roce,dy,bv,lp,lpc,lpcd,high,low,ta,tp,pros,cons):
    data = {
        "Title": title,
        "CompanyName": cn,
        "Link": link,
        "NSECode": nse,
        "BSECode": bse,
        "AboutCompany": ac,
        "MarketCap": mc,
        "P/ERatio": pe,
        "ROE": roe,
        "ROCE":roce,
        "DividendYeild": dy,
        "BookValue": bv,
        "LastPrice": lp,
        "LastPriceChange": lpc,
        "LastPriceChangeDate": lpcd,
        "High": high,
        "Low": low,
        "TotalAssets6Q": ta,
        "TotalProfits6Q": tp,
        "PROs": pros,
        "CONs": cons
    }
    return data

def saveJSON(nseCode, data):
    filepath = f'JSONs/{nseCode}.json'
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def masterJSON(nseCode, data, fileName="Stock.json"):
    # If file exists, load it; otherwise, start with an empty dict
    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = {}
    else:
        all_data = {}
    # Update or add the data for this NSE code
    all_data[nseCode] = data
    # Save the updated dictionary back to the file
    with open(fileName, 'w') as f:
        json.dump(all_data, f, indent=4)