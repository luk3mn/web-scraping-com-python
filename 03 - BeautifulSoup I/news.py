import requests
from bs4 import BeautifulSoup

# Faz uma requisição
response = requests.get('https://g1.globo.com/')

# Pega o conteúdo da requisição
content = response.content

# converte esse conteúdo para um objeto do BeautifulSoup (formato HTML)
site = BeautifulSoup(content, 'html.parser')

# prettify() => organiza o código fonte na identação HTML
# print(site.prettify())

# Agora encontra uma 'div' com atributo 'feed-post-body' e joga na variável 'noticia'
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Depois encontra uma tag 'a' em 'noticia' que tenha a class 'feed-post-link' e joga na variável 'titulo'
titulo = noticia.find('a', attrs={'class':'feed-post-link'})

# e imprimi o titulo
print(titulo.text)

# Obtendo o subtitulo => pega a tag 'div' cujo o atributo class seja 'feed-post-body-resumo' e guarda na variável 'subtitulo'
subtitulo = noticia.find('div', attrs={'class':'feed-post-body-resumo'})

# imrime o conteúdo da tag
print(subtitulo.text)