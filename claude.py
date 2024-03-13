from typing import List, Optional, Type

from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain_anthropic import ChatAnthropic

class ClaudeConfig(LLMSettings):
    """La configurazione per il plugin Claude."""

    anthropic_api_key: Optional[SecretStr]
    model: str = "claude-3-opus-20240229"
    max_tokens: Optional[int] = 4000
    temperature: float = 0.7
    streaming: bool = True

    _pyclass: Type = ChatAnthropic

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Claude",
            "description": "Configurazione per Claude AI di Anthropic",
            "link": "https://www.anthropic.com/",
        }
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.llm = ChatAnthropic(temperature=self.temperature, anthropic_api_key=self.anthropic_api_key)

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(ClaudeConfig)
    return allowed
