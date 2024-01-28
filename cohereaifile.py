import cohere 
co = cohere.Client('9YRZ6zTRjsQc7OyNaUaYde0f8PIBqI2kKQmTkvlz')

def get_response(input: str, character: str) -> str:    
    responses = []
    if character == "SpongeBob":
        model_id = "f31a864f-f802-4c70-8e33-62b6d317597f-ft"
    elif character == "Patrick":
        model_id = "3bfcb339-f835-4dea-aed9-3b76cb6f16b6-ft"
    elif character == "Sandy":
        model_id = "25d29448-d950-4502-ac62-7aa34ba13a71-ft"
    elif character == "Mr. Krabs":
        model_id = "526e408f-956e-4bfe-a816-2800d92d80e3-ft"
    elif character == "Squidward":
        model_id = "ee274ad6-85c1-4b65-9317-8dde7e27c1bd-ft"
    elif character == 'Thomas':
        model_id = "e8c5e1d6-3f9c-46fc-86e1-b33b006ff581-ft"
    elif character == "Gordon":
        model_id = "0d150ba3-ce02-46e9-ad9d-59c458dc3fc3-ft"
    elif character == "Edward":
        model_id = "91d7a719-c332-4f8e-95ee-a03e19359dc0-ft"
    elif character == "Duncan":
        model_id = "7b8138f7-208d-438e-93d1-691255abfeda-ft"
    else:
        model_id = 'command'
    for i in range(2):
        response = co.generate(
        model=model_id,
        prompt= input + character + ":",
        max_tokens=300,
        temperature=0.4,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')  
        responses.append(response.generations[0].text)

    response = co.rerank(
    model = 'rerank-english-v2.0',
    query = 'Which one sounds the most like' + character + "?",
    documents = responses,
    top_n = 3,
    )
    return response[0].document['text']
    # return response["results"][0]["document"]["text"]

if __name__ == "__main__":
    print(get_response("Who is your best friend?", "SpongeBob"))


