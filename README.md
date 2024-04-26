# deepgram_tts
A custom component for Home Assistant to use Deepgram's Text-To-Speech API with the Assist Integration. Right now the only way I've gotten this to work is by hardcoding the api key into the main tts.py file. When I find an error-free way to do this, I will update the repo.

## Installation
HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: mcshanesf/deepgram_tts, Category: Integration > Add > wait > Deepgram TTS > Install
<br><br>
Or manually copy deepgram_tts folder to /config/custom_components folder.

## Configuration
Add your api key to the following line in the tts.py file:   
``` yaml
class DeepgramProvider(Provider):
    """The Deepgram TTS API provider."""

    def __init__(self, hass, lang):
        """Initialize the provider."""
        self._hass = hass
        self._lang = lang
        self._api_key = "insert_your_api_key_here" #<---------
        self.name = "deepgram_tts"
```
Then add the following to the configuration.yaml file:
``` yaml
tts:
  - platform: deepgram_tts
```
## Model(Voice) Settings
To change the model(voice) used for the tts, edit the following code in the deepgram_tts.py file and restart Home Assistant. A list of available models can be found <a href="https://developers.deepgram.com/docs/tts-models">here.</a>
``` yaml
request_data = {'text': message}
        url = 'https://api.deepgram.com/v1/speak?model=aura-angus-en' ## Replace with your chosen model.
```

