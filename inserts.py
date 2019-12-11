from models.model import objSession, Lancamento


#Base.metadata.create_all(objEngine)

session = objSession()

#Banco_Teste = Banco("Banco de Teste 999",1,1,1)
#session.add(Banco_Teste)

#Pessoa_Teste = Pessoa("Fulano de Tal",1)
#session.add(Pessoa_Teste)

#Classificacao_Teste = Classificacao("Rendimentos de Teste","C",None,1)
#session.add(Classificacao_Teste)

#Lancamento_Teste = Lancamento(1,"20191210","Lancamento de teste",1,1,1,258,datetime.now(),None)


#session.query(Lancamento).filter(Lancamento.LancamentoId == 2044).update({'LancamentoDescricao': 'teste'+datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})

#session.query(Lancamento).filter(Lancamento.LancamentoId == 2044).delete()

#session.execute("EXECUTE spu_ListaClassificacao")
#session.commit()

lctos = session.query(Lancamento).all()
print('### Lancamentos:')
for lcto in lctos:
    print(f'({lcto.LancamentoId}) {lcto.LancamentoDescricao} - {lcto.LancamentoValor}')


#session.add(Lancamento_Teste)
#session.flush()
#print(Lancamento_Teste.LancamentoId)





session.commit()
session.close()
