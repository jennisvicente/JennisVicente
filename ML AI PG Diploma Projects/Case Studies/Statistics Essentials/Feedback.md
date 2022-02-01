Lending Clun

Data understanding15/15
Feedback: Good Work
Identifying and removing the redundant variables

Feedback: 
Ideal approach would be to check for the NA values from the code itself. This can be done as given below:

Identify the column where the NA values are more than 90%. 

Remove such type of column where the NA values are more than 90 %.

Identify the column where the NA value are high.

Check if these columns are necessary otherwise remove this.

Was this helpful to you?
Imputing missing values

Feedback: The objective is to identify predictors of default so that at the time of loan application, we can use those variables for approval/rejection of the loan. Now, there are broadly three types of variables - 1. those which are related to the applicant (demographic variables such as age, occupation, employment details etc.), 2. loan characteristics (amount of loan, interest rate, purpose of loan etc.) and 3. Customer behaviour variables (those which are generated after the loan is approved such as delinquent 2 years, revolving balance, next payment date etc.).
Data cleaning and Manipulation30/30
Feedback: Good Work
Was this helpful to you?
Data quality issues

Feedback: Things to be performed for Data Quality are

1.Convert date column to date type format.
2.Remove the ‘%’ sign from interest rate so that the data type can be float from object.
3.Convert other fields to relevant data types.
4.You have to convert loan status to two categories - default and non-default (1 and 0 respectively). 1 and 0 is not important but any variation of this could be accepted.
5.Extract numeric value from employment length.

It is very important to understand that while looking at the loan status, The ones marked 'current' are neither fully paid not defaulted, so you have to get rid of the current loans and does not take these into consideration. You have been awarded partially if this step is not performed.
Deriving new metrics

Feedback: A very important part of analysis is deriving new variables which can be important and can provide proper insights.
From date column you can derive the year and the month variables. Further analysis can be done on this.
Binning continuous variables

Feedback: While performing the analysis, it is very important to analyse the continuous variables. For analysing the continuous variables a very simple and good approach is to bin the variables into categories. You have to bin the continuous variables into categories like The 
Income 
Loan amount 
Installment, etc
can be Binned as Low, Medium and High.
Was this helpful to you?
Data Analysis60/60
Feedback: Good Work
Segmented Univariate Analysis

Feedback: 
A very important part of this case study is to perform the Segmented Univariate Analysis.
Segmented Univariate analysis can be performed for all these variables. 

1. Loan Purpose 

2. Grades 

3. Home ownership 

4. Year 

5. Sub-grade 

6. Verification status 

7. Interest rate 

8. Installment amount 

9 Annual inco.

Partial marks are awarded for the case where some variable are missed.


You also have to present the insights and the observations from the above Segmented Univariate Analysis.

Please follow the solution for this as this is very important in data science and you will learn a lot.
Bivariate Analysis

Feedback: Bivariate Analysis
This is the next big step for any analysis.
Here you have to relate any two variables and do the analysis.
For example comparing the default rates for each "grade" across "purpose" variable - this should be done either using plots or summary tables. Also, any two meaningful variables i.e. across which default rates varies significantly, such as grade/sub grade etc. can be chosen as the second categorical variable.
After doing the analysis correctly the interpretation has to be provided correctly.
Partial marks are provided for the case the efforts are taken for Bivariate analysis but complete insights is not provided along with proper figures.
Identifiying the top-5 important variables

Feedback: You have to Provide the analysis for the important variables which are affecting the default rates. This segment is taking care for the efforts of the code and the analysis done even if the Univariate and the Bivariate analysis is done partially and not completely for most of the combination and variables. But here you have to specifically list down the most affecting variables to the default rate. You have to provide this observation to the company you are doing analysis for. This section is important as it reflects all your work done at one single place and proper actions can be taken as a result of your analysis.
Was this helpful to you?
Presentation and Recommendations30/30
Feedback: Good Work
Was this helpful to you?
Plots

Feedback: The plots should clearly present the relevant insights and should be easy to read. The axes and important data points have to be labelled correctly. You have to include the plots for relevant analysis and include it in the presentations. Partial marks are given if less plots are included and the plots are not supporting the analysis done. 
Presentation

Feedback: The presentation you made should have a clear structure which clearly explains the results you got. The analysis you did should be explained clearly along with the insights which are taken from the analysis done.
Also make sure the conclusions are written correctly and the ppt should end with the conclusion for the assignment describing the decisions and the insights from the analysis done.
Conciseness and readability of the code15/15
Feedback: Good Work
Readability

Feedback: Done. Code is readable. Try to include more comments.
Conciseness

Feedback: Appropriate libraries and functions are used to make the code concise rather than using long, verbose code
