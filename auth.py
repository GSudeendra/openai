import openai

openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    content = response.choices[0].message["content"]
    return content
