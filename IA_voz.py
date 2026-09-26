import os
import tkinter as tk
from gtts import gTTS
from tkinter import messagebox, filedialog
from collections import Counter
import matplotlib.pyplot as plt 
from langdetect import detect, DetectorFactory

# Garante resultados consistentes na detecção do idioma
DetectorFactory.seed = 0


def validar_idioma_texto(texto, idioma_selecionado):
    """
    Verifica se o idioma detectado no texto corresponde ao idioma selecionado no menu.
    Retorna (True, "") se for válido, ou (False, mensagem_erro) se for inválido.
    """
    try:
        idioma_detectado = detect(texto)

        # Bloqueia texto em português com idioma selecionado em inglês
        if idioma_selecionado == "en" and idioma_detectado == "pt":
            return False, "O texto digitado está em Português, mas a opção selecionada é Inglês.\nAjuste o idioma ou altere o texto."

        # Bloqueia texto em inglês com idioma selecionado em português
        if idioma_selecionado == "pt" and idioma_detectado == "en":
            return False, "O texto digitado está em Inglês, mas a opção selecionada é Português.\nAjuste o idioma ou altere o texto."

    except Exception:
        # Caso o texto seja muito curto, numérico ou com símbolos onde não dá para detectar o idioma
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

    # Converter para áudio no idioma selecionado
    tts = gTTS(text=texto, lang=idioma)
    ultimo_arquivo = "saida.mp3"
    tts.save(ultimo_arquivo)
    
    # Reproduzir dependendo do sistema operacional
    if os.name == "nt":  # Windows
        os.system(f"start {ultimo_arquivo}")
    else:  # Linux/Mac
        os.system(f"mpg321 {ultimo_arquivo}")
    
    messagebox.showinfo("Sucesso", "Áudio gerado e reproduzido!")
    
    # Gerar gráfico de frequência de letras
    gerar_grafico_letras(texto)


def salvar_audio():
    if ultimo_arquivo:
        destino = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("Arquivos MP3", "*.mp3")],
            title="Salvar áudio como"
        )
        if destino:
            try:
                os.replace(ultimo_arquivo, destino)
                messagebox.showinfo("Sucesso", f"Áudio salvo em:\n{destino}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")
    else:
        messagebox.showwarning("Aviso", "Nenhum áudio foi gerado ainda.")


def gerar_grafico_letras(texto):
    # Contar apenas letras (ignorando espaços e pontuação)
    letras = [c.lower() for c in texto if c.isalpha()]
    contagem = Counter(letras)

    # Criar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(contagem.keys(), contagem.values(), color='lightgreen')
    plt.title("Frequência de Letras")
    plt.xlabel("Letras")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()


# Interface gráfica
janela = tk.Tk()
janela.title("Texto para Áudio")

entrada = tk.Text(janela, height=20, width=100)
entrada.pack(pady=10)

# Seleção de idioma
idioma_var = tk.StringVar(value="pt")
menu_idioma = tk.OptionMenu(janela, idioma_var, "pt", "en")
menu_idioma.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter para Áudio", command=converter_texto)
botao_converter.pack(pady=5)

botao_salvar = tk.Button(janela, text="Salvar Áudio", command=salvar_audio)
botao_salvar.pack(pady=5)

ultimo_arquivo = None

janela.mainloop()
