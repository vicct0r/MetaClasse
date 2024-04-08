# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)


# Criando uma função __repr__ para chamar dentro da minha MetaClass.

def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

# Meta está acessando a Classe antes de ser criada;
# Isso me permite com que eu faça algumas alterações ou restrições
# para a criação da minha classe de acordo com as necessidades do algoritmo.

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = meu_repr
        
        # Por exemplo:
        # No processo de criação da classe usando o Meta; 
        # Foi definido que se não houver no __dict__ da class o método 'falar';
        # Ele vai levantar um erro de implementação.
        # callable() força com que o usuário tenha que criar especificamente um método.
        
        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente o método "falar".')

        return cls


# Agora aqui está sendo passado minha MetaClass; 
# Ela vai fazer o que foi definido acima antes da criação dessa classe que já está 'instânciada'.

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia


    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome



p1 = Pessoa('Victor')
print(p1)