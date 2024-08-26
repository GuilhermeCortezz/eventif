instalar o pip: pip install wget

________________________________________________________________________

maquina virtual: python3 -m venv .eventif
ativar maquina virtual: source .eventif/bin/activate
desativar: deactivate
excluir: rm -rf .eventif

No Linux/MacOS: source nomedavenv/bin/activate
No Windows: myenv\ Scripts\ activate

________________________________________________________________________

instalar o django:

pip install django

verificar versao: django-admin --version

________________________________________________________________________

iniciar o projeto: 

django-admin startproject eventif .

python3 manage.py help

python3 manage.py runserver

python3 manage.py startapp core

________________________________________________________________________

Regular expression:

buscar: (src|href)="((img|css|js).*?)"
alterar: $1="{% static '$2' %}"

Instalar python-decouple para privar senhas: pip install python-decouple
Instalar dburl para privar bancos de dados: pip install dj-database-url
Instalar dj-static para fornecer arquivos estaticos: pip install dj-static

Criar pasta staticfiles: python3 manage.py collectstatic

Criar senha aleatoria: python3 contrib/secret_gen.py
Adicionar no .env:
SECRET_KEY=
DEBUG=True

Pacotes q precisam ser instalados: pip freeze > requirements.txt
Instalar os pacotes: pip install -r requirements.txt