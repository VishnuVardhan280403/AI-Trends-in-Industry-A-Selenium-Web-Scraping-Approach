from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from IPython.display import FileLink

def research_industry_with_selenium(company_name):
    CHROMEDRIVER_PATH = "C:\\Users\\T Vishnu vardhan\\OneDrive\\Desktop\\chromedriver\\chromedriver-win64\\chromedriver.exe"

    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Open Google and perform the search
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(f"{company_name} AI adoption and market trends")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Extract search result titles and links
        search_results = []
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result in results[:10]:  # Get top 10 results
            try:
                title = result.find_element(By.TAG_NAME, "h3").text
                link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                search_results.append({"title": title, "link": link})
            except Exception as e:
                continue  # Skip if any element is missing

        return search_results
    
    finally:
        # Always close the browser after use
        driver.quit()

company_name = "Tesla"
results = research_industry_with_selenium(company_name)

for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}\n   {result['link']}")
    
output_file = "tesla_ai_research.xlsx"
df = pd.DataFrame(results)
df.to_excel(output_file, index=False)
print(f"Results saved to {output_file}")
display(FileLink(output_file))

