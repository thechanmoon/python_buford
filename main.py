# from extractors.wwr import extract_jobs

# pkgs.chromium
# pkgs.chromedriver

# jobs = extract_jobs("python")

# print(jobs)

# for num in range(9):
#     print(f"2 x {num+1} = {2*(num+1)}")

from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_jobs

base_url = "https://www.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request page")
else:
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("ul", class_="josbsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    # print(len(jobs))
    for job in jobs:
        print(job)
        print("////////")
