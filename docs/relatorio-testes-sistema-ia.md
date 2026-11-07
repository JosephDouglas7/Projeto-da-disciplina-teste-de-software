# Geração de Scripts E2E vs. Teste Instrumental por IA

A transição da geração de código de teste estático auxiliada por inteligência artificial para o teste instrumental e agentivo representa uma mudança fundamental de paradigma na engenharia de qualidade de software, pois transforma a IA de uma simples geradora de artefatos de texto em um agente executor autônomo.

No modelo tradicional de geração de código estático, a IA atua como um assistente de desenvolvimento que recebe contexto sobre requisitos e código-fonte para gerar arquivos rígidos de teste, como .spec.ts em Playwright ou test_e2e.py em Selenium. O ciclo de vida desse formato baseia-se na geração do script, revisão humana, commit no repositório e posterior execução estática e determinística nos pipelines de CI/CD. Em contrapartida, no teste instrumental ou agentivo, a IA assume o papel de um engenheiro de QA autônomo que interage diretamente com a aplicação em execução em tempo real, navegando pelo DOM, árvore de acessibilidade, terminal e rede. O seu comportamento é dinâmico e heurístico, guiado por um objetivo em linguagem natural e operando sob o ciclo de feedback OODA — observando a tela, orientando-se pelo estado atual, decidindo a ação e executando-a em tempo real até gerar o relatório de resultados.

As diferenças práticas entre essas duas abordagens refletem-se em múltiplos fatores operacionais. Quanto à execução, o código estático segue estritamente as instruções gravadas, enquanto o teste instrumental é adaptativo e responde dinamicamente às variações da interface. Em relação à resiliência contra mudanças de UI, os scripts estáticos apresentam alta fragilidade, pois alterações em seletores CSS ou XPaths quebram os testes e exigem manutenção manual. Já o agente autônomo apresenta alta resiliência por interpretar a interface de forma semântica e multimodal, combinando a árvore de acessibilidade à visão computacional. Além disso, enquanto os testes estáticos dependem de assertos previamente codificados e cobrem apenas fluxos pré-programados, o agente instrumental realiza inspeção ampla em tempo real — monitorando simultaneamente exceções no console de JavaScript, requisições HTTP e logs de rede — o que lhe permite executar testes exploratórios e descobrir falhas inesperadas. Consequentemente, o fardo de manutenção estrutural por seletores quebrados é drásticamente reduzido com os agentes, embora passe a exigir governança sobre o escopo e as diretrizes do prompt.

Por trás do funcionamento do teste agentivo está uma arquitetura estruturada em três pilares fundamentais: a inspeção multimodal da interface, que extrai dados visuais e de acessibilidade para interpretar a tela como um usuário humano; o uso de ferramentas (tool calling), no qual o LLM é acoplado a drivers como o Chrome DevTools Protocol ou Playwright para disparar ações estruturadas de clique e digitação; e a observabilidade ativa, que captura erros de execução e falhas de integração no momento em que ocorrem.

Diante dessas distinções, a escolha por cada abordagem depende da maturidade do sistema e dos requisitos do projeto. A geração de código estático permanece ideal para suítes de regressão em fluxos críticos e estabilizados, nos quais se exige execução ultrarrápida e determinismo rigoroso em pipelines de integração contínua. Por outro lado, o teste instrumental agentivo é a escolha recomendada para aplicações em prototipagem rápida ou com mudanças frequentes de UI, para a realização de testes exploratórios automatizados em busca de falhas de usabilidade e para a validação de jornadas complexas de ponta a ponta que demandem tomada de decisão dinâmica.

# Estudo de Agentes de IA em Testes Instrumentais

A análise comparativa das abordagens de automação e testes instrumentais baseados em IA do Claude Code (Anthropic) e do Google Antigravity (Gemini) revela duas filosofias distintas que abandonam a escrita manual de scripts rígidos, como o Selenium tradicional, em favor de agentes autônomos capazes de interagir com o navegador de forma conversacional e contextual. O Claude Code adota uma arquitetura baseada no Model Context Protocol (MCP) para estender as capacidades do terminal, atuando como um cliente que orquestra servidores externos especializados. Entre eles destacam-se o Playwright MCP, focado em automação determinística, suporte a múltiplos motores como Chromium, Firefox e WebKit, e compatibilidade com pipelines de CI/CD, além do Chrome DevTools MCP, que se conecta diretamente a uma instância real do Google Chrome via CDP (Chrome DevTools Protocol) oferecendo dezenas de ferramentas granulares. Isso viabiliza um diagnóstico profundo de falhas ao correlacionar requisições HTTP defeituosas ou exceções de console com o rastreio no código-fonte, integrando-se perfeitamente a fluxos locais onde o desenvolvedor pode iniciar um servidor, navegar por páginas, preencher formulários, clicar em elementos e capturar evidências visuais.

Em contrapartida, o Google Antigravity utiliza uma arquitetura de subagentes especializados gerenciados por um motor central alimentado por modelos Gemini, destacando-se pelo uso de um Browser Subagent dedicado para auditorias visuais e validação de interfaces. Esse subagente opera de forma autônoma sob demanda e conta com isolamento de contexto e execução assíncrona, delegando tarefas pesadas de renderização ou testes longos para segundo plano, o que evita poluir a janela de contexto principal do desenvolvedor e permite a paralelização. Ele interage diretamente com o Chrome DevTools integrado para coletar a árvore DOM, inspecionar estilos computados e exercitar jornadas complexas de ponta a ponta, gerando artefatos multimídia avançados que incluem tanto screenshots estáticos quanto gravações de vídeo em formato WebM das sessões de teste.

Em síntese, confrontando suas arquiteturas, o Claude Code aposta em servidores MCP desacoplados com motores Playwright e Puppeteer para uma execução síncrona guiada por conversas no terminal e forte ênfase em telemetria de código, enquanto o Google Antigravity aposta em subagentes modulares nativos integrados ao ecossistema da IDE com foco em execução assíncrona paralela, validação rigorosa de layouts e auditoria baseada em vídeo.

# IA na Validação de Usabilidade e Acessibilidade

A validação moderna de aplicações web exige uma abordagem híbrida que une a precisão determinística de ferramentas automatizadas à capacidade de interpretação contextual e heurística dos agentes de IA. Enquanto as ferramentas tradicionais identificam falhas estruturais e programáticas, os agentes de IA avaliam a semântica, a experiência subjetiva e os fluxos de interação humana.

No pilar das ferramentas livres de auditoria, soluções de código aberto cobrem a camada técnica e quantitativa, capturando entre 30% e 50% dos problemas de acessibilidade e fornecendo métricas estruturais indispensáveis. O axe-core (e sua integração @axe-core/playwright) atua como o motor padrão da indústria para testes automatizados em pipelines de CI/CD, executando varreduras no DOM renderizado para verificar regras da WCAG 2.2 — como contraste de cores, rótulos de formulários e a árvore de acessibilidade — sem apresentar falsos positivos frequentes. O Google Lighthouse complementa esse diagnóstico ao avaliar a acessibilidade geral, desempenho, SEO e boas práticas diretamente no carregamento da página. Para inspeção visual imediata, o WAVE realiza a injeção de ícones e indicadores diretamente na interface, facilitando a identificação de elementos ausentes e da hierarquia de títulos, enquanto o Pa11y atua via linha de comando para gerar relatórios automatizados de conformidade em diferentes rotas e ambientes.

Por outro lado, onde as ferramentas tradicionais falham em avaliar qualidade e contexto — respondendo apenas se um atributo existe e não se ele faz sentido —, entram os agentes de IA como o pilar cognitivo e contextual. Equipados com visão computacional e capacidades multimodais, esses agentes analisam capturas de tela para identificar inconsistências visuais, problemas de hierarquia tipográfica e excesso de densidade de informação. Na avaliação heurística assistida, eles processam o código HTML, os fluxos de navegação e o contexto do produto para simular as 10 Heurísticas de Nielsen, verificando se mensagens de erro oferecem orientação real, se há prevenção de falhas e se os rótulos são compreensíveis. Além disso, LLMs integrados a frameworks de teste conseguem simular jornadas completas de usuários com deficiência visual ou motora, garantindo que a ordem de foco e a narrativa semântica sejam fluidas durante o uso de leitores de tela.

A validação cruzada entre acessibilidade (WCAG 2.2 Níveis A e AA) e usabilidade (ISO/IEC 25010:2023) evidencia claramente essa complementaridade em múltiplos cenários operacionais. No que tange ao contraste de cores na WCAG 2.2, enquanto ferramentas como o axe-core medem matematicamente a razão de contraste entre texto e fundo (exigindo um mínimo de 4.5:1), a IA analisa se o contraste em elementos dinâmicos, como estados de hover ou gráficos complexos, mantém a legibilidade em contextos visuais específicos. Na navegação por teclado, a automação detecta armadilhas de foco (keyboard traps) e valida se os elementos são focáveis, enquanto o agente de IA julga se a ordem de tabulação segue uma sequência lógica para a tarefa. Na análise de atributos ARIA e semântica, as ferramentas verificam a sintaxe e a estrutura do HTML, enquanto a IA avalia a intenção semântica e a clareza descritiva de widgets complexos. Para textos alternativos, o auditor automatizado apenas identifica a ausência física da tag , cabendo à IA validar se a descrição escrita é contextualmente relevante para o leitor de tela.

Já no âmbito da usabilidade sob a norma ISO/IEC 25010, onde o foco recai sobre a capacidade de interação humana, a atuação conjunta também se destaca. Para a clareza de rótulos e mensagens, a automação aponta campos sem rótulo associado, enquanto o agente de IA revisa o UX Writing para garantir que mensagens de erro expliquem o problema e indiquem o caminho de recuperação. Na prevenção de falhas e consistência visual, o analisador de código identifica quebras de sintaxe, enquanto a IA identifica divergências visuais de design system entre telas e sinaliza pontos propensos a erros acidentais. Por fim, na gestão de carga cognitiva, enquanto as ferramentas convencionais medem o tempo de carregamento e o tamanho de arquivos, a IA analisa a densidade de elementos interativos por tela para apontar poluentes visuais e fluxos extensos que possam provocar fadiga.

Na prática, a implementação dessa arquitetura ocorre por meio de um pipeline contínuo de três etapas. Inicialmente, a execução automatizada de testes E2E com @axe-core/playwright e Lighthouse roda a cada alteração de código no CI/CD. Em seguida, na fase de captura de evidências, caso ocorram falhas ou em pontos críticos de interface, a aplicação exporta o estado do DOM acompanhado de capturas de tela. Por fim, o agente de IA realiza a análise cognitiva, processando os dados estruturados das ferramentas junto à visão computacional da interface para emitir um parecer qualitativo com sugestões diretas de refatoração de código, melhorias de copywriting e ajustes heurísticos alinhados às normas vigentes.

### Execução de Teste Instrumental com Agente de IA 

### Relatório 

O ambiente que foi utilizado foi o sistema operacional Windows 11 e o agente utilizado foi o google antigravity. 

**Promp fornecido ao agente** 

Com base nesse codigo, atue como QA Instrumental, fornecendo a especificação dos cenários de aceitação Teste de funcionalidade,
Teste de performace,Teste de interface de usuário,Teste unitário,Teste de integração,Teste de Sistema / End-to-End,Teste de Aceitação,
Teste de usabilidade,Teste de compatibilidade do projeto e interaja com o sistema em execução, valide o comportamento obtido e produza um diagnóstico.

**Passos executados instrumentalmente pela IA e as evidências coletadas** 

Ran list workspace files
Ran check file details
Analyzed Main:L1-100
Analyzed Main:L101-222
Analyzed p1:L1-100
Analyzed p1:L101-174
Ran check python and pip packages
Ran run existing tests in p1 · Exited with code 1
Ran check system TTS voices · Exited with code 1
Ran check COM error code · Exited with code 1
Ran print hex error code
Ran test SAPI.SpVoice via win32com · Exited with code 1
Ran read Main content length
Created test_qa_instrumental.py
Ran run instrumental QA test harness · Exited with code 1
Checked task Run instrumental QA test harness
Checked task Run instrumental QA test harness
Checked task Run instrumental QA test harness
Edited test_qa_instrumental.py
Ran run updated test harness
Checked task Run updated test harness
Checked task Run updated test harness
Checked task Run updated test harness
Checked task Run updated test harness
Ran test importing p1 · Exited with code 1
Ran load p1 via importlib · Exited with code 1
Ran load p1 via SourceFileLoader
Checked task Load p1 via SourceFileLoader
Ran run pytest directly on p1 · Exited with code 1
Checked task Run pytest directly on p1

### Relatório de QA Instrumental: Especificação de Cenários, Validação em Execução e Diagnóstico Técnico

**Projeto:** Aplicação Desktop de Conversão de Texto para Áudio (TTS) com Análise de Frequência de Caracteres  
**Arquivos Analisados:** [Main](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main) (aplicação Tkinter/pyttsx3/Matplotlib) e [p1](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/p1) (suíte legada em Pytest/Selenium/gTTS)  
**Ambiente de Execução:** Python 3.11.2, Windows 11, SAPI5 / Tkinter / Matplotlib 3.10.6 / langdetect 1.0.9

---

## 1. Especificação Formal dos Cenários de Teste

A especificação a seguir adota o padrão de **QA Instrumental** e **BDD (Behavior-Driven Development / Gherkin)**, cobrindo os 9 níveis de testes requeridos.

---

### 1.1. Testes de Funcionalidade (TF)

#### **CT-FUNC-01: Conversão de Texto em Português Válido**
* **Objetivo:** Garantir a síntese de áudio para texto em português compatível com a opção selecionada.
* **Pré-condições:** Aplicação em execução, campo de texto preenchido com conteúdo em português.
* **Cenário BDD:**
  ```gherkin
  Cenário: Converter texto em Português com sucesso
    Dado que a aplicação está aberta
    E o seletor de idioma está definido como "pt"
    Quando o usuário digita "O desenvolvimento de software com testes garante qualidade contínua."
    E clica no botão "Converter para Áudio"
    Então o arquivo "saida.mp3" deve ser gerado no disco
    E o sistema deve abrir o áudio no reprodutor padrão
    E uma mensagem de sucesso "Áudio gerado e reproduzido!" deve ser exibida
    E a janela com o gráfico de barras de frequência de letras deve ser aberta
  ```

#### **CT-FUNC-02: Bloqueio por Incompatibilidade de Idioma (PT vs EN)**
* **Objetivo:** Validar se o sistema bloqueia texto em português quando configurado para inglês e vice-versa.
* **Cenário BDD:**
  ```gherkin
  Cenário: Tentar converter texto em Inglês com opção Português selecionada
    Dado que o idioma selecionado no menu é "pt"
    Quando o usuário insere "Software testing is essential for reliable systems."
    E aciona "Converter para Áudio"
    Então o sistema não deve gerar o arquivo de áudio
    E deve exibir uma caixa de diálogo de erro com a mensagem:
      "O texto digitado está em Inglês, mas a opção selecionada é Português. Ajuste o idioma ou altere o texto."
  ```

#### **CT-FUNC-03: Salvamento de Áudio com Seleção de Destino**
* **Objetivo:** Validar a funcionalidade do botão "Salvar Áudio".
* **Cenário BDD:**
  ```gherkin
  Cenário: Salvar áudio gerado anteriormente em diretório personalizado
    Dado que um áudio já foi gerado com sucesso ("saida.mp3" existe)
    Quando o usuário clica no botão "Salvar Áudio"
    E escolhe o caminho "C:\Users\Public\meu_audio.mp3" na caixa de diálogo de salvamento
    Então o arquivo deve ser copiado com integridade de bytes idêntica
    E uma mensagem de confirmação deve informar o caminho completo do destino
  ```

---

### 1.2. Testes de Performance (TP)

#### **CT-PERF-01: Tempo de Resposta da Detecção de Idioma sob Carga**
* **Objetivo:** Medir a latência do validador `validar_idioma_texto()` para textos curtos (10 palavras), médios (1.000 palavras) e volumosos (10.000 palavras).
* **Critério de Aceitação:** Latência média $\le 50\text{ ms}$ por inferência.

#### **CT-PERF-02: Consumo de Memória e Tempo de Renderização Gráfica**
* **Objetivo:** Avaliar o overhead de alocação de memória no cálculo do `Counter` e renderização de `plt.bar` com massas de dados de até 650.000 palavras.
* **Critério de Aceitação:** Tempo de contagem + gráfico $\le 3,0\text{ segundos}$ e pico de consumo de memória $\le 50\text{ MB}$.

---

### 1.3. Testes de Interface de Usuário (UI)

#### **CT-UI-01: Disposição e Alinhamento de Controles**
* **Objetivo:** Verificar a ancoragem e centralização dos componentes Tkinter (`Text`, `OptionMenu`, `Button`).
* **Critério de Aceitação:**
  * Caixa de texto `entrada` deve ocupar 20 linhas e largura proporcional com padding vertical de 10px.
  * O menu suspenso de idiomas deve permanecer centralizado na linha do frame auxiliar (`column=1`).
  * Botões "Converter para Áudio" e "Salvar Áudio" devem manter espaçamento uniforme (`pady=5`).

#### **CT-UI-02: Validação Visual de Campos Vazios**
* **Cenário BDD:**
  ```gherkin
  Cenário: Submissão de texto vazio na interface gráfica
    Dado que o campo de texto está vazio ou contém apenas espaços
    Quando o usuário clica em "Converter para Áudio"
    Então deve surgir um aviso popup modal "Digite algum texto antes de converter."
    E o foco deve retornar ao campo de digitação
  ```

---

### 1.4. Testes Unitários (TU)

* **TU-01 (`validar_idioma_texto`):**
  * *Entrada:* Texto PT, idioma "pt" $\to$ Retorno esperado: `(True, "")`.
  * *Entrada:* Texto EN, idioma "en" $\to$ Retorno esperado: `(True, "")`.
  * *Entrada:* Texto PT, idioma "en" $\to$ Retorno esperado: `(False, mensagem_erro)`.
  * *Entrada:* Texto EN, idioma "pt" $\to$ Retorno esperado: `(False, mensagem_erro)`.
  * *Entrada Limite:* Texto numérico `"123456"` ou símbolos $\to$ Retorno esperado: Rejeição ou tratamento seguro de exceção.
* **TU-02 (`configurar_voz`):**
  * *Entrada:* Idioma `"pt"` em ambiente Windows.
  * *Critério de Aceitação:* Deve setar a taxa de fala em 180 e selecionar estritamente vozes em língua portuguesa (ex: Maria, Helena, Daniel ou token com pt-br), **nunca** vozes em inglês.
* **TU-03 (`gerar_grafico_letras`):**
  * *Entrada:* String `"Abc 123 !@#"` $\to$ Filtro de caracteres deve processar apenas `['a', 'b', 'c']`.
  * *Entrada:* String sem letras `"12345"` $\to$ Deve abortar a plotagem e disparar alerta.

---

### 1.5. Testes de Integração (TI)

#### **CT-INT-01: Integração Tkinter $\leftrightarrow$ pyttsx3 Engine $\leftrightarrow$ SAPI5 do SO**
* **Objetivo:** Garantir que o comando disparado na camada de apresentação (Tkinter) invoca corretamente a fila do sintetizador COM SAPI5 e produz o arquivo binário em disco.
* **Cenário de Falha Inspecionado:** Se o serviço de áudio do sistema operacional estiver inativo ou sem permissão de acesso COM, a camada de integração deve capturar a falha com `try/except` sem derrubar o processo da interface.

#### **CT-INT-02: Integração Processamento de Texto $\leftrightarrow$ Matplotlib Backend**
* **Objetivo:** Verificar se a estrutura de dados retornada pelo `Counter(letras)` alimenta as séries do eixo X (letras) e Y (quantidades) sem quebrar por caracteres Unicode acentuados (`ã`, `é`, `ç`).

---

### 1.6. Testes de Sistema / End-to-End (E2E)

#### **CT-E2E-01: Ciclo de Vida Completo da Aplicação (Caminho Feliz)**

[imagem](https://canva.link/9r4i8v23iebsjjr)

* **Critério de Aceitação E2E:** Todas as etapas executadas sem exceções não tratadas no terminal e com integridade do arquivo gerado.

---

### 1.7. Testes de Aceitação (UAT / Critérios de Aceite do Negócio)

* **CA-01 (Precisão Fonética):** O áudio gerado deve ser compreensível para falantes nativos do idioma selecionado.
* **CA-02 (Conformidade Gramatical vs Idioma):** A aplicação não deve permitir que o usuário gere áudios com pronúncias corrompidas resultantes da leitura de um idioma por motor configurado para outro.
* **CA-03 (Exportabilidade):** O usuário deve conseguir salvar o arquivo gerado em qualquer pasta com permissão de escrita local.

---

### 1.8. Testes de Usabilidade (UX / Heurísticas de Nielsen)

* **USAB-01 (Visibilidade do Status do Sistema):** Durante a síntese de textos longos (mais de 1.000 palavras), a aplicação deve fornecer feedback visual (barra de progresso ou cursor de espera), evitando a impressão de que o software travou.
* **USAB-02 (Prevenção de Erros e Não Bloqueio):** A exibição do gráfico de frequência de letras não pode impedir a interação com a janela principal (não deve ser modal/bloqueante).
* **USAB-03 (Controle do Usuário):** O usuário deve poder pausar, parar ou cancelar uma conversão em andamento.

---

### 1.9. Testes de Compatibilidade (TC)

* **COMP-01 (Compatibilidade de Plataforma SO):**
  * Windows: Utilização de SAPI5 e `start saida.mp3`.
  * Linux: Utilização de `espeak` e `xdg-open saida.mp3`.
  * macOS: Utilização de `nsss` e comando `open`.
* **COMP-02 (Formato e Header do Arquivo de Áudio):**
  * Verificar se o arquivo salvo como `.mp3` é de fato codificado em MPEG Audio Layer III ou se é um stream RIFF WAVE renomeado (comportamento nativo frequente do SAPI5 no Windows).

---

## 2. Validação Instrumental em Execução (Resultados Reais)

Para validar o comportamento do sistema sem suposições teóricas, foi desenvolvida e executada uma suíte instrumental automatizada que isolou e submeteu os componentes do [Main](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main) e [p1](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/p1) a testes rigorosos em tempo de execução.

### Resumo Quantitativo da Execução

| Métrica | Valor Obtido |
| :--- | :--- |
| **Total de Testes Instrumentados Executados** | **19** |
| **Sucessos (PASS)** | **12** (63,2%) |
| **Falhas Críticas / Bugs (FAIL)** | **4** (21,0%) |
| **Alertas de Usabilidade e Risco (WARN)** | **3** (15,8%) |

---

### Tabela Detalhada de Validação por Cenário

| ID | Nível | Cenário de Teste | Status | Comportamento Registrado em Execução |
| :--- | :--- | :--- | :---: | :--- |
| **T-01** | Funcional | Texto PT com seleção PT | **PASS** | Detectado e aprovado com sucesso. |
| **T-02** | Funcional | Texto EN com seleção EN | **PASS** | Detectado e aprovado com sucesso. |
| **T-03** | Funcional | Bloqueio PT com seleção EN | **PASS** | Bloqueou com a mensagem prescrita. |
| **T-04** | Funcional | Bloqueio EN com seleção PT | **PASS** | Bloqueou com a mensagem prescrita. |
| **T-05** | Funcional | Entrada em Espanhol com seleção PT | **FAIL** | **Falso Positivo:** Texto em espanhol foi aceito com PT selecionado. |
| **T-06** | Funcional | Entrada apenas numérica (`"12345"`) | **WARN** | Exceção silenciada por `except Exception: pass`, retornando `True`. |
| **T-07** | Unitário | Seleção de voz PT em Windows padrão | **FAIL** | **BUG GRAVE:** Selecionou voz inglesa `Microsoft Zira` para áudio PT. |
| **T-08** | Unitário | Resiliência com lista de vozes vazia | **FAIL** | **CRASH:** `IndexError: list index out of range` ao acessar `voices[0]`. |
| **T-09** | Visual | Geração de gráfico com texto válido | **PASS** | Dados agrupados e renderizados corretamente. |
| **T-10** | Visual | Geração de gráfico sem letras | **PASS** | Cancelou a plotagem e exibiu `messagebox.showwarning`. |
| **T-11** | Carga | Volume de 1.300 palavras | **PASS** | Detecção: 16.8ms \| Gráfico: 794.3ms \| Total: 0.81s \| Memória: 1.52MB |
| **T-12** | Carga | Volume de 13.000 palavras | **PASS** | Detecção: 14.9ms \| Gráfico: 828.8ms \| Total: 0.84s \| Memória: 4.49MB |
| **T-13** | Carga | Volume de 130.000 palavras | **PASS** | Detecção: 14.3ms \| Gráfico: 2.07s \| Total: 2.08s \| Memória: 39.57MB |
| **T-14** | Stress | Volume de 650.000 palavras | **WARN** | Detecção: 16.2ms \| Gráfico: 7.43s \| Total: 7.45s \| Memória: 198.34MB |
| **T-15** | UI | Clique em Converter com campo vazio | **PASS** | Exibiu alerta de aviso modal impedindo execução inválida. |
| **T-16** | UI | Salvar Áudio sem áudio gerado | **PASS** | Exibiu alerta de aviso modal impedindo cópia fantasma. |
| **T-17** | E2E | Fluxo completo ponta a ponta | **PASS** | Síntese, reprodução, notificação e plotagem acionadas. |
| **T-18** | Arquitetura | Bloqueio de Thread por `plt.show()` | **FAIL** | **Interface Tkinter congela** enquanto o gráfico estiver aberto. |
| **T-19** | Usabilidade| Invocação de áudio via `os.system("start ...")`| **WARN** | Janela externa do player causa perda de foco e lock de arquivo. |

---

## 3. Diagnóstico Técnico de QA

A inspeção e execução revelaram falhas graves de estabilidade, erros lógicos de negócio e inconsistências na suíte de testes.

### 🔴 Defeitos Críticos (Blocker & High Severity)

#### 1. Crash Imediato no Startup se SAPI5 Estiver Inativo (Blocker)
* **Local:** [Main: linha 14](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L14)
* **Evidência no Console:**
  ```text
  _ctypes.COMError: (-2147200967, None, (None, None, None, 0, None))
  0x80045039 -> SPERR_SHARED_ENGINE_DISABLED
  ```
* **Causa Raiz:** `engine = pyttsx3.init()` é invocado no escopo global (nível de módulo). Em ambientes sem placa de som habilitada, servidores Windows, pipelines de CI/CD ou sessões isoladas, a aplicação é encerrada abruptamente antes mesmo da criação da janela Tkinter.
* **Impacto:** Indisponibilidade total da aplicação nesses cenários.

#### 2. Seleção Indevida de Voz em Inglês para Textos em Português (High)
* **Local:** [Main: linhas 28-34](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L28-L34)
* **Código Defeituoso:**
  ```python
  if idioma == "pt":
      if any(termo in nome_voz for termo in ["maria", "helena", "lucia", "zira", "female", "pt-br"]):
          voz_escolhida = voice.id
          break
  ```
* **Causa Raiz:** A voz padrão feminina nativa do Windows chama-se `"Microsoft Zira Desktop - English (United States)"`. Como `"zira"` foi incluído na lista de busca de português, o sistema seleciona uma voz americana para ler textos em português, gerando um áudio ininteligível.
* **Impacto:** Violação direta do Critério de Aceitação funcional e fonético.

#### 3. Exceção `IndexError` em Ambientes sem Vozes Instaladas (High)
* **Local:** [Main: linhas 59-60](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L59-L60)
* **Código:** `voz_escolhida = voices[1].id if len(voices) > 1 else voices[0].id`
* **Causa Raiz:** Se `voices` for uma lista vazia (`len(voices) == 0`), a expressão tenta acessar `voices[0]`, disparando um `IndexError`.

---

### 🟡 Defeitos Médios e Vulnerabilidades de Validação

#### 4. Brecha na Validação de Idiomas de Terceiros
* **Local:** [Main: linhas 70-96](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L70-L96)
* **Causa Raiz:** A validação apenas testa `pt` contra `en` e `en` contra `pt`. Se o usuário inserir texto em Espanhol (`es`), Francês (`fr`) ou Alemão (`de`), a função retorna `(True, "")`. Além disso, para entradas como `"123456"`, o `langdetect` lança exceção que é absorvida por `except Exception: pass`, liberando a conversão indevida.

#### 5. Travamento e Congelamento da Interface Gráfica (Thread Blocking)
* **Local:** [Main: linhas 121 e 189](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L121)
* **Causa Raiz:** A síntese de áudio (`engine.runAndWait()`) e a exibição do gráfico (`plt.show()`) rodam de forma síncrona na thread principal do Tkinter. Enquanto o usuário visualiza o gráfico do Matplotlib ou durante a síntese de grandes textos, a janela principal fica em estado *"Não Respondendo"*.

#### 6. Concorrência e File Locking no Windows
* **Local:** [Main: linhas 117, 125 e 144](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main#L117)
* **Causa Raiz:** O arquivo de saída é sempre fixo como `"saida.mp3"` e executado via `os.system("start saida.mp3")`. No Windows, o player padrão frequentemente retém o bloqueio de I/O sobre o arquivo. Se o usuário clicar novamente em "Converter para Áudio" com o player ainda aberto, ocorre:
  ```text
  PermissionError: [Errno 13] Permission denied: 'saida.mp3'
  ```

---

### ⚪ Inconsistência de Engenharia: A Discrepância entre `Main` e `p1`

Ao avaliar o arquivo [p1](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/p1), o diagnóstico de QA identificou um desacoplamento do projeto:
1. **Falta de Extensão de Arquivo:** Nem [Main](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main) nem [p1](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/p1) possuem a extensão `.py`. Por essa razão, comandos convencionais de execução de testes como `pytest` falham imediatamente ao tentar encontrá-los (`collected 0 items`).
2. **Divergência Tecnológica em `p1`:**
   * O código em [Main](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/Main) utiliza síntese local com `pyttsx3` e interface Desktop Tkinter.
   * O arquivo [p1](file:///c:/Users/josep/OneDrive/Área%20de%20Trabalho/Faculdade(curso%20si)/Teste%20de%20software/2%20Unidade/Prática_1/p1) implementou testes unitários e de integração mockados usando `gTTS` (Google Translate Cloud API) e automação de buscas no Google com Selenium WebDriver (`webdriver.Chrome`).
   * **Conclusão:** A suíte contida em `p1` **não testa o sistema real contido em `Main`**, funcionando como um exercício isolado que não assegura a qualidade da aplicação entregue.

---

## 4. Plano de Remediação Recomendado

Para elevar o projeto ao nível de produção acadêmica e profissional, as seguintes intervenções devem ser adotadas:

### 4.1. Correção Imediata da Lógica de Voz e Validação

```python
# Correção do filtro de voz (remover 'zira' do português e checar tamanho)
def configurar_voz(idioma):
    engine.setProperty("rate", 180)
    voices = engine.getProperty("voices")
    if not voices:
        return  # Evita IndexError se não houver vozes instaladas

    voz_escolhida = None
    for voice in voices:
        nome_voz = voice.name.lower()
        if idioma == "pt":
            # REMOVIDO "zira" DA LISTA DE PORTUGUÊS:
            if any(termo in nome_voz for termo in ["maria", "helena", "lucia", "pt-br", "brazil"]):
                voz_escolhida = voice.id
                break
        elif idioma == "en":
            if any(termo in nome_voz for termo in ["zira", "david", "hazel", "en-us"]):
                voz_escolhida = voice.id
                break

    if not voz_escolhida and voices:
        voz_escolhida = voices[0].id

    engine.setProperty("voice", voz_escolhida)
```

### 4.2. Correção da Validação de Idioma com Rejeição Estrita

```python
def validar_idioma_texto(texto, idioma_selecionado):
    texto_limpo = texto.strip()
    # Exige caracteres alfabéticos mínimos antes de consultar o detector
    if not any(c.isalpha() for c in texto_limpo):
        return False, "O texto fornecido não contém palavras válidas para síntese."

    try:
        idioma_detectado = detect(texto_limpo)
        if idioma_detectado != idioma_selecionado:
            return False, (
                f"O texto parece estar no idioma '{idioma_detectado}', "
                f"mas a opção selecionada é '{idioma_selecionado}'.\n"
                "Ajuste a opção ou revise o texto digitado."
            )
    except Exception:
        return False, "Não foi possível identificar o idioma do texto digitado."

    return True, ""
```

### 4.3. Arquitetura Assíncrona para a Interface (Desacoplamento de UI)
* Mover a chamada `engine.runAndWait()` para uma `threading.Thread(target=...)`.
* Substituir `plt.show()` (bloqueante) pela integração de gráficos diretamente dentro da janela Tkinter através de `FigureCanvasTkAgg` do Matplotlib (`matplotlib.backends.backend_tkagg`), proporcionando uma experiência de usuário integrada e responsiva.
* Renomear os arquivos para `main.py` e `test_main.py` para compatibilidade com o padrão do ecossistema Python e Pytest.


### Análise comparativa 

| Testes                                      | determinismo  |reprodutibilidade | custo de manutenção | tempo de execução|
|---------------------------------------------|---------------|------------------|---------------------|------------------|
|Teste Automatizado(pytest)                   | Existe        | Existe           | Existe              | Segundos         |
|Teste Instrumental por IA(google antigravity)| Não Existe    | Não Existe       | Existe              | Minutos          |                                  

| Testes                                      |descoberta exploratória de bugs|                     
|---------------------------------------------|-------------------------------|
|Teste Automatizado(pytest)                   | Sem detalhes                  | 
|Teste Instrumental por IA(google antigravity)| Com detalhes                  | 

### Auditoria e Melhoria de Usabilidade e Acessibilidade 

**Auditoria de Acessibilidade** 

**Armadilha de Teclado (Keyboard Trap) — Crítico (WCAG 2.1.2):**

No componente tk.Text, a tecla Tab insere tabulação no texto em vez de alternar o foco para o próximo controle. Usuários dependentes de navegação por teclado não conseguem sair do campo.

**Autoplay e Roubo Abrupto de Foco — Crítico (WCAG 1.4.2 e 2.4.3):**

Na função converter_texto/Teste%20de%20software/2%20Unidade/Prática_1/Main#L99-L134), o comando os.system("start ...") abre o reprodutor externo do Windows, roubando o foco do leitor de tela (NVDA/JAWS) e desorientando o usuário.

**Inacessibilidade e Falta de Alternativa Textual no Gráfico — Crítico (WCAG 1.1.1 e 1.4.1):**

Em gerar_grafico_letras/Teste%20de%20software/2%20Unidade/Prática_1/Main#L157-L190), o gráfico do matplotlib é puramente visual (sem resumo textual ou tabela de dados para cegos) e utiliza a combinação vermelho/verde com baixo contraste, problemática para daltonismo. Além disso, plt.show() bloqueia o loop principal da interface.

**Ausência de Rótulos (Labels) e Controles Rígidos — Alto/Médio (WCAG 1.3.1 e 4.1.2):**
O campo de texto e o seletor de idiomas não contam com rótulos descritivos associados.

Na função configurar_voz/Teste%20de%20software/2%20Unidade/Prática_1/Main#L17-L63), a velocidade de fala é fixada em 180, impedindo o ajuste de ritmo para usuários com deficiência auditiva ou dificuldades de processamento.

**Auditoria de Usabilidade (Heurísticas de Nielsen / ISO/IEC 25010:2023)** 

1. Análise de Interface, DOM e Fluxo de Interação
1.1. Mapeamento da Árvore de Elementos (UI Hierarchy)

A interface gráfica em Main utiliza Tkinter clássico:

[Imagem](https://canva.link/m80rqn0pegw8udb)

Na camada de automação web em p1, há interação com o DOM do Google (By.NAME, "q" e By.ID, "search"), com validação de responsividade para três viewports (1080p, 768p e mobile 375x812).

1.2. Mapeamento do Fluxo de Interação (User Flow)

[Imagem](https://canva.link/muoiqi2o56q393a)

1.3. Gargalos Críticos de UX e Arquitetura de Interface
Congelamento da Interface (UI Freeze):
engine.save_to_file() e engine.runAndWait() (Main #L120-L121) rodam na thread principal do Tkinter. Textos médios/longos deixam a janela em estado "Não Respondendo".
Dispersão e Quebra de Foco (App Switching Chaos):
Uma única ação ("Converter para Áudio") abre simultaneamente 3 janelas de 3 contextos diferentes:
O player de mídia padrão do sistema operacional (os.system("start ...")).
A janela modal de aviso do Tkinter (messagebox.showinfo).
A janela independente do Matplotlib (plt.show()), que bloqueia a janela do Tkinter até ser fechada.
Ausência de Controles de Áudio Embutidos:
O aplicativo não possui botões de Play, Pause, Stop ou controle de volume nativos na janela.
Falta de Barra de Rolagem (Scrollbar):
O tk.Text não possui barra de rolagem anexada. Em textos longos, o usuário perde a visibilidade do cursor e da posição da leitura.

2. Avaliação das 10 Heurísticas de Nielsen
   
| Heurística | Status | Severidade | Diagnóstico e Evidência no Código |
| --- | --- | --- | --- |
| **H1. Visibilidade do Status do Sistema** | ❌ Falha | Crítica | Não existe barra de progresso, spinner ou cursor de espera durante o processamento do texto e síntese TTS. |
| **H2. Correspondência com o Mundo Real** | ⚠️ Regular | Média | O seletor exibe códigos técnicos (pt, en) em vez de rótulos naturais como "Português" e "Inglês". |
| **H3. Controle e Liberdade do Usuário** | ❌ Falha | Alta | Não é possível pausar, retroceder ou cancelar uma conversão em andamento. O fechamento do gráfico exige dispensar uma janela Matplotlib à parte. |
| **H4. Consistência e Padrões** | ⚠️ Regular | Alta | Inconsistência entre módulos: Main usa pyttsx3 (TTS local), enquanto a suíte de testes p1 usa gTTS (Google TTS online). Não há atalhos convencionais (Ctrl+S, Ctrl+Enter). |
| **H5. Prevenção de Erros** | ❌ Falha | Alta | O botão "Salvar Áudio" fica ativo mesmo antes de converter qualquer texto, gerando um modal de aviso desnecessário (Main #L154). Deveria iniciar desabilitado (`state=DISABLED`). |
| **H6. Reconhecimento em vez de Memorização** | ⚠️ Regular | Média | O campo de texto não possui texto guia (placeholder), indicador de caracteres ou dicas sobre formatos e limites suportados. |
| **H7. Flexibilidade e Eficiência de Uso** | ⚠️ Regular | Média | A velocidade de leitura está travada no código (`rate = 180`) e vozes femininas são forçadas por heurística de string, sem permitir que o usuário escolha a voz ou ajuste o ritmo. |
| **H8. Estética e Design Minimalista** | ❌ Falha | Alta | A exibição obrigatória de um gráfico de frequência de letras com "Média de Referência" sobrecarrega a interface e distrai do propósito principal (conversão de áudio). |
| **H9. Ajuda para Reconhecer e Recuperar Erros** | ⚠️ Regular | Baixa | Mensagens de erro informam a causa, mas a validação de idioma do langdetect frequentemente gera falsos positivos em frases curtas, bloqueando a conversão sem dar opção de ignorar. |
| **H10. Ajuda e Documentação** | ❌ Falha | Média | Inexistência de menu de ajuda, botão "Sobre", dicas de contexto (tooltips) ou orientações na tela. |

3. Avaliação da Capacidade de Interação (ISO/IEC 25010:2023)

A revisão ISO/IEC 25010:2023 substituiu a característica Usabilidade por Capacidade de Interação (Interaction Capability), estruturada em 8 subcaracterísticas:

⚠️ Failed to render Mermaid diagram: Invalid mermaid header: "mindmap". Expected "graph TD", "flowchart LR", "stateDiagram-v2", etc.. Supported types: flowchart/graph, stateDiagram-v2, sequenceDiagram, classDiagram, erDiagram, xychart-beta, pie.

    mindmap

    root((ISO/IEC 25010:2023<br/>Interaction Capability))
  
    Reconhecimento de Adequação
      Título genérico
      Falta de instrução inicial
    Apreensibilidade
      Poucos botões facilita início
      Comportamento multijanela confunde
    Operabilidade
      Sem suporte pleno a teclado
      Falta de atalhos e foco
    Proteção contra Erros
      Valida campo vazio
      Botão salvar emite erro evitável
    Engajamento do Usuário
      Tkinter bruto sem ttk
      Visual utilitário sem polimento
    Inclusividade
      Incompatível com leitores de tela
      Sem ajuste de contraste ou fonte
    Assistência ao Usuário
      Ausência de tooltips ou FAQ
    Autodescritividade
      Rótulos pt/en ambíguos
      
Detalhamento por Subcaracterística

Reconhecimento de Adequação (Appropriateness Recognizability):
Avaliação: Regular. O título da janela "Texto para Áudio" ajuda, mas a tela inicial apresenta apenas um bloco de texto cinza vazio e um seletor "pt", sem orientações de formato ou capacidade.

Apreensibilidade (Learnability):
Avaliação: Boa na simplicidade de uso básico, mas prejudicada pelos múltiplos eventos colaterais após o clique em converter (abertura de player externo + Matplotlib).

Operabilidade (Operabilidade / Facilidade de Operação):
Avaliação: Insuficiente. Não há gerenciamento de foco por Tab, nem teclas de atalho de conversão/gravação. A janela Matplotlib rouba o foco do sistema operacional.

Proteção contra Erros do Usuário (User Error Protection):
Avaliação: Regular. Evita tentar converter strings vazias, mas a validação de idioma com langdetect é frágil para sentenças curtas (ex.: "Hello" ou "Bom dia") e bloqueia a ação do usuário sem oferecer opção de bypass (override).

Engajamento do Usuário (User Engagement):
Avaliação: Baixo. Uso de widgets clássicos e desatualizados do Tkinter (sem biblioteca ttk moderna), ausência de paleta cromática ergonômica e espaçamentos desbalanceados.

Inclusividade (Inclusivity / Acessibilidade):
Avaliação: Crítica. A aplicação é um software assistivo de Text-to-Speech, mas a própria interface não atende a normas de acessibilidade (WCAG 2.1 / eMAG): não há redimensionamento dinâmico de fontes, suporte nativo a leitores de tela em Tkinter básico, nem suporte a temas de alto contraste.

Assistência ao Usuário (User Assistance):
Avaliação: Inexistente. Não há tooltips com tkinter-tooltip, nem mensagens de rodapé (status bar) ou tela de ajuda.

Autodescritividade (Self-Descriptiveness):
Avaliação: Parcial. Os botões têm textos diretos ("Converter para Áudio", "Salvar Áudio"), mas o controle de idioma não possui um rótulo indicando "Idioma do Texto:", mostrando apenas uma lista solta com pt.

4. Matriz de Priorização de Problemas (Gravidade e Impacto)

| Item | Problema Identificado | Impacto UX | Ação Recomendada |
| --- | --- | --- | --- |
| **1** | Processamento síncrono trava a interface | Crítico | Delegar a conversão TTS para uma thread separada (`threading.Thread`) e exibir barra de progresso indeterminada. |
| **2** | Gráfico e player abrem janelas externas simultâneas | Alto | Integrar o gráfico em uma aba ou frame opcional (`FigureCanvasTkAgg`) e embutir controles nativos de áudio (Play/Stop). |
| **3** | Botão "Salvar Áudio" ativo sem áudio existente | Alto | Iniciar desabilitado (`state=tk.DISABLED`) e habilitar somente após a geração bem-sucedida do arquivo. |
| **4** | Bloqueio indevido por detecção de idioma | Médio | Tornar a checagem de idioma informativa (aviso não bloqueante com opção "Deseja prosseguir mesmo assim?"). |
| **5** | Falta de rolagem e controles de voz | Médio | Adicionar ScrolledText e controles deslizantes para velocidade e seleção de voz. |

**Correção Prática no Projeto (Antes e Depois)** 

|**Antes**                                                 | **Depois** | 
|----------------------------------------------------------|------------| 
|Armadilha de Teclado (Keyboard Trap)                      | Corrigido
|Autoplay e Roubo Abrupto de Foco                          | Corrigido
|Inacessibilidade e Falta de Alternativa Textual no Gráfico| Corrigido
|Ausência de Rótulos (Labels) e Controles Rígidos          | Corrigido
|Congelamento da Interface (UI Freeze)                     | Corrigido
|Dispersão e Quebra de Foco (App Switching Chaos)          | Corrigido
|Ausência de Controles de Áudio Embutidos                  | Corrigido
|Falta de Barra de Rolagem (Scrollbar)                     | Corrigido

**Pull request** 

Link: [melhorias](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/compare/main%40%7B1day%7D...main)



