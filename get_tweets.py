import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime
# Cadastrar as chaves de acesso

consumer_key = "XXX"
consumer_secret = "XXX"

access_token = "XXX"
access_token_secret = "XXX"

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
