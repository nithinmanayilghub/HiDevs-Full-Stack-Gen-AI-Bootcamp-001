# Housing Price Prediction Using Machine Learning Models

## Introduction
The ability to accurately predict housing prices is valuable for real estate professionals, investors, and home buyers alike. 
In this project, we'll walk through a housing price prediction project using the California housing dataset and various machine learning models. We'll focus on the machine learning model and demonstrate how to tune its hyperparameters to improve performance.
## Key Features
- Data preprocessing techniques such as handling missing values and outlier detection.
- Exploratory data analysis including correlation analysis and visualization.
- Model building using regression algorithms like Linear Regression, Random Forest, XGBoost, and more.
- Evaluation metrics such as R-squared score for model performance assessment.
- Feature importance analysis to understand the impact of different variables on housing prices.

## Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
XGBoost

The XGBoost regressor achieved the highest cross-validation R-squared score of around 0.83, outperforming other models like random forest and gradient boosting. However, its performance could be improved further through hyperparameter tuning.
We used GridSearchCV to tune the learning rate, max depth, and number of estimators for the XGBoost model. 
The best hyperparameters found were:

- learning_rate = 0.1
- max_depth = 4
- n_estimators = 1500

Implementing XGBoost with these hyperparameters resulted in an impressive R-squared score of around 0.85 on the test set!
To better understand which features were most important for the XGBoost model's predictions, we plotted the feature importance scores. This can provide valuable insights and potentially guide future feature engineering efforts.

Finally, we saved the tuned XGBoost model to a pickle file, allowing it to be easily loaded and used for housing price predictions in the future.

In summary, this project demonstrated the effectiveness of the XGBoost algorithm for housing price prediction and highlighted the importance of hyperparameter tuning to maximize a model's performance. The tuned XGBoost regressor achieved excellent results on the California housing dataset.

I hope this project has been insightful and encourages you to explore machine learning techniques like XGBoost for your own regression problems. 
