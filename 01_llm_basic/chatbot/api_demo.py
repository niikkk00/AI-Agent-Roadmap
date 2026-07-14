def send_message(messages):
  print("AI正在思考...")
  # print("发送的消息:",messages)
  return {
    "role":"assistant",
    "content":"你好，我是模拟AI"
  }

messages = []
while True:
  user_input = input("User: ")
  if user_input.lower() == "exit":
    print("退出聊天")
    break 
  messages.append({
    "role":"user",
    "content":user_input
  })
  response = send_message(messages)
  print("AI:",response["content"])
print("完整的聊天记录:",messages)

