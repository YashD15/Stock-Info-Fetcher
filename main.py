# REQUIRED FOR PROGRAM TRACKING
import sys
import os
import time
from datetime import datetime

# PATH FOR THE modules FOLDER
sys.path.append(os.path.abspath("modules"))

# MY CUSTOM MODULES
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

    # For CSV in FUTURE SCOPE
    # os.makedirs('CSV', exist_ok=True) 

    # HERE COMMENT OR UNCOMMENT THE FUNCTIONS YOU WANT TO USE AS PER NEED

    # IF YOU WANT DATA FOR A SINGLE STOCK
    # index = []
    # stock_code = input("🔍 Enter a stock code: ")
    # index.append(stock_code.upper())


    # IF YOU WANT DATA FOR STOCK OF WHOLE INDEX
    # CHANGE INDEX NAME HERE EG. "NS50", "test"
    indexName = "test"

    # HERE ALSO
    index = codes.test

    # TRACK THE SCRAPPING PROCESS FOR INDEX SCRAPPING --KEEP AS IT IS--
    print("📊 Current Index: ", indexName)
    print("No. of Stocks: ", len(index))
    startTime = time.time()
    print("⏱️ Started At: ", datetime.fromtimestamp(startTime))
    rem = len(index)

    # FETCH CODE FROM SINGLE STOCK OR WHOLE INDEX
    for code in index:

        # WHOLE INDEX PART
        print("\nRemaining: ",rem)
        print("Current Stock: ",code)

        # DOWNLOAD HTML OF WEBPAGE OF STOCK
        file = htmlMaker.htmlMaker(code)

        # READ THE HTML OF SPECIFIC STOCK
        soup = readFile.readFile(file)

        # SCRAP DETAILS IF HTML FOUND
        if soup:

            # STORE THE DATA IN VARIABLES
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

            # DISPLAY THE DATA FOR SINGLE STOCK
            # print("="*80)
            # print(f"🏷️  Title: {title}")
            # print(f"🏢 Company Name: {cn}")
            # print(f"🔗 Company Link: {cl}")
            # print("="*80)
            # print(f"💹 NSE Code: {nse}")
            # print(f"💹 BSE Code: {bse}")
            # print(f"ℹ️  About: {ac}")
            # print("="*80)
            # print(f"💰 Market Cap: {mc}")
            # print(f"📈 Stock PE: {pe}")
            # print(f"📊 ROE: {roe}")
            # print(f"📊 ROCE: {roce}")
            # print(f"💵 Dividend Yield: {div}")
            # print(f"📚 Book Value: {bval}")
            # print("="*80)
            # print(f"💲 Last Price: {lp}")
            # print(f"📉 Price Change (%): {lpcp}")
            # print(f"🗓️  Change Date: {lpcd}")
            # print(f"📈 52W High: {high}")
            # print(f"📉 52W Low: {low}")
            # print("="*80)
            # print(f"🏦 Total Assets (6Q): {assets}")
            # print(f"💼 Net Profits (6Q): {profits}")
            # print("="*80)
            # print(f"✅ PROs: {pro}")
            # print(f"⚠️  CONs: {con}")
            # print("="*80 + "\n")


            # Key Points (NOT WORKING)
            # print(para2.keyPoints(soup))

            # CREATE DICTIONARY OF ABOVE DATA
            data = jsonBuilder.jsonDict(title,cn,cl,nse,bse,ac,mc,pe,roe,roce,div,bval,lp,lpcp,lpcd,high,low,assets,profits,pro,con)
            
            # ADD JSON TO MASTER JSON (WHOLE INDEX)
            jsonBuilder.masterJSON(nse,data,indexName)

            # MAKE JSON FOR SINGLE STOCK EG. "IOC.JSON"
            # jsonBuilder.saveJSON(nse,data)

        # DELETES THE HTML AS ITS USE IS OVER
        os.remove(file)

        # TRACKER PART AND LITTLE DELAY DURING SCRAPPING
        rem -= 1
        time.sleep(2)


    # OVERALL RESULT FOR INDEX SCRAPPING
    endTime = time.time()
    print("\n✅ End Time: ", datetime.fromtimestamp(endTime))
    print(f"⏱️ Time Required: {endTime - startTime:.2f} sec")