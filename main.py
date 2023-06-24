print("Hello Buford")
from requests import get
from bs4 import BeautifulSoup
# print("000000000000000")
base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
search_term = "python"
option = "&button=&sort=any_time"
response = get(f"{base_url}{search_term}{option}")
# print("111111")
if response.status_code != 200:
    print("Error")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.find_all('section', class_='jobs'))
    # print(response.text)
    job_sections = soup.find_all('section', class_='jobs')
    # print(len(jobs))
    # print("22222")
    for job_section in job_sections:
        job_posts = job_section.find_all('li')
        # print("???????")
        # print("original length of job_posts", len(job_posts))
        # print("???????")
        job_posts.pop(-1)
        for job_post in job_posts:
            print(job_post)
        #     print('////////////////////////')
        # print(len(job_posts))