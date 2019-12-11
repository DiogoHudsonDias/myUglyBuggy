from UglyBuggy import app
from models.model import Banco, Pessoa, Classificacao, Lancamento, db
from flask import render_template, request, redirect
from datetime import datetime


@app.route('/')
def home():
    return redirect('/lancamentos/')

@app.route('/pessoa/', methods=["GET", "POST"])
def pessoa():
    try:
        str_mensagemErro: str = ""
        str_mensagemSucesso: str = ""
        bln_BuscaDadoUnico: bool = False
        bln_RedirecionaParaLista: bool  = False

        if request.method == "POST":
            bln_RedirecionaParaLista = True

            #Se recebe o ID, busco o objeto.
            if len(request.form['PessoaId']) > 0:
                bln_BuscaDadoUnico = True
                obj_Pessoa = Pessoa.query.filter_by(PessoaId = request.form['PessoaId']).first()
                str_mensagemSucesso = "Registro atualizado com sucesso!"

            else:
                bln_BuscaDadoUnico = False
                obj_Pessoa = Pessoa()
                str_mensagemSucesso = "Registro gravado com sucesso!"

            #Seto os Valores
            obj_Pessoa.PessoaNome = request.form['PessoaNome']

            if 'PessoaAtivo' in request.form:
                obj_Pessoa.PessoaAtivo = 1 if request.form['PessoaAtivo'] == 'on' else 0
            else:
                obj_Pessoa.PessoaAtivo = 0

            db.session.add(obj_Pessoa)

            db.session.commit()

        elif request.method == "GET" and request.args.get('PessoaId') and not request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = False

        elif request.method == "GET" and request.args.get ('PessoaId') and request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = True
            obj_Pessoa = Pessoa.query.filter_by (PessoaId = request.args.get ('PessoaId')).first ()
            obj_Pessoa.PessoaAtivo = 0
            db.session.add(obj_Pessoa)
            db.session.commit()
            str_mensagemSucesso = "Registro excluído com sucesso!"
            #Comentado, quando for necessário excluir
            #if bln_exclui:
            #    Pessoa.query.filter_by (PessoaId = request.args.get ('PessoaId')).delete()

    except Exception as e:
        str_mensagemErro = e

    if bln_BuscaDadoUnico:
        if bln_RedirecionaParaLista:
            return render_template('pessoa.html', Pessoa = Pessoa.query.all(), atualizando = False,
                                    str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)
        else:
            #Busca o Registro Informado
            obj_PessoaSelecionado = Pessoa.query.filter_by (PessoaId = request.args.get ('PessoaId'))

            return render_template('pessoa.html', Pessoa = obj_PessoaSelecionado.first(),
                                    atualizando = bln_BuscaDadoUnico, str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)
    else:
        return render_template('pessoa.html',Pessoa=Pessoa.query.all(), atualizando=bln_BuscaDadoUnico, str_mensagemErro=str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)

@app.route('/banco/', methods=["GET", "POST"])
def banco():
    try:
        str_mensagemErro: str = ""
        str_mensagemSucesso: str = ""
        bln_BuscaDadoUnico: bool = False
        bln_RedirecionaParaLista: bool  = False

        if request.method == "POST":
            bln_RedirecionaParaLista = True

            #Se recebe o ID, busco o objeto.
            if len(request.form['BancoId']) > 0:
                bln_BuscaDadoUnico = True
                obj_banco = Banco.query.filter_by(BancoId = request.form['BancoId']).first()
                str_mensagemSucesso = "Registro atualizado com sucesso!"

            else:
                bln_BuscaDadoUnico = False
                obj_banco = Banco()
                str_mensagemSucesso = "Registro gravado com sucesso!"

            #Seto os Valores
            obj_banco.BancoNome = request.form['BancoNome']

            if 'BancoAtivo' in request.form:
                obj_banco.BancoAtivo = 1 if request.form['BancoAtivo'] == 'on' else 0
            else:
                obj_banco.BancoAtivo = 0

            if 'BancoInvestimento' in request.form:
                obj_banco.BancoInvestimento = 1 if request.form['BancoInvestimento'] == 'on' else 0
            else:
                obj_banco.BancoInvestimento = 0

            if 'BancoSaldoMonetizado' in request.form:
                obj_banco.BancoSaldoMonetizado = 1 if request.form['BancoSaldoMonetizado'] == 'on' else 0
            else:
                obj_banco.BancoSaldoMonetizado = 0

            db.session.add(obj_banco)

            db.session.commit()

        elif request.method == "GET" and request.args.get('BancoId') and not request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = False

        elif request.method == "GET" and request.args.get ('BancoId') and request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = True
            obj_banco = Banco.query.filter_by (BancoId = request.args.get ('BancoId')).first ()
            obj_banco.BancoAtivo = 0
            db.session.add(obj_banco)
            db.session.commit()
            str_mensagemSucesso = "Registro excluído com sucesso!"
            #Comentado, quando for necessário excluir
            #if bln_exclui:
            #    Banco.query.filter_by (BancoId = request.args.get ('BancoId')).delete()

    except Exception as e:
        str_mensagemErro = e

    if bln_BuscaDadoUnico:
        if bln_RedirecionaParaLista:
            return render_template('banco.html', banco = Banco.query.all(), atualizando = False,
                                    str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)
        else:
            #Busca o Registro Informado
            obj_bancoSelecionado = Banco.query.filter_by (BancoId = request.args.get ('BancoId'))

            return render_template('banco.html', banco = obj_bancoSelecionado.first(),
                                    atualizando = bln_BuscaDadoUnico, str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)
    else:
        return render_template('banco.html',banco=Banco.query.all(), atualizando=bln_BuscaDadoUnico, str_mensagemErro=str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)

@app.route('/classificacao/', methods=["GET", "POST"])
def classificacao():
    str_mensagemErro: str = ""
    str_mensagemSucesso: str = ""
    bln_BuscaDadoUnico: bool = False
    bln_RedirecionaParaLista: bool = False

    try:
        if request.method == "POST":
            bln_RedirecionaParaLista = True

            #Se recebe o ID, busco o objeto.
            if len(request.form['ClassificacaoId']) > 0:
                bln_BuscaDadoUnico = True
                obj_Classificacao = Classificacao.query.filter_by(ClassificacaoId = request.form['ClassificacaoId']).first()
                str_mensagemSucesso = "Registro atualizado com sucesso!"

            else:
                bln_BuscaDadoUnico = False
                obj_Classificacao = Classificacao()
                str_mensagemSucesso = "Registro gravado com sucesso!"

            #Seto os Valores
            obj_Classificacao.ClassificacaoNome = request.form['ClassificacaoNome']
            obj_Classificacao.ClassificacaoTipo = request.form['ClassificacaoTipo']
            obj_Classificacao.PaiId = request.form['Pai']

            if 'Contabilizavel' in request.form:
                obj_Classificacao.Contabilizavel = 1 if request.form['Contabilizavel'] == 'on' else 0
            else:
                obj_Classificacao.Contabilizavel = 0

            db.session.add(obj_Classificacao)

            db.session.commit()

        elif request.method == "GET" and request.args.get('ClassificacaoId') and not request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = False

        elif request.method == "GET" and request.args.get ('ClassificacaoId') and request.args.get('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = True

            # obj_Classificacao = Classificacao.query.filter_by (ClassificacaoId = request.args.get ('ClassificacaoId')).first ()
            # obj_Classificacao.ClassificacaoAtivo = 0
            # db.session.add(obj_Classificacao)
            # db.session.commit()
            Classificacao.query.filter_by (ClassificacaoId = request.args.get ('ClassificacaoId')).delete()
            str_mensagemSucesso = "Registro excluído com sucesso!"

    except Exception as e:
        str_mensagemErro = e

    if bln_BuscaDadoUnico:
        if bln_RedirecionaParaLista:
            return render_template('classificacao.html', Classificacao = Classificacao.query.all(), atualizando = False,
                                    str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)
        else:
            #Busca o Registro Informado
            obj_ClassificacaoSelecionado = Classificacao.query.filter_by (ClassificacaoId = request.args.get ('ClassificacaoId'))

            #Lista de Classificações Sem pai
            obj_ClassificacaoPais = Classificacao.query.filter_by (Pai = None).order_by(db.text('ClassificacaoTipo DESC, ClassificacaoNome ASC '))

            return render_template('classificacao.html', Classificacao = obj_ClassificacaoSelecionado.first(),
                                    atualizando = bln_BuscaDadoUnico, str_mensagemErro = str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso, Pais = obj_ClassificacaoPais)
    else:
        return render_template('classificacao.html',Classificacao=Classificacao.query.all(), atualizando=bln_BuscaDadoUnico, str_mensagemErro=str_mensagemErro, str_mensagemSucesso = str_mensagemSucesso)

@app.route('/lancamentos/', methods=["GET", "POST"])
def lancamentos():
    try:
        str_mensagemErro: str = ""
        str_mensagemSucesso: str = ""
        bln_BuscaDadoUnico: bool = False
        bln_RedirecionaParaLista: bool = False

        strSqlBuscaLancamentos= """SELECT	CONVERT(varchar,Data,103) as DataLancamento,
                                                    Banco,
                                                    Descrição as Descricao,
                                                    Classificação as Classificacao,
                                                    [Pessoa/Fornecedor] as Pessoa,
                                                    Format(Valor,'C', 'pt-br') as Valor,
                                                    Format([Saldo da Conta],'C', 'pt-br') as Saldo, 
                                                    LC_ID as LancamentoId,
                                                    ClassificacaoTipo 
                                                FROM
                                                    vwu_LancamentoComSaldoPorBanco
                                                WHERE
                                                    1 = 1   """

        if not request.args.get('R'):
            strSqlBuscaLancamentos = strSqlBuscaLancamentos.replace('SELECT','SELECT TOP 20')


        #Se náo estiver marcado para ver futuros, filtro somente até a data corrente.
        if not request.args.get('F'):
            strSqlBuscaLancamentos = strSqlBuscaLancamentos + " AND Data <= GETDATE()"
            strSqlBuscaLancamentos = strSqlBuscaLancamentos + " ORDER BY Data DESC, ORdem Desc"
        else:
            strSqlBuscaLancamentos = strSqlBuscaLancamentos + " AND Data > GETDATE()"
            strSqlBuscaLancamentos = strSqlBuscaLancamentos + " ORDER BY Data DESC, ORdem Desc"
            #strSqlBuscaLancamentos = strSqlBuscaLancamentos + " ORDER BY Data ASC, ORdem Desc"


        #Se for um post
        if request.method == "POST":
            bln_RedirecionaParaLista = True

            # Se recebe o ID, busco o objeto.
            #if len (request.form['LancamentoId']) > 0:
            if 'LancamentoId' in request.form:
                bln_BuscaDadoUnico = True

                obj_lancamento = Lancamento.query.filter_by (LancamentoId = request.form['LancamentoId']).first ()
                str_mensagemSucesso = "Registro atualizado com sucesso!"

            else:
                bln_BuscaDadoUnico = False
                obj_lancamento = Lancamento()
                str_mensagemSucesso = "Registro gravado com sucesso!"

            #Se estiver setado para executar transferencia
                #senão, continua com inserçao/atualização
            if 'transfere' in request.form:
                str_mensagemSucesso = "Transferência executada com sucesso!"
                str_sql = "EXECUTE spu_InsereTransferencia "

                str_sql = str_sql + request.form['LancamentoData'][6:] + request.form['LancamentoData'][3:5] + \
                          request.form['LancamentoData'][0:2] + ', '
                str_sql = str_sql + str (request.form['BancoIdOrigem']) + ','
                str_sql = str_sql + str (request.form['BancoIdDestino']) + ','
                str_sql = str_sql + str (
                    float (request.form['LancamentoValor'].replace ('R$ ', '').replace ('.', '').replace (',', '.')))

                strSql = str_sql
                db.session.execute (strSql)
                db.session.commit ()

            else:
                if 'LancamentoId' in request.form:
                    strSqlLancamento: str = "EXECUTE spu_AlteraLancamento @Lancamentoid = " +  str(request.form['LancamentoId']) + ", "

                else:
                    strSqlLancamento: str = "EXECUTE spu_InsereLancamento "

                # Seto os Valores
                if 'LancamentoOrdem' in request.form:
                    obj_lancamento.LancamentoOrdem = request.form['LancamentoOrdem']

                if 'LancamentoData' in request.form:
                    obj_lancamento.LancamentoData = request.form['LancamentoData'][6:]+request.form['LancamentoData'][3:5]+request.form['LancamentoData'][0:2]
                    strSqlLancamento = strSqlLancamento + "@LancamentoData = '" + request.form['LancamentoData'][6:]+request.form['LancamentoData'][3:5]+request.form['LancamentoData'][0:2] + "' "

                if 'LancamentoDescricao' in request.form:
                    obj_lancamento.LancamentoDescricao = request.form['LancamentoDescricao']
                    strSqlLancamento = strSqlLancamento + ", @LancamentoDescricao = '" + request.form['LancamentoDescricao'] + "' "

                if 'BancoId' in request.form:
                    obj_lancamento.BancoId = request.form['BancoId']
                    strSqlLancamento = strSqlLancamento + ", @BancoId = " + str(request.form['BancoId']) + " "

                if 'PessoaId' in request.form:
                    obj_lancamento.PessoaId = request.form['PessoaId']
                    strSqlLancamento = strSqlLancamento + ", @PessoaId = " + str(request.form['PessoaId']) + " "

                if 'ClassificacaoId' in request.form:
                    obj_lancamento.ClassificacaoId = request.form['ClassificacaoId']
                    strSqlLancamento = strSqlLancamento + ", @ClassificacaoId = " + str(request.form['ClassificacaoId']) + " "

                if 'LancamentoValor' in request.form:
                    obj_lancamento.LancamentoValor = float(request.form['LancamentoValor'].replace('R$ ','').replace('.','').replace(',','.'))
                    strSqlLancamento = strSqlLancamento + ", @LancamentoValor = " + str(float(request.form['LancamentoValor'].replace('R$ ','').replace('.','').replace(',','.'))) + " "

                db.session.execute (strSqlLancamento)
                db.session.commit ()


        elif request.method == "GET" and request.args.get ('LancamentoId') and not request.args.get ('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = False

        elif request.method == "GET" and request.args.get ('LancamentoId') and request.args.get ('exclui'):
            bln_BuscaDadoUnico = True
            bln_RedirecionaParaLista = True
            str_mensagemSucesso = "Registro excluído com sucesso!"
            strSql = "execute spu_DeletaLancamento " + str(request.args.get ('LancamentoId'))
            db.session.execute(strSql)
            db.session.commit()


    except Exception as e:
        str_mensagemErro = e

    if bln_BuscaDadoUnico:
        if bln_RedirecionaParaLista:
            rtnLancamento = db.session.execute (strSqlBuscaLancamentos)

            #Lista de dados para DropDowns
            obj_Banco_tmp = db.session.execute ("execute spu_VisualizaBanco ")
            obj_Pessoa_tmp = db.session.execute ("execute spu_VisualizaPessoa ")
            obj_Receita_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'C'")
            obj_Despesa_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'D'")

            obj_Banco = [(di['BancoID'], di['BancoNome']) for di in obj_Banco_tmp]
            obj_Pessoa = [(di['PessoaID'], di['PessoaNome']) for di in obj_Pessoa_tmp]
            obj_Receita = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Receita_tmp]
            obj_Despesa = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Despesa_tmp]

            return render_template ('lancamentos.html',
                                    Lancamento = rtnLancamento,
                                    Bancos = obj_Banco,
                                    Pessoas = obj_Pessoa,
                                    Receitas = obj_Receita,
                                    Despesas = obj_Despesa,
                                    atualizando = False,
                                    str_mensagemErro = str_mensagemErro,
                                    str_mensagemSucesso = str_mensagemSucesso,
                                    str_hoje = datetime.now().strftime("%d/%m/%Y")
                                    )
        else:
            # Busca o Registro Informado
            obj_lancamentoSelecionado =  Lancamento.query.filter_by (LancamentoId = request.args.get('LancamentoId'))

            #Lista de dados para DropDowns
            obj_Banco_tmp = db.session.execute ("execute spu_VisualizaBanco ")
            obj_Pessoa_tmp = db.session.execute ("execute spu_VisualizaPessoa ")
            obj_Receita_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'C'")
            obj_Despesa_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'D'")

            obj_Banco = [(di['BancoID'], di['BancoNome']) for di in obj_Banco_tmp]
            obj_Pessoa = [(di['PessoaID'], di['PessoaNome']) for di in obj_Pessoa_tmp]
            obj_Receita = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Receita_tmp]
            obj_Despesa = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Despesa_tmp]

            return render_template ('lancamentos.html',
                                    Lancamento = obj_lancamentoSelecionado.first(),
                                    Bancos = obj_Banco,
                                    Pessoas = obj_Pessoa,
                                    Receitas = obj_Receita,
                                    Despesas = obj_Despesa,
                                    atualizando = bln_BuscaDadoUnico,
                                    str_mensagemErro = str_mensagemErro,
                                    str_mensagemSucesso = str_mensagemSucesso,
                                    ClassificacaoTipo=request.args.get('ClassificacaoTipo'),
                                    str_hoje = datetime.now().strftime("%d/%m/%Y")
                                    )
    else:
        rtnLancamento = db.session.execute (strSqlBuscaLancamentos)

        obj_Banco_tmp = db.session.execute ("execute spu_VisualizaBanco ")
        obj_Pessoa_tmp = db.session.execute ("execute spu_VisualizaPessoa ")
        obj_Receita_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'C'")
        obj_Despesa_tmp = db.session.execute ("execute spu_ListaClassificacao @ClassificacaoTipo = 'D'")

        obj_Banco = [(di['BancoID'], di['BancoNome']) for di in obj_Banco_tmp]
        obj_Pessoa = [(di['PessoaID'], di['PessoaNome']) for di in obj_Pessoa_tmp]
        obj_Receita = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Receita_tmp]
        obj_Despesa = [(di['ClassificacaoId'], di['ClassificacaoNome'], di['Pai'], di['PaiNome']) for di in obj_Despesa_tmp]

        return render_template ('lancamentos.html',
                                Lancamento = rtnLancamento,
                                Bancos = obj_Banco,
                                Pessoas = obj_Pessoa,
                                Receitas = obj_Receita,
                                Despesas = obj_Despesa,
                                atualizando = bln_BuscaDadoUnico,
                                str_mensagemErro = str_mensagemErro,
                                str_mensagemSucesso = str_mensagemSucesso,
                                str_hoje = datetime.now().strftime("%d/%m/%Y")
                                )

@app.route('/transfere/', methods=["POST"])
def transfere():
    try:

        str_mensagemSucesso = "Transferência executada com sucesso!"
        str_sql = "EXECUTE spu_InsereTransferencia "

        str_sql = str_sql + request.form['LancamentoData'][6:]+request.form['LancamentoData'][3:5]+request.form['LancamentoData'][0:2] + ', '
        str_sql = str_sql + str(request.form['BancoIdOrigem']) + ','
        str_sql = str_sql + str(request.form['BancoIdDestino']) + ','
        str_sql = str_sql + str(float(request.form['LancamentoValor'].replace ('R$ ', '').replace ('.', '').replace (',', '.')))

        strSql = str_sql
        db.session.execute(strSql)
        db.session.commit()

    except Exception as e:
        str_mensagemErro = e

    return render_template('teste.html')
@app.route('/teste/', methods=["GET", "POST"])
def teste():
    return render_template('teste.html')