## hello2 laboratory exercise

# 0. init

    # make a new report inside github.com
    git init
    git add README.md
    git commit -m "0. init"
    git remote add origin git@github.com:sdoro/hello2.git
    git push -u origin master

# 1. build a virtual environment with django 1.4.2

    virtualenv $HOME/.env
    source $HOME/.env/bin/activate
    # make/edit requirements.txt
    git add requirements.txt
    pip install -r requirements.txt
    git commit -m "1. build a virtual environment with django 1.4.2"
    git push

# 2. create a project named Rossi

    django-admin.py startproject Rossi
    git add Rossi README.md
    git commit -m "2. create a project named Rossi"
    git push

# 3. set database name backend to Pierino

    cd Rossi
    #edit Rossi/settings.py
    git add ../README.md Rossi/settings.py 
    git commit -m "3. set database name backend to Pierino"
    git push

# 4. verify that a browser can view and report url in a README.md files

    ./manage.py runserver $IP:$PORT
    http://hello2-sdoro.c9users.io/
    git commit -m "4. verify that a browser can view and report url in a README.md files"
    git push

# 5. create an app named Pierino

    ./manage.py startapp Pierino
    git add ../README.md Pierino
    git commit -m "5. create an app named Pierino"
    git push

# 6. install pif module

    pip install pif
    git add ../README.md
    git commit -m "6. install pif module"
    git push

# 7. make a view named myIp

    # edit Pierino/views.py
    git add ../README.md Pierino/views.py
    git commit -m "7. make a view named myIp"
    git push

# 8. change urls.py

    # edit Pierino/urls.py
    ./manage.py runserver $IP:$PORT
    git add ../README.md Rossi/urls.py
    git commit -m "8. change urls.py"
    git push

# 9. verify http

    # verify http://hello2-sdoro.c9users.io/helloIP
    git add ../README.md
    git commit -m "9. verify http"
    git push

# 10. modify urls.py adding 3 views

    # edit Rossi/urls.py
    git add ../README.md Rossi/urls.py
    git commit -m "10. modify urls.py adding 3 views"
    git push

# 11. build 3 view related to year, month, day ...

    # edit Rossi/settings.py
    MY_TEMPLATE=/home/ubuntu/workspace/template
    mkdir $MYTEMPLATE
    # make/edit $MY_TEMPLATE/base.html
    # make/edit $MY_TEMPATE/estesa.html
    # edit Pierino/views.py
    git add ../README.md Pierino/views.py Rossi/settings.py ../template
    git commit -m "11. build 3 view related to year, month, day ..."
    git push
