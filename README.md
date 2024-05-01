# Coisas importantes
Fala galera
Esse topico e **provisorio e sera removido na entrega final do projeto**, vou usar esse topico para colocar algumas coisas importantes sobre o projeto e explicar algumas coisas no github, alem de, se necessario, colocar algumas atualizacoes aqui

# Sobre o Git/Github
   Apesar do Github ser um repositorio remoto onde podemos sempre ter acesso ao nosso trabalho dw qualquer lugar, ele e o principal meio para a entrega do projeto de banco de dados, alem de ser uma otima ferramenta para atualizarmos o projeto apartir de nossos desktops proprios
   Porem, o git e github sao ferramentas com muitas coisas a aprender, por isso, tomei a liberdade de deixar um arquivo para auxilar em alguns [comandos principais](comando_git.md) que usaremos para trabalhar no gitub, e alguns passos para iniciarmos
   # Baixando o Git
   + Antes de tudo, precisamos do proprio Git instalado para comecar a utilizar os comandos do Git e Github:
   + Baixe o proprio Git pelo site deles ou clique [aqui](https://git-scm.com/downloads) para ir direto para a area de download
   + Durante o setup do Git, escolha o melhor disco de seu pc para instalar e confirme todas as opcoes **e desmarque todas as opcoes na tela de finalizacao do setup**
   + Apos terminar de baixar o Git, utilize o comando `git --version` no cmd, caso apareca a versao do Git, entao ja esta tudo pronto
   ## Comecando a usar o Git e Github
   ### Copiando o Repositorio do Github para seu pc:
   + Primeiro, crie uma pasta em seu pc, esta pasta sera onde colocaremos a pasta do repositorio do github
   + Depois, copie o caminho dessa pasta e abra o cmd, nele digite o comando ``git init``, este comando e responsavel por criar um repositorio local em seu computador
   + E entao, digite o comando ``git clone ssh://git@github.com/[usuario]/[nome-repositorio].git`` e espere ate que o processo seja concluido, este comando e responsavel por clonar o repositorio do Github para seu repositorio local por meio do Git. (obs: a parte ``ssh://git@github.com/[usuario]/[nome-repositorio].git`` e somente o link URL do repositorio)
   + E possivel que, apos o ultimo comando ser digitado, o Git solicite que voce efetue o login no Github, para que ele possa validar se voce realmente trabalha no projeto, caso ele solicite seu login pelo cmd basta digitar seu email e seu nome, **importante: o nome digitado aparecera como padrao no seu Github**
## Como a dinamica Git e Github funciona?
+ Agora com a ferramenta Git instalada e integrada corretamente ao repositorio Github, sera possivel desenvolver cada parte do projeto em nossos desktops e em qualquer tempo, sem a necessidade de centralizar o desenvolvimento do codigo em um desktop e nem de unificar o tempo de desenvolvimento. Dessa forma, o desenvolvimento de cada parte do projeto esta separada em branches (ramificacoes) onde faremos o desenvolvimento, e quando completo, integraremos tudo na main do projeto
  ## Coisas para ter atencao
  1. O Git/Github e uma ferramenta muito boa para desenvolver codigos e projetos, mas muito sensivel a erros de comandos (exemplo: upar uma mudanca do repositorio local sem querer e perder todo o desenvolvimento que estava na branch) portanto, atencao aos [comandos](comando_git.md)
  2. Lembre-se de a cada alteracao colocar, pelo menos, uma breve descricao do que foi alterado, assim evitando conflitos de desenvolvimento futuros
  3. Para uma alteracao ser validada e realmente alterar a branch ela tem de ser confirmada pelo usuario responsavel para isso (no momento sou eu por que eu nao adicionei ninguem ainda, mas vou mudar isso o quanto antes)
  4. Sempre faca a documentacao do projeto
     
  

     
   










# Projeto-Banco-de-Dados
Projeto de banco de dados feito pelos integrantes: 
+ Lucas Antunes Sampaio - R.A: 24.122.056-5
+ Rodrigo Simões Ruy - R.A: 24.122.092-0
+ Romulo Carneiro de Oliveira Canavesso - R.A: 24.122.093-8
