import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Define the prompt for the conversation
prompt_text = "You: Hello, what is the value of pi(π)?\nAI:"

# Generate a response from the model
response = openai.Completion.create(
  engine="model_name",  # Specify which GPT model to use Ex: gpt-3.5-turbo, dall-e-3
  prompt=prompt_text,
  temperature=0.5,
  max_tokens=125
)

# Print the AI's response
print(response.choices[0].text.strip())