import sys
import os
import time
sys.path.append(os.path.abspath("modules"))

# My modules
import readFile
import para1
import para2
import htmlMaker
import codes

# Main Function
if __name__ == "__main__":

    # Folder to store results
    os.makedirs('JSONs', exist_ok=True)
    os.makedirs('CSV', exist_ok=True)  

    # Some code to keep track of process(to implement)

    # Fetch each code form codes file
    for code in codes.nseCodes:
        print(code)



    # Take user input for NSE Code
    nse_code = input("Enter NSE Code: ")

    # Provide the code to BS4 to get HTML file
    file = htmlMaker.htmlMaker(nse_code)
    
    # Read the HTML file to scrap
    soup = readFile.readFile(file)

    # Scrap details when file found
    if soup:
        # Title
        title = f"Title: {para1.title(soup)}"
        print(title)

        # NSE
        nse = f"\nNSE Code: {para1.nse(soup)}"
        print(nse)

        # BSE
        bse = f"\nBSE Code: {para1.bse(soup)}"
        print(bse)

        # Market Cap
        mc =f"\nMarket Cap: {para1.marketCap(soup)}"
        print(mc)

        # Stock PE
        pe = f"\nP/E Ratio: {para1.stockPE(soup)}"
        print(pe)

        # Company Name
        cn = f"\nCompany Name: {para1.companyName(soup)}"
        print(cn)

        # Last Price (Issue)
        lp = f"\nLast Price: {para1.lPrice(soup)}"
        print(lp)

        # Last Price Change Percent (Issue)
        lpcp = f"\nLast Price Change %: {para1.lpChange(soup)}"
        print(lpcp)

        # Last Price Change Date
        lpcd = f"\nLast Price Change Date: {para1.lpDate(soup)}"
        print(lpcd)

        # Dividend Yeild
        div = f"\nDividend Yeild: {para1.dividend(soup)}"
        print(div)

        # ROE
        roe = f"\nROE: {para1.roe(soup)}"
        print(roe)

        # ROCE
        roce = f"\nROCE: {para1.roce(soup)}"
        print(roce)

        # About Company
        ac = f"\nAbout Company: {para2.aboutCompany(soup)}"
        print(ac)

        # Company Link
        cl = f"\nCompany web: {para2.companyLink(soup)}"
        print(cl)

        # Total Assets 6Q
        assets = f"\nTotal Assets 6Q: {para2.totalAssets(soup)}"
        print(assets)

        # Net Profits 6Q
        profits = f"\nTotal Profits 6Q: {para2.netProfits(soup)}"
        print(profits)

        # PROs & CONs
        pro , con = para2.PaC(soup)
        print("\nPROs: " ,pro)
        print("\nCONs: ", con)

        # High / Low
        high , low = para2.HLValues(soup)
        print("\nHigh: " , high)
        print("\nLow: ", low)

        #Book Value
        bval = para2.bookValue(soup)
        print("\nBook Value: ", bval)

        # Key Points (NOT WORKING)
        # print(para2.keyPoints(soup))