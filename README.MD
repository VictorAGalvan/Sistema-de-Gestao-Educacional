## Pessoas

A classe abstrata `Pessoa` serve como base para `Aluno`, `Professor` e `Responsavel`. Ela concentra funcionalidades comuns, como validação de CPF e cálculo de idade, enquanto as classes filhas são responsáveis por suas particularidades e especializações dentro do sistema.

## Turmas e Disciplinas

A classe `Turma` é responsável por gerenciar o grupo de alunos e as disciplinas associadas. A ligação entre turmas e disciplinas ocorre por meio da classe `Grade`, que atua como intermediária nessa relação.

A classe `Disciplina` gerencia suas próprias informações, além das avaliações aplicadas aos alunos. Também possui uma estratégia de cálculo responsável por determinar a nota final.

## Matrículas

A classe `Matricula` é um dos elementos centrais do sistema, pois conecta a parte cadastral dos alunos ao sistema acadêmico. Nela são armazenadas informações como aluno, turma, data da matrícula, código, estado atual e notas obtidas.

Embora o aluno possua o método `matricular()`, a responsabilidade pela criação e gerenciamento das matrículas pertence à turma. O método existente em `Aluno` funciona apenas como uma abstração que delega a operação para a classe `Turma`.

## Avaliações e Provas

A classe `Avaliacao` representa o modelo de uma atividade aplicada aos alunos, armazenando informações sobre o que está sendo avaliado.

A classe `Prova` representa a realização dessa avaliação por uma matrícula específica, armazenando dados como a nota obtida.

A relação entre avaliação, matrícula e prova é realizada por meio de uma estrutura baseada em dicionário, permitindo associar cada matrícula à sua respectiva prova.

## State Pattern

Para controlar as regras de negócio relacionadas ao estado da matrícula, foi criada a classe abstrata `StatusMatricula`, que define as operações `concluir()` e `cancelar()`.

As classes `EmAndamento`, `Cancelado` e `Concluido` herdam dessa abstração e implementam os comportamentos permitidos para cada estado, garantindo que as transições ocorram de forma controlada.

## Strategy Pattern

O cálculo das notas foi implementado utilizando o padrão Strategy.

A interface `Calculo` define o método `calcular()`, que deve ser implementado por todas as estratégias de cálculo.

As implementações disponíveis são `MediaPonderada` e `Somatorio`. Cada disciplina possui uma estratégia associada e delega para ela a responsabilidade de calcular a nota final dos alunos.

## Factory Pattern

A criação dos objetos relacionados às pessoas é centralizada na classe `FactoryPessoa`.

Ao invés de instanciar diretamente `Aluno`, `Professor` ou `Responsavel`, o sistema solicita a criação para a fábrica.

A responsabilidade da fábrica é validar a classe solicitada e retornar uma instância correspondente de alguma implementação da classe abstrata `Pessoa`.

## Funcionamento Geral do Sistema

1. A Factory cria alunos, professores e responsáveis.
2. As disciplinas são cadastradas com sua estratégia de cálculo.
3. As turmas são criadas.
4. Os alunos são matriculados nas turmas.
5. A matrícula recebe um estado inicial "Em Andamento".
6. Avaliações e provas são registradas.
7. As notas são calculadas pela estratégia associada à disciplina.
8. Ao final do período, a matrícula pode ser concluída ou cancelada conforme as regras do padrão State.
