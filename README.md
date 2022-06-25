## Tugas Analisis Big Data
### Tugas 1 - Proposal
- [Dokumen proposal v1](https://docs.google.com/document/d/1TyLHWkxW7CfnFsUjsUWcYRa5SYXmfC36/edit?usp=sharing&ouid=110983556134464747544&rtpof=true&sd=true)
- [Dokumen proposal final](https://docs.google.com/document/d/1CghxdK7C4Y0aUXMg1wqTqn5G9AskP9j8L1m2F_yXrz0/edit?usp=sharing)
- [Presentasi](https://docs.google.com/presentation/d/1SNH70KXWXs1bhYvs1mVsB4lrx5eZu5fwKCQUXGV7H-U/edit#slide=id.p)

### Tugas 2 - Dataset
- Dataset merupakan data sintetis dari aplikasi synthea https://github.com/synthetichealth/synthea
- Dataset on Github : ([link](https://github.com/laksmitawidya/fhir-project))
- Dataset based on FHIR standardization
The HL7® FHIR® (Fast Healthcare Interoperability Resources 1 ) standard defines how healthcare
information can be exchanged between different computer systems regardless of how it is stored in those
systems. It allows healthcare information, including clinical and administrative data, to be available
securely to those who have a need to access it, and to those who have the right to do so for the benefit
of a patient receiving care. The standards development organization HL7® (Health Level Seven®3
) uses a collaborative approach to develop and upgrade FHIR.
https://www.healthit.gov/sites/default/files/2019-08/ONCFHIRFSWhatIsFHIR.pdf
- Powered by : SyntheaTM or SyntheticMass
Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079
- Reference
https://synthea.mitre.org/downloads

### Tugas 3 - Map Reduce
```
cat observations.csv | python3 ~yourhome/fhir-dataset/mapper.py | python3 ~yourhome/fhir-dataset/reducer.py
```
- Simulasi paradigma map-reduce yang berjalan secara pararel/terdistribusi dengan menggunakan script python sederhana
- [Script Map](https://github.com/laksmitawidya/fhir-project/blob/master/mapper.py)
- [Script Reducer](https://github.com/laksmitawidya/fhir-project/blob/master/reducer.py)

### Tugas 4 - Spark
- Implementasi Python Spark menggunakan Apache PySpark untuk klasifikasi gejala yang di alami oleh pasien pada FHIR dataset berdasarkan observasi yang dihasilkan. Ada 3 label klasifikasi, yaitu: `ambulatory`, `wellness`, `outpatient.
Library yang digunakan :
- PySparkSQL
- MLlib
- SparkML google notebook : ([link](https://github.com/laksmitawidya/fhir-project/blob/master/FHIR_PySpark_Classification.ipynb))

### Tugas 5 - SparkSQL
- Manipulasi dan query beberapa data dengan fungsi dalam PySparkSQL 
- SparkSQL google notebook ([link](https://github.com/laksmitawidya/fhir-project/blob/master/PySpark_SQL.ipynb)).

### Tugas 6 - Tugas Kelompok
- Menggabungkan tugas individu dari anggota kelompok, dengan menghasilkan model, dashboard, dan API dengan standar FHIR 
- Proposal Kelompok : ([link](https://docs.google.com/document/d/1CghxdK7C4Y0aUXMg1wqTqn5G9AskP9j8L1m2F_yXrz0/edit?usp=sharing))
- Tugas Kelompok : ([link](https://github.com/vianhandika/ABD_Project/tree/main/Kelompok))
