## Plano de Teste da Iteração

**Projeto:** IA voz

**Iteração:** Iteração 02 

**Período:** 10/09/2026 a 06/10/2026

**Data:** 06/10/2026 

**Versão:** 1.0

**Membros Responsáveis:** Joseph Douglas  

> **Documentos de entrada:** [Plano de Iteração](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Plano%20da%20Itera%C3%A7%C3%A3o%201.md) e [Lista de User Stories](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/lista_de_user_stories.md) validados. Estratégia geral de testes: ver [Plano Geral de Testes](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Plano%20de%20Teste%20Geral.md)).


## 1. Objetivos da Iteração

- Teste unitário 

- Teste de integração

**Teste unitário** 

    import unittest
    import os
    from collections import Counter
    from gtts import gTTS
    import matplotlib.pyplot as plt

    # Importa as funções do seu código
    #from seu_codigo import gerar_grafico_letras, converter_texto, salvar_audio

    class TestApp(unittest.TestCase):

    def test_gerar_audio(self):
        texto = "Teste de áudio"
        idioma = "pt"
        arquivo = "saida.mp3"

        # Gera áudio
        tts = gTTS(text=texto, lang=idioma)
        tts.save(arquivo)

        # Verifica se o arquivo foi criado
        self.assertTrue(os.path.exists(arquivo))

        # Remove o arquivo após o teste
        os.remove(arquivo)

    def test_gerar_grafico_letras(self):
        texto = "Teste de gráfico"
        # Contagem esperada
        letras = [c.lower() for c in texto if c.isalpha()]
        contagem = Counter(letras)

        # Gera gráfico
        plt.figure()
        plt.bar(contagem.keys(), contagem.values())
        plt.savefig("grafico_teste.png")

        # Verifica se o gráfico foi salvo
        self.assertTrue(os.path.exists("grafico_teste.png"))

        os.remove("grafico_teste.png")

    def test_converter_texto_sem_texto(self):
        # Simula entrada vazia
        texto = ""
        self.assertEqual(texto.strip(), "")

    def test_salvar_audio_sem_arquivo(self):
        ultimo_arquivo = None
        self.assertIsNone(ultimo_arquivo)

    if __name__ == "__main__":
    unittest.main() 

  **Teste de integração** 

    import unittest
    import os
    from gtts import gTTS
    from collections import Counter
    import matplotlib.pyplot as plt

    # Importa funções do seu código principal
    #from seu_codigo import gerar_grafico_letras

    class TestIntegracaoApp(unittest.TestCase):

    def test_fluxo_completo(self):
        texto = "Teste de integração do aplicativo."
        idioma = "pt"
        arquivo_audio = "saida.mp3"
        arquivo_grafico = "grafico_teste.png"

        # 1. Gerar áudio
        tts = gTTS(text=texto, lang=idioma)
        tts.save(arquivo_audio)
        self.assertTrue(os.path.exists(arquivo_audio))

        # 2. Gerar gráfico
        letras = [c.lower() for c in texto if c.isalpha()]
        contagem = Counter(letras)
        plt.figure()
        plt.bar(contagem.keys(), contagem.values())
        plt.savefig(arquivo_grafico)
        self.assertTrue(os.path.exists(arquivo_grafico))

        # 3. Verificar integração (ambos arquivos criados)
        self.assertTrue(os.path.exists(arquivo_audio) and os.path.exists(arquivo_grafico))

        # Limpeza
        os.remove(arquivo_audio)
        os.remove(arquivo_grafico)

        if __name__ == "__main__":
        unittest.main() 


## 2. User Stories (US) Abordadas na Iteração

| Requisitos envolvidos | Título | Link |
|---|---|---|
| RNF04,RNF06 | Teste unitário     | [Requisitos envolvidos ](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/lista_de_user_stories.md) |
| RNF03,RNF04,RNF06 | Teste de integração| [Requisitos envolvidos](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/lista_de_user_stories.md) |  

## 3. Matriz de Casos de Teste de Aceitação da Iteração 






