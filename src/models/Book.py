import uuid


class Book:
    def __init__(self, title: str, author: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        """
        metodo verifica se o livro esta emprestado , se estiver ele manda um erro
        se nao ele empresta o livro e troca a variavel para true
        """
        if self.is_borrowed:
            raise ValueError("Livro ja esta emprestado")
        self.is_borrowed = True

    def return_book(self):
        """
        se a pessoa estiver com o livro ele é TRUE chega no if ele vira FALSE e nao cai no if e ele recebe FALSE
        se a pessoa nao tinha livro ele é FALSE ele vira TRUE e cai no if e retorna este erro
        """
        if not self.is_borrowed:
            raise ValueError("Livro nao esta emprestado")
        self.is_borrowed = False
