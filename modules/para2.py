# About Company
def aboutCompany(soup):
    try:
        # Locate the div with class 'company-info'
        company_info = soup.find("div", class_="company-info")
        if not company_info:
            return ""
        # Inside that, locate the 'about' div with paragraph <p>
        about_div = company_info.find("div", class_="about")
        if not about_div:
            return ""
        about_paragraph = about_div.find("p")
        if not about_paragraph:
            return ""
        # Extract plain text, ignoring <sup>, <a>, etc.
        for tag in about_paragraph.find_all(["sup", "a"]):
            tag.decompose()  # Remove references/links
        about_text = about_paragraph.get_text(strip=True)
        return about_text
    except Exception as e:
        print(f"Error: {e}")
        return ""
    
# Company Link
def companyLink(soup):
    try:
        # Locate the correct container
        container = soup.find("div", class_="company-links show-from-tablet-landscape")
        # Find all anchor tags
        links = container.find_all("a", href=True)
        website_url = ""
        for link in links:
            href = link["href"]
            text_parts = list(link.stripped_strings)
            # First external website (not bse/nse)
            if "http" in href and "bseindia.com" not in href and "nseindia.com" not in href:
                website_url = href.strip()
        return website_url
    except Exception as e:
        print(f"Error extracting company links info: {e}")
        return None
    
# Key Points (NOT WORKING)
def keyPoints(soup):
    # Locate the 'Key Points' title div
    key_points_heading = soup.find("div", class_="title", string="Key Points")
    if not key_points_heading:
        return []

    # The actual content is in the next sibling div with specific class
    key_points_container = key_points_heading.find_next_sibling("div", class_="sub commentary")
    if not key_points_container:
        return []

    # Clean the content by removing superscripts and anchor links
    for tag in key_points_container.find_all(["sup", "a"]):
        tag.decompose()

    # Replace <br> with newlines
    for br in key_points_container.find_all("br"):
        br.replace_with("\n")

    # Get the final cleaned text
    text = key_points_container.get_text(separator="\n", strip=True)

    # Split into list lines and clean
    points = [line.strip() for line in text.split("\n") if line.strip()]
    return points

    
# Total Assets 6Q
def totalAssets(soup):
    try:
        # Step 1: Find the "Balance Sheet" heading
        heading = soup.find("h2", string="Balance Sheet")
        if not heading:
            return []
        # Step 2: Find the next table after heading (within the same section)
        balance_sheet_section = heading.find_parent("div").find_next("table", class_="data-table")
        if not balance_sheet_section:
            return []
        # Step 3: Extract headings (years)
        heading_row = balance_sheet_section.find("thead").find("tr")
        headings = heading_row.find_all("th")[1:]  # Skip first <th> (it's label)
        year_labels = [th.get_text(strip=True) for th in headings]
        # Step 4: Extract the Total Assets row
        rows = balance_sheet_section.find_all("tr")
        total_assets_row = None
        for row in rows:
            first_cell = row.find("td", class_="text")
            if first_cell and "Total Assets" in first_cell.text:
                total_assets_row = row
                break
        if not total_assets_row:
            return []
        # Step 5: Extract the values of Total Assets
        asset_cells = total_assets_row.find_all("td")[1:]  # Skip label
        asset_values = [td.get_text(strip=True).replace(",", "") for td in asset_cells]
        # Step 6: Return last 6 (year, value) pairs
        last_6 = list(zip(year_labels[-6:], asset_values[-6:]))
        return last_6
    except Exception as e:
        print(f"Error: {e}")
        return []
    
# Net Profits 6Q
def netProfits(soup):
    try:
        # Step 1: Locate the result table
        result_table = soup.find("table", class_="data-table")
        if not result_table:
            return []
        # Step 2: Extract headings (quarter labels) from the <thead>
        heading_row = result_table.find("thead").find("tr")
        headings = heading_row.find_all("th")[1:]  # Skip the first empty <th>
        quarter_labels = [th.get_text(strip=True) for th in headings]
        # Step 3: Find the row with "Net Profit"
        net_profit_row = None
        rows = result_table.find_all("tr")
        for row in rows:
            first_cell = row.find("td", class_="text")
            if first_cell and "Net Profit" in first_cell.text:
                net_profit_row = row
                break
        if not net_profit_row:
            return []
        # Step 4: Extract all Net Profit <td> values (skip first <td>)
        cells = net_profit_row.find_all("td")[1:]
        net_profit_values = [td.get_text(strip=True).replace(",", "") for td in cells]
        # Step 5: Combine last 6 quarters and values as (quarter, value) tuples
        last_6 = list(zip(quarter_labels[-6:], net_profit_values[-6:]))
        return last_6
    except Exception as e:
        print(f"Error extracting data: {e}")
        return []
    
# PROs & CONs
def PaC(soup):
    try:
        analysis_section = soup.find("section", id="analysis")
        pros_list = []
        cons_list = []
        if analysis_section:
            # Extract Pros
            pros_ul = analysis_section.find("div", class_="pros").find("ul")
            if pros_ul:
                pros_list = [li.get_text(strip=True) for li in pros_ul.find_all("li")]
            # Extract Cons
            cons_ul = analysis_section.find("div", class_="cons").find("ul")
            if cons_ul:
                cons_list = [li.get_text(strip=True) for li in cons_ul.find_all("li")]
        return pros_list, cons_list
    except Exception as e:
        print(f"Error extracting pros and cons: {e}")
        return [], []