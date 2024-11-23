# Escolhe a imagem base Python
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do seu projeto para dentro do container
COPY ./app /app/

# Define a variável de ambiente para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expõe a porta que o Flask vai usar
EXPOSE 5000

# Comando para rodar o Uvicorn no Flask
CMD ["gunicorn", "app:app"]
