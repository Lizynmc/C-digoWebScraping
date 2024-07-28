from imports import *
from coletar_alunos import *
tempo_inicial = time.time()
#----------------------------------------------------------------------------------------------------------------------------------
collect_classes()
collect_students()
#----------------------------------------------------------------------------------------------------------------------------------
finalSemestre = 0

boletins = pd.concat(export_to_excell, axis=0, ignore_index=True)


nomeArquivo = 'Boletins.xlsx'
if os.path.exists(nomeArquivo):
    os.remove(nomeArquivo)

boletins.columns = colunas
boletins.drop(boletins.loc[boletins['Situacao'] == 'Cancelado'].index, inplace=True)
boletins.drop(boletins.loc[boletins['Situacao'] == 'Transferido'].index, inplace=True)

diretorioFinal = os.path.join('ArquivosExcell', f'{nomeArquivo}')
boletins.to_excel(diretorioFinal, index=False)

#Esse loop é o responsavel por separar as notas em diferentes planilhas por bimestre.
for numeracao in range(1, 5):
    #Aqui o código observa se já existe arquivos com esse nome.
    #Caso exista o aquivo tera seus dados subistituidos. caso não exita será criado um novo.
    nomeArquivo = f'Boletins {numeracao}º Bimestre.xlsx'

    if os.path.exists(nomeArquivo):
        os.remove(nomeArquivo)

    if numeracao == 2 or numeracao == 4:
        finalSemestre += 1

        if numeracao == 4:
            boletinsBimesteSeparado = boletins.loc[:,['Diario', 'Disciplina', 'CH', 'Aulas', 'Faltas', 'Freq', 'Situacao', 
            f'N{numeracao}' ,f'RE{numeracao}', f'ME{numeracao}', f'F{numeracao}',f'MD{finalSemestre}','MD','NAF','MFD', 
            'Matricula','Sigla', 'Curso']]
        
        else:
            boletinsBimesteSeparado = boletins.loc[:,['Diario', 'Disciplina', 'CH', 'Aulas', 'Faltas', 'Freq', 'Situacao', 
            f'N{numeracao}' ,f'RE{numeracao}', f'ME{numeracao}', f'F{numeracao}',f'MD{finalSemestre}', 'Matricula','Sigla', 'Curso']]
    
    else:
    #Aqui está sendo selecionada as colunas que serão colocadas nas planilhas. 
        boletinsBimesteSeparado = boletins.loc[:,['Diario', 'Disciplina', 'CH', 'Aulas', 'Faltas', 'Freq', 'Situacao', 
        f'N{numeracao}' ,f'RE{numeracao}', f'ME{numeracao}', f'F{numeracao}','Matricula','Sigla', 'Curso']]
    
    #Aqui já está sendo adicionados os dados a planilha
    
    diretorioFinal = os.path.join('ArquivosExcell', f'{nomeArquivo}')
    boletinsBimesteSeparado.to_excel(diretorioFinal, index=False)
    

print(f'Tempo de Execução: {(time.time() - tempo_inicial)/60}')