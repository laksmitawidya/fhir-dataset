### FHIR Dataset

**Powered by : SyntheaTM or SyntheticMass**

Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079

## Reference
https://synthea.mitre.org/downloads

## Running map - reduce hadoop
```
cat observations.csv | python3 ~yourhome/fhir-dataset/mapper.py | python3 ~yourhome/fhir-dataset/reducer.py
```
