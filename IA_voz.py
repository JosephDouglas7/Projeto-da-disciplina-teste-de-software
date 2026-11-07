from collections import Counter
import os
import re
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from langdetect import DetectorFactory, detect
import matplotlib.pyplot as plt
import pyttsx3

# Tentativa de inicializar o pygame para controle de áudio embutido
USAR_PYGAME = False
try:
  import pygame

  pygame.mixer.init()
  USAR_PYGAME = True
except Exception as e:
  print(f"Pygame não disponível ou sem suporte a áudio: {e}")

# Garante detecção consistente de idioma
DetectorFactory.seed = 0


class AppTextoParaAudio:

  def __init__(self, root):
    self.root = root
    self.root.title("Acessibilidade: Conversor de Texto para Áudio Suave")
    self.root.geometry("840x760")
    self.root.minsize(680, 540)

    self.ultimo_arquivo = os.path.abspath("saida.wav")
    self.audio_gerado = False
    self.processando = False

    self._criar_interface()
    self._configurar_navegacao_teclado()

  def _criar_interface(self):
    main_frame = ttk.Frame(self.root, padding="15")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 1. Rótulo e Campo de Texto com Scrollbar
    lbl_texto = ttk.Label(
        main_frame,
        text="Texto para conversão (Pressione Tab para navegar entre os campos):",
        font=("Segoe UI", 10, "bold"),
    )
    lbl_texto.pack(anchor="w", pady=(0, 5))

    frame_texto = ttk.Frame(main_frame)
    frame_texto.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

    self.scrollbar = ttk.Scrollbar(frame_texto, orient=tk.VERTICAL)
    self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    self.entrada = tk.Text(
        frame_texto,
        height=7,
        wrap=tk.WORD,
        font=("Segoe UI", 10),
        yscrollcommand=self.scrollbar.set,
    )
    self.entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.scrollbar.config(command=self.entrada.yview)

    # 2. Controles de Idioma e Suavidade da Voz (Sliders)
    frame_ajustes = ttk.LabelFrame(
        main_frame, text="Configurações de Voz e Suavidade", padding="10"
    )
    frame_ajustes.pack(fill=tk.X, pady=(0, 10))

    # Linha 1: Idioma e Autoplay
    linha_idioma = ttk.Frame(frame_ajustes)
    linha_idioma.pack(fill=tk.X, pady=(0, 8))

    lbl_idioma = ttk.Label(linha_idioma, text="Idioma:")
    lbl_idioma.pack(side=tk.LEFT, padx=(0, 5))

    self.idioma_var = tk.StringVar(value="pt")
    self.combo_idioma = ttk.Combobox(
        linha_idioma,
        textvariable=self.idioma_var,
        values=["pt", "en"],
        state="readonly",
        width=8,
    )
    self.combo_idioma.pack(side=tk.LEFT, padx=(0, 20))

    self.autoplay_var = tk.BooleanVar(value=False)
    chk_autoplay = ttk.Checkbutton(
        linha_idioma,
        text="Reproduzir áudio automaticamente",
        variable=self.autoplay_var,
    )
    chk_autoplay.pack(side=tk.RIGHT)

    # Linha 2: Sliders de Velocidade (Ritmo) e Volume
    linha_sliders = ttk.Frame(frame_ajustes)
    linha_sliders.pack(fill=tk.X)

    # Velocidade / Ritmo (Padrão 145 wpm = tom suave e natural)
    lbl_vel = ttk.Label(
        linha_sliders, text="Velocidade (Ritmo):", font=("Segoe UI", 9)
    )
    lbl_vel.grid(row=0, column=0, sticky="w", padx=(0, 5))

    self.vel_var = tk.IntVar(value=145)
    self.slider_vel = ttk.Scale(
        linha_sliders,
        from_=110,
        to=200,
        variable=self.vel_var,
        orient=tk.HORIZONTAL,
        command=lambda v: self.lbl_vel_val.config(text=f"{int(float(v))} ppm"),
    )
    self.slider_vel.grid(row=0, column=1, sticky="ew", padx=5)

    self.lbl_vel_val = ttk.Label(
        linha_sliders,
        text="145 ppm (Suave)",
        width=15,
        font=("Segoe UI", 9, "italic"),
    )
    self.lbl_vel_val.grid(row=0, column=2, sticky="w", padx=(5, 20))

    # Volume (Padrão 90% para evitar estalos)
    lbl_vol = ttk.Label(linha_sliders, text="Volume:", font=("Segoe UI", 9))
    lbl_vol.grid(row=0, column=3, sticky="w", padx=(0, 5))

    self.vol_var = tk.DoubleVar(value=0.90)
    self.slider_vol = ttk.Scale(
        linha_sliders,
        from_=0.3,
        to=1.0,
        variable=self.vol_var,
        orient=tk.HORIZONTAL,
        command=lambda v: self.lbl_vol_val.config(
            text=f"{int(float(v) * 100)}%"
        ),
    )
    self.slider_vol.grid(row=0, column=4, sticky="ew", padx=5)

    self.lbl_vol_val = ttk.Label(
        linha_sliders, text="90%", width=6, font=("Segoe UI", 9)
    )
    self.lbl_vol_val.grid(row=0, column=5, sticky="w")

    linha_sliders.columnconfigure(1, weight=1)
    linha_sliders.columnconfigure(4, weight=1)

    # 3. Ações Principais
    frame_acoes = ttk.Frame(main_frame)
    frame_acoes.pack(fill=tk.X, pady=(0, 10))

    self.btn_converter = ttk.Button(
        frame_acoes,
        text="Converter para Áudio (Alt+C)",
        command=self.iniciar_conversao,
        underline=14,
    )
    self.btn_converter.pack(side=tk.LEFT, padx=(0, 10))

    self.btn_salvar = ttk.Button(
        frame_acoes,
        text="Salvar Arquivo de Áudio (Alt+S)",
        command=self.salvar_audio,
        state=tk.DISABLED,
        underline=0,
    )
    self.btn_salvar.pack(side=tk.LEFT)

    # 4. Player de Áudio Embutido
    frame_player = ttk.LabelFrame(
        main_frame, text="Controles de Áudio Embutidos", padding="10"
    )
    frame_player.pack(fill=tk.X, pady=(0, 10))

    self.btn_play = ttk.Button(
        frame_player,
        text="▶ Ouvir Áudio",
        command=self.reproduzir_audio,
        state=tk.DISABLED,
    )
    self.btn_play.pack(side=tk.LEFT, padx=(0, 5))

    self.btn_pause = ttk.Button(
        frame_player,
        text="⏸ Pausar/Retomar",
        command=self.pausar_audio,
        state=tk.DISABLED,
    )
    self.btn_pause.pack(side=tk.LEFT, padx=(0, 5))

    self.btn_stop = ttk.Button(
        frame_player,
        text="⏹ Parar",
        command=self.parar_audio,
        state=tk.DISABLED,
    )
    self.btn_stop.pack(side=tk.LEFT)

    # 5. Estatísticas e Tabela Textual
    frame_stats = ttk.LabelFrame(
        main_frame,
        text="Estatísticas do Texto e Alternativa Textual",
        padding="10",
    )
    frame_stats.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

    self.lbl_resumo = ttk.Label(
        frame_stats,
        text="Resumo: Nenhum texto processado.",
        font=("Segoe UI", 9, "bold"),
    )
    self.lbl_resumo.pack(anchor="w", pady=(0, 5))

    colunas = ("letra", "quantidade", "porcentagem")
    self.tabela_frequencia = ttk.Treeview(
        frame_stats, columns=colunas, show="headings", height=4
    )
    self.tabela_frequencia.heading("letra", text="Caractere / Letra")
    self.tabela_frequencia.heading("quantidade", text="Ocorrências")
    self.tabela_frequencia.heading(
        "porcentagem", text="Proporção Relativa (%)"
    )

    self.tabela_frequencia.column("letra", anchor="center", width=120)
    self.tabela_frequencia.column("quantidade", anchor="center", width=120)
    self.tabela_frequencia.column("porcentagem", anchor="center", width=120)

    scroll_tabela = ttk.Scrollbar(
        frame_stats, orient=tk.VERTICAL, command=self.tabela_frequencia.yview
    )
    self.tabela_frequencia.configure(yscrollcommand=scroll_tabela.set)

    self.tabela_frequencia.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scroll_tabela.pack(side=tk.RIGHT, fill=tk.Y)

    self.btn_grafico = ttk.Button(
        main_frame,
        text="Abrir Gráfico Visual Opcional",
        command=self.exibir_grafico_visual,
        state=tk.DISABLED,
    )
    self.btn_grafico.pack(anchor="e", pady=(0, 5))

    # 6. Barra de Status
    self.status_var = tk.StringVar(value="Pronto.")
    self.barra_status = ttk.Label(
        self.root,
        textvariable=self.status_var,
        relief=tk.SUNKEN,
        anchor="w",
        padding=5,
    )
    self.barra_status.pack(side=tk.BOTTOM, fill=tk.X)

    self.root.bind("<Alt-c>", lambda e: self.iniciar_conversao())
    self.root.bind("<Alt-s>", lambda e: self.salvar_audio())

  def _configurar_navegacao_teclado(self):
    def foco_proximo(event):
      event.widget.tk_focusNext().focus()
      return "break"

    def foco_anterior(event):
      event.widget.tk_focusPrev().focus()
      return "break"

    self.entrada.bind("<Tab>", foco_proximo)
    self.entrada.bind("<Shift-Tab>", foco_anterior)

  def atualizar_status(self, mensagem):
    self.status_var.set(mensagem)
    self.root.update_idletasks()

  def suavizar_texto(self, texto):
    """Insere pausas naturais e remove quebras bruscas para a voz soar fluida."""
    # Substitui quebras de linha múltiplas por uma pausa de pontuação
    texto_tratado = re.sub(r"\n+", ". ", texto)
    # Garante espaço após pontuações para o motor respirar
    texto_tratado = re.sub(r"([,.!?;:])(?=[^\s])", r"\1 ", texto_tratado)
    # Remove espaços duplos
    texto_tratado = re.sub(r"\s+", " ", texto_tratado).strip()
    return texto_tratado

  def selecionar_voz_adequada(self, engine, idioma):
    """Seleciona prioritariamente vozes mais suaves e modernas."""
    voices = engine.getProperty("voices")
    voz_escolhida = None

    # Lista de termos priorizados por ordem de naturalidade e suavidade
    prioridades_pt = [
        "francisca",
        "helena",
        "maria",
        "lucia",
        "brazil",
        "portuguese",
    ]
    prioridades_en = [
        "jenny",
        "aria",
        "zira",
        "hazel",
        "susan",
        "english",
        "en-us",
    ]

    termos = prioridades_pt if idioma == "pt" else prioridades_en

    for termo in termos:
      for voice in voices:
        nome = voice.name.lower()
        voz_id = voice.id.lower()
        if termo in nome or termo in voz_id:
          voz_escolhida = voice.id
          break
      if voz_escolhida:
        break

    if not voz_escolhida and voices:
      for voice in voices:
        if idioma in voice.id.lower() or (
            hasattr(voice, "languages") and idioma in voice.languages
        ):
          voz_escolhida = voice.id
          break

    if not voz_escolhida and voices:
      voz_escolhida = voices[0].id

    if voz_escolhida:
      engine.setProperty("voice", voz_escolhida)

  def validar_idioma_texto(self, texto, idioma_selecionado):
    try:
      idioma_detectado = detect(texto)
      if idioma_selecionado == "en" and idioma_detectado == "pt":
        return (
            False,
            (
                "O texto digitado parece estar em Português, mas a opção"
                " selecionada é Inglês.\nAjuste o idioma antes de converter."
            ),
        )
      if idioma_selecionado == "pt" and idioma_detectado == "en":
        return (
            False,
            (
                "O texto digitado parece estar em Inglês, mas a opção"
                " selecionada é Português.\nAjuste o idioma antes de converter."
            ),
        )
    except Exception:
      pass
    return True, ""

  def liberar_bloqueio_audio(self):
    if USAR_PYGAME and pygame.mixer.get_init():
      try:
        pygame.mixer.music.stop()
        if hasattr(pygame.mixer.music, "unload"):
          pygame.mixer.music.unload()
      except Exception:
        pass

  def iniciar_conversao(self):
    if self.processando:
      return

    texto_original = self.entrada.get("1.0", tk.END).strip()
    idioma = self.idioma_var.get()
    velocidade = int(self.vel_var.get())
    volume = float(self.vol_var.get())

    if not texto_original:
      messagebox.showwarning(
          "Campo Vazio", "Por favor, digite algum texto antes de converter."
      )
      self.entrada.focus()
      return

    valido, mensagem_erro = self.validar_idioma_texto(texto_original, idioma)
    if not valido:
      messagebox.showerror("Incompatibilidade de Idioma", mensagem_erro)
      return

    self.liberar_bloqueio_audio()

    self.processando = True
    self.btn_converter.config(state=tk.DISABLED)
    self.btn_play.config(state=tk.DISABLED)
    self.btn_pause.config(state=tk.DISABLED)
    self.btn_stop.config(state=tk.DISABLED)
    self.atualizar_status("Gerando áudio suave... Aguarde.")

    # Suaviza a pontuação do texto para dicção fluida
    texto_processado = self.suavizar_texto(texto_original)

    thread = threading.Thread(
        target=self._executar_sintese,
        args=(texto_original, texto_processado, idioma, velocidade, volume),
        daemon=True,
    )
    thread.start()

  def _executar_sintese(
      self, texto_original, texto_audio, idioma, velocidade, volume
  ):
    try:
      engine = pyttsx3.init()
      # Configura o ritmo mais calmo e o volume calibrado
      engine.setProperty("rate", velocidade)
      engine.setProperty("volume", volume)

      self.selecionar_voz_adequada(engine, idioma)

      if os.path.exists(self.ultimo_arquivo):
        try:
          os.remove(self.ultimo_arquivo)
        except Exception:
          pass

      engine.save_to_file(texto_audio, self.ultimo_arquivo)
      engine.runAndWait()
      engine.stop()

      if (
          not os.path.exists(self.ultimo_arquivo)
          or os.path.getsize(self.ultimo_arquivo) == 0
      ):
        raise RuntimeError("O arquivo de áudio não pôde ser gerado.")

      self.root.after(0, self._conclusao_sintese, texto_original, True, "")
    except Exception as e:
      self.root.after(0, self._conclusao_sintese, texto_original, False, str(e))

  def _conclusao_sintese(self, texto_original, sucesso, erro):
    self.processando = False
    self.btn_converter.config(state=tk.NORMAL)

    if not sucesso:
      self.atualizar_status("Erro ao sintetizar áudio.")
      messagebox.showerror(
          "Falha na Síntese", f"Ocorreu um erro ao gerar o áudio:\n{erro}"
      )
      return

    self.audio_gerado = True
    self.btn_salvar.config(state=tk.NORMAL)
    self.btn_play.config(state=tk.NORMAL)
    self.btn_grafico.config(state=tk.NORMAL)

    self.atualizar_estatisticas_textuais(texto_original)
    self.atualizar_status("Áudio suave gerado com sucesso!")

    if self.autoplay_var.get():
      self.reproduzir_audio()

  def reproduzir_audio(self):
    if not self.audio_gerado or not os.path.exists(self.ultimo_arquivo):
      messagebox.showwarning(
          "Aviso", "O arquivo de áudio não foi encontrado para reprodução."
      )
      return

    if USAR_PYGAME and pygame.mixer.get_init():
      try:
        self.liberar_bloqueio_audio()
        pygame.mixer.music.load(self.ultimo_arquivo)
        pygame.mixer.music.play()
        self.btn_pause.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.NORMAL)
        self.atualizar_status("Reproduzindo áudio...")
        return
      except Exception as e:
        print(f"Falha na reprodução com pygame: {e}")

    if sys.platform == "win32":
      try:
        import winsound

        winsound.PlaySound(
            self.ultimo_arquivo, winsound.SND_FILENAME | winsound.SND_ASYNC
        )
        self.btn_stop.config(state=tk.NORMAL)
        self.atualizar_status("Reproduzindo áudio (modo nativo)...")
        return
      except Exception as e:
        messagebox.showerror(
            "Erro de Reprodução", f"Não foi possível tocar o áudio:\n{e}"
        )

  def pausar_audio(self):
    if USAR_PYGAME and pygame.mixer.get_init():
      try:
        if pygame.mixer.music.get_busy():
          pygame.mixer.music.pause()
          self.atualizar_status("Áudio pausado.")
        else:
          pygame.mixer.music.unpause()
          self.atualizar_status("Reproduzindo áudio...")
      except Exception:
        pass

  def parar_audio(self):
    if USAR_PYGAME and pygame.mixer.get_init():
      try:
        pygame.mixer.music.stop()
        self.btn_pause.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.DISABLED)
        self.atualizar_status("Reprodução interrompida.")
      except Exception:
        pass
    elif sys.platform == "win32":
      try:
        import winsound

        winsound.PlaySound(None, winsound.SND_PURGE)
        self.btn_stop.config(state=tk.DISABLED)
        self.atualizar_status("Reprodução interrompida.")
      except Exception:
        pass

  def atualizar_estatisticas_textuais(self, texto):
    for item in self.tabela_frequencia.get_children():
      self.tabela_frequencia.delete(item)

    letras = [c.lower() for c in texto if c.isalpha()]
    contagem = Counter(letras)

    if not contagem:
      self.lbl_resumo.config(
          text="Resumo: O texto não contém caracteres alfabéticos."
      )
      return

    total_palavras = len(texto.split())
    total_letras = len(letras)
    media_frequencia = sum(contagem.values()) / len(contagem)

    self.lbl_resumo.config(
        text=(
            f"Resumo: {total_palavras} palavras | {total_letras} letras |"
            f" Média por letra: {media_frequencia:.1f}"
        )
    )

    for letra, qtd in contagem.most_common():
      porcentagem = (qtd / total_letras) * 100
      self.tabela_frequencia.insert(
          "", tk.END, values=(letra.upper(), qtd, f"{porcentagem:.2f}%")
      )

    self.dados_grafico = (contagem, total_palavras, total_letras)

  def exibir_grafico_visual(self):
    if not hasattr(self, "dados_grafico"):
      return

    contagem, total_palavras, total_letras = self.dados_grafico
    media_frequencia = sum(contagem.values()) / len(contagem)

    def plotar():
      plt.figure(figsize=(9, 5))
      plt.bar(contagem.keys(), contagem.values(), color="forestgreen")
      plt.axhline(
          y=media_frequencia,
          color="firebrick",
          linestyle="--",
          linewidth=1.5,
          label=f"Média: {media_frequencia:.1f}",
      )
      plt.title(
          f"Frequência de Letras (Palavras: {total_palavras} | Letras:"
          f" {total_letras})"
      )
      plt.xlabel("Letras")
      plt.ylabel("Ocorrências")
      plt.legend()
      plt.tight_layout()
      plt.show()

    threading.Thread(target=plotar, daemon=True).start()

  def salvar_audio(self):
    if not self.audio_gerado or not os.path.exists(self.ultimo_arquivo):
      messagebox.showwarning("Aviso", "Nenhum áudio disponível para salvar.")
      return

    destino = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[
            ("Arquivos de Áudio WAV", "*.wav"),
            ("Todos os Arquivos", "*.*"),
        ],
        title="Salvar áudio como",
    )
    if destino:
      try:
        with open(self.ultimo_arquivo, "rb") as f_origem, open(
            destino, "wb"
        ) as f_destino:
          f_destino.write(f_origem.read())
        messagebox.showinfo("Sucesso", f"Áudio salvo em:\n{destino}")
        self.atualizar_status(f"Arquivo salvo: {os.path.basename(destino)}")
      except Exception as e:
        messagebox.showerror(
            "Erro", f"Não foi possível salvar o arquivo:\n{e}"
        )


if __name__ == "__main__":
  janela = tk.Tk()
  app = AppTextoParaAudio(janela)
  janela.mainloop()
