import openai
import os
import phi
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools # Brings in financial tools for retrieving stock data, company news, and more.
from phi.tools.duckduckgo import DuckDuckGo # Imports the DuckDuckGo tool, which provides web search capabilities.
from dotenv import load_dotenv
from phi.model.groq import Groq

# Imports the components needed to set up and run the web application that hosts your agents.
from phi.playground import Playground, serve_playground_app

# Load environment variables from .env file
load_dotenv()

phi.api_key = os.getenv("PHI_API_KEY")

## Designed to search the web for information using the DuckDuckGo tool.
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,
)


## Specialized for handling financial queries by providing stock prices, analyst recommendations, and company
## news using Yahoo Finance tools
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Setting Up the Playground Application
app = Playground(agents=[finance_agent, web_search_agent]).get_app()


if __name__=="__main__":

    # Launches the web server for the Playground application. The "playground:app" argument specifies the 
    # location of the app within your module, and reload=True enables auto-reloading during development 
    # whenever changes are detected.
    serve_playground_app("playground:app", reload=True)

