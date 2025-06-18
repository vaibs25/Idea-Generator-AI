import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables (for API key)
load_dotenv()

# Initialize Groq model
model = Groq(id="llama3-70b-8192")

# Agent 1: 
startup_idea_agent = Agent(
    name="StartupIdeaAgent",
    model=model,
    tools=[DuckDuckGo()],
    instructions=["generate the startup ideas based on the current market trends."],
    show_tool_calls=True,
    markdown=True,
)

# Agent 2: 
content_creater_agent = Agent(
    name="ContentCreaterAgent",
    model=model,
    instructions=["Suggest the content ideas blogpost, youtube videos or socail media topics"],
    markdown=True,
)

# Function to decide which agent should respond
def idea_ai(user_prompt):
    idea_keywords = ["generate", "idea", "startup", "current trends"]
    if any(keyword in user_prompt.lower() for keyword in idea_keywords):
        response = startup_idea_agent.run(user_prompt)
    else:
        response = content_creater_agent.run(user_prompt)
    return response.content

# CLI loop
if __name__ == "__main__":
    print("Welcome to Idea Generator!")
    #print("Ask anything about your studies or study tips. Type 'exit' to quit.")

    while True:
        user_input = input("\n👩‍🎓 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = idea_ai(user_input)
        print("\nIdea Generator AI:\n" + response)