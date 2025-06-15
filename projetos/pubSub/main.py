from google.cloud import pubsub_v1
import os

# Caminho da chave de autenticação
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"

# Variáveis do projeto e tópico
project_id = "graphic-fiber-452023-i7"
topic_id = "nps-topic-expresso"

def publish_message(message: str):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    # A mensagem precisa ser codificada em bytes
    data = message.encode("utf-8")
    
    # Publica a mensagem
    future = publisher.publish(topic_path, data)
    print(f"Mensagem publicada: {future.result()}")

if __name__ == "__main__":
    publish_message("Olá, Pub/Sub! Mensagem enviada com sucesso.")