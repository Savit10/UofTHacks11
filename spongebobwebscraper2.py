from bs4 import BeautifulSoup
import requests
import json
import jsonlines

# Define the base URL
base_url = 'http://en.spongepedia.org'

# Send a GET request to the main transcripts page
response = requests.get(base_url + '/index.php?title=transcripts')

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the links to the transcript pages for seasons 1-9
season_links = soup.find_all('a', href=True, string=lambda t: t and 'Season' in t)

# Create a list of character names
characters = ["SpongeBob", "Patrick", "Sandy", "Mr. Krabs", "Squidward"]

# Create a dictionary of jsonlines.Writer for each character
writers = {character: jsonlines.open(f'{character}.jsonl', mode='w') for character in characters}

# For each season
for season_link in season_links:
    # Send a GET request to the season's transcript page
    season_response = requests.get(base_url + season_link['href'])

    # Parse the HTML content of the season's page with BeautifulSoup
    season_soup = BeautifulSoup(season_response.content, 'html.parser')

    # Find the links to the transcript pages for each episode in the season
    episode_table = season_soup.find('table', {'border': '1'})
    if episode_table is not None:
        episode_links = episode_table.find_all('a', href=True)
        for episode_link in episode_links:
            # Send a GET request to the episode's transcript page
            episode_response = requests.get(base_url + episode_link['href'])

            # Parse the HTML content of the episode's page with BeautifulSoup
            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')

            # Find the main content of the page
            content_div = episode_soup.find('div', {'id': 'mw-content-text'})

            if content_div is not None:
                # Find the dialogue tag within the main content
                dialogue_tag = content_div.find('span', {'class': 'mw-headline', 'id': 'Dialogue'})

                if dialogue_tag is not None:
                    # Find all the <p> tags after the dialogue tag within the main content
                    dialogues = dialogue_tag.find_all_next('p')
                    
                    previous_name = ""
                    previous_dialogue = ""

                    # Initialize a dictionary to store the messages for each character
                    character_messages = {name: [] for name in characters}

                    # Extract the text from each <p> tag and write it to the .jsonl file
                    for dialogue in dialogues:
                        dialogue_text = dialogue.get_text(strip=True)
                        if dialogue_text:
                            name, _, dialogue_speech = dialogue_text.partition(':')
                            if name in characters:
                                # Create a dictionary for the user message
                                user_message = {
                                    "role": "user",
                                    "content": previous_dialogue
                                }

                                # Create a dictionary for the chatbot message
                                chatbot_message = {
                                    "role": "chatbot",
                                    "content": dialogue_speech
                                }

                                # Append the messages to the character's list
                                character_messages[name].extend([user_message, chatbot_message])

                                # Update the previous name and dialogue
                                previous_name = name
                                previous_dialogue = dialogue_speech

# Write the messages to a .jsonl file for each character
for name, messages in character_messages.items():
    # Ensure that the character's messages array contains at least one message from the "User" and one from the "Chatbot"
    if any(message["role"] == "user" for message in messages) and any(message["role"] == "chatbot" for message in messages):
        # Open a jsonlines.Writer for the character in 'a' mode
        with jsonlines.open(f'{name}.jsonl', mode='a') as writer:
            writer.write({"messages": messages})