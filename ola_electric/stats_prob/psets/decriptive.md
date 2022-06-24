Use the dataset [here](../../predictive_modelling/data/dataTrain_carListings.csv). 
This dataset contains the prices of different car models and brands. Answer the questions raised below:

1. Find out the average prices and the some measure of variability of car prices across brands.
2. Do the same exercise with mileage.

Now based on 1. can you come up with some rules to price the cars based on their brand?
Try doing it for the mileage. Do you think there is some trend?

Without computing the skewness in the car-prices can you guess what will be the nature of the skewness? Positive, negative?

Compute the skewness [`pandas.DataFrame.skew()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html). Also find skewness by brand. Did your intuition match the result so computed?