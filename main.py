# from extractors.wwr import extract_jobs

# pkgs.chromium
# pkgs.chromedriver

# jobs = extract_jobs("python")

# print(jobs)

# for num in range(9):
#     print(f"2 x {num+1} = {2*(num+1)}")

# from requests import get
# from bs4 import BeautifulSoup
# from extractors.wwr import extract_jobs

# base_url = "https://www.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#     print("Can't request page")
# else:
#     # print(response.text)
#     soup = BeautifulSoup(response.text, "html.parser")
#     job_list = soup.find("ul", class_="josbsearch-ResultsList")
#     jobs = job_list.find_all('li', recursive=False)
#     # print(len(jobs))
#     for job in jobs:
#         print(job)
#         print("////////")


from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
"""
# from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(options=options)
browser.get("https://www.indeed.com/jobs?q=python&limit=50")
# resonse = get("https://www.indeed.com/jobs?q=python&limit=50")
print(browser.page_source)
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)
"""
options = Options()
options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드
browser = webdriver.Chrome(options=options)
browser.get(
    'https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')

print(browser.page_source)
