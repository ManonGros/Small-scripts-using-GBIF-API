import json
import requests


def number_of_collection_with_preserved_specimen(step=1000):
    """
    Count the number of collections for which GBIF has occurrences of preserved specimens
    """
    return number_of_facet_with_preserved_specimen("collectionCode", step)


def number_of_dataset_with_preserved_specimen(step=1000):
    """
    Count the number of dataset for which GBIF has occurrences of preserved specimens
    """
    return number_of_facet_with_preserved_specimen("datasetKey", step)


def number_of_facet_with_preserved_specimen(facet, step=1000):
    """
    Count the number of dataset or collections for which GBIF has occurrences of preserved specimens
    """
    offset = 0
    end_of_records = False
    nb_facet = 0
    base_request = "http://api.gbif.org/v1/occurrence/search?"
    base_request += "limit=0&facet=" + facet
    base_request += "&basis_of_record=PRESERVED_SPECIMEN"
    base_request += "&facetLimit=" + str(step)
    while not end_of_records:
        response = requests.get(base_request + "&facetOffset=" + str(offset))
        if response.ok:
            response = response.json()
            nb_facet_in_page = len(response["facets"][0]["counts"])
            nb_facet += nb_facet_in_page
            # Increment page
            offset += step
            end_of_records = (nb_facet_in_page < step)
        else:
            print("ERROR", base_request + "&facetOffset=" + str(offset))
            end_of_records = True
    return nb_facet
