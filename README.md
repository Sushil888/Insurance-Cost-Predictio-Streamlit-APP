## Problem Statement:
* The aim of this project is to predict the insurance premium price based on various customer health and demographic attributes. By accurately predicting premiums, insurance companies can make data-driven decisions, and customers can understand the key factors impacting their premium amounts.

## Target Metric:
* The main objective is to minimize the prediction error in estimating insurance premiums, which is evaluated using Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE) and R-squared (R²) as key metrics.

## Steps Taken to Solve the Problem:

## 1. Exploratory Data Analysis (EDA):

* Analyzed data distributions, missing values, and outliers.
* Visualized relationships between features, especially focusing on factors such as age, chronic diseases, and BMI, as they were anticipated to influence premium prices.
* Examined correlation matrices to identify potential multicollinearity among variables.

## 2. Hypothesis Testing:

* Tested various hypotheses around the relationship between health attributes and premium prices. For example, verified if conditions like diabetes and a family history of cancer significantly impact premiums.
*Conducted statistical tests to validate assumptions and understand the significance of each feature.

## 3. Machine Learning Modeling:

* Built a baseline model using linear regression and iteratively improved it with more complex algorithms like Random Forest and Gradient Boosting to capture non-linear relationships.
* Evaluated the model's performance through cross-validation to ensure robustness.
* Used feature importance from the Random Forest model to identify key predictors (e.g., age, chronic diseases) that had a strong impact on premium price predictions.

## Insights and Recommendations:

* Age and chronic health conditions were found to be the most significant factors impacting premium prices. It is recommended that these variables receive special attention in pricing strategies.
* Variables such as BMI and diabetes status also showed substantial influence, suggesting the need for targeted risk assessment in these areas.
* For future improvement, incorporating more demographic data (e.g., geographic location) and external health indicators could further refine the model’s accuracy.

## Final Scores Achieved:

* Root Mean Squared Error (RMSE): [2070.98]
* Mean Absoluter Percentage Error (MAPE): [4.32%]
* R-squared (R²): [0.90]
* These metrics indicate the model’s effectiveness in predicting premium prices accurately.

## Deployment:

* The model was deployed as a Streamlit application, allowing users to input their details and receive a premium price prediction.
* The app was built and deployed using VS Code, ensuring a user-friendly interface for real-time predictions.
