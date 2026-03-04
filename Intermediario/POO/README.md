# Programação Orientada a Objetos - POO

Vamos trabalhar com uma parte interessante do python que é a programação orientada a objetos, essa parte é interessante para que possamos executar tarefas mais complexas onde a programação procedural e programação funcional não dão conta, ou apresentariam alguns problemas.

Para issovamos primeiros entender algumas definições.

**Classe:** É um formato a ser seguido com informações comuns de maneira a auxiliar na construção de objetos semelhantes, é como se o objeto fosse o bolo e a classe fosse a forma do bolo.  

    A classe possui um determinado formato, 
    - Nome da Classe;
    - Caracteristicas que o objeto daquela classe vai possuir = Atributos;
    - funções que posso executar com aquela classe = Métodos

Ou seja, toda classe possui esses três blocos de informações, e esses três blocos de informações são presentes em todos os objetos que você vai construir com essa classe.

**Instância:** Quando executamos o processo de criar um objeto com uso da classe criada, estamos executando uma instancia, ou seja
    
    Instância é seguir um padrão definido na classe para criação de um determinado objeto, ou seja

            Instanciar =  Produzir um objeto

**Objeto:** Coisa material ou abstrata que é feita a partir de uma classe e pode ser descrita por meio de seus atributos, métodos e estados atual.

**Estado:** É o consjunto de todos os atributos que possuem ou não um valor, seja ele numérico ou não. esses atributos podem ser acessados de maneira direta, apesar de não ser recomendável.

**Atributos:** Atributos de uma classe são variáveis que definem as características, propriedades ou estado de um objeto, representando dados comuns a todas as instâncias daquela classe, como nome, cor ou idade

**Métodos:** Métodos de uma classe são funções definidas dentro de uma classe na Programação Orientada a Objetos (POO) que descrevem os comportamentos, ações ou operações que os objetos dessa classe podem realizar


~~~python
class minhaClasse:
    def __init__(self, atributo_1, ....):
        self.atributo_1
        ...
        pass
~~~