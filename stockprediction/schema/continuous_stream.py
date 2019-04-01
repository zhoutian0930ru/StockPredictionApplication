# using the intrinio library to get th ecurrent stock prices
from intriniorealtime.client import IntrinioRealtimeClient

def on_quote(quote, backlog):
    print("QUOTE: " , quote, "BACKLOG LENGTH: ", backlog)
    while True:
        print(quote.get())

options = {
    'username': 'a026fc2142bf458225ac545b32f611ed',
    'password': '8b284f775a32680a28c13b261660ed76',
    'channels':['MSFT'],
    'provider': 'iex',
    'on_quote': on_quote
}

client = IntrinioRealtimeClient(options)
client.connect()
client.keep_alive()
