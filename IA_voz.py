from collections import Counter
import os
import tkinter as tk
from tkinter import filedialog, messagebox

from langdetect import DetectorFactory, detect
import matplotlib.pyplot as plt
import pyttsx3

# Garante resultados consistentes na detecção do idioma
DetectorFactory.seed = 0

# Inicializa o motor TTS local (pyttsx3)
engine = pyttsx3.init()


def configurar_voz(idioma):
  """Configura a velocidade padrão e tenta selecionar uma voz feminina com base no idioma."""
  engine.setProperty("rate", 180)  # Velocidade normal

  # Buscar vozes disponíveis no sistema operacional
  voices = engine.getProperty("voices")
  voz_escolhida = None

  for voice in voices:
    nome_voz = voice.name.lower()
    # Tenta filtrar por vozes femininas comuns ou pelo idioma selecionado
    if idioma == "pt":
      if any(
          termo in nome_voz
          for termo in ["maria", "helena", "lucia", "zira", "female", "pt-br"]
      ):
        voz_escolhida = voice.id
        break
    elif idioma == "en":
      if any(
          termo in nome_voz
          for termo in [
              "zira",
              "hazel",
              "susan",
              "catherine",
              "female",
              "en-us",
              "en_us",
          ]
      ):
        voz_escolhida = voice.id
        break

  # Se não achar uma específica pelo nome, pega a primeira voz disponível do idioma correspondente
  if not voz_escolhida and voices:
    for voice in voices:
      if idioma in voice.id.lower() or idioma in voice.languages:
        voz_escolhida = voice.id
        break

  # Se ainda assim não encontrar, usa a segunda voz (geralmente feminina em sistemas Windows) ou a primeira
  if not voz_escolhida:
    voz_escolhida = voices[1].id if len(voices) > 1 else voices[0].id

  engine.setProperty("voice", voz_escolhida)


def validar_idioma_texto(texto, idioma_selecionado):
  """Verifica se o idioma detectado no texto corresponde ao idioma selecionado no menu.

  Retorna (True, "") se for válido, ou (False, mensagem_erro) se for inválido.
  """
  try:
    idioma_detectado = detect(texto)

    # Bloqueia texto em português com idioma selecionado em inglês
    if idioma_selecionado == "en" and idioma_detectado == "pt":
      return (
          False,
          (
              "O texto digitado está em Português, mas a opção selecionada é"
              " Inglês.\nAjuste o idioma ou altere o texto."
          ),
      )

    # Bloqueia texto em inglês com idioma selecionado em português
    if idioma_selecionado == "pt" and idioma_detectado == "en":
      return (
          False,
          (
              "O texto digitado está em Inglês, mas a opção selecionada é"
              " Português.\nAjuste o idioma ou altere o texto."
          ),
      )

  except Exception:
    pass

  return True, ""


def converter_texto():
  global ultimo_arquivo
  texto = entrada.get("1.0", tk.END).strip()
  idioma = idioma_var.get()

  if not texto:
    messagebox.showwarning("Aviso", "Digite algum texto antes de converter.")
    return

  # Validação do idioma do texto x idioma selecionado
  valido, mensagem_erro = validar_idioma_texto(texto, idioma)
  if not valido:
    messagebox.showerror("Idioma Incompatível", mensagem_erro)
    return

  # Configura a voz (feminina e velocidade padrão)
  configurar_voz(idioma)

  ultimo_arquivo = "saida.mp3"

  # Salva o arquivo de áudio usando o pyttsx3
  engine.save_to_file(texto, ultimo_arquivo)
  engine.runAndWait()

  # Reproduz o áudio gerado
  if os.name == "nt":  # Windows
    os.system(f"start {ultimo_arquivo}")
  else:  # Linux/Mac
    os.system(f"xdg-open {ultimo_arquivo}")

  messagebox.showinfo("Sucesso", "Áudio gerado e reproduzido!")

  # Gerar gráfico de frequência de letras
  gerar_grafico_letras(texto)


def salvar_audio():
  if ultimo_arquivo and os.path.exists(ultimo_arquivo):
    destino = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("Arquivos MP3", "*.mp3")],
        title="Salvar áudio como",
    )
    if destino:
      try:
        with open(ultimo_arquivo, "rb") as f_origem, open(
            destino, "wb"
        ) as f_destino:
          f_destino.write(f_origem.read())
        messagebox.showinfo("Sucesso", f"Áudio salvo em:\n{destino}")
      except Exception as e:
        messagebox.showerror(
            "Erro", f"Não foi possível salvar o arquivo:\n{e}"
        )
  else:
    messagebox.showwarning("Aviso", "Nenhum áudio foi gerado ainda.")


def gerar_grafico_letras(texto):
  letras = [c.lower() for c in texto if c.isalpha()]
  contagem = Counter(letras)

  if not contagem:
    messagebox.showwarning(
        "Aviso", "O texto não contém letras suficientes para gerar o gráfico."
    )
    return

  total_palavras = len(texto.split())
  total_letras = len(letras)
  media_frequencia = sum(contagem.values()) / len(contagem)

  plt.figure(figsize=(10, 6))
  plt.bar(contagem.keys(), contagem.values(), color="lightgreen")
  plt.axhline(
      y=media_frequencia,
      color="red",
      linestyle="--",
      linewidth=1.5,
      label=f"Média de Referência (Normalidade): {media_frequencia:.1f}",
  )
  plt.title(
      f"Frequência de Letras\n(Total de Palavras: {total_palavras} | Total de"
      f" Letras: {total_letras})",
      fontsize=12,
  )
  plt.xlabel("Letras")
  plt.ylabel("Quantidade")
  plt.legend()
  plt.tight_layout()
  plt.show()


# Interface gráfica
janela = tk.Tk()
janela.title("Texto para Áudio")

entrada = tk.Text(janela, height=20, width=100)
entrada.pack(pady=10)

# Frame para controles (idioma centralizado)
controles_frame = tk.Frame(janela)
controles_frame.pack(pady=5, fill=tk.X, padx=20)

controles_frame.grid_columnconfigure(0, weight=1)
controles_frame.grid_columnconfigure(1, weight=1)
controles_frame.grid_columnconfigure(2, weight=1)

# Seleção de idioma (Centralizado - Coluna 1)
idioma_var = tk.StringVar(value="pt")
menu_idioma = tk.OptionMenu(controles_frame, idioma_var, "pt", "en")
menu_idioma.grid(row=0, column=1, padx=5, sticky="n")

botao_converter = tk.Button(
    janela, text="Converter para Áudio", command=converter_texto
)
botao_converter.pack(pady=5)

botao_salvar = tk.Button(janela, text="Salvar Áudio", command=salvar_audio)
botao_salvar.pack(pady=5)

ultimo_arquivo = None

janela.mainloop()
