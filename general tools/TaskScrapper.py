from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

tasks = []
dates = []
names = []
driver.get('https://educaproject.educalms.com/task/views/view_task_detail.php')

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll(attrs={'class':'body-task'}):
    task=a.find('span', attrs={'class':'task-type-title'})
    date=a.find('div', attrs={'class':'content-date ml-0'})
    name=a.find('div', attrs={'class':'full_name user_login'})
    tasks.append(task.text)
    dates.append(date.text)
    names.append(name.text)

df = pd.DataFrame({'Usuario': names, 'Tareas': tasks, 'Fechas': dates})
df.to_csv('Exportado.csv', index=False, encoding='utf-16')
