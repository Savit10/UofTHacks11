from elevenlabs import clone, generate, play, set_api_key
import elevenlabs
set_api_key("d630c7244416e787e8e3525776b914c5")

# voices = elevenlabs.voices()
# for voice in voices:
#     print(voice)

def speak(text: str, character: str) -> None:
    if character == "SpongeBob":
        voice = "gSYax3JbGCw19C3ya4fP"
    elif character == "Patrick":
        voice = "jDEVTjwk5XW2gm84tEAd"
    elif character == "Sandy":
        voice = "7i5y26JQ0Y4qZgvkx9jh"
    elif character == "Squidward":
        voice = "TW2H6YkkPD06FDvFL2KZ"
    else:
        voice = "Bella"
    audio = generate(
    text=text,
    voice=voice,
    model="eleven_multilingual_v2"
    )
    play(audio)

if __name__ == '__main__':
    speak("My name is Sandy! I love krabby patties", "Sandy")

# audio = generate(
#   text="My name is patrick! I love krabby patties",
#   voice="jDEVTjwk5XW2gm84tEAd",
#   model="eleven_multilingual_v2"
# )
# play(audio)
