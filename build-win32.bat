pyinstaller --onefile .\main.py --add-data "assets/*;assets/" --add-data "dependencies/win32/*;dependencies/" --add-data "dependencies/bin/*;dependencies/bin/" --name="Mario Party Toolkit" --noconsole --icon="assets/diceBlock.ico"