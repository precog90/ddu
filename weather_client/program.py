import requests
import bs4
import collections

report = collections.namedtuple('report', ['city', 'condition', 'temp'])

def main():
    # print the header
    print_header("WEATHER APP")
    # get city from user
    city = input("What city you want the weather for? ")
    # get html from web
    html = get_html_from_web(city)
    # parse the html
    weather_report = get_weather_from_html(html)

    print("Forecast in {} is {} and {}".format(
        weather_report.city,
        weather_report.condition,
        weather_report.temp
    ))
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
    #weather_information = {'city': 'columns small-12', 'condition': 'condition-icon small-6 medium-12 columns', 'temp': 'current-temp', 'feels_like': 'feels-like'}
    city = soup.find('h1').text.rstrip()
    condition_data = soup.findAll('div', attrs={'class': 'condition-icon small-6 medium-12 columns'})
    units = (soup.find('span', attrs={'class': 'wu-label'})).text.strip()
    temp = (soup.find('span', attrs={'class': 'wu-value wu-value-to'})).text + units
    for x in condition_data:
        condition = x.find('p').text
    #print(city)
    #print(condition)
    #print(temp)
    #print(units)
    #for city in city_data:
     #   city = city.text
      #  print(city)
        #data = soup.findAll('div', attrs={'class': 'condition-icon small-6 medium-12 columns'})
        #print(data)
        #for x in data:
        #    print(x.find('p').text)
         #   print()
    weather_report = report(city, condition, temp)
    return weather_report



if __name__ == '__main__':
    main()