import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if "TRANSLATOR_KEY" not in current_app.config or not current_app.config["TRANSLATOR_KEY"]:
        return _("ERROR: the translation service is not configured.")
    auth = {
        "Ocp-Apim-Subscription-Key": current_app.config["TRANSLATOR_KEY"],
        "Ocp-Apim-Subsciption-Region": "koreacentral",
    }
    r = requests.post(
        f"https://api.cognitive.microsoft.translator.com/translate?api-version=3.0&from={source_language}&to={dest_language}",
        headers=auth,
        json=[{"Text": text}],
    )
    if r.status_code != 200:
        return _("ERROR: the translation service failed.")
    return r.json()[0]["translations"][0]["text"]
