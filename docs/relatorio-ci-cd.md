# Visão Geral e Arquitetura da Esteira 

**Diagrama do pipeline (Mermaid)** 

Link: [Diagrama](https://canva.link/ns21ryeg587tncd)  

### Descrição dos estágios

A aplicação inicia com a configuração da interface gráfica (GUI) em tkinter e ttk, criando uma janela principal responsiva de 840x760 pixels voltada à acessibilidade, instanciando variáveis de controle de estado e montando blocos lógicos como a caixa de texto com barra de rolagem, painel de ajustes, botões, tabela estatística e barra de status, além de configurar atalhos de teclado e navegação por foco. Na etapa seguinte, o usuário insere o texto e aciona a conversão, momento em que o sistema executa uma validação para verificar se o campo está vazio — emitindo um aviso caso esteja — e utiliza a biblioteca langdetect para conferir se o idioma do texto coincide com a opção selecionada no combobox. Com os dados validados, o processo avança para uma thread em segundo plano para evitar o travamento da interface, aplicando uma rotina de suavização por expressões regulares que ajusta a pontuação e as pausas naturais do texto. Dentro dessa thread, o motor pyttsx3 é inicializado com as configurações de velocidade e volume definidas pelo usuário, aplicando uma varredura inteligente para selecionar a voz mais suave disponível e salvando o resultado em um arquivo temporário (saida.wav) após validar sua integridade. O término da síntese é comunicado à thread principal de forma segura através do método root.after, que restaura os botões, atualiza o status, gera as estatísticas e a tabela de frequência de caracteres utilizando collections.Counter, e dispara o autoplay caso esteja ativado. Por fim, o usuário dispõe de controles de reprodução multicanal via pygame ou winsound, opções para salvar o arquivo de áudio em um diretório personalizado e a capacidade de abrir uma thread dedicada para visualizar um gráfico de barras com a frequência das letras gerado pelo matplotlib. 

### Cultura DevOps e Testes Contínuos

A análise crítica do pipeline à luz dos princípios de DevOps revela tanto acertos arquiteturais quanto lacunas importantes. Em relação à Eliminação de Atritos, a aplicação se manifesta positivamente ao utilizar multithreading para impedir o travamento da interface gráfica durante processamentos pesados, além de implementar atalhos de teclado e navegação por foco que reduzem o esforço de interação humana; contudo, o código carece de um sistema centralizado de logs estruturados, dependendo excessivamente de impressões no console e alertas modais em vez de canalizar erros para coletores de telemetria. No que tange à Repetibilidade com Docker, o script atual viola esse princípio de isolamento por possuir fortes acoplamentos com o sistema operacional local — exigindo servidor gráfico para o tkinter, dependências de áudio nativas como o winsound e pacotes externos como o espeak para o funcionamento do pyttsx3, o que demandaria uma refatoração profunda da arquitetura para conteinerização. No pilar de Shift-Left, a qualidade e a eficiência são antecipadas por meio de validações preventivas de campo vazio e checagem automática de idioma via langdetect antes de iniciar a síntese, embora falhe por não incorporar testes automatizados via pytest em pipelines de CI/CD, deixando a garantia de qualidade totalmente dependente de validação manual. Por fim, no Shift-Right, a observabilidade e a resiliência em ambiente real aparecem através de feedbacks claros na barra de status, de um mecanismo inteligente de fallback de áudio entre o pygame e o subsistema nativo, e de opções de autoplay, mas esbarram na ausência de métricas de telemetria para monitorar a saúde da aplicação e a taxa de falhas em larga escala.

### Ambiente Escolhido 

**Justificativa da escolha**

O Docker é uma plataforma de código aberto voltada para o desenvolvimento, o empacotamento e a execução de aplicações por meio de containers. Em termos simples, ele permite empacotar uma aplicação junto com todas as suas dependências — como bibliotecas, arquivos de configuração e um sistema operacional base mínimo — em uma única unidade padronizada chamada container, garantindo que o software funcione de maneira idêntica em qualquer ambiente, seja no notebook de um desenvolvedor, em um servidor de testes ou em produção na nuvem.

Antes do Docker, era comum utilizar Máquinas Virtuais (VMs) para isolar aplicações, mas as VMs emulam um hardware inteiro, incluindo um sistema operacional completo, o que consome bastante memória e poder de processamento. O Docker adota uma abordagem diferente por meio da containerização, na qual os containers compartilham o kernel do sistema operacional da máquina hospedeira (*host*), em vez de rodarem um sistema operacional dedicado. Graças a isso, os containers são extremamente leves e rápidos, iniciando em segundos e ocupando muito menos espaço em disco do que uma máquina virtual tradicional.

Para operar, a plataforma baseia-se em conceitos fundamentais como o *Dockerfile*, que é um arquivo de texto com todas as instruções para construir uma imagem; a Imagem (*Image*), um pacote imutável e somente leitura que serve como modelo ou "receita de bolo"; o Container, que é a instância em execução dessa imagem e o ambiente isolado onde a aplicação roda de fato; e o Docker Hub ou *Registries*, repositórios centrais onde desenvolvedores armazenam e compartilham imagens de tecnologias como PostgreSQL, Node.js, Python e Nginx.

Dentre as principais vantagens de adotar essa tecnologia destacam-se a portabilidade, que resolve o clássico problema de o código funcionar na máquina do desenvolvedor mas falhar em produção; o isolamento, que impede conflitos entre versões de bibliotecas de diferentes projetos; e a escalabilidade e eficiência, que otimizam o uso de recursos de hardware ao viabilizar a criação ou remoção rápida de instâncias de serviços. 

**descrição da infraestrutura** 

A infraestrutura do Docker é estruturada com base em um modelo cliente-servidor (*client-server*) e em uma arquitetura modular em camadas, interagindo diretamente com os recursos do sistema operacional hospedeiro por meio de ferramentas de espaço de usuário (*user-space*) e primitivas do kernel. Na camada de interface, o Docker Client (`docker CLI`) atua como o ponto principal de interação onde o usuário digita comandos no terminal, como `docker run` ou `docker build`, que são traduzidos em requisições e enviados ao Docker Daemon (`dockerd`). Este último funciona como o serviço em segundo plano e o "cérebro" da infraestrutura no *Docker Host*, gerenciando imagens, containers, redes e volumes enquanto processa as chamadas recebidas via API REST, geralmente por meio de um socket Unix ou conexão de rede.

Para a criação e o gerenciamento do ciclo de vida dos containers, o Docker delega as operações a uma pilha de execução padronizada. Nessa etapa, o `dockerd` repassa as tarefas ao `containerd`, um runtime de alto nível responsável por gerenciar o início, a parada, a pausa, a remoção e o download de imagens. Entre eles atua o `containerd-shim`, um processo supervisor intermediário que mantém os containers desacoplados do daemon principal, garantindo que as aplicações em execução não sejam derrubadas caso o Docker Daemon precise ser reiniciado ou atualizado. Na base dessa pilha encontra-se o `runc`, um runtime de baixo nível compatível com as especificações da *Open Container Initiative* (OCI) que interage diretamente com o kernel do sistema operacional para criar o container, aplicar restrições de segurança, isolamento e configuração de recursos, encerrando-se logo após iniciar o processo.

Toda essa eficiência e o isolamento dos containers dependem diretamente de recursos nativos do núcleo do sistema operacional, primariamente o Linux Kernel. Os *Namespaces* (Espaços de Nomes) fornecem o isolamento de visibilidade ao atribuir a cada container seus próprios espaços de processos (PID), rede (net), sistema de arquivos e pontos de montagem (mnt), comunicação entre processos (IPC) e identificadores de sistema (UTS), fazendo com que ele enxergue apenas seu próprio ecossistema. Paralelamente, os *Control Groups* (`cgroups`) gerenciam e limitam o consumo máximo de CPU, memória RAM, largura de banda de rede e I/O de disco de cada container para evitar o esgotamento dos recursos da máquina física, enquanto sistemas de arquivos em camadas como o UnionFS ou OverlayFS permitem que múltiplos containers compartilhem imagens base comuns de maneira eficiente, adicionando apenas uma fina camada de escrita exclusiva para cada instância ativa.

Por fim, a infraestrutura apoia-se em objetos fundamentais e mecanismos de armazenamento para operar. As imagens funcionam como modelos somente leitura compostos por camadas empilhadas que definem o sistema base, os binários e as dependências da aplicação, sendo armazenadas, distribuídas, baixadas (*pull*) e enviadas (*push*) através de *Registries* locais ou remotos, como o Docker Hub. Complementando esse ecossistema, os volumes e as redes são gerenciados pelo daemon para assegurar tanto a persistência de dados fora do ciclo de vida efêmero do container quanto as regras de comunicação isolada entre diferentes containers e o ambiente externo, utilizando drivers como *bridge*, *host* e *overlay*.

### Instruções de Configuração 

**Variáveis de ambiente necessárias** 

- Usar Sistemas operacionais windows ou linux 
- Instalação das bibliotecas utilizadas no aplicativo 

### Links de Acesso 

**URL pública da aplicação publicada**  

Link: [URL pública](http://127.0.0.1:5000)

**URL do endpoint de /health**  

Link: [URL do enpoint](http://192.168.0.6:5000)

**link da execução do pipeline no GitHub Actions** 



### Evidências de Funcionamento 

**Logs/screenshots da execução bem-sucedida** 

**evidência do smoke test e badges**

