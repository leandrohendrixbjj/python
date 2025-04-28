-- Deleta a tabela 'pessoa' se ela já existir
DROP TABLE IF EXISTS pessoa;

-- Cria a tabela 'pessoa' novamente
CREATE TABLE pessoa (
    id SERIAL PRIMARY KEY, -- Campo ID autoincremento
    nome VARCHAR(255) NOT NULL, -- Nome da pessoa
    data_criacao TIMESTAMP DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo')
    data_resposta TIMESTAMP -- Data de resposta, pode ser nula
);

-- Opcional: Inserir uma pessoa de exemplo
INSERT INTO pessoa (nome) VALUES ('Pessoa de Exemplo');

select * from pessoa;
