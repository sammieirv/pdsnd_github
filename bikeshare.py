import time
import pandas as pd
import numpy as np

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
    cities = ['chicago','new york city', 'washington']
    months = ['january', 'february', 'march','april','may','june']
    days =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        try:
            city = cities.index(input('\nInput name of city to analyze: "chicago" or "new york city"or washington"\n').lower())
            month = months.index(input('\nInput name of month to filter by, or "all" to apply no filter\n').lower()) 
            day = days.index(input('\nInput name of the day of week to filter by or "all" to apply no filter\n').lower())
            return cities[city] ,months[month], days[day]       
        except:
            print('Incorrect input: please try again')
        

    # TO DO: get user input for month (all, january, february, ... , june)
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
     

   


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
    
    
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    try:
        df['Birth Year']= df['Birth Year'].fillna(method ='ffill',axis =0)
        df['Birth Year']= df['Birth Year'].astype(int)
    except:
        print('\nNote:There is no Birth Year column for this dataset\n')
    
   
    
    if month != 'all':                          
        months = ['january', 'february', 'march','april','may','june']
        month = months.index(month)+1
        
        df = df[df['month']== month]
        
    if day != 'all':
        df =df[df['day_of_week']==day.title()]
        
   
    df['hour'] =df['Start Time'].dt.hour
    return df

def display_raw_data(df):
    """ Display the first few dataset that has been choosen
    """
    i = 0
    raw = input('\nDo you want to see the dataset? Please enter only "yes" or "no"\n').lower()
    pd.set_option('display.max_columns', 200)
    
    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5])
            raw = input('\nDo you want to see five more rows of the dataset? Please enter only "yes" or                                      "no"\n').lower()
            i +=5
            
        else:
            raw = input('\nYour input is invalid. Please enter only "yes" or "no"\n').lower()
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)
    # TO DO: display the most common month


    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_hour =df['hour'].mode()[0]
    hour_count = df['hour'].count()
    print('The most common start hour is:{}, with count: {}'.format(most_common_hour, hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return most_common_month, most_common_day_of_week,  most_common_hour

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    count_start_station =df['Start Station'].count()
    print('The most_common_used_start_station: {}, count: {}'.format(most_common_used_start_station,count_start_station))

    # TO DO: display most commonly used end station
    most_common_used_end_station =df['End Station'].mode()[0]
    count_end_station =df['End Station'].count()
    print('The most_common_used_end_station: {}, count: {}'.format( most_common_used_end_station,count_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    mt = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print(mt)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =df['Trip Duration'].sum()
    print('The total travel time is:{}'.format(total_travel_time))
   
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mtt = round(mean_travel_time,2)
    print('The mean travel time is:{}'.format(mtt))
   
    
    return df
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    usertypes =df['User Type'].value_counts()
    print('The count of user types is:{}'.format(usertypes))
    
    try:
    # TO DO: Display counts of gender
        
        gender_count = df['Gender'].value_counts()
        b =print('The count of gender is:{}'.format(gender_count))
        earliest_birthyear  =df['Birth Year'].min()
        recent_birthyear =df['Birth Year'].max()
        most_common_birthyear =df['Birth Year'].mode()[0]
        c = print('earliest birthyear is:{}, recent birthyear is:{}, most common birthyear is {}'.format(earliest_birthyear,recent_birthyear,most_common_birthyear))
        
                                     
           
        return b,c
    except:
        print('Gender is not in the database')


    # TO DO: Display earliest, most recent, and most common year of birth
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
