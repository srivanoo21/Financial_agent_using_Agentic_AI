## Importing Libraries and Modules

import openai
import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")

## The Web Search Agent is set up to perform web searches using the DuckDuckGo tool
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## The Finance AI Agent is dedicated to retrieving financial information such as stock prices, analyst 
## recommendations, fundamentals, and company news.
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)


# The multi-agent is designed to combine the strengths of both the Web Search Agent and the Finance AI Agent
multi_ai_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # team - includes both agents, allowing the multi-agent to delegate queries based on the requirements.
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla", stream=True)

