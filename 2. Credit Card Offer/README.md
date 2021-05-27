
# Credit Card Offer

![image](https://user-images.githubusercontent.com/81169091/119857268-b6609980-bf13-11eb-84e9-9d64f5d927d1.png)

This Project was completed during the mid week of the bootcamp.

## OJECTIVE:

We have a credit card dataset and we used Machine Learnings Binary Classification to find if their customers accepted the offer - yes/no

## DEFINING OUR GOALS:

- [X] Quered the data in SQL using MySql Workbench
- [X] Coded in python in Jupyter Notebook:
     - [X] we used three Machine learning Models . 
          - [X] Logistic Regression
          - [X] Randomn Forest Regressiom
          - [X] Gaussian NB 
     - [X] The dataset is highly imbalanced.
          - [X] imbalanced was dealt using SMOTE
     - [X] Wrangled the Quarterly Balances 
          - [X] added two more columns, differences of the quarters.
     - [X] Dropped columns
          - [X] Average Balances
     - [X] Binned the Household Size column using Q-cuts
    
    
## VISUALISATION OF THE DATA :
The visualisation of the data was done using tableau and you can see it [here](https://public.tableau.com/profile/prebitha.staphney.abraham#!/vizhome/Data-Mid-Bootcamp-Project-Classification2_16207571376970/0?publish=yes)

![2021-05-27 (5)](https://user-images.githubusercontent.com/81169091/119858298-a1d0d100-bf14-11eb-90cd-9548b67652cf.png)


**VALIDATION** : Comparing the Models acuracy, AOC , F1 score, Kappa

    
|Qualification               | Acuracy    | AOC/RUC | F1-Score| kappa |
| -----------                | -----------| --------| --------| ----- |
| Logistic regression        | 74.9 %     |  50 %   |   0     | 0     |
| Randomn Forest Classifier  | 94.24 %    |  50 %   |   14.6% | 1 %   |
| Gaussian NB                | 93.34 %    |  53.5 % |   12.7% | 10%   |
| **After SMOTE**            |            |         |         |       |
| Logistic regression        | 71.13 %    |  71.1 % |  72.59% | 42.2% |
| Randomn Forest Classifier  | 96.88 %    |  96.9 % |  96.82% | 93.77%|
| Gaussian NB                | 74.36 %    |  74.3 % |  76.46% | 48.66%|


**CONCLUSION**

The Randomn Forest Classifier has the best acuracy and the model will be good in prediction since it has high AUC, F1 and Kappa score 
