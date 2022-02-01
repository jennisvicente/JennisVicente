Telecom Churn Case Study

Data understanding, preparation, and feature engineering43/43
Feedback: 
You missed several things in Data understanding, preparation, and feature engineering
Refer Bivariate EDA section in sample solution for comprehensive EDA.
Was this helpful to you?
All important data quality checks are performed and inconsistent/missing data is handled appropriately.

Feedback: You have identified the different types of variables/columns (numeric, categorical and date).  You have identified missing values in columns.  You have imputed missing values in numeric and categorical column
Filtering high-value customers

Feedback: You have filtered the high-value customers correctly by using either of columns 'total_rech_amt_', 'total_rech_data_' or 'av_rech_amt_data_'.
Tag churners

Feedback: 
You have tagged customer as a churner and non-churner based on  total call usage or total data usage of the ninth month.
You have deleted all the variables that relate to the ninth month., e.g. - total_ic_mou_9, roam_ic_mou_9
Feature engineering

Feedback: You have not derived new features, which are different from the ones that were created while filtering customers and tagging churners.
EDA and plots

Feedback: You have not done enough  univariate analysis or bivariate analysis using plots and summary tables
Modelling42/42
Feedback: You have tuned hyperparameters correctly using the functions GridSearchCV, RandomSearchCV or an equivalent technique and chosen best parameters of the model
Data sampling

Feedback: You have properly divided the data into training and testing set. 
You have not maintained the same ratio of churners in both the sets else
Preprocessing

Feedback: done
Dimensionality reduction

Feedback: You have correctly preprocessed the categorical data.  You have used PCA correctly for dimensionality reduction.  Have chosen a specific number of features from the dimensionality reduction technique
Model building

Feedback: 
You have built two or more predictive models.
You have generated synthetic features using techniques such as SMOTE to handle class imbalance. 
Was this helpful to you?
Model evaluation

Feedback: You have evaluated the models on test or validation set and reported the performance of the model using a metric other than 'accuracy' . Please look in the solution on the platform for ideal Solution
Was this helpful to you?
Identifying important churn indicators and business recommendation25/25
Feedback: good
Preprocessing

Feedback: In this task you have to 
scale(numeric variables) and create dummy variables (for categorical variables)
Partial marks are awarded if numeric variables are not scaled or dummy variabled are not created.
Model building

Feedback: In this task you have to
create a model without dimensionality reduction technique (to understannd feature importance)
Model evaluation

Feedback: In this task you have to
1. Evaluate models using appropriate metrics.
2. Do hyperparameter tuning correctly for the choice of model.

Was this helpful to you?
Identify important churn indicators

Feedback: In this task you have to
plot feature importance and select feature using a feature selection technique or using buisness domain knowledge.
Business recommendations

Feedback: In this task you have to
Provide a list of actions that needs to be taken by the business.
more than two unique actionable points should be recommended to the business based on the analysis and the model created.
Code readability and conciseness10/10
Feedback: good
Code readability

Feedback: You have written well commented code
Code readability conciseness

Feedback: You have avoided the use of 'for' loops where vector operations could be use
