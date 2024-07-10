# Packaging
Refer to https://packaging.python.org/tutorials/packaging-projects/
for more filled out instructions

## To Update Requirements and Version Number
https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py

Just take a look at setup.py and follow the instructions provided in the link.

In a nutshell:
1. change version number in setup.py
2. commit
3. create a git tag with the appropriate version number (not necessary for the packaging but helps with development.)
4. git push (make sure the tag gets pushed)

## To Package
https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
1. Run `python3 -m pip install --user --upgrade setuptools wheel`
2. From the root of this repository run `python3 setup.py sdist bdist_wheel` this should create a `dist` directory with relevant package components

## To Upload
https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
1. Run `python3 -m pip install --user --upgrade twine`
2. Run `python3 -m twine upload dist/*` this will prompt you for pypi creditials, input those and you should be set


## To PyPi
1. Create an account here https://pypi.org/
2. Gain access to push here https://pypi.org/project/bridges/

## packaging for bridges website

```
zip -r bridges-python-VERSION.zip bridges/ setup.py
```
