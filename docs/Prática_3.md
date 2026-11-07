### Auditoria e Melhoria de Usabilidade e Acessibilidade 

**Auditoria de Acessibilidade** 

Armadilha de Teclado (Keyboard Trap) — Crítico (WCAG 2.1.2):

No componente tk.Text, a tecla Tab insere tabulação no texto em vez de alternar o foco para o próximo controle. Usuários dependentes de navegação por teclado não conseguem sair do campo.

Autoplay e Roubo Abrupto de Foco — Crítico (WCAG 1.4.2 e 2.4.3):

Na função converter_texto/Teste%20de%20software/2%20Unidade/Prática_1/Main#L99-L134), o comando os.system("start ...") abre o reprodutor externo do Windows, roubando o foco do leitor de tela (NVDA/JAWS) e desorientando o usuário.

Inacessibilidade e Falta de Alternativa Textual no Gráfico — Crítico (WCAG 1.1.1 e 1.4.1):

Em gerar_grafico_letras/Teste%20de%20software/2%20Unidade/Prática_1/Main#L157-L190), o gráfico do matplotlib é puramente visual (sem resumo textual ou tabela de dados para cegos) e utiliza a combinação vermelho/verde com baixo contraste, problemática para daltonismo. Além disso, plt.show() bloqueia o loop principal da interface.

Ausência de Rótulos (Labels) e Controles Rígidos — Alto/Médio (WCAG 1.3.1 e 4.1.2):
O campo de texto e o seletor de idiomas não contam com rótulos descritivos associados.

Na função configurar_voz/Teste%20de%20software/2%20Unidade/Prática_1/Main#L17-L63), a velocidade de fala é fixada em 180, impedindo o ajuste de ritmo para usuários com deficiência auditiva ou dificuldades de processamento.

**Auditoria de Usabilidade (Heurísticas de Nielsen / ISO/IEC 25010:2023)** 

**Correção Prática no Projeto (Antes e Depois)** 

