import mysql.connector
from sqlalchemy import create_engine


DATABASE_URL = "mysql+mysqlconnector://admin:1234@localhost/fastapi"
engine = create_engine(DATABASE_URL, echo=True)

conn = engine.connect()

query = """
USE fastapi;

INSERT INTO Acessos (CodPerfil, CodTransacao, Inclui, Altera, Exclui, Executa)
VALUES (2, 13, NULL, NULL, NULL, NULL),
        (2, 14, NULL, NULL, NULL, NULL),
        (2, 15, NULL, NULL, NULL, NULL),
        (3, 1, NULL, NULL, NULL, NULL),
        (3, 2, NULL, NULL, NULL, NULL),
        (3, 3, NULL, NULL, NULL, NULL),
        (3, 4, NULL, NULL, NULL, NULL),
        (3, 5, NULL, NULL, NULL, NULL),
        (3, 6, NULL, NULL, NULL, NULL),
        (3, 7, NULL, NULL, NULL, NULL),
        (3, 8, NULL, NULL, NULL, NULL),
        (3, 9, NULL, NULL, NULL, NULL),
        (3, 10, NULL, NULL, NULL, NULL),
        (3, 11, NULL, NULL, NULL, NULL),
        (3, 12, NULL, NULL, NULL, NULL),
        (3, 13, NULL, NULL, NULL, NULL),
        (3, 14, NULL, NULL, NULL, NULL),
        (3, 15, NULL, NULL, NULL, NULL),
        (4, 1, NULL, NULL, NULL, NULL),
        (4, 2, NULL, NULL, NULL, NULL),
        (4, 3, NULL, NULL, NULL, NULL),
        (4, 4, NULL, NULL, NULL, NULL),
        (5, 1, NULL, NULL, NULL, NULL),
        (5, 2, NULL, NULL, NULL, NULL),
        (5, 3, NULL, NULL, NULL, NULL),
        (5, 4, NULL, NULL, NULL, NULL),
        (5, 5, NULL, NULL, NULL, NULL),
        (5, 6, NULL, NULL, NULL, NULL),
        (5, 7, NULL, NULL, NULL, NULL),
        (5, 8, NULL, NULL, NULL, NULL),
        (5, 9, NULL, NULL, NULL, NULL),
        (5, 10, NULL, NULL, NULL, NULL),
        (5, 11, NULL, NULL, NULL, NULL),
        (5, 12, NULL, NULL, NULL, NULL),
        (5, 13, NULL, NULL, NULL, NULL),
        (5, 14, NULL, NULL, NULL, NULL),
        (5, 15, NULL, NULL, NULL, NULL),
        (6, 1, NULL, NULL, NULL, NULL),
        (6, 2, NULL, NULL, NULL, NULL),
        (6, 3, NULL, NULL, NULL, NULL),
        (6, 4, NULL, NULL, NULL, NULL),
        (6, 5, NULL, NULL, NULL, NULL),
        (6, 6, NULL, NULL, NULL, NULL),
        (6, 7, NULL, NULL, NULL, NULL),
        (6, 8, NULL, NULL, NULL, NULL),
        (6, 9, NULL, NULL, NULL, NULL),
        (6, 10, NULL, NULL, NULL, NULL),
        (6, 11, NULL, NULL, NULL, NULL),
        (6, 12, NULL, NULL, NULL, NULL),
        (6, 13, NULL, NULL, NULL, NULL),
        (6, 14, NULL, NULL, NULL, NULL),
        (6, 15, NULL, NULL, NULL, NULL);

SET IDENTITY_INSERT Perfis ON;

INSERT INTO Perfis (CodPerfil, DescPerfil, PerfilAdministrador, DataAtualizacao)
VALUES (1, 'Administrador', 'S', '2024-01-09 18:06:48.230'),
       (2, 'Adm', 'N', '2024-01-05 18:56:14.110'),
       (3, 'Coord', 'N', '2024-01-05 18:56:25.157'),
       (4, 'Associados', 'N','2024-01-03 16:23:49.620'),
       (5, 'Presidente', 'N', '2024-01-04 17:34:13.110'),
       (6, 'Diretoria', 'N', N'2024-01-04 17:34:43.763');

SET IDENTITY_INSERT Perfis OFF;
SET IDENTITY_INSERT Transacoes ON;

INSERT INTO Transacoes (CodTransacao, DescTransacao, TipoTransacao, DataAtualizacao)
VALUES  (1, 'Utilitários', 'Menu', '2023-12-28 19:52:49.310'),
        (2, 'Utilitários - Segurança', 'Menu', '2023-12-28 19:53:18.237'),
        (3, 'Utilitários - Segurança - Transações', 'Tela/Botão', '2023-12-28 19:53:35.577'),
        (4, 'Utilitários - Segurança - Perfis', 'Tela/Botão', '2023-12-28 19:54:21.513'),
        (5, 'Associado', 'Tela/Botão	', '2024-01-03 16:41:55.377'),
        (6, 'Adicionais_SAERJ', 'Tela/Botão	', '2024-01-03 16:42:37.423'),
        (7, 'Pagamentos', 'Tela/Botão	', '2024-01-03 16:42:58.207'),
        (8, 'Empresas', 'Tela/Botão	', '2024-01-03 16:43:19.953'),
        (9, 'Protocolos', 'Tela/Botão	', '2024-01-03 16:43:35.737'),
        (10, 'Eleicoes', 'Tela/Botão	', '2024-01-03 16:44:01.253'),
        (11, 'Chapas_Eleicoes', 'Tela/Botão	', '2024-01-03 16:44:16.643'),
        (12, 'Diretorias', 'Tela/Botão	', '2024-01-03 16:44:31.940'),
        (13, 'Logs', 'Tela/Botão	', '2024-01-03 16:44:52.220'),
        (14, 'Parametros', 'Tela/Botão	', '2024-01-03 16:45:10.237'),
        (15, 'Tabelas', 'Tela/Botão	', '2024-01-03 16:45:32.220'),
        (16, 'Utilitários - Segurança - Usuários', 'Tela/Botão', '2024-01-09 18:06:32.340');
SET IDENTITY_INSERT Transacoes OFF;
SET IDENTITY_INSERT Usuarios ON;

INSERT INTO Usuarios (Numero, Iniciais, CodPerfil, Nome, Email, Status, Senha, IdRecuperaSenha, ResetouSenha) 
VALUES  (1, 'ADMI', 1, 'Administrador', 'adelino.vale@informaker.com.br', 'A', 0x0100DDE24E4211EDA1B7B44C734750DAABC8D0BB741974F94A10, NULL, NULL),
        (2, 'TSA', 3, 'Tania Santos de Andrade Barbosa', 'tania@saerj.org.br', 'A', 0x010037C87C3E07007B41D5FAFEF55C3E72360E9C6C34F74F4102, NULL, NULL),
        (3, 'ALM', 2, 'Andrea Laino Marinho', 'deia402010@gmail.com', 'A', 0x01005F2D4B5131E189E8A39FD9C28F10AD2852704E67D3F8266D, NULL, NULL),
        (4, 'MAA', 2, 'Marcelo Artur Almeida Santos', 'marceloartur.santos@gmail.com', 'A', 0x0100280DC044637265A84592491C5C755964AD0A21EBC2266BB5, NULL, NULL),
        (5, 'JAC', 5, 'Jorge de Albuquerque Calasans Maia', 'jorgecalasans@gmail.com', 'A', 0x0100828065524C93A6F7281B5F959CD845DEAB79077BE2B85075, NULL, NULL),
        (6, 'FLV', 6, 'Flavio Lobianco Vicente', 'flalobi@gmail.com', 'A', 0x01003596A238B9CCF1A24109C8E65E34AF19223552C357B64DB4, NULL, NULL),
        (7, 'PAB', 6, 'Patricia Arguelles Betim Paes Leme', 'patpleme@gmail.com', 'A', 0x01003D041E448984374D90F6E5B88BC39AEBC7C3D057D1581BB9, NULL, NULL);
        
SET IDENTITY_INSERT Usuarios OFF;


"""

# Execute o script SQL
conn.execute(query)

# Feche a conexão
conn.close()