# Wine Review Analysis: Exploring Machine Learning for Quality Prediction

## Introduction
This project aims to predict wine quality based on various chemical properties using machine learning techniques. By leveraging data analysis and algorithms, we uncover valuable insights and build predictive models to aid wine enthusiasts, producers, and connoisseurs.

## Data Exploration and Preprocessing

### Handling Imbalanced Data
The dataset exhibited imbalanced class distributions for wine quality ratings. We addressed this issue by employing upsampling techniques, specifically random oversampling, to balance the classes.
### Outlier Detection and Treatment
We devoted significant effort to identifying and handling outliers in the dataset. Techniques such as visualizations (boxplots, histograms), interquartile range calculations, Z-score transformationswere employed to detect and mitigate the influence of extreme values.
### Feature Scaling
Standard scaling was applied to normalize the data, and Principal Component Analysis (PCA) was conducted to reduce the dimensionality while retaining essential information. We determined that eight principal components could capture over 95% of the variation in the original data.
### Correlation Analysis and Feature Selection
Correlation analysis revealed strong correlations among certain features, such as fixed acidity and citric acid, fixed acidity and density, and free sulfur dioxide and total sulfur dioxide. Based on these insights, we performed feature selection, retaining the most informative features for our predictive models.
### Model Building and Evaluation
#### Support Vector Machines (SVMs)
We explored Support Vector Machines (SVMs) for classification, achieving a weighted average of 83.3% on the original dataset and 81.8% on the PCA-transformed data.
#### Random Forest Classifier
The Random Forest Classifier demonstrated excellent performance and provided valuable insights into feature importance. By fine-tuning our feature selection process based on highly correlated variables, we achieved an impressive  weighted average of 96%.
#### Model Comparison and Selection
After evaluating multiple models using classification reports (precision, recall, and F1-score), the Random Forest Classifier emerged as the best-performing model, exhibiting high scores across all metrics.
Conclusion
This project successfully developed highly accurate predictive models for wine quality prediction based on chemical properties. The Random Forest Classifier stood out as the top-performing model, achieving an impressive accuracy of 96%.
These findings contribute to our understanding of the factors influencing wine quality and pave the way for practical applications in the wine industry, benefiting producers and connoisseurs alike.
Usage
To run this project, follow these steps:

## Clone the repository: 
```git clone https://github.com/your-repo/wine-review-analysis.git```
Install the required dependencies: 
```pip install -r requirements.txt```
## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
