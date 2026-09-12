## Histórico das alterações 

|Data      | Versão | Descrição         | Autor        | 
|----------|--------|-------------------|--------------|
|09/09/2026|1.0     |Documento de testes|Joseph Douglas|  

## 1- Introdução 
Esse documente descreve os requisitos a testar,os tipos de testes definidos para cada iteração, os recursos de software a serem empregados e o cronograma dos testes ao longo do projeto. As seções referentes aos requisitos, recursos e cronograma servem para permitir ao gerente do projeto acompanhar a evolução dos testes. 

Com esse documento, você deve:

- Identificar informações do projeto e os componentes do software que deve ser testado.
- Listar os Requisitos a testar.
- Recomendar e descrever as estratégias de teste a serem empregados.
- Identificar os recursos necessários e prover uma estimativa dos esforços de teste.
- Listar os elementos resultantes do projeto de testes.
  
Também é possível apresentar aqui o programa que será testado. 

## 2- Requisitos a testar 

**casos de uso** 
|Identificador do caso de uso | Nome do caso de uso          | 
|-----------------------------|------------------------------| 
| UC1                         |Gerar áudio de um texto       |  
| UC2                         |Baixar áudio                  | 
| UC3                         |Visualizar o gráfico de barras| 

**Requisitos não-funcionais:** 

|Identificador do requisito|Nome do requisito                                        | 
|--------------------------|---------------------------------------------------------| 
|RNF01                     |Rapidez do aplicativo                                    | 
|RNF02                     |Gerar gráfico de barras                                  | 
|RNF03                     |Confiabilidade alta                                      | 
|RNF04                     |usabilidade alta                                         | 
|RNF05                     |compatibilidade com sistemas operacionais linux e windows| 
|RNF06                     |Desempenho alto                                          | 

# 3- Tipos de testes  

- Teste de funcionalidade
- Teste de performace
- Teste de interface de usuário
- Teste unitário
- Teste de integração
- Teste de Sistema / End-to-End
- Teste de Aceitação
- Teste de usabilidade
- Teste de compatibilidade

## 3.1 - Teste de funcionalidade  

<br/>
<table>
    <tr>
        <th>
            Saber se as funcionalidades funcionam
        </th>
        <th colspan="4">
            saber se as funcionalidades do aplicativo estão funcionando
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            (X) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração (X)
        </th>
        <th>
            Sistema (X)
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta (X)
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/> 

## 3.2 - Teste de performace  

<br/>
<table>
    <tr>
        <th>
            Ver a rapidez de resposta
        </th>
        <th colspan="4">
           Ver o tempo de resposta da geração de áudio e geração de gráfico
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            (X) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração (X)
        </th>
        <th>
            Sistema (X)
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (X)
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/> 

## 3.3 - Teste de interface de usuário 

<br/>
<table>
    <tr>
        <th>
            Saber se a interface está ótima para o cliente
        </th>
        <th colspan="4">
            Saber se a interface está boa para o usuário final
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            (X) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração (X)
        </th>
        <th>
            Sistema (X)
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta (X)
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>  

## 3.4 - Teste unitário 

<br/>
<table>
    <tr>
        <th>
            Funcionalidade das funções separadas
        </th>
        <th colspan="4">
            Ver se todas as funcionalidades do app funcionam separadas
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            (X) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ()
        </th>
        <th>
            Sistema ()
        </th>
        <th>
            Unidade (X)
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (X)
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/> 

## 3.5 - Teste de integração 

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            () automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ()
        </th>
        <th>
            Sistema ()
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>  

## 3.6 - Teste de Sistema / End-to-End  

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            () automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ()
        </th>
        <th>
            Sistema ()
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>   

## 3.7 - Teste de Aceitação 

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            () automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>

## 3.8 - Teste de usabilidade 

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            () automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/> 

## 3.9 - Teste de compatibilidade 

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            () manual
        </th>
        <th colspan="2">
            () automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ()
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ()
        </th>
        <th colspan="2">
            Caixa preta ()
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/> 



