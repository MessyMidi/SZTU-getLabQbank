from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)

tikubh_value = input("请输入 tikubh 的值（如 1471, 1486 等）：")

url_template = f"http://10.1.20.14/redir.php?catalog_id=6&cmd=learning&tikubh={tikubh_value}&page={{}}"

driver.get(url_template.format(1))

output_file = f"题库_{tikubh_value}.txt"

with open(output_file, 'w', encoding='utf-8') as f:

    def scrape_page():
        shiti_elements = driver.find_elements(By.CSS_SELECTOR, "div.shiti-content div.shiti")
        answer_elements = driver.find_elements(By.CSS_SELECTOR, "span[style='color:#666666']")

        for shiti, answer in zip(shiti_elements, answer_elements):
            question = shiti.text
            answer_text = answer.text
            print(f"题目: {question}\n答案: {answer_text}\n")
            f.write(f"题目: {question}\n答案: {answer_text}\n\n")

    def get_total_pages():
        page_info = driver.find_element(By.CSS_SELECTOR, "div.fy").text
        total_pages = int(re.search(r'/(\d+)\s*页', page_info).group(1))
        return total_pages

    def scrape_all_pages():
        total_pages = get_total_pages()
        current_page = 1

        while current_page <= total_pages:
            print(f"正在爬取第 {current_page} 页...")
            f.write(f"第 {current_page} 页\n")
            scrape_page()
            current_page += 1
            if current_page <= total_pages:
                next_url = url_template.format(current_page)
                driver.get(next_url)
                time.sleep(2)

    scrape_all_pages()

driver.quit()

print(f"题目和答案已保存到 {output_file}")
