# Padrões de projeto GOFs Comportamentais
## 1. Introdução
Os padrões comportamentais são voltados aos algoritmos e a designação de responsabilidades entre objetos.  

Os padrões comportamentais de classes utilizam a herança para distribuir o comportamento entre classes, e os padrões de comportamento de objeto utilizam a composição de objetos em contrapartida a herança. Alguns descrevem como grupos de objetos cooperam para a execução de uma tarefa que não poderia ser executada por um objeto sozinho.

## 2. Chain of Responsibility  
O Chain of Responsibility é um padrão de projeto comportamental que permite que você passe pedidos por uma corrente de handlers. Ao receber um pedido, cada handler decide se processa o pedido ou o passa adiante para o próximo handler na corrente.  

O Chain of Responsibility é aplicado quando é esperado que o programa processe diferentes tipos de pedidos em várias maneiras, mas os exatos tipos de pedidos e suas sequências são desconhecidos de antemão.

## Estrutura
1. Handler - declara a interface comum a todos os handlers concretos. Ele geralmente contém apenas um único método para lidar com pedidos, mas algumas vezes ele pode conter outro método para configurar o próximo handler da corrente.
2. Handler Base - é uma classe opcional onde é possível colocar o código padrão que é comum a todas as classes handler.
3. Handlers Concretos - contém o código real para processar pedidos. Ao receber um pedido, cada handler deve decidir se processa ele e, adicionalmente, se passa ele adiante na corrente. Os handlers são geralmente auto contidos e imutáveis, aceitando todos os dados necessários apenas uma vez através do construtor.
4. Client - pode compor correntes apenas uma vez ou compô-las dinamicamente, dependendo da lógica da aplicação.

### 2.1 Vantagens
-  É possível controlar a ordem de tratamento dos pedidos.
-  Princípio de responsabilidade única. É possível desacoplar classes que invocam operações de classes que realizam operações.
-  Princípio aberto/fechado. É possível introduzir novos handlers na aplicação sem quebrar o código cliente existente.
### 2.2 Desvantagens
- Alguns pedidos podem acabar sem tratamento.

### 2.3 Aplicação no Projeto
-- A PRINCIPIO NÃO É APLICÁVEL --
- - -

## 3. Command
O Command é um padrão de projeto comportamental que transforma um pedido em um objeto independente que contém toda a informação sobre o pedido. Essa transformação permite que você parametrize métodos com diferentes pedidos, atrase ou coloque a execução do pedido em uma fila, e suporte operações que não podem ser feitas.

## Estrutura
1. Classe Remetente - responsável por iniciar os pedidos. Essa classe deve ter um campo para armazenar a referência para um objeto comando. O remetente aciona aquele comando ao invés de enviar o pedido diretamente para o destinatário. Observe que o remetente não é responsável por criar o objeto comando. Geralmente ele é pré criado através de um construtor do cliente.
2. Interface Comando - geralmente declara apenas um único método para executar o comando.
3. Comandos Concretos - implementam vários tipos de pedidos. Um comando concreto não deve realizar o trabalho por conta própria, mas passar a chamada para um dos objetos da lógica do negócio.
4. Classe Destinatária - contém a lógica do negócio. Quase qualquer objeto pode servir como um destinatário. A maioria dos comandos apenas lida com os detalhes de como um pedido é passado para o destinatário, enquanto que o destinatário em si executa o verdadeiro trabalho.
5. Client - cria e configura objetos comando concretos. O cliente deve passar todos os parâmetros do pedido, incluindo uma instância do destinatário, para o construtor do comando. Após isso, o comando resultante pode ser associado com um ou múltiplos destinatários.

### 3.1 Vantagens
-  Princípio de responsabilidade única. É possível desacoplar classes que invocam operações de classes que fazem essas operações.
-  Princípio aberto/fechado. É possível introduzir novos comandos na aplicação sem quebrar o código cliente existente.
-  É possível implementar desfazer/refazer.
-  É possível implementar a execução adiada de operações.
-  É possível montar um conjunto de comandos simples em um complexo.

### 3.2 Desvantagens

O código pode ficar mais complicado uma vez que você está introduzindo uma nova camada entre remetentes e destinatários.

### 3.3 Aplicação no Projeto
-- APLICÁVEL EM "RATING"
- - -

## 4. Iterator
O Iterator é um padrão de projeto comportamental que permite a você percorrer elementos de uma coleção sem expor as representações dele (lista, pilha, árvore, etc.)
Além de implementar o algoritmo em si, um objeto iterador encapsula todos os detalhes da travessia, tais como a posição atual e quantos elementos faltam para chegar ao fim. Por causa disso, alguns iteradores podem averiguar a mesma coleção ao mesmo tempo, independentemente um do outro.

O Iterator é utilizado quando se quer que o código seja capaz de percorrer diferentes estruturas de dados ou quando os tipos dessas estruturas são desconhecidos de antemão.

### Estrutura
1. Interface Iterador - declara as operações necessárias para percorrer uma coleção: buscar o próximo elemento, pegar a posição atual, recomeçar a iteração e outras
2. Iteradores Concretos - implementam algoritmos específicos para percorrer uma coleção. O objeto iterador deve monitorar o progresso da travessia por conta própria. Isso permite que diversos iteradores percorram a mesma coleção independentemente de cada um.
3. Interface Coleção - declara um ou mais métodos para obter os iteradores compatíveis com a coleção.
4. Coleções Concretas - retornam novas instâncias de uma classe iterador concreta em particular cada vez que o cliente pede por uma.
5. Client - trabalha tanto com as coleções como os iteradores através de suas interfaces. Dessa forma o cliente não fica acoplado a suas classes concretas, permitindo usar várias coleções e iteradores com o mesmo código client.
   
### 4.1 Vantagens
- Princípio de responsabilidade única. é possível limpar o código cliente e as coleções ao extrair os pesados algoritmos de travessia para classes separadas.
- Princípio aberto/fechado. é possível implementar novos tipos de coleções e iteradores e passá-los para o código existente sem quebrar coisa alguma.
- É possível iterar sobre a mesma coleção em paralelo porque cada objeto iterador contém seu próprio estado de iteração.
- Pelas mesmas razões, é possível atrasar uma iteração e continuá-la quando necessário.

### 4.2 Desvantagens
- Aplicar o padrão pode ser um preciosismo se sua aplicação só trabalha com coleções simples.
- Usar um iterador pode ser menos eficiente que percorrer elementos de algumas coleções especializadas diretamente.
### 4.3 Aplicação no Projeto
-- APLICÁVEL EM "PICTURE" --
- - -

## 5. Mediator
O Mediator é um padrão de projeto comportamental que permite que você reduza as dependências caóticas entre objetos. O padrão restringe comunicações diretas entre objetos e os força a colaborar apenas através do objeto mediador.

## Estrutura
1. Componentes - são várias classes que contém alguma lógica de negócio. Cada componente tem uma referência a um mediador, declarada com o tipo de interface do mediador. O componente não está ciente da classe atual do mediador, então é possível reutilizar o componente em outros programas ao ligá-lo com um mediador diferente.
2. Interface do Mediador - declara métodos de comunicação com os componentes, os quais geralmente incluem apenas um método de notificação. Os componentes podem passar qualquer contexto como argumentos desse método, incluindo seus próprios objetos, mas apenas de tal forma que nenhum acoplamento ocorra entre um componente destinatário e a classe remetente.
3. Mediadores Concretos - encapsulam as relações entre vários componentes. Os mediadores concretos quase sempre mantém referências de todos os componentes os quais gerenciam e, algumas vezes, até gerenciam o ciclo de vida deles.
4. Componentes não devem estar cientes de outros componentes - se algo importante acontece dentro ou para um componente, ele deve apenas notificar o mediador. Quando o mediador recebe a notificação, ele pode facilmente identificar o remetente, o que é suficiente para decidir que componente deve ser acionado em retorno. Da perspectiva de um componente, tudo parece como uma caixa preta. O remetente não sabe quem vai acabar lidando com o seu pedido, e o destinatário não sabe quem enviou o pedido em primeiro lugar.

### 5.1 Vantagens
- Princípio de responsabilidade única. É possível extrair as comunicações entre vários componentes para um único lugar, tornando as de mais fácil entendimento e manutenção.
- Princípio aberto/fechado. É possível introduzir novos mediadores sem ter que mudar os próprios componentes.
- É possível reduzir o acoplamento entre os vários componentes de um programa.
- É possível reutilizar componentes individuais mais facilmente.

### 5.2 Desvantagens
- Com o tempo um mediador pode evoluir para um Objeto Deus. Na programação orientada a objetos, um Objeto Deus é um objeto que sabe demais ou faz demais. O objeto deus é um exemplo de um antipadrão em projetos de software.

### 5.3 Aplicação no Projeto
-- A PRINCIPIO NO FILTRO --

- - -

## 6. Memento
O Memento é um padrão de projeto comportamental que permite que você salve e restaure o estado anterior de um objeto sem revelar os detalhes de sua implementação.
O padrão Memento é usado quando se quer produzir retratos do estado de um objeto para ser capaz de restaurar um estado anterior do objeto.

## Estrutura  
1. Classe Originadora - pode produzir retratos de seu próprio estado, bem como restaurar seu estado de retratos quando necessário.
2. Memento - é um objeto de valor que age como um retrato do estado da originadora. É uma prática comum fazer o memento imutável e passar os dados para ele apenas uma vez, através do construtor.
3. Cuidadora - sabe não só “quando” e “por quê” capturar o estado da originadora, mas também quando o estado deve ser restaurado.
4. Nessa implementação, a classe memento está aninhada dentro da originadora. Isso permite que a originadora acesse os campos e métodos do memento, mesmo que eles tenham sido declarados privados. Por outro lado, a cuidadora tem um acesso muito limitado aos campos do memento, que permite ela armazenar os mementos em uma pilha, mas não permite mexer com seu estado.

### 6.1 Vantagens
- É possível produzir retratos do estado de um objeto sem violar seu encapsulamento.
- É possível simplificar o código da originadora permitindo que a cuidadora mantenha o histórico do estado da originadora.
### 6.2 Desvantagens
- A aplicação pode consumir muita RAM se os clientes criarem mementos com muita frequência.
- Cuidadoras devem acompanhar o ciclo de vida da originadora para serem capazes de destruir mementos obsoletos.
- A maioria das linguagens de programação dinâmicas, tais como PHP, Python, e JavaScript, não conseguem garantir que o estado dentro do memento permaneça intacto.
### 6.3 Aplicação no Projeto
-- A PRINCIPIO SEM APLICAÇÃO -- 

- - -

## 7. Observer
O Observer é um padrão de projeto comportamental que permite que você defina um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando. Também pode ser conhecido como Observador, Assinante do evento, Event-Subscriber, Escutador, Listener.
O padrão Observer pode ser usado quando mudanças no estado de um objeto podem precisar mudar outros objetos, e o atual conjunto de objetos é desconhecido de antemão ou muda dinamicamente.

## Estrutura
1. Publicadora - manda eventos de interesse para outros objetos. Esses eventos ocorrem quando a publicadora muda seu estado ou executa algum comportamento. As publicadoras contêm uma infraestrutura de inscrição que permite novos assinantes se juntar aos atuais assinantes ou deixar a lista.
2. Quando um novo evento acontece, a publicadora percorre a lista de assinantes e chama o método de notificação declarado na interface do assinante em cada objeto assinante.
3. Interface Assinante - declara a interface de notificação. Na maioria dos casos ela consiste de um único método atualizar. O método pode ter vários parâmetros que permite que a publicadora passe alguns detalhes do evento junto com a atualização.
4. Assinantes Concretos - realizam algumas ações em resposta às notificações enviadas pela publicadora. Todas essas classes devem implementar a mesma interface para que a publicadora não fique acoplada à classes concretas.
5. Geralmente, assinantes precisam de alguma informação contextual para lidar com a atualização corretamente. Por esse motivo, as publicadoras quase sempre passam algum dado de contexto como argumentos do método de notificação. A publicadora pode passar a si mesmo como um argumento, permitindo que o assinante recupere quaisquer dados diretamente.
6. Cliente - cria a publicadora e os objetos assinantes separadamente e então registra os assinantes para as atualizações da publicadora.

### 7.1 Vantagens
- Princípio aberto/fechado. É possível introduzir novas classes assinantes sem ter que mudar o código da publicadora (e vice versa se existe uma interface publicadora).
- É possível estabelecer relações entre objetos durante a execução.

### 7.2 Desvantagens
- Assinantes são notificados em ordem aleatória
  
### 7.3 Aplicação no Projeto
-- A CLASSE DO CHAT FAZ ISSO --
- - -

## 8. State
O State é um padrão de projeto comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. É como se o objeto mudasse de classe.
O padrão State pode ser usado quando se tem um objeto que se comporta de maneira diferente dependendo do seu estado atual, quando o número de estados é enorme, e quando o código estado específico muda com frequência.

## Estrutura
1. Contexto - armazena uma referência a um dos objetos concretos de estado e delega a eles todos os trabalhos específicos de estado. O contexto se comunica com o objeto estado através da interface do estado. O contexto expõe um setter para passar a ele um novo objeto de estado.
2. Interface do Estado - declara métodos específicos a estados. Esses métodos devem fazer sentido para todos os estados concretos porque você não quer alguns dos seus estados tendo métodos inúteis que nunca irão ser chamados.
3. Estados Concretos - fornecem suas próprias implementações para os métodos específicos de estados. Objetos de estado podem armazenar referências retroativas para o objeto de contexto.Através dessa referência o estado pode buscar qualquer informação desejada do objeto contexto, assim como iniciar transições de estado.
4. Ambos os estados de contexto e concretos podem configurar o próximo estado do contexto e realizar a atual transição de estado ao substituir o objeto estado ligado ao contexto.

### 8.1 Vantagens
- Princípio de responsabilidade única. Organiza o código relacionado a estados particulares em classes separadas.
- Princípio aberto/fechado. Introduz novos estados sem mudar classes de estado ou contexto existentes.
- Simplifica o código de contexto ao eliminar condicionais de máquinas de estado pesadas
### 8.2 Desvantagens
- Aplicar o padrão pode ser um exagero se a máquina de estado só tem alguns estados ou raramente muda eles.
### 8.3 Aplicação no Projeto
-- A PRINCIPIO NENHUM -- 
- - -

## 9. Strategy

### 9.1 Vantagens

### 9.2 Desvantagens

### 9.3 Aplicação no Projeto

- - -

## 10. Template Method

### 10.1 Vantagens

### 10.2 Desvantagens

### 10.3 Aplicação no Projeto

- - -

## 11. Visitor

### 11.1 Vantagens

### 11.2 Desvantagens

### 11.3 Aplicação no Projeto

- - -

## 12. Conclusão

- - -

## 13. Referências

[1] - Padrões de projeto comportamentais. Disponível em: <https://refactoring.guru/pt-br/design-patterns/behavioral-patterns>.  

[2] - ALESSANDRO FERREIRA LEITE. Conheça os Padrões de Projeto. Disponível em: <https://www.devmedia.com.br/conheca-os-padroes-de-projeto/957>.

‌
‌
- - -

## 14. Versionamento
|Data|Nome|Detalhes|Versão|
|----|----|--------|------|
|03/04/2021|Nícalo Ribeiro| Criação da estrutura base do documento| 0.1|
|03/04/2021|Nícalo, Wagner, Hugo| Adição dos conceitos de Chain of Responsibility | 0.2 |
|03/04/2021|Nícalo, Wagner, Hugo| Adição dos conceitos de Command e Iterator | 0.3 |
|03/04/2021|Nícalo, Wagner, Hugo| Adição dos conceitos de Mediator, Memento, Observer e State | 0.4 |