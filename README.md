# 💡 Stock Data Web Scraper (NSE/BSE)  
🚀 *Scrape Real-Time Stock Details from Indian Markets*  
**Stock Data Web Scraper** is a Python-based CLI tool that fetches **financial details** of Indian stocks listed on **NSE** and **BSE** by scraping data from **screener.in**. The scraper accepts either a **single stock** or an **array of stocks** from an index, downloads the HTML, extracts required information, and outputs it in **CLI or JSON format**.

---

## 🔧 Features
- 📥 **Single Stock Scraping** — Input a stock code and get instant details  
- 📊 **Multiple Stocks (Index) Scraping** — Provide a list/array of stock codes and scrape in a loop  
- 💾 **HTML Caching** — Temporarily saves downloaded HTML for parsing  
- 🔍 **Data Extraction** — Uses BeautifulSoup to parse and retrieve required fields  
- 🖥️ **CLI Output** — Directly prints details if single stock is chosen  
- 📂 **JSON Output** — Creates a JSON file for single or multiple stocks  
- 🧹 **Auto Cleanup** — Deletes the temporary HTML file after processing  

---

## 📌 Important Note
- **Do not** delete HTML and JSONs folders.
- **Future Scope** - Create and add data in csv format.
- Ideas to implement and design are **Welcome**.  

---

## 📋 Data Scraped
The scraper currently extracts:
Company Name, Company Link, NSE code, BSE code, About, Market cap, Stock PE, ROE, ROCE, Dividend Yeild, Book value,
Last price, Last price change, Last price date, High Low value, Total assets 6Q, Net profits 6Q, PROs, CONs  

---

## 📚 Available Indices (as of *14 Aug 2025*)
- NIFTY 50 , NIFTY NEXT 50 , NIFTY 100 , NIFTY BANK  
- NIFTY IT , NIFTY FMCG , NIFTY AUTO , NIFTY METAL  
- NIFTY PHARMA , NIFTY MIDCAP SELECT , NIFTY MIDCAP 50
- NIFTY SMALLCAP 50
*(More can be added easily in `codes.py` as tuple)*  

---

## 🛠️ Tech Stack
- 🐍 **Python** — Core scripting language  
- 🍲 **BeautifulSoup4** — HTML parsing and data extraction  
- 🌐 **Requests** — For fetching HTML from the website  
- 📂 **JSON Module** — Save scraped data in structured format  
- 🧹 **OS Module** — Handle file creation and deletion  

---

## 📦 Installation
```bash
git clone https://github.com/YashD15/Stock-Info-Fetcher.git
cd Stock-Info-Fetcher
pip install -r requirements.txt
python main.py