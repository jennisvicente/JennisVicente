Investment 

Data understanding and preparation30/30
Feedback: good work
Was this helpful to you?
Identifying unique companies

Feedback: In this task you have to 
1. reported number of unique companies in rounds2 file. Ideal answer for this case is 66368.

2. correctly reported unique number of companies in companies file. Ideal answer for this case is 66368. You may come up to a number 66370 also depending on the encoding followed for reading the csv file. This is actually interesting and the explanation for this is provided  in the task 2.1. 
Converting permalinks to lower/uppercase

Feedback: In this task you have to convert the permalink column to either uppercase or to lowercase. The permalink is case insensitive and therefore to compare or to find out the unique number of permalink you have to make the case to be uniform. This is a much needed task as to list the unique number of companies and to map them uniquely in both the files.
Was this helpful to you?
Identifying the unique keys

Feedback: There have to be a unique permalink for a company. You have to perform the task before of converting the permalink column to a uniform case and then find the unique number of companies in the files given. You also have to appropriately enter the corresponding correct data in the excel file for analysis. 
Merging files

Feedback: You should use the inner join to merge the two dataframes as you have to just keep the values for which the data is present in both the dataframes. 
Cleaning and manipulating data75/75
Feedback: good work
Converting to appropriate unicode format

Feedback: There seem to be 2 extra permalinks in the rounds file which are not present in the companies file. This can be a data quality issue since if this were genuine, we have two companies whose investment round details are available but their metadata (company name, sector etc.) is not available in the companies table.

this is most likely a data quality issue we have introduced while reading the data file into python. Specifically, this is most likely caused because of encoding.

First, let's try to figure out the encoding type of this file. Then we can try specifying the encoding type at the time of reading the file. The chardet library shows the encoding type of a file.

Apparently, pandas cannot decode "cp1254" in this case. After searching a lot on stackoverflow and Google, the best conclusion that can be drawn is that this file is encoded using multiple encoding types (may be because the company_permalink column contains names of companies in various countries, and hence various languages).

you should follow this 
https://stackoverflow.com/questions/45871731/removing-special-characters-in-a-pandas-dataframe.

where you first encode and again decode.
Identify missing values

Feedback: 
We require the columns 

1.“raised_amount_usd”

2.“country_code”

3.“category_list”

For the analysis further in the complete assignment.
You have to consider the operation on NaN values in these columns to get the correct results. In this task, you atleast need to check the percentage or the number for the missing values to take the decision on the operation to be performed on this missing values for making the data uniform and accurate for analysis
Missing value imputation

Feedback: The na values in the “raised_amount_usd” should be removed as there is a huge difference between the mean and the median of this value. So assuming this value to be mean inplace of na is not appropriate in this case.
The na values in the “country_code” can either be substituted with USA or can also be removed.
The na value in the category list has to be removed to perform the merging operation with the mapping file with this dataframe based on category.
Was this helpful to you?
Sector and country analysis

Feedback: 
In this task,
1. You should correctly extract the first string before the pipe operator. This string should be extracted to perform the analysis based on the category. 

2. You should convert "category_list" column to lowercase /uppercase in both - "mapping" & "master_frame" file as you did it before while merging rounds and companies dataframe.

3. Also the code for substituting the category list column by na in place of '0', is necessary as the data is not accurate and showing 0 in place of na. This is a data quality issue and should have been taken care before the analysis.

Data Analysis105/105
Feedback: good
Funding type analysis

Feedback: In this task,You have to 
1.Correctly calculate the  average funding amount for all 4 types (venture, angel, seed, PE). Partial marks are allocated if the answer is deviating from the exact answer due to the data cleaning process performed in the earlier tasks.
2. Identifying suitable investment type - the answer should be “venture” for this case.
Country analysis

Feedback: In this task, you have to 
1. Identify the top 9 countries correctly (using total amount of funding in each country)
2. Identify the top 3 english speaking countries correctly. The answer for this should contain USA and GBR. The third country may vary depending on the data cleaning you have done.
Partial marks are allocated if the answer is deviating from the exact answer due to the data cleaning process performed in the earlier tasks.
Sector and country analysis

Feedback: In this task, you have to 
1. Have to calculate the total number of investments correctly (i.e. for 5-15 million, venture) for the top 3 countries
2. Have to calculate the total amount of investments correctly (i.e. for 5-15 million, venture) for the top 3 countries
3. Have to calculate the top three sectors in each country
4. Have to calculate the number of investments in the top three sectors for each of the three countries
5. Have to do the Calculation of highest invested company - the calculation has to be done based on the sum of investment amount in the company in the top identified sector
6. Have to do the Calculation of highest invested company - the calculation has to be done based on the sum of investment amount in the company in the second best sector
Presentation of results60/60
Feedback: good work
Plots

Feedback: The plots should clearly present the relevant insights and should be easy to read. The axes and important data points have to be labelled correctly. You have to include the plots for relevant analysis and include it in the presentations. Partial marks are given if less plots are included and the plots are not supporting the analysis done.
Presentation

Feedback: The presentation you made should have a clear structure which clearly explains the results you got. The analysis you did should be explained clearly along with the insights which are taken from the analysis done.
Also make sure the conclusions are written correctly and the ppt should end with the conclusion for the assignment describing the decisions and the insights from the analysis done.
Was this helpful to you?
Conciseness and readability of code30/30
Feedback: good work
Readability

Feedback: The code should be readable and well commented.
Try to be more descriptive in the comments above every cell of code. Regarding what you are doing in the code and for what purpose it is being done. This helps us to check your logic and we can evaluate you even if your code has a silly mistake due to which the results are going wrong.
Was this helpful to you?
Conciseness

Feedback: Appropriate libraries and functions are used to make the code concise rather than using long, verbose code
