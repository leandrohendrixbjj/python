import os
import logging
from google.cloud import pubsub_v1
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PubSubPublisher:
    def __init__(self, topic_id: str):
        
        # Credenciais, Projeto e Tópico
        self._credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self._project_id = os.getenv("PUBSUB_PROJECT_ID")
        self.topic_id = topic_id

        # Valdação: Credenciais, Projeto e Tópico
        self._validate_init_params()
        
        # Publicação
        self._publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(self.project_id, self.topic_id)

    @property
    def project_id(self):
        return self._project_id

    @property
    def publisher(self):
        return self._publisher    
    
    def _validate_init_params(self):
        if not self._credentials_path:
            raise ValueError("Variável de ambiente GOOGLE_APPLICATION_CREDENTIALS não definida.")
        if not self._project_id:
            raise ValueError("Variável de ambiente PUBSUB_PROJECT_ID não definida.")
        if not self.topic_id:
            raise ValueError("O nome do tópico não pode ser vazio.")


    def publish(self, message: str, attributes: dict = None):

        if not message:
            raise ValueError("A mensagem não pode ser vazia.")        
        
        try:
            data = message.encode("utf-8")
            future = self.publisher.publish(self.topic_path, data, **(attributes or {}))
            message_id = future.result()
            logger.info(f"Mensagem publicada com ID: {message_id}")
            return message_id
        except Exception as e:
            logger.error(f"Erro ao publicar mensagem: {e}")
            raise
