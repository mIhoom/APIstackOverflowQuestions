import requests
import json
import webbrowser

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "2022-04-20",
    "tagged" : "python",
    "min" : 15
}

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)
try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])