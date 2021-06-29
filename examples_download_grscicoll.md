## Examples of use of GRSciColl export function

* Downloading all GRSciColl institutions: http://api.gbif.org/v1/grscicoll/institution/export
* Downloading US institutions: http://api.gbif.org/v1/grscicoll/institution/export?country=US
* Downloading Argentinian institutions: http://api.gbif.org/v1/grscicoll/institution/export?country=AR

* Downloading US Federal institutions: http://api.gbif.org/v1/grscicoll/institution/export?institutionalGovernance=FEDERAL&country=US

* Downloading all GRSciColl collections: http://api.gbif.org/v1/grscicoll/collection/export
* Downloading US collections: http://api.gbif.org/v1/grscicoll/collection/export?country=US
* Downloading collections containing exoskeletons: http://api.gbif.org/v1/grscicoll/collection/export?preservationType=BIOLOGICAL_EXOSKELETONS

## List of searchable parameters

Link to API documentation: https://www.gbif.org/developer/registry#collections

### For institutions:

* `q`
* `contact`
* `code`
* `name`
* `alternativeCode`
* `identifier`
* `identifierType`
* `machineTagNamespace`
* `machineTagName`
* `machineTagValue`
* `country`
* `active`
* `type` (possible values: https://api.gbif.org/v1/enumeration/basic/InstitutionType)
* `institutionalGovernance` (possible values: https://api.gbif.org/v1/enumeration/basic/InstitutionGovernance)
* `discipline` (can be specified more than once, possible values: https://api.gbif.org/v1/enumeration/basic/Discipline)

### For collections:

* `q`
* `institution`
* `contact`
* `code`
* `name`
* `alternativeCode`
* `identifier`
* `identifierType`
* `machineTagNamespace`
* `machineTagName`
* `machineTagValue`
* `country`
* `active`
* `contentType` (can be specified more than once, possible values: https://api.gbif.org/v1/enumeration/basic/CollectionContentType)
* `preservationType` (can be specified more than once, possible values: https://api.gbif.org/v1/enumeration/basic/PreservationType)
* `accessionStatus` (possible values: https://api.gbif.org/v1/enumeration/basic/AccessionStatus)
* `personalCollection`



