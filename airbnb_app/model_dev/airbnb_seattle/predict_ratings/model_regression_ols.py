import statsmodels.api as sm
import numpy as np
import pandas as pd
import pickle

# https://www.theanalysisfactor.com/assessing-the-fit-of-regression-models/
from model_dev.settings import OUTPUT_MODEL_PICKLE_FILE_OLS


def model_dev_perform_regression_ols(X_train, X_test, y_train, y_test):
    # BASIC OLS REGRESSION... PUT IT ALL IN
    Xr = X_train  # Set dependent variable
    yr = y_train  # Target outcome is review_scores_rating
    Xr = sm.add_constant(Xr)  ## let's add an intercept (beta_0) to our model
    ols_model = sm.OLS(yr, Xr).fit()  ## sm.OLS(output, input)

    # Print out the statistics
    ols_model.summary()

    # Let's use the basic OLS regression from sklearn
    from sklearn.linear_model import LinearRegression
    lm = LinearRegression()
    lm_model = lm.fit(X_train, y_train)

    # What are the features that have the most weight?
    ols_coefficients = pd.DataFrame({'feature': X_train.columns, 'importance': lm.coef_})
    ols_coefficients.sort_values('importance', ascending=False)[:10]

    # Get OLS mean squared error on test dataset
    from sklearn import metrics
    ols_y_predict = lm.predict(X_test)
    ols_mse = np.sqrt(metrics.mean_squared_error(y_test, ols_y_predict))
    # ols_mse

    with open(OUTPUT_MODEL_PICKLE_FILE_OLS, 'wb') as model_saved_file:
        pickle.dump(lm_model, model_saved_file)
