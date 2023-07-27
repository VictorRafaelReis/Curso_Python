"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;


# Atributos de Instância: São atribuidos, declarados, dentro do método construtor.

# OBS: Método construtor: é um método especial utilizado para a construção do objeto.


# Em Java, uma classe lâmpada, incluindo seus atributos ficaria mais ou menos assim:

    public class Lampada() {
        private int voltagem;  # Visivel somente na classe
        public String cor;  # Visivel em todos arquivos 
        protected Boolean ligada = false;  # Visivel em todo o pacote

        public Lampada(int voltagem, String cor) {
            this.voltagem = voltagem;
            this.cor = cor;
        }
    }


# Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto. Caso queiramos demonstrar que determinado
atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente
dentro da própria classe onde está declarado, utiliza-se __ duplo underline no inicio de seu nome.
Isso é conhecido como Name Mangling.


# Em Python, a mesma classe lâmpada, incluindo seus atributos ficaria assim:

    #Classes com atributos de instância público

        class Lampada:
            
            def __init__(self, voltagem, cor):
                self.voltagem = voltagem
                self.cor = cor
                self.ligada = false

            
        class ContaCorrent:
        
            def __init__(self, numero, limite, saldo):
                self.numero = numero
                self.limite = limite
                self.saldo = saldo

    
    # OBS: self é o objeto que está executando o método.

    #Classe com atributos de instância privado:

        class Acesso:
            
            def __init__(self, email, senha):
                self.__email = email  # público
                self.__senha = senha  # privado

            def mostra_email(self):  # Forma correta de acessar um atributo privado
                print(self.__email)
                 
            def mostra_senha(self):  # Forma correta de acessar um atributo privado
                print(self.__senha)

        
        # Acessando os atributos privados da classe Acesso fora da classe, (Não recomendado), apenas por exemplo.

            user = Acesso('user@gmail.com', '123456')

            print(user.email)

            # print(user.__senha)  # AttributeError

            print(user._Acesso__senha)  # Teremos acesso ao atributo senha (Name Mangling), mesmo ele sendo privado. Já que o Python não tem esse bloqueio de segurança como no java

            user.mostra_senha()  # Forma correta de acessar um atributo privado 


    # O que significa atributos de instância?

        # Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

            user1 = Acesso('user1@gmail.com', '123456')
            user2 = Acesso('user2@gmail.com', '654321')

            user1.mostra_email()
            user2.mostra_email()
    
    
# Atributos de Classe:

    # Atributos de classe, são atribuidos, claro, que são declarados diretamente na classe, ou seja,
    fora do construtor. Geralmente já iniciamos um valor, e este valor é compartilhado entre todas as
    instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como
    é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo
    valor para este atributo.

        class Produto:
            
            # Atributo de classe   
            imposto = 1.05
            contador = 0

            def __init__(self, nome, descricao, valor):
                self.id = Produto.contador + 1
                self.nome = nome
                self.descricao = descricao
                self.valor = (valor * Produto.imposto)
                Produto.contador = self.id

            
        produto1 = Produto('Playstation 4', 'Video Game', 2300)
        produto2 = Produto('Xbox S', 'Video Game', 4500)

        print(produto1.valor)  # Acesso possível, mas incorreto de um atributo de classe
        print(produto2.valor)  # Acesso possível, mas incorreto de um atributo de classe

        # OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

            print(Produto.imposto)  # Acesso correto de um atributo de classe

        # OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
        são chamados de atributos estáticos;


# Atributos Dinâmicos -> 
        
"""