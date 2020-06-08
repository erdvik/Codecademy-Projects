def main():
    updated_damages = update_damages(damages)
    hurricanes = construct_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
    hurricanes_by_year = construct_dictionary_year(hurricanes)
    affected_areas_count = count_affected_areas(hurricanes)
    print(affected_areas_count)
    most_affected_area = find_most_affected_area(affected_areas_count) 
    print(most_affected_area)
    highest_death_hurricane = find_most_deaths(hurricanes)
    print(highest_death_hurricane)

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
    updated_damages = []
    for damage in damages:
        if damage != 'Damages not recorded':
            if damage[-1] == 'M':
                updated_damages.append(float(damage.strip('M'))*conversion['M'])
            if damage[-1] == 'B':
                updated_damages.append(float(damage.strip('B'))*conversion['B'])
        else:
            updated_damages.append(damage)
    return updated_damages

# write your construct hurricane dictionary function here:

def construct_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    for name in names:
        index = names.index(name)
        hurricane = {"Name": names[index],
                     "Month": months[index],
                     "Year": years[index],
                     "Max Sustained Wind": max_sustained_winds[index],
                     "Areas Affected": areas_affected[index],
                     "Damage": updated_damages[index],
                     "Deaths": deaths[index]}
        hurricanes[name] = hurricane
    return hurricanes

# write your construct hurricane by year dictionary function here:

def construct_dictionary_year(hurricanes):
    hurricanes_year = {}
    for hurricane in hurricanes:
        hur = hurricanes.get(hurricane)
        year = hur.get("Year")
        if year not in hurricanes_year:
            value_list = [hur]
            hurricanes_year[year] = value_list
        else:
            hurricanes_year[year].append(hur)
    return hurricanes_year

# write your count affected areas function here:

def count_affected_areas(hurricanes):
    areas_count = {}
    for hurricane in hurricanes.values():
        for area in hurricane.get("Areas Affected"):
            if area not in areas_count:
                areas_count[area] = 1
            else:
                areas_count[area] += 1
    return areas_count

# write your find most affected area function here:

def find_most_affected_area(affected_area_count):
     v=list(affected_area_count.values())
     k=list(affected_area_count.keys())
     count = max(v)
     area = k[v.index(count)]
     return area, count

# write your greatest number of deaths function here:

def find_most_deaths(hurricanes):
    max_death_hurricane = ""
    death_count = 0
    for hurricane in hurricanes.values():
        death_number = hurricane.get("Deaths")
        if death_number > death_count:
            max_death_hurricane = hurricane.get("Name")
            death_count = death_number
    return max_death_hurricane, death_count

# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:


if __name__== "__main__":
    main()