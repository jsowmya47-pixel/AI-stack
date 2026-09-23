import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"what is ai in one line?"
        }
    ]
)
print(response["message"]["content"])