## Licença 

O Visual Studio Code (VS Code) possui uma licença dividida em duas partes principais, diferenciando o código-fonte do instalador final. Enquanto o código-fonte do projeto base, denominado *Code - OSS*, está disponível no GitHub sob a Licença MIT — uma licença de código aberto altamente permissiva —, os binários oficiais fornecidos pela Microsoft em seu site são distribuídos sob uma licença proprietária do tipo *freeware*.

Na prática, isso significa que o editor é totalmente gratuito tanto para uso pessoal quanto comercial ou empresarial. No entanto, os binários oficiais da Microsoft incluem ferramentas de telemetria para coleta de dados de uso e relatórios de erro, embora esse recurso possa ser desativado diretamente nas configurações do programa. Para quem busca uma alternativa totalmente livre de telemetria e da marca registrada da Microsoft, existe o projeto comunitário VSCodium, que compila diretamente o código aberto do *Code - OSS* sem os componentes proprietários da empresa.


|Recurso / Característica  | Visual studio code                                                  | Visual Studio (Pago: Professional / Enterprise)                           | 
|--------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------| 
|Categoria                 | Editor de código-fonte leve e modular                               |Ambiente de Desenvolvimento Integrado (IDE) completo                       |
|Custo                     | 100% Gratuito (uso pessoal ou comercial)                            |Pago (licenças avulsas ou assinaturas mensais/anuais)                      |
|Plataformas Suportadas    | Windows, macOS e Linux                                              |Exclusivo para Windows (versão para Mac foi descontinuada)                 |
|Foco de Uso               | Scripts, desenvolvimento web, Python, Node.js, suporte via extensões|Aplicações corporativas pesadas, .NET, C++, arquiteturas complexas         | 
|Desempenho e Recursos     | Início rápido, baixo uso de RAM e CPU                               |Mais pesado, consome mais recursos do sistema                              |
|Depuração (Debugging)     | Funcionalidades básicas e intermediárias via extensoes              |Ferramentas avançadas de profiling, depuração de memória e diagnósticos    |
|Testes Automatizados      | Básico (depende de extensões da linguagem)                          |Suporte avançado para testes de carga, cobertura de código e testes em lote|
|Ferramentas de Arquitetura| Não possui nativamente                                              |Diagramação de código, análise de dependências e métricas de arquitetura   |
|Suporte e SLA             | Suporte comunitário (GitHub e fóruns)                               |Suporte técnico dedicado da Microsoft e termos de serviço garantidos       |

## Arquitetura de execução

### selenium webdriver X unittest  


<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; margin: 16px 0;">
  <thead>
    <tr style="background-color: #2c3e50; color: #ffffff; text-align: left;">
      <th style="padding: 12px 16px; border: 1px solid #dcdfe6; width: 20%;">Característica</th>
      <th style="padding: 12px 16px; border: 1px solid #dcdfe6; width: 40%;">Selenium WebDriver</th>
      <th style="padding: 12px 16px; border: 1px solid #dcdfe6; width: 40%;">Unittest (Framework)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Propósito Principal</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Automação de interações com navegadores web (browser automation) e testes funcionais End-to-End (E2E).</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Framework de estrutura, organização e execução de testes (Test Runner).</td>
    </tr>
    <tr style="background-color: #f8f9fa;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Arquitetura de Comunicação</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Cliente-Servidor (JSON Wire Protocol / W3C WebDriver Protocol): O código envia comandos via HTTP/REST para um Driver específico do navegador (ChromeDriver, GeckoDriver), que traduz e comanda o browser real.</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Baseada em Classes e Métodos (<code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">unittest.TestCase</code>): Arquitetura orientada a objetos puramente em código, executando diretamente na máquina virtual da linguagem (ex: Python).</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Ciclo de Vida (Setup/Teardown)</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Gerencia a abertura, redimensionamento, navegação e fechamento de instâncias físicas ou headless do navegador (ex: <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">driver.get()</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">driver.quit()</code>).</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Gerencia o ciclo de vida lógico dos casos de teste através de ganchos (hooks) como <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">setUp()</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">tearDown()</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">setUpClass()</code> e <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">tearDownClass()</code>.</td>
    </tr>
    <tr style="background-color: #f8f9fa;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Gerenciamento de Asserções</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Possui recursos limitados ou externos para validações visuais/estruturais (muitas vezes dependendo de bibliotecas de terceiros como PyHamcrest ou do próprio framework de testes).</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Rico em Assertions nativas: Fornece dezenas de métodos prontos para validação (ex: <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">assertEqual</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">assertTrue</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">assertRaises</code>, <code style="background-color: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; font-family: monospace;">assertIn</code>).</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Execução Concorrente / Paralela</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Nativa/Externa: Requer ferramentas adicionais ou configurações avançadas (como Selenium Grid, pytest-xdist ou plugins) para rodar testes em paralelo em múltiplos navegadores.</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Sequencial por Padrão: Executa os casos de teste de forma síncrona e sequencial em uma única thread (a menos que integrado a runners externos como pytest ou unittest-parallel).</td>
    </tr>
    <tr style="background-color: #f8f9fa;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Tratamento de Assincronicidade</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Lida diretamente com o dinamismo da web utilizando Esperas (Waits) explícitas e implícitas para elementos assíncronos (AJAX, carregamento de DOM).</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Não possui conceito nativo de tempo de espera web; executa códigos lógicos síncronos instantaneamente.</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6; font-weight: 600; color: #2c3e50;">Relatórios e Logs</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Gera logs brutos de comunicação com o driver do navegador. Relatórios visuais avançados dependem de bibliotecas adicionais (ex: HTMLTestRunner).</td>
      <td style="padding: 12px 16px; border: 1px solid #dcdfe6;">Possui um console runner nativo padrão que relata sucessos, falhas, erros e contadores de tempo de execução no terminal.</td>
    </tr>
  </tbody>
</table> 

## Linguagens suportadas e aderência à stack tecnológica do grupo 

<table>
  <thead>
    <tr>
      <th>Tecnologia / Biblioteca</th>
      <th>Categoria</th>
      <th>Função no Código</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python</strong> (<code>os</code>, <code>collections</code>)</td>
      <td>Linguagem &amp; Biblioteca Padrão</td>
      <td>Manipulação do sistema operacional e contagem de frequências</td>
      <td>A base da aplicação. O módulo <code>os</code> gerencia caminhos e executa comandos para abrir o arquivo de áudio gerado; <code>Counter</code> (<code>collections</code>) mapeia e conta a frequência de letras.</td>
    </tr>
    <tr>
      <td><strong>Tkinter</strong> (<code>tkinter</code>)</td>
      <td>Interface Gráfica (GUI)</td>
      <td>Criação da janela, caixas de texto, botões, menus e alertas</td>
      <td>Biblioteca padrão do Python para desenvolvimento de interfaces de usuário (janelas, botões, campos de texto e caixas de diálogo como <code>messagebox</code> e <code>filedialog</code>).</td>
    </tr>
    <tr>
      <td><strong>pyttsx3</strong></td>
      <td>Text-to-Speech (TTS)</td>
      <td>Conversão de texto em áudio de forma local</td>
      <td>Motor de síntese de voz <em>offline</em>. É responsável por configurar a velocidade, selecionar a voz do sistema operacional compatível com o idioma e salvar o arquivo resultante (<code>save_to_file</code>).</td>
    </tr>
    <tr>
      <td><strong>langdetect</strong></td>
      <td>Processamento de Linguagem Natural (PLN)</td>
      <td>Detecção automática do idioma do texto digitado</td>
      <td>Biblioteca baseada no algoritmo de Nakatani para detecção de idiomas. Garante resultados consistentes (<code>DetectorFactory.seed = 0</code>) para validar se o idioma digitado bate com o selecionado na interface.</td>
    </tr>
    <tr>
      <td><strong>Matplotlib</strong> (<code>matplotlib.pyplot</code>)</td>
      <td>Visualização de Dados</td>
      <td>Geração de gráficos de barras da frequência de letras</td>
      <td>Utilizada para plotar o gráfico estatístico contendo a contagem das letras, o total de palavras/letras e a linha horizontal indicando a média de referência.</td>
    </tr>
  </tbody>
</table> 

