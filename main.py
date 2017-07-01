import requests
from string import strip

text_file = open("profiles", "r")
profiles = text_file.read().split(',')


def get_data_for_profile(profile_name):
    url = "https://instagram.com/" + profile_name
    r = requests.get(url)

    followers_start_string = '"followed_by": {"count": '
    followers_end_string = '},'
    followers_start_index = r.text.find(followers_start_string) \
        + len(followers_start_string)
    followers_end_index = r.text.find(
            followers_end_string, followers_start_index)
    followers = int(r.text[followers_start_index:followers_end_index])

    follows_start_string = '"follows": {"count": '
    follows_end_string = '},'
    follows_start_index = r.text.find(follows_start_string) \
        + len(follows_start_string)
    follows_end_index = r.text.find(follows_end_string, follows_start_index)
    follows = int(r.text[follows_start_index:follows_end_index])

    profile_data = {
            'profile_name': '@' + profile_name,
            'followers': followers,
            'follows': follows,
    }
    return profile_data


def pretty_print_profile(profile_data):
    print(profile_data['profile_name'])
    print("Followers: " + str(profile_data['followers']))
    print("Follows: " + str(profile_data['follows']) + '\n')


def pretty_print_recap():
    print("Total follows " + str(total_follows))
    print("Total followers " + str(total_followers) + "\n")
    print("Average follows " + str(total_follows / len(profiles)))
    print("Average followers " + str(total_followers / len(profiles)) + "\n")


print("Instamonitor v0.1\n")
print(str(len(profiles)) + " profile(s) found...\n")

total_follows = 0
total_followers = 0

for profile in profiles:
    profile = strip(profile)
    profile_data = get_data_for_profile(profile)
    total_follows += profile_data['follows']
    total_followers += profile_data['followers']
    pretty_print_profile(profile_data)

pretty_print_recap()
