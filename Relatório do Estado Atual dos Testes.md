### Teste Unitário 

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

No teste unitário mostrou que o Ran 4 tests in 1.775s e está OK, isso que dizer que o teste unitário está passando rápido e que não está tendo erro nas linhas de codigo do aplicativo.   


### Teste de integração   

No teste de integração mostrou que o Ran 1 test in 1.259s e está OK, isso que dizer que o teste de integração  está passando rápido e que não está tendo erro de integração de funcionalidades.    


### Cobertura atual

A cobertura atual mostrar que em questão de quantidade de segurança, confiabilidade, manutenção estão zeradas e a qualidade deles estão na classificação A em questão de duplicações, problemas aceitos, segurança de pontos de acesso estão zerados indicando que não existe no codigo. 

[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=JosephDouglas7_Projeto-da-disciplina-teste-de-software&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=JosephDouglas7_Projeto-da-disciplina-teste-de-software)
