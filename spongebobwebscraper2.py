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
writers = {character: jsonlines.open(f'{character}CHATBOT.jsonl', mode='w') for character in characters}

# Initialize a dictionary to store the messages for each character
character_messages = {name: [] for name in characters}

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
                    
                    previous_dialogue = ""

                    # Extract the text from each <p> tag and write it to the .jsonl file
                    # For each dialogue
                    # For each dialogue
                    for dialogue in dialogues:
                        dialogue_text = dialogue.get_text(strip=True)
                        if dialogue_text:
                            name, _, dialogue_speech = dialogue_text.partition(':')
                            if name in characters:
                                # Create a dictionary for the user message
                                user_message = {
                                    "role": "User",
                                    "content": previous_dialogue
                                }

                                # Create a dictionary for the chatbot message
                                chatbot_message = {
                                    "role": "Chatbot",
                                    "content": dialogue_speech
                                }

                                # Create a pair of messages
                                message_pair = [user_message, chatbot_message]

                                # Only append the pair to the character's list if it's not already there
                                if message_pair not in character_messages[name]:
                                    character_messages[name].append(message_pair)

                                # Update the previous dialogue
                                previous_dialogue = dialogue_speech

                    # Write the messages to a .jsonl file for each character
                    for name, messages in character_messages.items():
                        # Open a jsonlines.Writer for the character in 'a' mode
                        with jsonlines.open(f'{name}CHATBOT.jsonl', mode='a') as writer:
                            # Write each pair of messages as a "messages" array in a JSON object
                            for message_pair in messages:
                                writer.write({"messages": message_pair})