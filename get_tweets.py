import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime
# Cadastrar as chaves de acesso

consumer_key = "O3cqQEQDtgtvfbQGuKQjojKmK"
consumer_secret = "CtxQ8WCUESXyTTCXBIdZ4imdV4GWY5TWRCv3tYbrPjoopuMvNY"

access_token = "1399157924744863746-g6RS4y8ywiYg4lj7zN6JfPm7NYTbSL"
access_token_secret = "8Ez0s371E74yJIt3eCFPNuj8LdCnNmjY1D4zoA0rnKUkL"

# Definir um arquivo de saida para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt", "w")

# Implementar uma classe para a conexão com twitter

class MyListener(StreamListener):

    def on_data(self, data):
        #print(data) Para imprimir na tela o que está sendo coletado
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True
    def on_error(self, status):
        print(status)

# Implementar nossa função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=["Bolsonaro"])