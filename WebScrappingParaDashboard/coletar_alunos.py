from coletar_turmas import *
from imports import *
from imports import colunas

matriculas = []
#----------------------------------------------------------------------------------------------------------------------------------
def collect_students():
    global matriculas
    global get_matriculas 
    i = 0
    a = 0
    t = 0 
    for link in armazenar[0]:
            p = 0
            driver.get(link)
            driver.find_element(By.XPATH, '//*[@id="content"]/ul[2]/li[2]/a').click()
            matriculas.append([])
            while True:
                try:
                    get_matriculas = driver.find_element(By.XPATH, f'//*[@id="content"]/div[6]/div[1]/div/form/table/tbody/tr[{1+p}]/td[3]/a').text
                    matriculas[i].append(get_matriculas)
                    p += 1
                except:
                    i += 1
                    print(len(matriculas[0]))
                    break

            if any(not sublista for sublista in matriculas):
                print("Pelo menos uma lista interna está vazia.")
            else:
                print("Nenhuma lista interna está vazia.")

    while True:
        if a == len(matriculas[t]):
             a=0
             t+=1
        if t == len(matriculas):
             return
        # try:
        driver.implicitly_wait(0.8) 
        driver.get(f'Link de acesso a turmas e alunos de um curso específico')
        

        # except IndexError:
        #     if a == len(matriculas[t]):
        #         t += 1
        #         a = 0
        #         param_break +=1
        #         continue
        #     else:sys.exit()
        driver.implicitly_wait(0.8) 
        name_aluno = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/dl/div[1]/dd').text
        driver.implicitly_wait(0.8)
        html_turmas = driver.find_element(By.CLASS_NAME, "borda").find_element(By.TAG_NAME, "tbody").get_attribute('outerHTML').replace('tbody', 'table')
        driver.implicitly_wait(0.8)
        tabela = pd.read_html(html_turmas, header=None, encoding='utf-8')[0]
        tabela['Matricula'] = [name_aluno]*len(tabela)
        tabela['Sigla'] = [armazenar[1][t]]*len(tabela)
        tabela['Curso'] = [armazenar[2][t]]*len(tabela)
        df = pd.DataFrame(tabela)
        colunas_excluir = df.eq('Detalhar').sum()
        df = df.drop(columns=colunas_excluir[colunas_excluir >= 1].index)
        df = df.dropna(axis=1, thresh=5)
        export_to_excell.append(df)
        # df = df.drop(24, axis=1)
        a += 1
        driver.implicitly_wait(0.5)
        print(f'{name_aluno}, turma:{armazenar[1][t]}, curso: {armazenar[2][t]}')
#-----------------------------------------------------------------------------------------------------------------------------------------
