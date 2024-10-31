import streamlit as st
from openai import OpenAI
client = OpenAI()
MODEL = "ft:gpt-4o-2024-08-06:diogo-resende:email-writer-data-heroes:ALBNWysv"

# Streamlit app
st.title("Promotional Email Writer")

# Input field for the email topic (now using st.text_area)
topic = st.text_area("Enter the topic of the email:", height=200)

# Define the system and user message
system_prompt = """You are a skilled social media manager specialized in Analytics and AI.
                  Your main task is to write engaging, concise, and persuasive emails for subscribers"""

topic = "New GenAI course section: Fine Tuning an GPT model"

user_prompt = f"Write an email about: {topic}"

# Generate email button
if st.button("Generate Email"):
    if topic:
        # Construct the user prompt
        user_prompt = f"Write an email about: {topic}"

        # Prepare the messages for the OpenAI API
        test_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        try:
            response = client.chat.completions.create(
            model=MODEL,
            messages=test_messages,
            temperature=1,
            #max_tokens=700
        )
            # Extract the generated email from the response
            generated_email = response.choices[0].message.content
            st.subheader("Generated Email:")
            st.write(generated_email)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic.")
