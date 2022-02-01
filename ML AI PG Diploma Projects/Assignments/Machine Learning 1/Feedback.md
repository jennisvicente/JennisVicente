Bike Sharing 

Data Understanding, Preparation, and EDA80/80
Feedback: 
Taken care of all the nuances regarding Data Understanding, Preparation, and EDA, good work!

Exploratory Analysis

Feedback: 
1. You checked for the correlation between the target variable and the dependent variables, as well as correlation among different dependent variables. You used, pair plots, corellation heat maps and box plots for this, well done!
2. You observed  the categorical data and its distribution, good job! 
3. You conducted a good exploratory analysis and drew great insights which you can further use in the model, keep it up! 
Data preparation - Assigning string values to categorical variables

Feedback: 
You understood that there are a few discrepancies in the data types of a few variables such as season, weathersit, weekday and month. These variables are given as numeric type and if we don't change them,  the numeric values may misindicate some order in the solution. Hence we need to assign suitable strings/categories to them. 
You did this rightly, good job. 
Data Preparation - Dummy variables/Mapped Variables

Feedback: 
Categorical variables need to be transformed before analysis.  
You have created appropriate dummy variables for all the categorical variables by either mapping them to appropriate values or by creating dummies for different categories.Good job! 
(Check out other ways to do this, such as One-Hot encoding and LabelEncoder) 
Test-train split

Feedback: 
You did random sampling correctly and the test and created  train datasets successfully. 

Feature Scaling

Feedback: 
After the test-train split, we need to scale the variables for better interpretability. But we only need the scale the numeric columns and not the dummy variables. 
1. The scaling has to be done only on the train dataset as you don't want it to learn anything from the test data. You did this perfectly and used fit_transform to scale the train data, good job! 
2. You also scaled the test data correctly, good job! 
Was this helpful to you?
Model Building and Evaluation155/155
Feedback: 
R^2 and adjusted R^2 for test and train fairly comparable for your model, well done! 

Model building overall process

Feedback: 
You applied RFE appropriately to the train data and selected the top variables suggested by it. Good job!
Also a good job in observing the adj.R-squared value before and after RFE. You can get a good idea about how dropping variables is affecting the prediction capability of your model. 
Was this helpful to you?
Model building - measuring multicollinearity

Feedback: 
A high VIF value for a feature implies that, our regression model can give significant results without that feature. You checked for VIF values and removed the features with high VIF values iteratively. 
In your final model, all the predictors have a good VIF value, well done!
Was this helpful to you?
Final model - features

Feedback: 
You dropped different features according to their p and VIF values. Your final model is simple enough with only 9 features, good job! 
You final model also performed pretty well, with good R-squared and adjusted R-squared values. 
Model Evaluation - Residual Analysis

Feedback: After building the model with selected features, you performed residual analysis. The residuals for the data are normally distributed and are hardly correlated. This proved that your model is pretty good. well done!
Was this helpful to you?
Model Evaluation - Predictions

Feedback: 
You scaled the test data appropriately using the transform on the test data. 
Also, r2_score of the test set is on par with the r2_score of the ideal solution. Good job! 
Was this helpful to you?
Model evaluation - results

Feedback: 
R^2 and adjusted R^2 for test and train fairly comparable for your model, well done! 

Coding Guidelines15/15
Feedback: 
Your indentations in the code are very helpful and detailed. You also presented insights for almost all the steps. Good job! 
You wrote a short and crisp code with optimal usage of vector operations, libraries and functions. Good job!
Coding Guidelines - Good Practices

Subjective Questions50/50
Feedback: 
You were elaborate with all the subjective questions. All the answers are correct and presented very well. Good job! 

Assignment-based Subjective Question Answers

General Subjective Question Answers
