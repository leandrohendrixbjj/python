from app.pubsub_client import PubSubPublisher

if __name__ == "__main__":
    pubsub = PubSubPublisher('nps-topic-padrao')

    msg = "Olá, Pub/Sub com melhorias!"
    atributos = {
        "origem": "app-python",
        "tipo": "mensagem-de-teste"
    }

    pubsub.publish(msg, attributes=atributos)
