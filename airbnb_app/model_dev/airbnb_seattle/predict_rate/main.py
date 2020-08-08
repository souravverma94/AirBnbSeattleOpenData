from model_dev.airbnb_seattle.dataset.main import create_input_df
from model_dev.airbnb_seattle.predict_rate.data_prepare import *

global listings_df, reviews_df, calendar_df


def display_nan_values_percentage():
    global listings_df, reviews_df, calendar_df
    # print(f"listings_df len(listings_df) {len(listings_df)}")
    # print(f"listings_df count(listings_df)  {listings_df.count()}")

    # nan_values_percent = (len(listings_df) - listings_df.count()) / len(listings_df) * 100
    # print(f"nan_values_percent {nan_values_percent}")


def create_rate_prediction_model():
    global listings_df, reviews_df, calendar_df
    listings_df, reviews_df, calendar_df = create_input_df()

    # display_nan_values_percentage()
    listings_df, reviews_df, calendar_df = drop_nan_values_from_input_df(listings_df, reviews_df, calendar_df)
    listings_df, reviews_df, calendar_df = prepare_data_clean_data(listings_df, reviews_df, calendar_df)


if __name__ == '__main__':
    create_rate_prediction_model()
