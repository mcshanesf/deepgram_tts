import logging
import asyncio
import aiohttp
import async_timeout
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    _LOGGER.debug("Setting up deepgram_tts platform")

SUPPORT_LANGUAGES = ["en-US"]
DEFAULT_LANG = "en-US"
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
})

def get_engine(hass, config, discovery_info=None):
    """Set up the TTS engine."""
    lang = config.get(CONF_LANG, DEFAULT_LANG)
    return DeepgramProvider(hass, lang)


class DeepgramProvider(Provider):
    """The Deepgram TTS API provider."""

    def __init__(self, hass, lang):
        """Initialize the provider."""
        self._hass = hass
        self._lang = lang
        self._api_key = "insert_your_api_key_here"
        self.name = "deepgram_tts"

    @property
    def default_language(self):
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    async def async_get_tts_audio(self, message, language, options=None):
        """Load TTS using Deepgram API."""
        websession = async_get_clientsession(self._hass)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self._api_key}'
        }
        request_data = {'text': message}
        url = 'https://api.deepgram.com/v1/speak?model=aura-angus-en'

        try:
            async with async_timeout.timeout(10):
                response = await websession.post(url, json=request_data, headers=headers)

                if response.status != 200:
                    _LOGGER.error("Error %d on load url %s", response.status, response.url)
                    return (None, None)
                response_data = await response.read()

        except (asyncio.TimeoutError, aiohttp.ClientError) as e:
            _LOGGER.error("Timeout or error while connecting to Deepgram TTS API: %s", e)
            return (None, None)

        if response_data:
            return ("mp3", response_data)  # Assuming Deepgram returns MP3 audio format
        return (None, None)
