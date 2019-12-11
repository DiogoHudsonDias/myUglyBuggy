from flask_sqlalchemy import SQLAlchemy
from UglyBuggy import app
from datetime import datetime

db = SQLAlchemy(app)

class Banco(db.Model):
    __tablename__ = 'Banco'
    BancoId = db.Column('BancoId',db.Integer, primary_key=True)
    BancoNome = db.Column('BancoNome', db.String(50))
    BancoAtivo = db.Column('BancoAtivo', db.Boolean, default=True)
    BancoInvestimento = db.Column('BancoInvestimento', db.Boolean, default=False)
    BancoSaldoMonetizado = db.Column('BancoSaldoMonetizado', db.Boolean, default=False)

class Pessoa(db.Model):
    __tablename__ = 'Pessoa'
    PessoaId=db.Column('PessoaId',db.Integer, primary_key=True)
    PessoaNome=db.Column('PessoaNome', db.String(50))
    PessoaAtivo=db.Column('PessoaAtivo', db.Boolean, default=True)



class Classificacao(db.Model):
    __tablename__ = 'Classificacao'
    ClassificacaoId=db.Column('ClassificacaoId',db.Integer, primary_key=True)
    ClassificacaoNome=db.Column('ClassificacaoNome', db.String(50))
    ClassificacaoTipo = db.Column('ClassificacaoTipo', db.String(1))
    Contabilizavel=db.Column('Contabilizavel', db.Boolean)
    PaiId = db.Column('Pai', db.Integer, db.ForeignKey('Classificacao.ClassificacaoId'))
    Pai = db.relationship ('Classificacao', remote_side = [ClassificacaoId])


class Lancamento(db.Model):
    __tablename__ = 'Lancamento'
    LancamentoId=db.Column('LancamentoId',db.Integer, primary_key=True)
    LancamentoOrdem = db.Column('LancamentoOrdem', db.Integer)
    LancamentoData = db.Column('LancamentoData', db.Date)
    LancamentoDescricao = db.Column('LancamentoDescricao', db.String(200))
    BancoId = db.Column(db.Integer, db.ForeignKey('Banco.BancoId'))
    PessoaId = db.Column(db.Integer, db.ForeignKey('Pessoa.PessoaId'))
    ClassificacaoId = db.Column(db.Integer, db.ForeignKey('Classificacao.ClassificacaoId'))
    LancamentoValor = db.Column('LancamentoValor', db.Numeric)
    LancamentoDataInsercao = db.Column('LancamentoDataInsercao', db.Date, default=datetime.now())
    LancamentoIdTransferenciaOrigem = db.Column(db.Integer, db.ForeignKey('Lancamento.LancamentoId'))

    banco = db.relationship('Banco', foreign_keys=BancoId)
    pessoa = db.relationship('Pessoa', foreign_keys=PessoaId)
    classificacao = db.relationship('Classificacao', foreign_keys=ClassificacaoId)
    lancamentoOrigem = db.relationship('Lancamento', foreign_keys=LancamentoIdTransferenciaOrigem)

    # @ListaLancamentoExtrato
    # def ListaLancamentoExtrato(self):
    #     return 'teste'

# def __init__(self, strBanco, priority, description):
#     self.strBanco = Banco
#     self.category = category
#     self.priority = priority
#     self.description = description
#     self.creation_date = datetime.utcnow()
#     self.is_done = False