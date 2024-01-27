import cohere 
co = cohere.Client('9YRZ6zTRjsQc7OyNaUaYde0f8PIBqI2kKQmTkvlz')

def get_response(input: str, character: str) -> str:    
    responses = []
    for i in range(10):
        response = co.generate(
        model='command',
        prompt= input,
        max_tokens=300,
        temperature=0.4,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')  
        responses.append('Prediction: {}'.format(response.generations[0].text))

    response = co.rerank(
    model = 'rerank-english-v2.0',
    query = 'Which one sounds the most like' + character,
    documents = responses,
    top_n = 3,
    )