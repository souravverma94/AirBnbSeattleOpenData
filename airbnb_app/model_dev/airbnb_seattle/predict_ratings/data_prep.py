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


def data_prep_price_and_cleaning_fee_to_numbers(listings_df):
    listings_df['price'] = listings_df['price'].str.replace('$', '')
    listings_df['price'] = listings_df['price'].str.replace("[$, ]", "")
    listings_df['price'] = listings_df['price'].str.replace(',', '').astype('float64')
    listings_df['cleaning_fee'] = listings_df['cleaning_fee'].str.replace('$', '')
    listings_df['cleaning_fee'] = listings_df['cleaning_fee'].str.replace(',', '').astype('float64')

    # Missing data for cleaning fee indicates a $0 cleaning fee
    listings_df['cleaning_fee'].fillna(0, inplace=True)

    return listings_df


def prepare_data_clean_data(listings_df, reviews_df, calendar_df):
    pd.options.mode.chained_assignment = None  # default='warn'

    prepare_data_fixed_data_types(listings_df, reviews_df, calendar_df)

    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].str.replace("%", "").astype("float")
    listings_df = data_prep_price_and_cleaning_fee_to_numbers(listings_df)
    listings_df['host_response_rate'] = listings_df['host_response_rate'].str.replace("%", "").astype("float")

    return [listings_df, reviews_df, calendar_df]

