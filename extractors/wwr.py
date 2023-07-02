from requests import get
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
# search_term = "python"
    search_term = keyword
    option = "&button=&sort=any_time"
    response = get(f"{base_url}{search_term}{option}")
    if response.status_code != 200:
        print("Error")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.find_all('title'))
        job_sections = soup.find_all('section', class_='jobs')
        print(soup.find_all('section', class_='jobs'))
        for job_section in job_sections:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                # print(job_post)
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                # print(anchor)
                company, kind, region = anchor.find_all(
                    'span', class_="company")
                title = anchor.find('span', class_='title')
                # print(company.string, kind.string, region.string, title.string)
                job_data = {
                    'company': company.string,
                    'region': region.string,
                    'postion': title.string
                }

                results.append(job_data)
                # print("///////////////")
                # print("///////////////")
        # print(len(results))
        # print(results[0])
        # print(results[1])
        # print(results[2])
        # print(results[3])

    # for index, result in enumerate(results):
    #     print(index + 1, ' - ', result)
    return results
