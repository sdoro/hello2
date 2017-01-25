## hello2 laboratory's exercise

### 00. init

    # make a new report inside github.com
    git init
    git add README.md
    git commit -m "0. init"
    git remote add origin git@github.com:sdoro/hello2.git
    git push -u origin master

### 01. build a virtual environment with django 1.10.4 (and verify)

    virtualenv $HOME/.env
    source $HOME/.env/bin/activate
    # make/edit requirements.txt
    git add requirements.txt
    pip install -r requirements.txt
    pip freeze
    git commit -m "1. build a virtual environment with django 1.10.4"
    git push

### 02. create a project named Rossi

    django-admin.py startproject Rossi
    git add Rossi README.md
    git commit -m "2. create a project named Rossi"
    git push

### 03. set database name backend to Pierino.db

    cd Rossi
    #edit Rossi/settings.py
    ./manage.py makemigrations Pierino
    ./manage.py migrate
    git add ../README.md Rossi/settings.py 
    git commit -m "3. set database name backend to Pierino"
    git push

### 04. verify that a browser can view and report url in a README.md files

    ./manage.py runserver $IP:$PORT
    http://hello2-sdoro.c9users.io/
    git commit -m "4. verify that a browser can view and report url in a README.md files"
    git push

### 05. create an app named Pierino

    ./manage.py startapp Pierino
    git add ../README.md Pierino
    git commit -m "5. create an app named Pierino"
    git push

### 06. install pif module (and verify)

    pip install pif
    git add ../README.md
    pip freeze
    git commit -m "6. install pif module"
    git push

### 07. make a view named myIp

    # edit Pierino/views.py
    git add ../README.md Pierino/views.py
    git commit -m "7. make a view named myIp"
    git push

### 08. change urls.py

    # edit Pierino/urls.py
    ./manage.py runserver $IP:$PORT
    git add ../README.md Rossi/urls.py
    git commit -m "8. change urls.py"
    git push

### 09. verify http

    # verify http://hello2-sdoro.c9users.io/helloIP
    git add ../README.md
    git commit -m "9. verify http"
    git push

### 10. modify urls.py adding 3 views

    # edit Rossi/urls.py
    git add ../README.md Rossi/urls.py
    git commit -m "10. modify urls.py adding 3 views"
    git push

### 11. build 3 view related to year, month, day ...

    # edit Rossi/settings.py
    mkdir Rossi/Pierino/template
    # make/edit base.html
    # make/edit estesa.html
    # edit Pierino/views.py
    git add ../README.md Pierino/views.py Rossi/settings.py ../template
    git commit -m "11. build 3 view related to year, month, day ..."
    git push

### 12. make and use static file (with a simple style.css)

    mkdir -p Pierino/static/Pierino/css
    > Pierino/static/Pierino/css/style.css
    # edit Pierino/static/Pierino/css/style.css
    # edit Pierino/templates/base.html
