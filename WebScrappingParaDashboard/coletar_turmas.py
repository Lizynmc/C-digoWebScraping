from imports import *
armazenar = [[], [], []]
#lista aninhada de index 0: Url da turma
#lista aninhada de index 1: Sigla do Curso
#lista aninhada de index 2: Nome do Curso

#----------------------------------------------------------------------------------------------------------------------------------

optionHeadless = Options()
optionHeadless.add_argument('--headless')
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=Options())
#driver.maximize_window()

#----------------------------------------------------------------------------------------------------------------------------------
def collect_classes():
    initialPage = 'Link do sistema onde os cursos em andamento estão disponíveis'
   
    i = 0
    driver.get(initialPage)
    driver.find_element(By.ID, 'id_username').send_keys("login")
    driver.find_element(By.ID, 'id_password').send_keys("login" + Keys.ENTER)
    
    while True:
        driver.implicitly_wait(2)

        try:

            driver.implicitly_wait(10)
            verifyClass = int(driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{1+i}]').find_element(By.CLASS_NAME, 'field-get_qtd_alunos').text)

            if verifyClass > 0:
                
                siglaCurso = driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{1+i}]').find_element(By.CLASS_NAME, 'field-sigla').text
                nomeCurso = driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{1+i}]').find_element(By.CLASS_NAME, 'field-descricao').text
                driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{1+i}]/th/a[2]').click()
                turmaUrl = driver.current_url
                armazenar[0].append(turmaUrl)
                armazenar[1].append(siglaCurso)
                armazenar[2].append(nomeCurso)

                driver.get(initialPage)
                i += 1
            else:
                i += 1
                continue
        except:
            break
#------------------------------------------------------------------------------------------------------------