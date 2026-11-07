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


