import requests
from Adafruit_Thermal import *

QUOTES_API = "https://api.paperquotes.com/apiv1/qod/"
TOKEN = "deleted"

printer = Adafruit_Thermal()


def main():
    params = {"language": "English"}

    res = requests.get(
        QUOTES_API, params=params, headers={"Authorization": f"Token {TOKEN}"}
    )
    resJson = res.json()

    if res.status_code == 200:
        printer.print(
            f'Quote of the Day\n\n{resJson["quote"]}\n   - {resJson["author"]}'
        )
    else:
        printer.print("I couldn't get the quote of the day today.")


if __name__ == "__main__":
    main()
