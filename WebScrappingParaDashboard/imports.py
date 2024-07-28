from selenium import webdriver
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as Service
from selenium.webdriver.edge.options import Options as Options
from selenium.webdriver import Keys
import pickle
import pandas as pd
import sys
import time
import os

colunas = ['Diario', 'Disciplina', 'CH', 'Aulas', 'Faltas', 'Freq', 'Situacao', 
       'N1','RE1', 'ME1', 'F1', 'N2', 'RE2', 'ME2', 'F2', 'MD1', 'N3', 'RE3', 'ME3', 'F3', 'N4', 'RE4', 'ME4', 'F4', 'MD2', 'MD', 'NAF', 'MFD','Matricula','Sigla', 'Curso']


export_to_excell = []