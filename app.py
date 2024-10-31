import streamlit as st
from openai import OpenAI
client = OpenAI()
MODEL = "ft:gpt-4o-2024-08-06:diogo-resende:email-writer-data-heroes:ALBNWysv"

# Streamlit app
st.title("Promotional Email Writer")

# Input field for the email topic
topic = st.text_input("Enter the topic of the email:")

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
            generated_email = response['choices'][0]['message']['content']
            st.subheader("Generated Email:")
            st.write(generated_email)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic.")
