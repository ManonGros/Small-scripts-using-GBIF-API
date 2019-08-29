# coding: utf-8
import pandas as pd
import requests
import json


def match_species(species_list, # pandas table
                  nameCol="scientificName",
                  species_api="http://api.gbif.org/v1/species/match?verbose=true&name="):
    '''
    Species matching API
    This function aims to emulate the GBIF species matching tool
    on GBIF (https://www.gbif.org/tools/species-lookup).
    It takes and input file containing scientific names
    (under the column `scientificName`) and look up a match in
    the GBIF taxonomy.
    ----
    The aletrnative matches are also included in the output file (they
    are tagged in the `is_alternative`).
    ---
    The function uses the GBIF Species API (https://www.gbif.org/developer/species):
    ```
    http://api.gbif.org/v1/species/match?
    ```
    '''
    # Upload species list
    matched_species = []
    # For each name
    for species in species_list.index:
        # Replace space by %20 for API request in names
        name = species_list.loc[species, nameCol].replace(" ", "%20")
        # Find a match for the name with the API
        match = requests.get(species_api+name)
        # If the response is ok
        if match.ok:
            # Process the response
            match_result = match.json()
            match_result["inputName"] = species_list.loc[species, nameCol]
            # If the response contains alternative matches, make one line per match
            if "alternatives" in match_result:
                match_result["has_alternatives"] = True
                for alt in match_result["alternatives"]:
                    alt["inputName"] = species_list.loc[species, nameCol]
                    alt["is_alternative"] = True
                    matched_species.append(alt)  # add alternative
                match_result.pop('alternatives')
            # Strore the result
            matched_species.append(match_result)
    result = pd.DataFrame(matched_species)
    # Store taxon keys as integers
    taxon_keys = ['acceptedUsageKey', 'usageKey', 'kingdomKey', 'phylumKey','classKey', 'orderKey', 'familyKey', 'genusKey', 'speciesKey']
    result[taxon_keys] = result[taxon_keys].fillna(0).astype(int)
    # Fill NAs with NULL
    result = result.fillna("NULL")
    # Return result
    return result


def create_download_given_query(login,
                                password,
                                download_query,
                                api="http://api.gbif.org/v1/"):
    '''
    Query the download API
    '''
    headers = {'Content-Type': 'application/json'}
    download_request = requests.post(api + "occurrence/download/request",
                                     data=json.dumps(download_query),
                                     auth=(login, password),
                                     headers=headers)
    if download_request.ok:
        print("ok")
    else:
        print(download_request)
    return download_request
