#!/usr/bin/python3

# Developer : Hamdy Abou El Anein


import json
import urllib.request
import wget
import os
from easygui import *
import sys

borderlands = ""
country_languages = ""


def area():
    global areatotal

    try:
        areatotal = int(country[0]["area"])
    except:
        areatotal = "No information"
        pass


def flagdownload():
    global image_final
    filePath = "flagraw.svg"

    if os.path.exists(filePath):
        os.remove(filePath)

    filePath1 = "flag.png"

    if os.path.exists(filePath1):
        os.remove(filePath1)
    try:
        url = flaglink
        filename = wget.download(url, out="flagraw.svg")
        try:
            cmd = "magick -size 200x200 flagraw.svg flag.png"
            os.system(cmd)

        except:
            cmd = "convert  -resize 200x200 flagraw.svg flag.png"
            os.system(cmd)

        image_final = "flag.png"
    except:
        pass


def gdp():  # PIB
    global gdp_tot
    gdp_tot = ""
    try:
        urlData = (
            ("https://api.tradingeconomics.com/historical/country/")
            + str(choice_country)
            + str("/indicator/gdp?c=guest:guest&format=json")
        )
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        lang = len(country) - 1
        old_date = str(country[lang]["LastUpdate"])
        new_date = old_date[:-15]
        gdp_tot = (
            ("\nGDP - PIB : ")
            + str(country[lang]["Value"])
            + str(" billions USD")
            + str(" year ")
            + str(new_date)
        )
    except:
        gdp_tot = ("\nGDP - PIB : ") + str("No data")
        pass


def languages():
    global country_languages
    country_languages = ""
    count1 = 0
    counter = (len(lang)) - 1
    while count1 <= counter:
        urlData = ("https://restcountries.eu/rest/v2/name/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        country_languages = (
            country_languages + str(" ") + str(country[0]["languages"][count1]["name"])
        )
        count1 += 1
        # country_languages = (("\nLanguage : ")+str(country[0]["languages"][count1]["name"]))
        if count1 > counter:
            break


def short_languages():  # Language function for countries with code name only
    global country_languages
    country_languages = ""
    count1 = 0
    counter = (len(lang)) - 1
    while count1 <= counter:
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        country_languages = (
            country_languages + str(" ") + str(country["languages"][count1]["name"])
        )
        count1 += 1
        # country_languages = (("\nLanguage : ")+str(country[0]["languages"][count1]["name"]))
        if count1 > counter:
            break


def bord_countries():
    global borderlands, bordertotal
    borderlands = ""
    if len(bord) > 0:
        try:
            count = 0
            counter = (len(bord)) - 1

            while count <= counter:
                urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(bord[count])
                webURL = urllib.request.urlopen(urlData)
                data = webURL.read()
                encoding = webURL.info().get_content_charset("utf-8")
                country_bord = json.loads(data.decode(encoding))
                country_name = country_bord["name"]
                count = count + 1
                borderlands = borderlands + str(" ") + str(country_name)
                if count > counter:
                    break
        except:
            print("Border-error")
            pass
    else:
        borderlands = "No border"


def getdata():
    global bord, lang, unaccent_nation, flaglink, country
    if choice_country == "KOR":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "iot":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "ind":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "maf":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "PSE":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "ZAF":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    elif choice_country == "VIR":
        urlData = ("https://restcountries.eu/rest/v2/alpha/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country["flag"]
        bord = country["borders"]
        lang = country["languages"]
        gdp()
        bord_countries()
        short_languages()
        flagdownload()
        area()

        msg = (
            str(("\nCountry : ") + (country["name"]))
            + str(("\nRegion : ") + (country["region"]))
            + str(("\nSubregion : ") + (country["subregion"]))
            + str(("\nInternet domain : ") + (country["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country["callingCodes"][0]))
            + str(("\nCapital : ") + (country["capital"]))
            + str(("\nPopulation : ") + str(country["population"]))
            + str(("\nTimezone : ") + (country["timezones"][0]))
            + str(("\nCurrencies : ") + (country["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + str((gdp_tot) + str("\nBorders : ") + (borderlands))
            + str(("\nLanguages : ") + str(country_languages))
        )

        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)
    else:

        urlData = ("https://restcountries.eu/rest/v2/name/") + str(choice_country)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset("utf-8")
        country = json.loads(data.decode(encoding))
        flaglink = country[0]["flag"]
        bord = country[0]["borders"]
        lang = country[0]["languages"]
        gdp()
        bord_countries()
        languages()
        flagdownload()
        area()
        msg = (
            str(("\nCountry : ") + (country[0]["name"]))
            + str(("\nRegion : ") + (country[0]["region"]))
            + str(("\nSubregion : ") + (country[0]["subregion"]))
            + str(("\nInternet domain : ") + (country[0]["topLevelDomain"][0]))
            + str(("\nCalling code : ") + (country[0]["callingCodes"][0]))
            + str(("\nCapital : ") + (country[0]["capital"]))
            + str(("\nPopulation : ") + str(country[0]["population"]))
            + str(("\nTimezone : ") + (country[0]["timezones"][0]))
            + str(("\nCurrencies : ") + (country[0]["currencies"][0]["name"]))
            + str(("\nArea : ") + str(areatotal) + str(" Km2"))
            + (gdp_tot)
            + str("\nBorders : ")
            + (borderlands)
            + str("\nLanguages : ")
            + str(country_languages)
        )
        choices = ["Retry", "Quit"]
        reply = buttonbox(msg, image=image_final, choices=choices)
        if reply == "Retry":
            SelectCountry()
        elif reply == "Quit":
            sys.exit(0)
        else:
            sys.exit(0)


def SelectCountry():
    global choice_country
    choice_country = None
    country_list = [
        "Afghanistan",
        "Åland Islands",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antarctica",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "The Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island",
        "Brazil",
        "British Indian Ocean Territory",
        "Brunei",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cape Verde Cabo Verde",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Christmas Island",
        "Cocos (Keeling) Islands",
        "Colombia",
        "Comoros",
        "Republic of the Congo",
        "Cook Islands",
        "Costa Rica",
        "Ivory Coast Côte d'Ivoire",
        "Croatia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czech Republic Czechia",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Eswatini",
        "Ethiopia",
        "Falkland Islands",
        "Faroe Islands",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "French Southern and Antarctic Lands French Southern Territories",
        "Gabon",
        "The Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Heard Island and McDonald Islands",
        "Vatican City Holy See",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran (Islamic Republic of)",
        "Iraq",
        "Republic of Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "North Korea Korea (Democratic People's Republic of)",
        "South Korea",
        "Kuwait",
        "Kyrgyzstan",
        "Laos Lao People's Democratic Republic",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macau Macao",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Mayotte",
        "Mexico",
        "Federated States of Micronesia",
        "Moldova, Republic of",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Niue",
        "Norfolk Island Norfolk Island",
        "Republic of Macedonia North Macedonia",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn Islands",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Réunion",
        "Romania",
        "Russia",
        "Rwanda",
        "Saint Barthélemy",
        "Saint Helena, Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Collectivity of Saint Martin (French part)",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "São Tomé and Príncipe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Svalbard and Jan Mayen",
        "Sweden",
        "Switzerland",
        "Syria Syrian Arab Republic",
        "Taiwan",
        "Tajikistan",
        "Tanzania",
        "Thailand",
        "East Timor Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom United Kingdom of Great Britain and Northern Ireland",
        "United States United States of America",
        "United States Minor Outlying Islands",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela",
        "Vietnam",
        "British Virgin Islands Virgin Islands",
        "United States Virgin Islands",
        "Wallis and Futuna",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    ]

    msg = "Choose a country"
    title = "Choose a country"
    choices = country_list
    choice_country = choicebox(msg, title, choices)

    if choice_country == "Bouvet Island":
        choice_country = "bouvet"
    elif choice_country == "Burkina Faso":
        choice_country = "burkina"
    elif choice_country == "Cape Verde Cabo Verde":
        choice_country = "verde"
    elif choice_country == "Cayman Islands":
        choice_country = "cayman"
    elif choice_country == "Central African Republic":
        choice_country = "african"
    elif choice_country == "Christmas Island":
        choice_country = "christmas"
    elif choice_country == "Cocos (Keeling) Islands":
        choice_country = "cocos"
    elif choice_country == "Republic of the Congo":
        choice_country = "congo"
    elif choice_country == "Cook Islands":
        choice_country = "cook"
    elif choice_country == "Costa Rica":
        choice_country = "rica"
    elif choice_country == "Ivory Coast Côte d'Ivoire":
        choice_country = "ivory"
    elif choice_country == "Curaçao":
        choice_country = "curacao"
    elif choice_country == "Czech Republic Czechia":
        choice_country = "czech"
    elif choice_country == "Dominican Republic":
        choice_country = "dominican"
    elif choice_country == "El Salvador":
        choice_country = "salvador"
    elif choice_country == "Equatorial Guinea":
        choice_country = "guinea"
    elif choice_country == "Falkland Islands":
        choice_country = "falkland"
    elif choice_country == "Faroe Islands":
        choice_country = "faroe"
    elif choice_country == "French Guiana":
        choice_country = "guiana"
    elif choice_country == "French Polynesia":
        choice_country = "polynesia"
    elif (
        choice_country
        == "French Southern and Antarctic Lands French Southern Territories"
    ):
        choice_country = "southern"
    elif choice_country == "The Gambia":
        choice_country = "gambia"
    elif choice_country == "Guinea-Bissau":
        choice_country = "bissau"
    elif choice_country == "Heard Island and McDonald Islands":
        choice_country = "mcdonald"
    elif choice_country == "Vatican City Holy See":
        choice_country = "vatican"
    elif choice_country == "Hong Kong":
        choice_country = "hong"
    elif choice_country == "Iran (Islamic Republic of)":
        choice_country = "iran"
    elif choice_country == "Republic of Ireland":
        choice_country = "ireland"
    elif choice_country == "Isle of Man":
        choice_country = "isle"
    elif choice_country == "North Korea Korea (Democratic People's Republic of)":
        choice_country = "korea"
    elif choice_country == "South Korea":
        choice_country = "KOR"  # Short country code
    elif choice_country == "Laos Lao People's Democratic Republic":
        choice_country = "laos"
    elif choice_country == "Macau Macao":
        choice_country = "macau"
    elif choice_country == "Marshall Islands":
        choice_country = "marshall"
    elif choice_country == "Federated States of Micronesia":
        choice_country = "micronesia"
    elif choice_country == "Moldova, Republic of":
        choice_country = "moldova"
    elif choice_country == "New Caledonia":
        choice_country = "caledonia"
    elif country_list == "New Zealand":
        choice_country = "zealand"
    elif choice_country == "Norfolk Island Norfolk Island":
        choice_country = "norfolk"
    elif choice_country == "Republic of Macedonia North Macedonia":
        choice_country = "macedonia"
    elif choice_country == "Northern Mariana Islands":
        choice_country = "mariana"
    elif choice_country == "Papua New Guinea":
        choice_country = "papua"
    elif choice_country == "Pitcairn Islands":
        choice_country = "pitcairn"
    elif choice_country == "Puerto Rico":
        choice_country = "puerto"
    elif choice_country == "Réunion":
        choice_country = "reunion"
    elif choice_country == "Saint Barthélemy":
        choice_country = "barthelemy"
    elif choice_country == "Saint Helena, Ascension and Tristan da Cunha":
        choice_country = "cunha"
    elif choice_country == "Saint Kitts and Nevis":
        choice_country = "nevis"
    elif choice_country == "Saint Lucia":
        choice_country = "lucia"
    elif choice_country == "Collectivity of Saint Martin (French part)":
        choice_country = "maf"
    elif choice_country == "Saint Pierre and Miquelon":
        choice_country = "miquelon"
    elif choice_country == "Saint Vincent and the Grenadines":
        choice_country = "grenadines"
    elif choice_country == "San Marino":
        choice_country = "marino"
    elif choice_country == "São Tomé and Príncipe":
        choice_country = "sao"
    elif choice_country == "Saudi Arabia":
        choice_country = "saudi"
    elif choice_country == "Sierra Leone":
        choice_country = "sierra"
    elif choice_country == "Sint Maarten (Dutch part)":
        choice_country = "maarten"
    elif choice_country == "Solomon Islands":
        choice_country = "solomon"
    elif choice_country == "South Africa":
        choice_country = "ZAF"  # Short country code
    elif choice_country == "South Georgia and the South Sandwich Islands":
        choice_country = "sandwich"
    elif choice_country == "South Sudan":
        choice_country = "sudan"
    elif choice_country == "Sri Lanka":
        choice_country = "lanka"
    elif choice_country == "Svalbard and Jan Mayen":
        choice_country = "svalbard"
    elif choice_country == "Syria Syrian Arab Republic":
        choice_country = "syria"
    elif choice_country == "East Timor Timor-Leste":
        choice_country = "timor"
    elif choice_country == "Trinidad and Tobago":
        choice_country = "trinidad"
    elif choice_country == "Turks and Caicos Islands":
        choice_country = "turks"
    elif choice_country == "United Arab Emirates":
        choice_country = "emirates"
    elif (
        choice_country
        == "United Kingdom United Kingdom of Great Britain and Northern Ireland"
    ):
        choice_country = "kingdom"
    elif choice_country == "United States United States of America":
        choice_country = "usa"
    elif choice_country == "United States Minor Outlying Islands":
        choice_country = "minor"
    elif choice_country == "British Virgin Islands Virgin Islands":
        choice_country = "virgin"
    elif choice_country == "United States Virgin Islands":
        choice_country = "VIR"  # Short country code
    elif choice_country == "Wallis and Futuna":
        choice_country = "wallis"
    elif choice_country == "Åland Islands":
        choice_country = "Aland"
    elif choice_country == "Palestine":
        choice_country = "PSE"
    elif choice_country == "Bosnia and Herzegovina":
        choice_country = "bosnia"
    elif choice_country == "India":
        choice_country = "ind"
    elif choice_country == "British Indian Ocean Territory":
        choice_country == "iot"
    elif choice_country == None:
        sys.exit(0)
    getdata()


SelectCountry()
