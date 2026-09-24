import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content": "Explain AI and 3 min types of AI in bullet points"
         
        }
    ]
)

print(response["message"]["content"])