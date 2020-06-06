import time
import pandas as pd
import numpy as np
import math

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ["chicago", "new york city", "washington"]
    while True:
        city = input("Type the city would you like to review: chicago, new york city, or washington? ").lower()
        if city in city_list:
            break
        else:
            print("Try another valid value")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        month = input("Type the month would you like to review: all, january, february, march, april, may, june? ").lower()
        if month in month_list:
            break
        else:
            print("That is not a valid month, try one in the list")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_list = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("Which day would you like to review: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday? ").lower()
        if day in day_list:
            break
        else:
            print("Try another valid value")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('\nMost common month: ', common_month, '\n')
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nMost common day of week: ', common_day, '\n')
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost common hour: ', common_hour, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station: ', common_start_station, '\n')
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost common end station: ', common_start_station, '\n')



    # TO DO: display most frequent combination of start station and end station trip
    start_station = df['Start Station']
    end_station = df['End Station']
    trip_stations = "trip loop starts at "+start_station +" and ends at " + end_station
    trip_stations_count = trip_stations.mode()[0]
    print('\nMost common', trip_stations_count, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_seconds = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    def convert(seconds):
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%dh:%02dm:%02ds" % (hour, min, sec)
    print('\nTotal trip time: ', convert(trip_seconds),'\n')

    # TO DO: display mean travel time
    print('\nMean trip time: ', convert(mean_travel_time),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts(dropna=True)
    print('\nUser Types: ','\n', count_user_types,'\n')
    while True:
        try:
            # TO DO: Display counts of gender
            count_gender = df['Gender'].value_counts(dropna=True)
            print('\nGender Demographics: ','\n', count_gender,'\n')
            gender_demographics = int(df['Gender'].max())
            print('\nHigher user base by gender: ','\n', count_gender,'\n')
            # TO DO: Display earliest, most recent, and most common year of birth
            earliest_birth_year = int(df['Birth Year'].min())
            most_recent_birth_year = int(df['Birth Year'].max())
            common_birth_year = int(df['Birth Year'].mode()[0])
            print('\nThe earliest birth year is: {}\n \nMost recent birth year is: {}\n \nMost common year of birth is: {}\n'.format(earliest_birth_year, most_recent_birth_year, common_birth_year))
            break
        except:
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        user_stats(df)
        trip_duration_stats(df)

        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        if raw_data.lower() == 'yes': #show 5 rows of raw data and then add to count
                   while True:
                           i = 0
                           print(df.iloc[i:i+10])
                           i += 10
                           more_data = input('\nWould you like to see additional raw data? Enter yes or no.\n').lower()
                           if more_data not in ('yes','y'):
                               break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
