from openai import OpenAI
# from boto.s3.connection import S3Connection
import os
# from dotenv import load_dotenv
# load_dotenv()

def generate_image(prompt):
    # s3 = S3Connection(os.environ['OPEN_AI_TOKEN'])
    # client = OpenAI(api_key=s3)
    # client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    client = OpenAI(api_key=os.environ.get('THEANSWERTOEVERYTHINGEVER'))
    response = client.images.generate(
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url

if __name__ == "__main__":
    print(generate_image("SpongeBob SquarePants playing soccer with Patrick"))