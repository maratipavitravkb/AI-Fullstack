import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content": "you are teaching to 3 years  old child Give the answers only in 2 to 3 lines only"
         
        },

        {
            "role" :"user",
            "content":"Explain ml"
        }
    ]
)

print(response["message"]["content"])