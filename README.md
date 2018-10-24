# Small scripts using GBIF API

This repository contains a few scripts I wrote to use the [GBIF API](https://www.gbif.org/developer/summary) with python.

## Counts the number of species occurring in a list of countries

You can use [this function](https://github.com/ManonGros/Small-scripts-using-GBIF-API/blob/master/species_per_continent/species_in_country_list.py).

For usage, see for example: [How many butterfly species do we have per continent?](https://github.com/ManonGros/Small-scripts-using-GBIF-API/blob/master/species_per_continent/species_per_continent.ipynb)

## Counts the number of unique dataset keys and collection codes associated with  preserved specimens

See example [here](https://github.com/ManonGros/Small-scripts-using-GBIF-API/blob/master/datasets_containing_preserved_specimens/dataset_containing_preserved_specimens.ipynb)

## Look for words in the dataset description which could be associated with a dataset type

The model is not good but the script could be reused for something else.
See the notebook [here](https://github.com/ManonGros/Small-scripts-using-GBIF-API/blob/master/words_associated_with_dataset_type_naive_baysian_model/gather_dataset_descriptions_markdown.ipynb)
