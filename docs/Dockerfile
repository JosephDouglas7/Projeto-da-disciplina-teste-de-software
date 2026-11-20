# Usa uma imagem oficial leve do Python baseada no Debian
FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc e garante logs em tempo real no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema operacional necessárias para:
# - Tkinter (python3-tk, tk-dev)
# - pyttsx3 no Linux (espeak-ng, libespeak1)
# - Áudio e Pygame (alsa-utils, pulseaudio, libsdl2-mixer-2.0-0, libsdl2-2.0-0)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    tk-dev \
    espeak-ng \
    libespeak1 \
    alsa-utils \
    pulseaudio \
    libsdl2-mixer-2.0-0 \
    libsdl2-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as bibliotecas Python utilizadas no código
RUN pip install --no-cache-dir \
    langdetect \
    matplotlib \
    pyttsx3 \
    pygame

# Copia o arquivo do seu código para dentro do container
# (Certifique-se de que o seu arquivo se chama IA_voz.py ou ajuste o nome abaixo)
COPY IA_voz.py .

# Comando para iniciar a aplicação
CMD ["python", "IA_voz.py"] 

# Como construir e executar (Importante para GUI e Áudio): 

#Construir a imagem:
docker build -t conversor-texto-audio .

Liberar o acesso à tela no host (Linux):
xhost +local:docker 

# Executar o container repassando vídeo e áudio: 

docker run --rm -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --device /dev/snd \
    conversor-texto-audio
