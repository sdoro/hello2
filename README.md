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
