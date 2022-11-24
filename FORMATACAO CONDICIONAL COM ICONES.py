#CRIANDO GRÁFICOS DE COLUNA E EMPILHADO
import xlsxwriter as opcoesDoXlsxWriter
import os

#1 - indicando onde será criado o arquivo, seu nome e sua extensão. Importante a questão das barras duplas (testar).
nomeCaminhoArquivo = 'C:\\Users\\Windows\\Desktop\\Python Projetos\\xlsxwriter\Grafico.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Resumo") #Para renomear o nome da Sheet1 para Dados.

#2 - Para criar a formatação
linhaNegrito = planilhaExcel.add_format({'bold': 1})

#Preenchendo os dados para planilha
titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ["Ana", "Pedro", "Allan", "Francisco", "Rosa", "Amanda"],
    [400, 300, 89, 34, 350, 120],
]

sheetDados.write_row('A1', titulos, linhaNegrito)
sheetDados.write_column('A2', dadosTabela[0])
sheetDados.write_column('B2', dadosTabela[1])

#Criando o Gráfico de Colunas
graficoColunas = planilhaExcel.add_chart({'type': 'column'})

#Configurando as séries
graficoColunas.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$7',
    'values': '=Resumo!$B$2:$B$7',
})

#Adicionando um título no gráfico e alguns rótulos do eixo
graficoColunas.set_title({'name': 'Gráfico total de vendas'})
graficoColunas.set_x_axis({'name': 'Vendedores'})
graficoColunas.set_y_axis({'name': 'Vendas'})

#Definindo um estilo de gráfico do excel
graficoColunas.set_style(11)

#Inserindo o gráfico na planilha com deslocamentos x e y
sheetDados.insert_chart('D2', graficoColunas, {'x_offset': 25, 'y_offset': 10})

#######################################################################################################################

#Criando o Gráfico de Colunas
graficoEmpilhado = planilhaExcel.add_chart({'type': 'area', 'subtype': 'stacked'})

#Configurando as séries
graficoEmpilhado.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$7',
    'values': '=Resumo!$B$2:$B$7',
})

#Adicionando um título no gráfico e alguns rótulos do eixo
graficoEmpilhado.set_title({'name': 'Gráfico Empilhado'})
graficoEmpilhado.set_x_axis({'name': 'Vendedores'})
graficoEmpilhado.set_y_axis({'name': 'Vendas'})

#Definindo um estilo de gráfico do excel
graficoEmpilhado.set_style(12)

#Inserindo o gráfico na planilha com deslocamentos x e y
sheetDados.insert_chart('L2', graficoEmpilhado, {'x_offset': 25, 'y_offset': 10})

#3 - Para fechar e salvar as informações
planilhaExcel.close()

#4 - Abrir o arquivo para verificar o resultado
os.startfile(nomeCaminhoArquivo)
