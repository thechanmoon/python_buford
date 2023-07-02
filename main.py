from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_page_count(keyword):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드
    browser = webdriver.Chrome(options=options)
    # browser.get('https://kr.indeed.com/jobs?q=python')
    browser.get(f'https://www.indeed.com/jobs?q={keyword}')
    # print("Can't connect")
    # browser.get('https://kr.indeed.com/jobs?q=python')
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # print("test : ", soup)
    pagenation = soup.find('nav', class_='ecydgvn0')
    if pagenation == None:
        return
    pages = pagenation.find_all("div", recursive=False)
    # print("test 1 : ", pages)
    count = len(pages)
    if count > 4:
        return 5
    else:
        return count
    # print(len(pages))


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    base_url = 'https://www.indeed.com/jobs'
    for page in range(pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드
        browser = webdriver.Chrome(options=options)
        browser.get(f'{base_url}?q={keyword}')
        # if browser.get(f'https://www.indeed.com/jobs?q={keyword}') != None:
        #     print("Can't connect")
        # else:
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)

        # print(jobs)
        results = []
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")

            if zone == None:
                # print("job li")
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_='companyName')
                loction = job.find('div', class_="companyLocation")

                job_data = {
                    'link': f'https://www.indeed.com{link}',
                    'company': company.string,
                    'loctation': loction.string,
                    'postion': title,

                }
                results.append(job_data)
                # print(title, link)
                # print("/////\n//////")
            # else:
            #     print("mosaic li")
        return results


results = extract_indeed_jobs("python")

for result in results:
    print(result, "\n/////\n")

# print(get_page_count("python"))
# print(get_page_count("java"))
# print(get_page_count("django"))
# print(get_page_count("next"))
