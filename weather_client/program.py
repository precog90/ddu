import requests
import bs4

def main():
    # print the header
    print_header("WEATHER APP")
    # get city from user
    city = input("What city you want the weather for? ")
    # get html from web
    html = get_html_from_web(city)
    # parse the html
    get_weather_from_html(html)
    # display for the forecast


def print_header(banner_name):
    print()
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()


def get_html_from_web(city):
    url = 'https://www.wunderground.com/weather/ca/{}'.format(city)
    response = requests.get(url)
    return response
    #print(response.status_code)
    #print(response.text[0:200])


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    print(soup)


if __name__ == '__main__':
    main()