import json
import requests


def number_of_species_in_country_list(scientificName, countryList, step=1000):
    """
    Count the number of species for which GBIF has occurrences in a given list of countries
    You must use the ISO country code
    Example: butterflies in Latvia and Canada
    number_of_species_in_country_list("Lepidoptera", ["LV", "CA"])
    # In 2018/10/01 returns
    5278
    """
    offset = 0
    end_of_records = False
    nb_species = 0
    base_request = "http://api.gbif.org/v1/occurrence/search?"
    base_request += "limit=0&facet=speciesKey"
    base_request += "&scientificName=" + scientificName
    base_request += "&facetLimit=" + str(step)
    for country_code in countryList:
        base_request += "&country=" + country_code
    while not end_of_records:
        response = requests.get(base_request + "&facetOffset=" + str(offset))
        if response.ok:
            response = response.json()
            nb_species_in_page = len(response["facets"][0]["counts"])
            nb_species += nb_species_in_page
            # Increment page
            offset += step
            end_of_records = (nb_species_in_page < step)
        else:
            print("ERROR", base_request)
            end_of_records = True
    return nb_species
