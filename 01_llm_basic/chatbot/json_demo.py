user = {
  "role":"user",
  "content":"你好"
}
print(user)

messages = []
messages.append(user)
print(messages)

assistant = {
  "role":"assistant",
  "content":"你好，我是AI"
}
messages.append(assistant)
print(messages)

import json

with open("01_llm_basic/chatbot/history.json","w",encoding="utf-8") as f:
  json.dump(messages,f,ensure_ascii=False,indent=4)

with open("01_llm_basic/chatbot/history.json","r",encoding="utf-8") as f:
  history = json.load(f)
  print(history)

print(type(history))
print(type(history[0]))