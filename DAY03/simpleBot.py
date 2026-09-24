import ollama 
while True:
    question = input("Ask the quetion ")
    response = ollama.chat(
        model = "llama3.2:3b",
        messages=[
            {
                "role":"system",
                "content": "Give the answers only in 2 to 3 lines only"
             
            },

            {
                "role" :"user",
                "content":question
            }
        ]
    )

    print(response["message"]["content"])
