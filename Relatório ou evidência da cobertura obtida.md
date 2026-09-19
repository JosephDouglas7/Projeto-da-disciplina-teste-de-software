# Relatório/evidência da cobertura obtida 

[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=JosephDouglas7_Projeto-da-disciplina-teste-de-software&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=JosephDouglas7_Projeto-da-disciplina-teste-de-software)

## Passos de instalação das dependências, execução dos testes e cálculo/geração da cobertura 

### script de CI usando o GitHub Actions

**1** Procure na parte esquerda da página SonarQube cloud click na opção administração e click em administração a opção metodos de análises  

**2** Em metodos de análises escolha a opção com ações do github 

**3.** Desative a análise automática
   
Desative a análise automática antes de configurar este projeto para análise baseada em CI. 

**4.** Crie um GitHub secreto
   
No seu repositório do GitHub, vá para Configurações > Segredos e variáveis > Ações (abre em nova aba) e crie um novo secreto com os seguintes detalhes:

No campo Nome, digite SONAR_TOKEN 

No campo valor, digite a palavra chave 

**5.** Crie ou atualize uma construção de arquivo 

Crie ou atualize seu .github/workflows/build.yml 

**6.** Crie um arquivo sonar-project.properties  

Crie um arquivo de configuração no diretório raiz do projeto e nomeie-o sonar-project.properties 







