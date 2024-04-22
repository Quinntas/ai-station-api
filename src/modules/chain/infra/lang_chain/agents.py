from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

from src.modules.chain.infra.lang_chain.llm import prompt, llm_with_tools
from src.modules.chain.infra.lang_chain.tools import tools
from src.utils.env import env

agent = (
        {
            env.CHAIN_INPUT_KEY: lambda x: x[env.CHAIN_INPUT_KEY],
            env.CHAIN_SYSTEM_INPUT: lambda x: x[env.CHAIN_SYSTEM_INPUT],
            env.CHAIN_AGENT_SCRATCHPAD_KEY: lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
            ),
            env.CHAIN_MEMORY_KEY: lambda x: x[env.CHAIN_MEMORY_KEY],
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    handle_parsing_errors="Check your output and make sure it conforms, use the Action/Action Input syntax",
)
