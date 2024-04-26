# deepgram_tts
A custom component for Home Assistant to use Deepgram's Text-To-Speech API with the Assist Integration

## Installation
HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: mcshanesf/deepgram_tts, Category: Integration > Add > wait > Deepgram TTS > Install
<br><br>
Or manually copy deepgram_tts folder to /config/custom_components folder.

## Configuration
Add the following to your secrets.yaml file in the config folder:<br><br>

``` yaml
deepgram_api_key: "your_actual_deepgram_api_key_here"
```

Now add the following to your configuration.yaml file:

``` yaml
tts:
  - platform: deepgram_tts
    language: 'en-us'
    api_key: !secret deepgram_api_key
```

Restart Home Assistant and you should see deepgram_tts as an option in the Voice Assistant settings. 

## Model(Voice) Settings
To change the model(voice) used for the tts, edit the following code in the deepgram_tts.py file and restart Home Assistant. A list of available models can be found <a href="https://developers.deepgram.com/docs/tts-models">here.</a>
``` yaml
request_data = {'text': message}
        url = 'https://api.deepgram.com/v1/speak?model=aura-angus-en' ## Replace with your chosen model.
```

