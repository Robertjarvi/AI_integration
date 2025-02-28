from slack_bolt import App

app = App(token="xoxb-your-slack-bot-token")

@app.event("app_mention")
def handle_mention(event, say):
    say("Bonjour ! Je suis prêt à exécuter votre script.")

if __name__ == "__main__":
    app.start(port=3000)
