# gp-practice-import

This python script is designed to take a source of data for GPs and GP practices, and transform that data into a different format, acceptable for an NHSS application to import. 

## Description

Details on GPs and GP practices in Scotland are publicly available on the Public Health Scotland Website
https://publichealthscotland.scot/services/national-reference-files/standard-files/

There are 2 relevant files here for this script

* Practices (gpprac) - https://publichealthscotland.scot/media/dataref/gpprac
* GPs (gpref) - https://publichealthscotland.scot/media/dataref/gpref

These are flat, text-based files with a specific layout. Each line of the file represents a single Practice or GP. And each line contains details about that Practice or GP such as name and unique code. Public Health Scotland also include details on the layout of the file so it can be understood.

* Practice - https://publichealthscotland.scot/services/national-reference-files/smr-reference-file-layouts/scottish-gp-practices/
* GPs - https://publichealthscotland.scot/services/national-reference-files/smr-reference-file-layouts/scottish-gp-details/

These files are not in a format acceptable for our application to import. We need to remove some extranous details and convert the data to a CSV format to be compliant with our application. This script will automate that conversion process.

## Prerequisites

You must have python v3 installed on you machine to run this script. The home for downloading Python onto your machine can be found here https://www.python.org/downloads/

And numerous guides for installation can be found online

## Instructions on running script

First download the 2 files (gpprac and gpref) onto your local machine and save them into the `input` folder in this directory. They must be called gpprac and gpref without any file extensions.

Then from the root directory of this repository run the python script in a terminal with this command

`python3 index.py`

## Output

Running the script should output 2 files into the output folder, relative to the 2 input files - `gpprac.csv` and `gpref.csv`.

These should include the following columns

### gpprac.csv

* code - the code of the practice
* address1 - The first line of the address of the practice
* address2 - The second line of the address of the practice
* address3 - The third line of the address of the practice
* address4 - The fourth line of the address of the practice
* postcode - The postcode of the address of the practice
* is_active - Whether the practice is still active or not. This is derived from the `Practice end date` in the input file. If the end date doesn't exist then the practice is deemed active
* telephone - The telephone number of the practice. The application will not accept strings for a phone number so we must remove any instances of strings (e.g. "NOT KNOWN") and replace it with a placeholder number ("11111 111111")

### gpref.csv

* first_name - The forename of the GP
* last_name - The surname of the GP
* telephone - The telephone number of the GP. This is a required field for the application, but it does not exist in the input file. To work around this, every GP belongs to a practice (see the `Practice code` field in the gpref layout file). So we use the Practice code to "look up" the practice details in the _gpprac_ file and use the GP's associated practice phone number for the GP's phone number.
