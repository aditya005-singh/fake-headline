import random

# Subjects – well-known people, groups, or funny concepts
subjects = [
    "Virat Kohli",
    "Elon Musk",
    "A group of Delhi aunties",
    "Prime Minister Modi",
    "A dancing traffic cop",
    "Nirmala Sitharaman",
    "Aliens from Chandni Chowk",
    "A confused software engineer",
    "Ranveer Singh in pajamas",
    "ChatGPT's evil twin",
]

# Actions – what they’re doing (funny, bizarre, or dramatic)
actions = [
    "declares war on",
    "launches a startup with",
    "dances bhangra with",
    "accidentally marries",
    "challenges to a samosa-eating contest",
    "starts a podcast with",
    "gets stuck in traffic with",
    "goes on hunger strike against",
    "writes poetry for",
    "celebrates Diwali with",
]

# Places or things – weird locations or situations
places_or_things = [
    "a cow at India Gate",
    "Mumbai local train driver",
    "a haunted golgappa stall",
    "Baba Ramdev’s private yoga island",
    "a mysterious samosa-shaped UFO",
    "a talking ATM in Bengaluru",
    "IPL trophy made of laddoos",
    "underwater Parliament session",
    "a robot rickshaw driver",
    "at Chandrayaan Dhaba, Moon",
]

# Headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"\n🛑 BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print(headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        break

print("\n📰 Thanks for using the Fake News Headline Generator. Stay tuned for more nonsense!")
