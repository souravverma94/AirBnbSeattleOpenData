from model_dev.airbnb_seattle.predict_ratings.constants import PREDICTOR_COLUMN_NAME
from model_dev.airbnb_seattle.predict_ratings.model_regression_ols import model_dev_perform_regression_ols


def model_dev_create_train_test(model_data):
    # Create Training / Test splits
    from sklearn.model_selection import train_test_split

    X = model_data.drop(PREDICTOR_COLUMN_NAME, axis=1)
    y = model_data[PREDICTOR_COLUMN_NAME]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=243)

    return [X_train, X_test, y_train, y_test]


def model_dev_main(model_data):
    X_train, X_test, y_train, y_test = model_dev_create_train_test(model_data)
    model_dev_perform_regression_ols(X_train, X_test, y_train, y_test)
