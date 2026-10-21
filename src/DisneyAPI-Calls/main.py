import requests
import csv

# Data from September 21- October 6 collect
# Data from September 15-21 is invalid


# SpaceShip Earth, Test Track and Soaring Across America
def spaceship_earth_get_posts():
     # define the API endpoint
    space_ship_earth_url = 'https://api.themeparks.wiki/v1/entity/480fde8f-fe58-4bfb-b3ab-052a39d4db7c/live'

    try:
        spaceship_earth_response = requests.get(space_ship_earth_url, timeout=15)

        if spaceship_earth_response.status_code == 200:
            spaceship_earth_posts = spaceship_earth_response.json()
            return spaceship_earth_posts
        else:
            print('Error', spaceship_earth_response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error', e)
        return None

def test_track_get_posts():
    test_track_url = 'https://api.themeparks.wiki/v1/entity/37ae57c5-feaf-4e47-8f27-4b385be200f0/live'

    try:
        test_track_response = requests.get(test_track_url)

        if test_track_response.status_code == 200:
            test_track_posts = test_track_response.json()
            return test_track_posts
        else:
            print('Error', test_track_response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error', e)
        return None

def ride3_get_posts():
    soarin_across_america_url = 'https://api.themeparks.wiki/v1/entity/81b15dfd-cf6a-466f-be59-3dd65d2a2807/live'

    try:
        soarin_america_response = requests.get(soarin_across_america_url)


        if soarin_america_response.status_code == 200:
            ride3_posts = soarin_america_response.json()
            return ride3_posts
        else:
            print('Error', soarin_america_response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error', e)
        return None

def write_data_to_csv():

    with open("spaceship_earth_data.csv", "a", newline="") as collect:

        writer = csv.writer(collect)

        data_posts = spaceship_earth_get_posts()

        if data_posts:

            live_data_from_ride2 = data_posts["liveData"][0]
            print("success")

            writer.writerow([live_data_from_ride2["name"],
                             live_data_from_ride2["entityType"],
                             live_data_from_ride2["status"],
                             live_data_from_ride2["queue"]["STANDBY"]["waitTime"],
                             live_data_from_ride2["lastUpdated"]])
        else:
            print("error", data_posts)

def write_data_to_ride2_csv2():

    with open("Test_Track_data.csv", "a", newline="") as ride2_collect:

        writer = csv.writer(ride2_collect)

        ride2_data_posts = test_track_get_posts()

        if ride2_data_posts:

            live_data_from_ride2 = ride2_data_posts["liveData"][0]
            print("success")

            writer.writerow([live_data_from_ride2["name"],
                             live_data_from_ride2["entityType"],
                             live_data_from_ride2["status"],
                             live_data_from_ride2["queue"]["STANDBY"]["waitTime"],
                             live_data_from_ride2["lastUpdated"]])
        else:
            print("error", ride2_data_posts)


def write_data_to_ride3_csv3():

    with open("Sorin_Across_America_data.csv", "a", newline="") as ride3_collect:

        writer = csv.writer(ride3_collect)

        ride3_data_posts = ride3_get_posts()


        if ride3_data_posts:

            live_data_from_ride2 = ride3_data_posts["liveData"][0]
            print("success")

            writer.writerow([live_data_from_ride2["name"],
                             live_data_from_ride2["entityType"],
                             live_data_from_ride2["status"],
                             live_data_from_ride2["queue"]["STANDBY"]["waitTime"],
                             live_data_from_ride2["lastUpdated"]])
        else:
            print("error", ride3_data_posts)



def main():

    write_data_to_csv()
    write_data_to_ride2_csv2()
    write_data_to_ride3_csv3()




if __name__ == '__main__':
    main()