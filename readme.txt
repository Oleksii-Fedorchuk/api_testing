# install PyCharm Community Edition > https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce
# create new project
# clone this project from git, enter in PyCharm terminal > git clone https://github.com/Oleksii-Fedorchuk/api_testing.git
# enter in PyCharm terminal to install all needed requirements > pip install -r requirements.txt
# navigate to the folder with tests by PyCharm console > /Users/username/PycharmProjects/api_testing/tests/tests.py
# enter in pycharm terminal to start test with html reporter > pytest tests.py
# you can find a test report in the same folder
# here I implemented marks for tests so you can chose "smoke" or "regression" test rub
#for smoke test run >  pytest tests.py -m smoke -v
#for regression test run >  pytest tests.py -m regression -v