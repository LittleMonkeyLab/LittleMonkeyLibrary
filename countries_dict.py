import pandas as pd

df_countries = pd.read_csv('all_items_duplicated.csv')
df_countries = df_countries[df_countries['Collection_Name']=='14 Global intelligence']
country_names = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
    "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", 'Belgium', 'Kosovo', 'Yugoslavia','Mi̇lli̇ İsti̇hbarat Teşki̇latı', 
    'Belgian','Turkish', 'Ottoman Special Organization', 'Belgian', 'British', 'Portuguese', 'Chinese', 'Greek', 'Spanish', 'French', 'Canadian', 'Czechoslovak', 'Soviet','Polish', 'KGB',
    'FSB', 'Dutch', 'German', 'Mossad', 'Norwegian', 'Ottoman', 'Italian', 'Teşkilat-ı Mahsusa', 'Tsar', 'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT',
    'Vichy Regime','Safavids','Hungarian','Austro','Swedish','Nasser','Jewish','Finnish'
]
replacements = {
    'Belgian': 'Belgium',
    'Turkish': 'Turkey',
    'British': 'United Kingdom',
    'Portuguese': 'Portugal',
    'Chinese': 'China',
    'Greek': 'Greece',
    'Spanish': 'Spain',
    'French': 'France',
    'Canadian': 'Canada',
    'Czechoslovak': 'Czechia',
    'Mi̇lli̇ İsti̇hbarat Teşki̇latı': 'Turkey',
    'Soviet': 'Russia',
    'Polish': 'Poland',
    'FSB': 'Russia',
    'Dutch': 'Netherlands',
    'German': 'Germany',
    'Germany':'Germany',
    'Mossad': 'Israel',
    'Norwegian': 'Norway',
    'Ottoman Special Organization':'Turkey',
    'Ottoman':'Turkey',
    'Italian':'Italy',
    'KGB':'Russia',
    'Teşkilat-ı Mahsusa':'Turkey',
    'Tsar':'Russia',
    'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT':'Romania',
    'Vichy Regime':'France',
    'Safavids':'Iran',
    'Hungarian':'Hungary',
    'Austro':'Austria',
    'Swedish':'Sweden',
    'Nasser':'Egypt',
    'Jewish':'Israel',
    'Finnish':'Finland'
    }

df_countries['Country'] = ''

for country in country_names:
    # Find rows where the Title column contains the country name
    mask = df_countries['Title'].str.contains(country, regex=False)
    
    # Update Country column by concatenating with '|' if multiple countries are found
    df_countries.loc[mask, 'Country'] += country + '|' if not df_countries.loc[mask, 'Country'].empty else ''

# Replace aliases with their respective country names
df_countries['Country'] = df_countries['Country'].str.rstrip('|').replace(replacements, regex=True)
df_countries = df_countries.assign(Country=df_countries['Country'].str.split('|')).explode('Country')
df_countries = df_countries.drop_duplicates(subset=['Country', 'Zotero link'])
df_countries['Country'].replace('', 'Country not known', inplace=True)

# continent_country_names = [
#     "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
#     "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
#     "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
#     "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
#     "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
#     "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
#     "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
#     "Gambia", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
#     "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
#     "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
#     "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
#     "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
#     "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia",
#     "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
#     "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
#     "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
#     "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
#     "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
#     "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
#     "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
#     "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
#     "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", 'Belgium', 'Kosovo', 'Yugoslavia','Mi̇lli̇ İsti̇hbarat Teşki̇latı', 
#     'Belgian','Turkish', 'Ottoman Special Organization', 'Belgian', 'British', 'Portuguese', 'Chinese', 'Greek', 'Spanish', 'French', 'Canadian', 'Czechoslovak', 'Soviet','Polish', 'KGB',
#     'FSB', 'Dutch', 'German', 'Mossad', 'Norwegian', 'Ottoman', 'Italian', 'Teşkilat-ı Mahsusa', 'Tsar', 'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT',
#     'Vichy Regime','Safavids','Hungarian','Austro','Swedish','Nasser','Jewish','Finnish'
# ]
# continent_replacements = {
#     'Belgian': 'Belgium',
#     'Turkish': 'Turkey',
#     'British': 'United Kingdom',
#     'Portuguese': 'Portugal',
#     'Chinese': 'China',
#     'Greek': 'Greece',
#     'Spanish': 'Spain',
#     'French': 'France',
#     'Canadian': 'Canada',
#     'Czechoslovak': 'Czechia',
#     'Mi̇lli̇ İsti̇hbarat Teşki̇latı': 'Turkey',
#     'Soviet': 'Russia',
#     'Polish': 'Poland',
#     'FSB': 'Russia',
#     'Dutch': 'Netherlands',
#     'German': 'Germany',
#     'Germany':'Germany',
#     'Mossad': 'Israel',
#     'Norwegian': 'Norway',
#     'Ottoman Special Organization':'Turkey',
#     'Ottoman':'Turkey',
#     'Italian':'Italy',
#     'KGB':'Russia',
#     'Teşkilat-ı Mahsusa':'Turkey',
#     'Tsar':'Russia',
#     'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT':'Romania',
#     'Vichy Regime':'France',
#     'Safavids':'Iran',
#     'Hungarian':'Hungary',
#     'Austro':'Austria',
#     'Swedish':'Sweden',
#     'Nasser':'Egypt',
#     'Jewish':'Israel',
#     'Finnish':'Finland'
#     }

# df_countries['Continent'] = ''

# for continent in continent_country_names:
#     mask = df_countries['Title'].str.contains(continent, regex=False)
#     df_countries.loc[mask, 'Continent'] += continent + '|' if not df_countries.loc[mask, 'Continent'].empty else ''

# df_countries['Continent'] = df_countries['Continent'].str.rstrip('|').replace(continent_replacements, regex=True)
# df_countries = df_countries.assign(Continent=df_countries['Continent'].str.split('|')).explode('Country')
# df_countries = df_countries.drop_duplicates(subset=['Continent', 'Zotero link'])
# df_countries['Continent'].replace('', 'Continent not known', inplace=True)

# continent_dict = {
#     "Afghanistan": "Asia",
#     "Albania": "Europe",
#     "Algeria": "Africa",
#     "Andorra": "Europe",
#     "Angola": "Africa",
#     "Antigua and Barbuda": "North America",
#     "Argentina": "South America",
#     "Armenia": "Asia",
#     "Australia": "Oceania",
#     "Austria": "Europe",
#     "Azerbaijan": "Asia",
#     "Bahamas": "North America",
#     "Bahrain": "Asia",
#     "Bangladesh": "Asia",
#     "Barbados": "North America",
#     "Belarus": "Europe",
#     "Belgium": "Europe",
#     "Belize": "North America",
#     "Benin": "Africa",
#     "Bhutan": "Asia",
#     "Bolivia": "South America",
#     "Bosnia and Herzegovina": "Europe",
#     "Botswana": "Africa",
#     "Brazil": "South America",
#     "Brunei": "Asia",
#     "Bulgaria": "Europe",
#     "Burkina Faso": "Africa",
#     "Burundi": "Africa",
#     "Côte d'Ivoire": "Africa",
#     "Cabo Verde": "Africa",
#     "Cambodia": "Asia",
#     "Cameroon": "Africa",
#     "Canada": "North America",
#     "Central African Republic": "Africa",
#     "Chad": "Africa",
#     "Chile": "South America",
#     "China": "Asia",
#     "Colombia": "South America",
#     "Comoros": "Africa",
#     "Congo (Congo-Brazzaville)": "Africa",
#     "Costa Rica": "North America",
#     "Croatia": "Europe",
#     "Cuba": "North America",
#     "Cyprus": "Asia",
#     "Czechia": "Europe",
#     "Democratic Republic of the Congo": "Africa",
#     "Denmark": "Europe",
#     "Djibouti": "Africa",
#     "Dominica": "North America",
#     "Dominican Republic": "North America",
#     "Ecuador": "South America",
#     "Egypt": "Africa",
#     "El Salvador": "North America",
#     "Equatorial Guinea": "Africa",
#     "Eritrea": "Africa",
#     "Estonia": "Europe",
#     "Eswatini": "Africa",
#     "Ethiopia": "Africa",
#     "Fiji": "Oceania",
#     "Finland": "Europe",
#     "France": "Europe",
#     "Gabon": "Africa",
#     "Gambia": "Africa",
#     "Georgia": "Europe",
#     "Germany": "Europe",
#     "Ghana": "Africa",
#     "Greece": "Europe",
#     "Grenada": "North America",
#     "Guatemala": "North America",
#     "Guinea": "Africa",
#     "Guinea-Bissau": "Africa",
#     "Guyana": "South America",
#     "Haiti": "North America",
#     "Holy See": "Europe",
#     "Honduras": "North America",
#     "Hungary": "Europe",
#     "Iceland": "Europe",
#     "India": "Asia",
#     "Indonesia": "Asia",
#     "Iran": "Asia",
#     "Iraq": "Asia",
#     "Ireland": "Europe",
#     "Israel": "Asia",
#     "Italy": "Europe",
#     "Jamaica": "North America",
#     "Japan": "Asia",
#     "Jordan": "Asia",
#     "Kazakhstan": "Asia",
#     "Kenya": "Africa",
#     "Kiribati": "Oceania",
#     "Kuwait": "Asia",
#     "Kyrgyzstan": "Asia",
#     "Laos": "Asia",
#     "Latvia": "Europe",
#     "Lebanon": "Asia",
#     "Lesotho": "Africa",
#     "Liberia": "Africa",
#     "Libya": "Africa",
#     "Liechtenstein": "Europe",
#     "Lithuania": "Europe",
#     "Luxembourg": "Europe",
#     "Madagascar": "Africa",
#     "Malawi": "Africa",
#     "Malaysia": "Asia",
#     "Maldives": "Asia",
#     "Mali": "Africa",
#     "Malta": "Europe",
#     "Marshall Islands": "Oceania",
#     "Mauritania": "Africa",
#     "Mauritius": "Africa",
#     "Mexico": "North America",
#     "Micronesia": "Oceania",
#     "Moldova": "Europe",
#     "Monaco": "Europe",
#     "Mongolia": "Asia",
#     "Montenegro": "Europe",
#     "Morocco": "Africa",
#     "Mozambique": "Africa",
#     "Myanmar (formerly Burma)": "Asia",
#     "Namibia": "Africa",
#     "Nauru": "Oceania",
#     "Nepal": "Asia",
#     "Netherlands": "Europe",
#     "New Zealand": "Oceania",
#     "Nicaragua": "North America",
#     "Niger": "Africa",
#     "Nigeria": "Africa",
#     "North Korea": "Asia",
#     "North Macedonia": "Europe",
#     "Norway": "Europe",
#     "Oman": "Asia",
#     "Pakistan": "Asia",
#     "Palau": "Oceania",
#     "Palestine State": "Asia",
#     "Panama": "North America",
#     "Papua New Guinea": "Oceania",
#     "Paraguay": "South America",
#     "Peru": "South America",
#     "Philippines": "Asia",
#     "Poland": "Europe",
#     "Portugal": "Europe",
#     "Qatar": "Asia",
#     "Romania": "Europe",
#     "Russia": "Asia",
#     "Rwanda": "Africa",
#     "Saint Kitts and Nevis": "North America",
#     "Saint Lucia": "North America",
#     "Saint Vincent and the Grenadines": "North America",
#     "Samoa": "Oceania",
#     "San Marino": "Europe",
#     "Sao Tome and Principe": "Africa",
#     "Saudi Arabia": "Asia",
#     "Senegal": "Africa",
#     "Serbia": "Europe",
#     "Seychelles": "Africa",
#     "Sierra Leone": "Africa",
#     "Singapore": "Asia",
#     "Slovakia": "Europe",
#     "Slovenia": "Europe",
#     "Solomon Islands": "Oceania",
#     "Somalia": "Africa",
#     "South Africa": "Africa",
#     "South Korea": "Asia",
#     "South Sudan": "Africa",
#     "Spain": "Europe",
#     "Sri Lanka": "Asia",
#     "Sudan": "Africa",
#     "Suriname": "South America",
#     "Sweden": "Europe",
#     "Switzerland": "Europe",
#     "Syria": "Asia",
#     "Tajikistan": "Asia",
#     "Tanzania": "Africa",
#     "Thailand": "Asia",
#     "Timor-Leste": "Asia",
#     "Togo": "Africa",
#     "Tonga": "Oceania",
#     "Trinidad and Tobago": "North America",
#     "Tunisia": "Africa",
#     "Turkey": "Asia",
#     "Turkmenistan": "Asia",
#     "Tuvalu": "Oceania",
#     "Uganda": "Africa",
#     "Ukraine": "Europe",
#     "United Arab Emirates": "Asia",
#     "United Kingdom": "Europe",
#     "United States of America": "North America",
#     "Uruguay": "South America",
#     "Uzbekistan": "Asia",
#     "Vanuatu": "Oceania",
#     "Venezuela": "South America",
#     "Vietnam": "Asia",
#     "Yemen": "Asia",
#     "Zambia": "Africa",
#     "Zimbabwe": "Africa",
#     'Belgium': 'Europe',
#     'Kosovo': 'Europe',
#     'Yugoslavia': 'Europe'
# }

# def get_continent(country):
#     return continent_dict.get(country, 'Unknown')

# # Create 'Continent' column using the function
# df_countries['Continent'] = df_countries['Continent'].apply(get_continent)