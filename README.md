# Big Data Analysis

## Dataset

**Dataset based on FHIR standardization**
The HL7® FHIR® (Fast Healthcare Interoperability Resources 1 ) standard defines how healthcare
information can be exchanged between different computer systems regardless of how it is stored in those
systems. It allows healthcare information, including clinical and administrative data, to be available
securely to those who have a need to access it, and to those who have the right to do so for the benefit
of a patient receiving care. The standards development organization HL7® (Health Level Seven®3
) uses a collaborative approach to develop and upgrade FHIR.
https://www.healthit.gov/sites/default/files/2019-08/ONCFHIRFSWhatIsFHIR.pdf

**Powered by : SyntheaTM or SyntheticMass**

Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079

## Reference
https://synthea.mitre.org/downloads

## How To
### Running map - reduce
```
cat observations.csv | python3 ~yourhome/fhir-dataset/mapper.py | python3 ~yourhome/fhir-dataset/reducer.py
```
