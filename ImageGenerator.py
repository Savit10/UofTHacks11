from openai import OpenAI

def generate_image(prompt) -> str:
    my_api_key = "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"
    client = OpenAI(api_key=my_api_key)
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url