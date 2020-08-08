import pandas as pd


def drop_nan_values_from_input_df(listings_df, reviews_df, calendar_df):
    # drop NaN rows
    listings_df = listings_df.dropna(axis=0)
    reviews_df = reviews_df.dropna(axis=0)
    calendar_df = calendar_df.dropna(axis=0)

    return [listings_df, reviews_df, calendar_df]


def prepare_data_fixed_data_types(listings_df, reviews_df, calendar_df):
    pd.options.mode.chained_assignment = None  # default='warn'

    listings_df['host_response_rate'] = listings_df['host_response_rate'].astype(str)
    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].astype(str)
    listings_df['price'] = listings_df['price'].astype(str)

    return [listings_df, reviews_df, calendar_df]


def prepare_data_clean_data(listings_df, reviews_df, calendar_df):
    pd.options.mode.chained_assignment = None  # default='warn'

    prepare_data_fixed_data_types(listings_df, reviews_df, calendar_df)

    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].str.replace("%", "").astype("float")
    listings_df['price'] = listings_df['price'].str.replace("[$, ]", "").astype("float")
    listings_df['host_response_rate'] = listings_df['host_response_rate'].str.replace("%", "").astype("float")

    return [listings_df, reviews_df, calendar_df]
