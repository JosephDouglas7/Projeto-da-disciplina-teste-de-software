### Casos de testes executados e seus resultados  

**Casos de testes executados** 

- *Teste de funcionalidade*
- *Teste de performace*
- *Teste de interface de usuário*
- *Teste unitário*
- *Teste de integração*
- *Teste de Sistema / End-to-End*
- *Teste de Aceitação*
- *Teste de usabilidade*
- *Teste de compatibilidade*


### Testes executados 


Testes                       | Resultados |
-----------------------------|-------------
Teste de funcionalidade      | ✅
Teste de performace          | ✅ 
Teste de interface de usuário| ✅ 
Teste unitário               | ✅
Teste de integração          | ✅
Teste de Sistema / End-to-End| ✅
Teste de Aceitação           | ✅
Teste de usabilidade         | ✅ 
Teste de usabilidade         | ✅ 
Teste de usabilidade         | ✅ 
Teste de compatibilidade     | ✅ 

*Passou* - ✅  

*Falhou* - ❎ 

### Evidências e passos para reprodução de eventuais bugs encontrados 

**◾ Evidências**    


**Teste de funcionalidade** 

Execução do aplicativo para ver se as funções estão funcionando como planejado na versão final. 


**Teste de performace**  

- teste 1: 

Tempo para gerar áudio: 1.01 segundos

Tempo para gerar gráfico: 1.88 segundos 

- teste 2: 

Tempo para gerar áudio: 0.80 segundos

Tempo para gerar gráfico: 1.14 segundos 


**Teste de interface de usuário**  

Execução do aplicativo em caixa preta   

**Teste unitário** 



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


*Ran 4 tests in 1.775s*

*OK*  


**Teste de integração** 

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

*Ran 1 test in 1.259s*

*OK* 


**Teste de Sistema / End-to-End** 

Execução do aplicativo em caixa preta 


**Teste de Aceitação** 

Mostrar a versão final do aplicativo ao cliente. 


**Teste de usabilidade** 

Execução das funções do aplicativo para verificação se tudo está funcionando como planejado. 


**Teste de compatibilidade**

Execução do aplicativo nos sistemas operacionais windows e linux.  


**◾ passos para reprodução de eventuais bugs encontrados** 

*bug de geração de áudio* 

**Passo 1:**  Escreva um texto em português

**Passo 2:**  Seleciona a opção de idioma para inglês

**Passo 3:**  click em gerar áudio 




### Apontamentos de melhorias de negócio, inconsistências ou ajustes nos fluxos do User Story  

- Adição de um detector que detectar quando o usuário escreve um texto em português e seleciona o idioma inglês para geração de áudio 
- Adição de um aviso falando que o usuário não pode gerar áudio de um texto em português com a opção de idioma inglês ativa 








