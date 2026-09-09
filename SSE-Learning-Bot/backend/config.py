"""Configuration and settings for SSE Learning Bot backend."""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings loaded from environment."""
    
    # AI / LLM (Gemini)
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    
    # Deepgram (STT and TTS)
    deepgram_api_key: str = os.getenv("DEEPGRAM_API_KEY", "")
    deepgram_stt_model: str = os.getenv("DEEPGRAM_STT_MODEL", "nova-3")
    deepgram_tts_model: str = os.getenv("DEEPGRAM_TTS_MODEL", "aura-asteria-en")
    
    # Fallbacks / Proxies
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_llm_model: str = os.getenv("OPENAI_LLM_MODEL", "gpt-4o-mini")
    BASE_URL: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
    
    @property
    def openrouter_api_key(self) -> str:
        load_dotenv(override=True)
        return os.getenv("OPENROUTER_API_KEY", "").strip('"').strip("'")

    @property
    def openrouter_model(self) -> str:
        load_dotenv(override=True)
        return os.getenv("OPENROUTER_MODEL", "nvidia/llama-3.1-nemotron-70b-instruct:free").strip('"').strip("'")

    @property
    def openrouter_base_url(self) -> str:
        load_dotenv(override=True)
        return os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1").strip('"').strip("'")

    @property
    def tavily_api_key(self) -> str:
        load_dotenv(override=True)
        return os.getenv("TAVILY_API_KEY", "").strip('"').strip("'")

    @classmethod
    def reload(cls):
        """Reload settings from environment."""
        load_dotenv(override=True)


# Global settings instance
settings = Settings()

