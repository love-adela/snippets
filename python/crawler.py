"""
* To execute this program : python crawler.py http://...
* Dependencies : pip install requests, beautifulsoup4, logbook   
"""

from collections import deque
import csv
from datetime import datetime
import hashlib
import random
import sys
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from logbook import Logger, StreamHandler
import requests


StreamHandler(sys.stdout).push_application()
log = Logger(__name__)

# TODO: 상수로 .csv 파일의 경로 설정하는 것 대신 commandline argument로 경로를 만들 것
CSV_PATH = 'pages.csv'

# TODO: (1) URL과 해당주소를 방문한 날짜를 dict로 저장하기.
# TODO: (1) visited와 queue의 내용을 파일에 저장해 두었다가 프로그램 재 실행시 기존의 내용을 다시 불러 올 수 있게 변경하기.
visited = set()
queue = deque()


def find_links(soup, url):
    parsed_url = urlparse(url)
    prefix = f'{parsed_url.scheme}://{parsed_url.netloc}'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith(prefix):
            yield href


def process_content(soup, encoding, url, fetched_at):
    # 웹페이지의 내용을 별도의 파일에 저장
    filename = get_filename(url)
    with open(filename, 'w') as fout:
        fout.write(soup.text)

    with open(CSV_PATH, 'a') as fout:
        writer = csv.writer(fout)
        formatted_dt = fetched_at.strftime('%Y-%m-%d %H:%M:%S')
        title = soup.title.text.strip()
        writer.writerow([formatted_dt, title, url, filename])


def get_filename(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest() + '.html'


def crawl(url):
    log.info(f'Fetching {url}')

    resp = requests.get(url)
    fetched_at = datetime.now()

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = find_links(soup, url)
        process_content(soup, resp.encoding, url, fetched_at)

        for link in links:
            # 어떤 경우에는 충분히 robust하지 못한 모습을 보여줍니다. 예를
            # 들어서, 다음의 두 URL을 다른 URL로 인식하기 때문에 같은
            # 페이지임에도 불구하고 두 번 방문하게 됩니다.
            #
            # https://finance.yahoo.com
            # https://finance.yahoo.com/
            #
            # 또한, 다음과 같이 의미상 같은 URL이지만, 변수의 순서가 바뀌었기
            # 때문에 다른 URL로 인식되는 문제도 가지고 있습니다.
            #
            # https://google.com/search?q=test&hl=en-us
            # https://google.com/search?hl=en-us&q=test
            #
            # TODO: 이러한 경우 같은 URL이라는 것을 인식할 수 있도록 코드를
            # 수정하기.
            if link not in visited:
                queue.append(link)
                visited.add(link)
    else:
        log.warn(f'Failed to fetch {url}')


if __name__ == '__main__':
    # TODO:command line arguments로 URL를 사용할 것. 
    # Click (https://click.palletsprojects.com) 사용 
    init_url = sys.argv[1]
    queue.append(init_url)

    while queue:
        url = queue.popleft()
        crawl(url)
        # spam bot 인식 방지 
        time.sleep(random.random() * 2)
