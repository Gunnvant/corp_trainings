## Python Case Study

**Task 1.a**
You have been given a dump of data from UK's crime listing. The dataset is [here](https://drive.google.com/file/d/1vJ9uU5QmmhBRttCd-2IZXu7fefJD0R99/view?usp=sharing). 

The dataset contains data pertaining to three main categories:
1. Street crimes
2. Crime outcomes
3. Stop and Search events on a highway

In the current form, the data is distributed across different csv files. For each neighborhood, there are atmost three variants, one corresponding to street crimes, one corresponding to crime outcomes and one corresponding to stop and search events.

Your task is to concatenate all the data corresponding to each category in a single file. 

At the end of this exercise you will have generated three files. One corresponding to each of the three main categories mentioned above.

In order to accomplish this task you can use the following rules:
1. Any filename that has the phrase `street.csv`, pertains to the category `Street Crimes`
2. Any filename that has the phrase `outcomes.csv`, pertains to the category `Crime Outcomes`
3. Any filename that has the phrase `stop-and-search.csv`, pertains to the category `Stop and Search`

**Task 1.b**
Once you have developed the logic to do this segregation. You now need to modularize this code.
Your task is now to create three python files:
1. utils.py: This should contain the core logic as python functions or a python class that can accomplish the segregation task
2. config.py: This should contain the path of the folder containing the raw data and the path to where aggregated files are to be written.
3. run.py: This should be the main entry point of the application, you run this file to do the aggregation task

**Task 2.a**
You have been tasked with generating a csv file out of a json datatset. The location of the dataset is [here](https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.json?accessType=DOWNLOAD)

The first thing you need to do is generate the data-dictionary from this json file. This file has a field named `meta`, embedded in this field is the detail on each column. You need to create a csv file which contains the following fields:
1. Name of the column
2. Description of the column (if available)
3. Datatype

After you have generated the data dictionary you need to put the relevant data into a tabular form (csv or a tsv file). You must keep in mind the data types while putting the data in a table. If a field is a numeric field you need to make sure that while creating a csv or a tsv file the data-type is taken care of.

**Task 2.b**
After you have developed the logic to extract data dictionary as well as putting the json data into tabular format, for the data above, you will need to do this task periodically for different json files. You now need to process [this file](https://data.ny.gov/api/views/9a8c-vfzj/rows.json?accessType=DOWNLOAD)

The task now is to modularize your code by following the project structure followed in `Task 1.a` and `Task 1.b`.

Create three files:
1. `utils.py`: This file should have the core logic of creating data dictionary and converting the json data into a table
2. `config.py`: This file will contain information on the paths of raw json and path where the data dictionary and tabular data needs to be written
3. `run.py`: This file will be the entry point of the application, you will need to run this file and it will have imports from `utils.py` and `config.py`