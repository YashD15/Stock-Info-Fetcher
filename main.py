import sys
import os
import time
from datetime import datetime
sys.path.append(os.path.abspath("modules"))

# My modules
import readFile
import para1
import para2
import htmlMaker
import codes
import jsonBuilder

# Main Function
if __name__ == "__main__":

    # Folder to store results
    os.makedirs('JSONs', exist_ok=True)

    # For CSV in future
    # os.makedirs('CSV', exist_ok=True) 

    # What Index to be work on
    indexName = "N100"
    index = codes.N100
    print("Current Index: ", indexName)
    print("No. of Stocks: ", len(index))

    # Some code to keep track of process(to implement)
    startTime = time.time()
    print("Started At: ", datetime.fromtimestamp(startTime))
    rem = len(index)

    # Fetch each code form codes file
    for code in index:
        print("\nRemaining: ",rem)
        print(code)

        # Provide the code to BS4 to get HTML file
        file = htmlMaker.htmlMaker(code)

        # Read the HTML file to scrap
        soup = readFile.readFile(file)

        # Scrap details when file found
        if soup:
            # Title
            title = para1.title(soup)
            # Company Name
            cn = para1.companyName(soup)
            # Company Link
            cl = para2.companyLink(soup)
            # NSE
            nse = para1.nse(soup)
            # BSE
            bse = para1.bse(soup)
            # About Company
            ac = para2.aboutCompany(soup)
            # Market Cap
            mc = para1.marketCap(soup)
            # Stock PE
            pe = para1.stockPE(soup)
            # ROE
            roe = para1.roe(soup)
            # ROCE
            roce = para1.roce(soup)
            # Dividend Yeild
            div = para1.dividend(soup)
            #Book Value
            bval = para2.bookValue(soup)
            # Last Price
            lp = para1.lPrice(soup)
            # Last Price Change Percent
            lpcp = para1.lpChange(soup)
            # Last Price Change Date
            lpcd = para1.lpDate(soup)
            # High / Low
            high , low = para2.HLValues(soup)
            # Total Assets 6Q
            assets = para2.totalAssets(soup)
            # Net Profits 6Q
            profits = para2.netProfits(soup)
            # PROs & CONs
            pro , con = para2.PaC(soup)

            # Key Points (NOT WORKING)
            # print(para2.keyPoints(soup))

            data = jsonBuilder.jsonDict(title,cn,cl,nse,bse,ac,mc,pe,roe,roce,div,bval,lp,lpcp,lpcd,high,low,assets,profits,pro,con)
            jsonBuilder.masterJSON(nse,data,indexName)
            # jsonBuilder.saveJSON(nse,data)

        os.remove(file)
        rem -= 1
        time.sleep(2)

    endTime = time.time()
    print("\nEnd Time: ", datetime.fromtimestamp(endTime))
    print(f"Time Required: {endTime - startTime:.2f} sec")