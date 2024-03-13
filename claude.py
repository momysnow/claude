from typing import List, Optional, Type

from cat.mad_hatter.decorators import tool, hook, plugin

from pydantic import BaseModel, ConfigDict, SecretStr

from datetime import datetime, date

from cat.factory.llm import LLMSettings

from langchain_anthropic import ChatAnthropic  # Importa la classe ChatAnthropic

class ClaudeConfig(LLMSettings):
    """La configurazione per il plugin Claude."""

    anthropic_api_key: Optional[SecretStr]

    model: str = "claude-3-opus-20240229"  # Specifica la versione di Claude

    max_tokens: Optional[int] = None  # Claude determina automaticamente il numero di token

    temperature: float = 0.7

    streaming: bool = True  # Claude supporta lo streaming

    _pyclass: Type = ChatAnthropic  # Usa la classe ChatAnthropic di langchain_anthropic

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Claude",
            "description": "Configurazione per Claude AI di Anthropic",
            "link": "https://www.anthropic.com/",
        }
    )

@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(ClaudeConfig)
    return allowed
