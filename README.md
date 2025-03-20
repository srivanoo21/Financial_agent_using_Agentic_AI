# Agentic AI Playground (playgound.py)

This project sets up an interactive agentic AI application using the Phi framework. The application creates two specialized agents—a Web Search Agent and a Finance AI Agent—that you can use to perform web searches and retrieve financial data.

## Overview

The Python script performs the following tasks:

- **Loads Dependencies:**  
  Imports necessary libraries and modules such as OpenAI, Phi, environment variable handling, and various tool integrations.

- **Environment Setup:**  
  Reads environment variables from a `.env` file. You must include your Phi API key in this file, which is required to authenticate with the Phi service.

- **Agent Creation:**  
  Configures two agents:
  - **Web Search Agent:**  
    Uses the DuckDuckGo tool for web searches and always includes sources in its responses.
  - **Finance AI Agent:**  
    Uses Yahoo Finance tools to fetch stock prices, fundamentals, analyst recommendations, and company news. The output is formatted in tables.

- **Playground Setup:**  
  Creates a web interface (Playground) that lets you choose which agent to run based on your query.

- **Application Execution:**  
  Launches a web server to interact with the agents through your browser.





# Multi-Agent AI Application (MultiAgent.py)

This project demonstrates a multi-agent AI system using the Phi framework. In this script, we create two specialized agents—a Web Search Agent and a Finance AI Agent—and then combine them into a multi-agent that can handle queries involving both web searches and financial data retrieval. The script is designed to be executed directly in the VS Code terminal.

## Overview

The Python script performs the following tasks:

- **Loads Dependencies:**  
  Imports necessary libraries and modules, including OpenAI (if needed), OS, and various components from the Phi framework such as agents, models, and tools for both web search and financial data.

- **Defines Two Specialized Agents:**  
  - **Web Search Agent:**  
    Uses the DuckDuckGo tool to perform web searches and always includes sources in its responses.
  - **Finance AI Agent:**  
    Uses Yahoo Finance tools to fetch stock prices, analyst recommendations, stock fundamentals, and company news. The output is formatted in tables for clarity.

- **Combines Agents into a Multi-Agent:**  
  Integrates both specialized agents into a single multi-agent. This unified agent can delegate parts of the query to each team member based on the content of the request.

- **Executes a Query:**  
  Processes a complex query—asking for a summary of analyst recommendations and the latest news for Tesla—and prints the response directly in the VS Code terminal with streaming enabled.

## How to Run the Script

1. **Open VS Code Terminal:**
   - Open the project folder in VS Code.
   - Open the integrated terminal.

2. **Run the Script:**
   ```bash
   python financial_agent.py




## Differences between both the approaches

**Playground.py:**
- Designed for interactive experimentation and play.
- Runs on a web server and is accessible via agno.com (formerly phidata.com), providing a graphical user interface where you can choose agents and test queries.
- Ideal for exploring and demonstrating the agents in an interactive web-based environment.

**MultiAgent.py:**
- Intended for direct execution in the VS Code terminal.
- Combines two specialized agents into one multi-agent and executes queries directly in the terminal.
- Suited for testing, debugging, or running scripted queries without the need for a web interface.
