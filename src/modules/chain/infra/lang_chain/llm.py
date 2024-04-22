from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from src.modules.chain.infra.lang_chain.tools import tools
from src.utils.env import env


# TODO: Implement change model strategy
# TODO: if is external api, care about rate limit
class LLMStrategy:
    def __init__(self, chat_model: BaseChatModel):
        self.llm = chat_model


llm_strategy = LLMStrategy(
    ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.6, openai_api_key=env.OPENAI_KEY))

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "{system_input}"
    ),
    MessagesPlaceholder(variable_name=env.CHAIN_MEMORY_KEY),
    (
        "user",
        "{input}"
    ),
    MessagesPlaceholder(variable_name=env.CHAIN_AGENT_SCRATCHPAD_KEY),
])

llm_with_tools = llm_strategy.llm.bind_tools(tools)
