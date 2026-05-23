from ollama import chat

def stream_response(user_prompt: str, llm="llama3.1:8b"):

    """
    generates LLM response chunk by chunk on given user prompt.
    By default, LLM used is "llama3.1:8b". Change model name according to model installed in your system.
    INPUT: user prompt (string)
    OUTPUT: LLM response (string)
    """
    stream = chat(
        model=llm,
        messages=[{'role': 'user', 'content': user_prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":

    user_text = str(input("enter prompt= "))
    if user_text:
        stream_response(user_prompt=user_text)
    else:
        print("Enter prompt to generate response.")