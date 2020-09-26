import requests
import lxml.html as html

HOME_URL = 'https://larepublica.pe/'
XPATH_LINK_TO_ARTICLE = '//h4[@class="LastNewsHeadline"]/a/@href'
XPATH_TITLE = '//h1[@class="DefaultTitle"]/text()'
XPATH_RESUME = '//h2[@class="DefaultSubtitle"]/text()'
XPATH_BODY = '//section/p/text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()