from typing import List, Optional, Type

from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, ConfigDict, SecretStr
from datetime import datetime, date
from cat.factory.llm import LLMSettings
from langchain_anthropic import ChatAnthropic

class ClaudeConfig(LLMSettings):
    """Setup for the Claude plugin."""

    anthropic_api_key: Optional[SecretStr]
    model: str = "claude-3-opus-20240229"
    max_tokens: Optional[int] = 4096
    temperature: float = 0.7
    streaming: bool = True

    _pyclass: Type = ChatAnthropic

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Claude",
            "description": "Setup for Anthropic's Claude AI",
            "link": "https://www.anthropic.com/",
        }
    )

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(ClaudeConfig)
    return allowed
