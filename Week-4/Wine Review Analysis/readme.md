# Housing Price Prediction with XGBoost and Hyperparameter Tuning

The ability to accurately predict housing prices is valuable for real estate professionals, investors, and home buyers alike. 
In this project, we'll walk through a housing price prediction project using the California housing dataset and various machine learning models. We'll focus on the XGBoost regressor model and demonstrate how to tune its hyperparameters to improve performance.
We started by importing the necessary libraries and loading the California housing dataset into a pandas DataFrame. After exploring the data and handling outliers, we split it into training and testing sets.
To evaluate models, we created a pipeline that included a StandardScaler and various regression algorithms like linear regression, random forest, gradient boosting, and more. We used 5-fold cross-validation to compare the models' performance on the training set.
The XGBoost regressor achieved the highest cross-validation R-squared score of around 0.83, outperforming other models like random forest and gradient boosting. However, its performance could be improved further through hyperparameter tuning.
We used GridSearchCV to tune the learning rate, max depth, and number of estimators for the XGBoost model. The best hyperparameters found were:

learning_rate = 0.1
max_depth = 4
n_estimators = 1500

Implementing XGBoost with these hyperparameters resulted in an impressive R-squared score of around 0.85 on the test set!
To better understand which features were most important for the XGBoost model's predictions, we plotted the feature importance scores. This can provide valuable insights and potentially guide future feature engineering efforts.
Finally, we saved the tuned XGBoost model to a pickle file, allowing it to be easily loaded and used for housing price predictions in the future.
In summary, this project demonstrated the effectiveness of the XGBoost algorithm for housing price prediction and highlighted the importance of hyperparameter tuning to maximize a model's performance. The tuned XGBoost regressor achieved excellent results on the California housing dataset.
I hope this project has been insightful and encourages you to explore machine learning techniques like XGBoost for your own regression problems. 
