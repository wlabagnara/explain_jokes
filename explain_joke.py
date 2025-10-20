import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to get explanation from OpenAI
def get_joke_explanation(joke):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Use the appropriate model name
        messages=[
            {"role": "user", "content": f"Explain this joke: {joke}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app layout
st.title("Joke Explainer")

# Text input for the joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        # Get explanation from OpenAI
        explanation = get_joke_explanation(joke_input)
        # Display the explanation
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.warning("Please enter a joke before submitting.")