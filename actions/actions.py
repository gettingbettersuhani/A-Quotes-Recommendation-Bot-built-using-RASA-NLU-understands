import pandas as pd
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionQuote(Action):

    def name(self):
        return "action_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):

        user_message = tracker.latest_message.get("text")

        df = pd.read_csv("dataset/quotes.csv")

        category = "motivation"

        if "sad" in user_message:
            category = "sad"
        elif "happy" in user_message:
            category = "happy"
        elif "motivate" in user_message:
            category = "motivation"

        quotes = df[df["category"] == category]

        quote = quotes.sample()["quote"].values[0]

        dispatcher.utter_message(text=quote)

        return []