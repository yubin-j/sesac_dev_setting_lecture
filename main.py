from agent import llmAgent

if __name__ == "__main__":
  agent = llmAgent()
  reply = agent.handle("사용자", "안녕 날씨알려줘")
  print("응답:", reply)