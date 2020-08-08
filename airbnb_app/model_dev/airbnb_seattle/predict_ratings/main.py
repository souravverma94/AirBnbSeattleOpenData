from model_dev.airbnb_seattle.dataset.main import create_input_df
from model_dev.airbnb_seattle.predict_ratings.data_prep import *
from model_dev.airbnb_seattle.predict_ratings.data_prep_listings import data_prep_listings_df
from model_dev.airbnb_seattle.predict_ratings.model_main import model_dev_main

global listings_df, reviews_df, calendar_df


def display_nan_values_percentage():
    global listings_df, reviews_df, calendar_df
    # print(f"listings_df len(listings_df) {len(listings_df)}")
    # print(f"listings_df count(listings_df)  {listings_df.count()}")

    # nan_values_percent = (len(listings_df) - listings_df.count()) / len(listings_df) * 100
    # print(f"nan_values_percent {nan_values_percent}")

    return


def data_prep_remove_records_without_predictor_variable(listings_df):
    listings_df = listings_df[listings_df['review_scores_rating'].isnull() == 0]
    return listings_df


def data_prep_remove_all_ratings(listings_df):
    # Remove all ratings but our overall review_scores_rating outcome
    print(listings_df.info())
    model_data = listings_df.loc[:, ('host_response_time',
                                      'host_response_rate',
                                      'host_acceptance_rate',
                                      'host_is_superhost',
                                      'neighbourhood_group_cleansed',
                                      'property_type',
                                      'room_type',
                                      'accommodates',
                                      'bathrooms',
                                      'bedrooms',
                                      'beds',
                                      'bed_type',
                                      'price',
                                      'cleaning_fee',
                                      'minimum_nights',
                                      'maximum_nights',
                                      'instant_bookable',
                                      'cancellation_policy',
                                      'review_scores_rating',
                                      'name_length',
                                      'summary_length',
                                      'space_length',
                                      'description_length',
                                      'amenities_length')]

    return model_data


def data_prep_get_dummy_variables_for_categorical_fields(model_data):
    print(f"get_dummies model_data {model_data}")
    # Get dummy variables for our 5 categorical fields
    model_data = pd.get_dummies(model_data,
                                columns=['neighbourhood_group_cleansed', 'property_type', 'room_type', 'bed_type',
                                         'cancellation_policy'])

    return model_data


def create_rate_prediction_model_data():
    listings_df, reviews_df, calendar_df = create_input_df( )

    # display_nan_values_percentage()
    # listings_df, reviews_df, calendar_df = drop_nan_values_from_input_df(listings_df, reviews_df, calendar_df)

    listings_df, reviews_df, calendar_df = prepare_data_clean_data(listings_df, reviews_df, calendar_df)

    listings_df = data_prep_listings_df(listings_df)
    listings_df = data_prep_remove_records_without_predictor_variable(listings_df)
    model_data = data_prep_remove_all_ratings(listings_df)
    model_data = data_prep_get_dummy_variables_for_categorical_fields(model_data)

    return model_data


if __name__ == '__main__':
    model_data = create_rate_prediction_model_data()
    model_dev_main(model_data)

