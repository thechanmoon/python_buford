from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
search_term = "python"
option = "&button=&sort=any_time"
response = get(f"{base_url}{search_term}{option}")
if response.status_code != 200:
    print("Error")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.find_all('title'))
    job_sections = soup.find_all('section', class_='jobs')
    print(soup.find_all('section', class_='jobs'))
    # for job_section in job_sections:
    #     job_posts = job_section.find_all('li')
    #     job_posts.pop(-1)
    #     for job_post in job_posts:
    #         print(job_post)

# pkgs.chromium
# pkgs.chromedriver
