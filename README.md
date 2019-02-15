# BME547-TSH-Test-Data-Conversion
* name: WeiHsien, Lee
* assignment: TSH Test Data Conversion
* due date; 2/14/2019 23:59

## Function
This assignment is to design a code to read over patients
data and diagnose the TSH results. Which then can be used to
analyze the patient for hypothyroidism or hyperthyroidism 
and then stored to JSON output file.

## Data input
Sample input data is found in a text file called ``test_data.txt``.
 The data for a single patient is found on four lines with 
 the following format:
```
FirstName LastName
Age
Gender
TSH, result1, result2, result3, etc.
```

## Data output
JSON output files for each patient is created named 
in the format "firstName lastName.json". 

## test_dictionary
This program tests for the diagnosis and TSH
and can see the accuracy of function ``diagnose()``