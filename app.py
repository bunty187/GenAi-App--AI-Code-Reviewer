from openai import OpenAI
import streamlit as st

f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.snow()
st.title("💬An AI Code Reviewer")

## Take the user input
prompt = st.text_area("Enter your python code...")

## if the button is clicked generate the responses
if st.button("Check") == True:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": """You are a Code Reviewer.
                                            Note down all the bugs and error. 
                                            Display the correct code.
                                          """},
            {"role": "user", "content": prompt}
        ]
    )
    ## print the response on the web page
    st.write(response.choices[0].message.content)
