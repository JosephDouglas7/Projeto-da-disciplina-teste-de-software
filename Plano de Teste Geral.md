# Plano Geral de Testes de Software

Projeto: IAVoz 
Equipe/Grupo: G2
Processo: YP-Agentic
Data: 06/10/2026
Versão: 1.0 

## 1. Visão Geral do Sistema
   
[Documento de visão](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/documento_de_visao.md)

##  2. Escopo do Plano de Testes

### 2.1 Itens no Escopo (O que será testado) 

- Teste unitário,Teste de integração dos componentes do sistema
- Testes dos Requisitos Funcionais([User_stories](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/lista_de_user_stories.md))
- Testes dos Requisitos Não Funcionais ([Documento de visão](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/documento_de_visao.md))

### 2.2 Itens Fora do Escopo

- Teste de funcionalidade,Teste de performace,Teste de interface de usuário,Teste de Sistema / End-to-End,Teste de Aceitação,Teste de usabilidade,Teste de compatibilidade.

## 3. Estratégia de Testes por Requisito Não Funcional (RNF) 

>[Documento de visão](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/documento_de_visao.md)

| RNF | Tipo / Categoria | Abordagem / Estratégia de Teste | Critério de Aceitação / Métrica |
|---|---|---|---|
| [RNF01](link) | Desempenho / Carga | Teste de desepenho automatizado (selenium) | Tempo de resposta >= 1s|
| [RNF04](link) | Usabilidade | Teste manual caixa preta | Nenhuma vulnerabilidade alta/crítica |
| [RNF05](link) | Compatibilidade | Teste manual caixa preta | Taxa de conclusão >= 90% |

## 4. Tipos e Níveis de Teste 

### 4.1 Testes de Unidade  

- Foco: funções, classes e métodos isolados
- Responsável: Desenvolvedor 
- Ferramentas: unittest 

### 4.2 Testes de Integração 

- Foco: comunicação entre módulos, persistência e APIs externas.
- Responsável: Desenvolvedor / Testador.
- Ferramentas: unittest

### 4.3 Testes de Sistema e Aceitação 

- Foco: fluxo de ponta a ponta baseado em User Stories, com validação do cliente.
- Responsável: Equipe de Teste / Cliente.
- Detalhamento por iteração: Veja o [Plano da interação](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Plano%20da%20Itera%C3%A7%C3%A3o%201.md)

### 5. Ferramentas Utilizadas 

| Categoria | Ferramenta | Finalidade |
|---|---|---|
| Gestão de Testes | GitHub / Issues | Registro de casos e defeitos |
| Automação Unit/Integração | unittest | Execução automatizada |
| Análise Estática | [SonarQube] | Cobertura e dívida técnica |

### 6. Riscos e Contingências 

| Risco | Impacto | Ação Mitigatória |
|---|---|---|
| Bug de geração de áudio | Alto | adicionar um detector para saber qual idioma é compativel com o texto escrito | 

## 7. Referências 

- [Documento de Visão](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/documento_de_visao.md)]
- [Lista de User Stories](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/lista_de_user_stories.md)
- [Plano de Teste da Iteração](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Plano%20da%20Itera%C3%A7%C3%A3o%201.md)
- [Relatório de Testes de aceitação1](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Relat%C3%B3rio%20de%20testes%20de%20aceita%C3%A7%C3%A3o(QA).md)
- [Relatório de Testes de aceitação2](https://github.com/JosephDouglas7/Projeto-da-disciplina-teste-de-software/blob/main/Relat%C3%B3rio%20de%20Testes%20de%20Aceita%C3%A7%C3%A3o2(QA).md)
  

   
