from llm import send_message

messages = []
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("退出聊天")
        break
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = send_message(messages)
    messages.append({
    "role": "assistant",
    "content": response
  })
    print("AI:", response)

