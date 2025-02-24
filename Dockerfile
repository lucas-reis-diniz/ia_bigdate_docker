# Usando uma imagem base do Python
FROM python:3.9

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para dentro do container (incluindo o subdiretório sentiment_analysis)
COPY . /app

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Definindo o comando padrão ao rodar o container
CMD ["bash"]
