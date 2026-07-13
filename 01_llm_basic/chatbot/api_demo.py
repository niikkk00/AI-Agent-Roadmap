user_input = "你好"
messages = [
  {
    "role":"user",
    "content":user_input
  }
]

def send_message(messages):
  print("正在发送给AI...")
  print("发送的消息:",messages)
  return {
    "role":"assistant",
    "content":"你好，我是模拟AI"
  }
response = send_message(messages)
messages.append(response)
print("完整的聊天记录:",messages)