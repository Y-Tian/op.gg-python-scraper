#import libraries
import sys
import urllib2
from bs4 import BeautifulSoup

matchup_stat = []
skill_order = []
rune_page = []

print "Running champion statistics database..."

def get_tier(soup):
    champ_tier = soup.find('div', attrs={'class':'champion-stats-header-info__tier'})
    tier = champ_tier.text.strip()
    return tier

def get_matchup(soup):
    for get_champ in soup.find_all('td', attrs={'class':'champion-stats-header-matchup__table__champion'}):
        get_champ_stripped = get_champ.text.strip()
        matchup_stat.append(get_champ_stripped)
    count = 0
    for get_winrate in soup.find_all('td', attrs={'class':'champion-stats-header-matchup__table__winrate'}):
        get_winrate_stripped = get_winrate.text.strip()
        matchup_stat.insert(count, get_winrate_stripped)
        count = count + 2
    matchup_stat.reverse()

def get_skill_tree(soup):
    count = 0
    while count < 3:
        skill_name = soup('li', attrs={'class':'champion-stats__list__item tip'})[count].span
        skill_name_stripped = skill_name.text.strip()
        skill_order.append(skill_name_stripped)
        count = count + 1
    skill_order.reverse()

def get_rune_page(soup):
    for element in soup.find_all('div', attrs={'class':'perk-page__item perk-page__item--keystone perk-page__item--active'}):
        for stat in element.find_all("img"):
            rune_page.append(stat['alt'])
        break

    #apparently broken html on op.gg is causing this to return null
    #print soup.find_all('div', attrs={'class':'perk-page__item  perk-page__item--active'})
    #print soup.findAll('perk-page__item  perk-page__item--active')
    #for element in soup.find_all('div', attrs={'class':'perk-page__item  perk-page__item--active'}):
    #    for stat in element.find_all("img"):
    #        rune_page.append(stat['alt'])

def print_stats(tier):
    #print champion tier
    print tier
    #print matchups
    count = 0
    print "Top 3 counter picks:"
    while count < 3:
        print matchup_stat.pop(), matchup_stat.pop()
        count = count + 1
    print "Top 3 strong against:"
    while count < 6:
        print matchup_stat.pop(), matchup_stat.pop()
        count = count + 1
    #print skill build order
    print "Preferred skill build order:", skill_order.pop(), "->", skill_order.pop(), "->", skill_order.pop()
    #print keystone
    print "Preferred keystone:", rune_page.pop()

while True:
    input_name = raw_input("Please enter champion name or type 'exit': ")
    if input_name == 'exit':
        exit()

    quote_page = 'http://na.op.gg/champion/' + input_name + '/statistics'
    print "Fetching from:", quote_page

    page = urllib2.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')
    
    get_matchup(soup)
    get_skill_tree(soup)
    get_rune_page(soup)
    print_stats(get_tier(soup))

    
    
