import bs4
import requests

url = 'https://www.webdesignrankings.com/resources/lolcolors/'
html = requests.get(url).text

response = bs4.BeautifulSoup(html, 'html.parser')

color_codes = []

for i in range(1, 66):
    palette = response.select(f'#palette_{i}')

    color_set = []
    for color in palette:
        a = color.select('a > .droplet_1')
        a = color.select_one('path')
        color_set.append(a.get('style').split()[-1])

    color_codes.append(color_set)

color_codes = sum(color_codes, [])
print(color_codes)


# palette_65 > a:nth-child(4) > span
# palette_64 > a:nth-child(1) > span
# palette_63 > a:nth-child(1) > span
# palette_1 > a:nth-child(1) > span