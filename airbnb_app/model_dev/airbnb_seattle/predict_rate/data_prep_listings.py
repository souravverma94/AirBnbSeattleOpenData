import pandas as pd


def prepare_data_fixed_data_types(listings_df):
    pd.options.mode.chained_assignment = None  # default='warn'

    listings_df['host_response_rate'] = listings_df['host_response_rate'].astype(str)
    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].astype(str)
    listings_df['price'] = listings_df['price'].astype(str)

    return listings_df


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


def data_prep_description_elements(listings_df):
    # Get lengths of description elements
    listings_df.loc[:, 'name_length'] = listings_df['name'].str.len()
    listings_df.loc[:, 'summary_length'] = listings_df['summary'].str.len()
    listings_df.loc[:, 'space_length'] = listings_df['space'].str.len()
    listings_df.loc[:, 'description_length'] = listings_df['description'].str.len()
    listings_df.loc[:, 'amenities_length'] = listings_df['amenities'].str.len()
    listings_df.loc[:, 'name_length'].fillna(0, inplace=True)
    listings_df.loc[:, 'summary_length'].fillna(0, inplace=True)
    listings_df.loc[:, 'space_length'].fillna(0, inplace=True)
    listings_df.loc[:, 'description_length'].fillna(0, inplace=True)
    listings_df.loc[:, 'amenities_length'] = listings_df['amenities'].str.len()

    # Drop original description variables
    listings_df = listings_df.drop(['name', 'summary', 'space', 'description', 'amenities'], 1)

    return listings_df


def data_prep_host_response_to_numbers(listings_df):
    # Recode host_response_time to integers as it is a spectrum
    listings_df['host_response_time'].replace('within an hour', 1, inplace=True)
    listings_df['host_response_time'].replace('within a few hours', 2, inplace=True)
    listings_df['host_response_time'].replace('within a day', 3, inplace=True)
    listings_df['host_response_time'].replace('a few days or more', 4, inplace=True)

    # Impute missing values using forward-fill method
    listings_df['host_response_time'].fillna(method='ffill', inplace=True)

    return listings_df


def data_prep_acceptance_response_to_numbers(listings_df):
    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].replace('%', '', regex=True).astype(
        'float64') / 100.00
    listings_df['host_response_rate'] = listings_df['host_response_rate'].replace('%', '', regex=True).astype(
        'float64') / 100.00

    # Impute missing values using forward-fill method
    listings_df['host_response_rate'].fillna(method='ffill', inplace=True)
    listings_df['host_acceptance_rate'].fillna(method='ffill', inplace=True)

    return listings_df


def data_prep_host_is_superhost_to_binary(listings_df):
    listings_df['host_is_superhost'].replace('t', 1, inplace=True)
    listings_df['host_is_superhost'].replace('f', 0, inplace=True)
    listings_df['instant_bookable'].replace('t', 1, inplace=True)
    listings_df['instant_bookable'].replace('f', 0, inplace=True)

    return listings_df


def data_prep_property_type_to_categories(listings_df):
    # Clean property_type category to 5 categories
    def recode(value):
        if value not in ['House', 'Apartment', 'Touwnhouse', 'Condominium']:
            return 'Other'
        return value

    listings_df['property_type'] = listings_df['property_type'].apply(recode)

    return listings_df


def data_prep_bed_type_to_categories(listings_df):
    def recode(value):
        if value not in ['Real Bed']:
            return 'Other'
        return value

    listings_df['bed_type'] = listings_df['bed_type'].apply(recode)

    return listings_df


def data_prep_handle_missing_values(listings_df):
    # Can't be sure what a missing value for these so we'll fill na
    listings_df['bathrooms'].fillna(method='ffill', inplace=True)
    listings_df['bedrooms'].fillna(method='ffill', inplace=True)
    listings_df['beds'].fillna(method='ffill', inplace=True)
    listings_df['host_is_superhost'].fillna(method='ffill', inplace=True)

    return listings_df


def prepare_data_clean_data(listings_df):
    pd.options.mode.chained_assignment = None  # default='warn'

    prepare_data_fixed_data_types(listings_df)

    listings_df['host_acceptance_rate'] = listings_df['host_acceptance_rate'].str.replace("%", "").astype("float")
    listings_df = data_prep_price_and_cleaning_fee_to_numbers(listings_df)
    listings_df['host_response_rate'] = listings_df['host_response_rate'].str.replace("%", "").astype("float")

    return [listings_df]


def data_prep_listings_df(listings_df):
    listings_df = data_prep_description_elements(listings_df)
    listings_df = data_prep_host_response_to_numbers(listings_df)
    listings_df = data_prep_acceptance_response_to_numbers(listings_df)
    listings_df = data_prep_host_is_superhost_to_binary(listings_df)
    listings_df = data_prep_property_type_to_categories(listings_df)
    listings_df = data_prep_bed_type_to_categories(listings_df)
    listings_df = data_prep_handle_missing_values(listings_df)

    return listings_df
