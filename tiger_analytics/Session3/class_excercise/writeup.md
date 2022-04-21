Use the dataset stored [here](https://drive.google.com/file/d/1WShGELaUTe_NsMvLfDl10OVQJgNgkFwg/view?usp=sharing)

Once you download the data you will end up with a zip file. You will need to unzip it and you will find that there are several csv files. These files contain the data on pollution level collected by IOT sensors. You will observe that many files have same latitude and longitude data. Your task is the following:

1. Find out how many total csv files are there?
2. Club all the files that belong to each location together. One simple way to do this is to generate a dictionary that has lat-longs as keys and files with same location as values.
3. Find out which location has the maximum number of files clubbed together. 