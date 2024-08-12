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



Regular expression:

buscar: (src|href)="((img|css|js).*?)"
alterar: $1="{% static '$2' %}"