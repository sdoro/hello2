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
