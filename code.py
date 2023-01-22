import openai_secret_manager
import openai
import re

# Let's setup the API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")
openai.api_key = secrets["api_key"]

def generate_content(topic, num_paragraphs, num_sentences):
    prompt = (f"Write a {num_paragraphs} paragraphs article about {topic} with {num_sentences} sentences each.")
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    paragraphs = message.split("\n")
    output = ''
    for i in range(num_paragraphs):
        output += paragraphs[i]+'\n'
    return output

topic = input("Enter the topic : ")
num_paragraphs = int(input("Enter the number of paragraphs : "))
num_sentences = int(input("Enter the number of sentences per paragraph : "))

print(generate_content(topic, num_paragraphs, num_sentences))
