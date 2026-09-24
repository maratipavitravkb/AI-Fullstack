import ollama 
msgs=[
    {"role":"system",
     "content": " Imagine you are an ant .Give the answers only in 2 to 3 lines only"
}
]
while True:
    question = input("Ask the quetion ")
    if question.lower() == "exit":
        break
    msgs.append (
        {"role":"user",
        "content":question}
        )    
    response = ollama.chat(
        model = "llama3.2:3b",
        messages=msgs
    )
    msgs.append(
            {"role":"assistant",
            "content":response["message"]["content"]}
            )
    print("AI: "  ,response["message"]["content"])


print("Conversation history:")
for msg in msgs:
    if msg['role'] == 'system':
        continue

    print(msg['role'],":", {msg['content']})
    