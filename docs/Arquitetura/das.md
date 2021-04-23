# DAS - Documento de Arquitetura de Software

## 1. Introdução

### 1.1 Finalidade

Este documento tem como finalidade especificar e documentar as decisões arquiteturais do software Encare, usando diferentes visões arquiteturais para detalhar diferentes aspectos do sistema.

### 1.2 Escopo

O escopo desse documento de arquitetura abrange todo a arquitetura do software em diferentes níveis a ser desenvolvido na disciplina. 

### 1.3 Definições, Acrônimos e Abreviações

|Sigla|Descrição|
|---|---|
|DAS|Documento de Arquitetura de Software| 
|MTV|Model Template View|

### 1.4 Visão Geral

O projeto trata de uma aplicação web que tem como objetivo facilitar a procura por serviços de cuidados pessoais. Para isso o projeto contará com uma API que utilizará o framework django e um frontend em ReactJS

## 2. Representação Arquitetural

Esse diagrama mostra de uma forma mais ampla como o software irá trabalhar, mostrando como se relacionam o backend, fronted, usuário, banco de dados e API externa. com isso podemos ter uma visão ampla sobre dodo o processo que envolve todas essas camadas de software.  

Nesse diagrama temos os seguintes participantes:
- **Usuário**: Responsável pelas ações que o sistema terá que lidar. Aqui nesse classe estão também os Administradores do site que irão gerenciar o site, mas também são usuário do site. 
- **Frontend ReactJS**: É a primeira camada do software em relação ao usuário e é a única parte do sistema que client-side. Tem como principal função realizar a comunicação do sistema com o usuário por meio de páginas renderizadas e as interações e a partir disso realizar as requisições necessárias. 
- **Backend Django Python**: É a primeira camada server-side e tem como função tratar as requisições, processar os dados, consultar os dados, consultar APIs externas e prover a modelagem em classes dos dados. É aqui onde ocorre a modelagem de dados.
- **API externa de Mapas**: É uma API onde possa calcular as distâcias entre duas localizações para ser usada nos filtros de distância.
- **Banco de Dados PostgreSQL**: Tem como função de armazenar e persistir os dados da aplicação. 

![Diagrama1](./img/Entidade-relacionamento.png)

A seguir iremos explicar brevemente sobre cada uma das tecnologias escolhidas:

### 2.1. Python Django:

[Django](https://www.djangoproject.com/start/overview/) é um framework Python de alto nível que encorja o desenvolvimento rápido e um design límpo e pragmático. foi construido por desenvolvedores experientes e cuida de boa parte do trabalho para que o desenvolverdor possa cuidar do mais importante. Tem como principais caracteristicas:
- Desenvolvido para ser rápido como for possível.
- Inclui dezenas de extras que ajudam a resolver várias tarefas de desenvolvimento Web, como autenticação, RSS feed, entre outros...
- Cuida da segurança de muito processos, como autenticação e acesso ao banco de dados.
- É escalável para possíveis grandes demandas de requisições.
- Muito versátipo

### 2.2. ReactJS:

Para o frontend, a equipe decidiu pela utilização do [ReactJS](https://pt-br.reactjs.org/), uma biblioteca JavaScript bastante popular e voltada a desenvolvimento web. As suas principais caracteristicas são:
 - Baseado em componentes 
 - Pode ser renderizado no servidor através do servidor.
 - Dados são passsados das classes mães para as classes filhas por meio das props. 
 - Um componente por usar plugins externos. 

### 2.3. PostgreSQL:

[PostegreSQL](https://www.postgresql.org/about/) é uma poderosa ferramenta de banco de dados relacional de código aberto que usa e extende as liguagem SQL com algumas funcionalidades que escalam e dimensionam as cargas de dados mais complicadas. 

Essa será a ferramenta usada para persistir os dados da aplicação.

## 3. Metas Arquiteturais e Restrições

### 3.1 Metas:
|Meta|Descrição|
|---|---|
|Portabilidade|O software deverá ser portátil para navegadores mobile e desktop|
|Usabilidade|O usuário deverá ser capaz de realizar as tarefas no menor tempo possível|

### 3.2 Restrições:

|Restrição|Descrição|
|---|---|
|Conectividade|A aplicação precisará de internet para trabalhar|
|Plataforma| A aplicação irá rodar somente em navegadores web|
|Público|A aplicação será voltada ao público brasileiro que seja voltado a cuidados pessoais|
|Língua|A aplicação será voltada a pessoas que falam o português do Brasil|
|Equipe|A equipe possui apenas 7 integrantes|
|Horas semanais de trabalho por integrante|4 horas|
|Deadline|A aplicação deverá ser finalizada até o fim da disciplina|
|Hospedagem|Será usada uma conta básica na Amazon AMS|

## 4. Visão de Casos de Uso

A visão de casos de uso apresenta uma visão próxima do usuário, descrevendo cenários de uso da aplicação.

![Diagrama de Casos de Uso](./img/diagrama_casos_uso_ne.png)

## 5. Visão Lógica

## 6. Visão de Processos

## 7. Visão de Implantação

## 8. Visão de Implementação

A visão de implementação específica os componentes de código do projeto, como organização dos arquivos, dependências e pacotes em diferentes camadas e subcamadas. Essa visão é representada principalmente pelo diagrama de componentes.

As versões anteriores do diagrama abaixo podem ser visualizadas em [Modelagem](../Modelagem/diagrama_componentes/diagrama_componentes.md).

![Diagrama de Componentes v4](img/Diagrama_componentes_v4.png)

## 9. Visão de Dados (Opcional)

## 10. Tamanho e Desempenho

Segundo o SEBRAE, o Brasil possui aproximadamente 700 mil estabelecimentos de serviços voltados a beleza e estética. Outro dado interessante é que aproximadamente 42,3% dos consumidores desejam cuidados pessoais com a finalidade de ficarem mais bonitos. No ambiente do Distrito Federal, os estabeleciemntos de cuidados pessoais somam cerca de 8 mil estabelecimentos. 

Tendo os dados acima, podemos estimar qual será o uso da plataforma do ponto de vista dos estabelecimentos. Como o planejado é o uso do sistema inicialmente no Distrito Federal, então o sistema terá que suportar o uso por 8 mil estabelecimentos e seus respectivos clientes. Assim podemos concluir que o uso da plataforma, no caso em que todos os estabelecimentos de beleza forem cadastrados, não será sobrecarregado, visto que esse número, a nível computacional, não é relevante para desempenho. O que realmente pode pesar é o acesso simultâneo de clientes na plataforma, que, como é um número desconhecido, pode ser que interfira em um abom desempenho da aplicação. 

Em nível nacional, o desempenho tem que ser avaliado mais ainda, pois são mais de 700.000 estabelecimento, e consequentemente nesse caso pode complicar por sem um número bem maior de estabelecimentos que estarão cadastrados e ainda mais usuários do tipo cliente. Sendo assim para avançar para nível nacional, o produto pode precisar passar por uma avaliação criteriosa de desempenho para não oferecer um uso lento para o usuário (tanto dono de estabelecimento quanto cliente) a fim de evitar possíveis problemas.

Por fim é necesário destacar que essas estimativas são com base nos poucos dados disponíveis sobre possíveis usuários no Brasil e no Distrito Federal, findando em uma estimativa que pode ter uma diferença considerável para a real estimativa. 

## 11. Qualidade

A arquitetura descrita neste documento contribui com as seguintes características de qualidade[7]:

|Característica|Definição|Contribuição|
|----|----|----|
|Manutenibilidade| A capacidade de um software comportar modificações, melhorias, correções ou adaptação a novos requisitos. | A arquitetura documentada pode ser modificada para se adequar às modificações, trazendo mais segurança para modificações no código.
|Confiabilidade| A capacidade do software evitar falhas e manter um desempenho adequado quando elas acontecem, sob condições especificadas. | A modularização facilita o processo de testes, o que diminui o número de potenciais falhas.
|Portabilidade| A capacidade de um software operar em diferentes ambientes | A separação de responsabilidades e camadas do software permite uma melhor adaptação para diferentes ambientes de hardware e software. Esta característica está diretamente relacionada com o [RNF02](../Modelagem/backlog/Backlog.md).
|Eficiência de Desempenho| A capacidade do produto fornecer um desempenho apropriado, no que se trata de uso de recursos e tempo. | A modularização fornecida pelas modelagens contribui na avaliação de complexidade e uso de recursos.
|Usabilidade| A facilidade de um usuário compreender, aprender, utilizar e apreciar o software, quando usado sob condições especificadas. | A arquitetura do software contribui ao facilitar a modificação de recursos que afetem a usabilidade, como por exemplo, melhorar a estética, ou a prevenção a erros do usuário. Essa característica está ligada ao [RNF01](../Modelagem/backlog/Backlog.md).

## Referências

[1] Template do [documento de arquitetura de software](https://github.com/UnBArqDsw2020-2/2020.2_G2_Encare/files/6305164/Software.Architecture.Document.pdf). Disponibilizado no moodle da disciplina.
[2] React: Uma biblioteca JavaScript para criar interfaces para usuários. Disponível em: <https://pt-br.reactjs.org/>. Acesso em 19 abr. 2021.
[3] About PostgreSQL. Disponível em: <https://www.postgresql.org/about/>. Acesso em 20 abr. 2021
[4] Django: the web framework for perfectionists with deadlines. Disponível em: <https://www.djangoproject.com/start/overview/>. Acesso em 20 abr. 2021. 
[5] Painel setorial de informações estratégicas - SEBRAE. Disponível em: <https://www.sebrae.com.br/Sebrae/Portal%20Sebrae/UFs/BA/Anexos/P06%20Servi%C3%A7os%20Beleza%20e%20Est%C3%A9tica%20rev01_04052018.pdf>. Acesso eme 22 abr. 2021.
[6] Mercado da beleza cresce 8% no DF e movimenta R$ 350 milhoes por mês. Disponível em: <https://www.correiobraziliense.com.br/app/noticia/cidades/2015/07/01/interna_cidadesdf,488556/mercado-da-beleza-cresce-8-no-df-e-movimenta-r-350-milhoes-por-mes.shtml>. Acesso em 22 abr. 2021. 
[7] KOLBERG et al. Qualidade de Software. Disponível em: <https://www.inf.ufpr.br/lmperes/2019_1/ci221/trabalhos/trab3/atividadeA/aula_fatores_qualidade_geral_iso9126_25010.pdf>. Acesso em 23 abr. 2021.

## Versionamento

|Data|Nome|Detalhes|Versão|
|----|---|---|---|
| 16/04/21 | Wagner Martins | Criação do documento | 0.1 |
| 16/04/21 | Wagner Martins | Adição da finalidade | 0.2 |
| 19/04/21 | João Pedro Carvalho | Adição da visão geral e das siglas  | 0.3 |
| 20/04/21 | João Pedro Carvalho | Adição da representação arquitetural  | 0.4 |
| 20/04/21 | João Pedro Carvalho | Adição das metas e restrições arquiteturais  | 0.5 |
| 20/04/21 | Wagner Martins | Adição do diagrama de casos de uso | 0.6 |
| 22/04/21 | Wagner Martins | Adição do diagrama de componentes na visão de implementação | 0.7 |
| 22/04/21 | João Pedro Carvalho | Adição do tamanho e desempenho | 0.8 |
| 23/04/21 | Wagner Martins | Adição das especificações de qualidade | 0.9 |

