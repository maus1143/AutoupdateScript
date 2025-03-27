import sys
import time
import os
import urllib.request

scriptversion = "1.0"

repo_base_url = "https://github.com/maus1143/AutoupdateScript"
version_file_url = repo_base_url + "version.txt"
script_file_url = repo_base_url + "main_script.py"

script_name = os.path.basename(__file__)

Secondary_color_theme = "\033[94m"
main_color_theme = "\033[0m"
good = "\033[92m"
red = "\033[91m"

def get_latest_version():
    """Holt die aktuelle Versionsnummer aus der Online-Version."""
    try:
        with urllib.request.urlopen(version_file_url) as response:
            return response.read().decode("utf-8").strip()
    except Exception as e:
        print(f"{red}Fehler beim Abrufen der aktuellen Version:{main_color_theme} {e}")
        return None

def update_script():
    """Lädt die neueste Version des Scripts herunter, ersetzt sich selbst und startet neu."""
    print(f"{Secondary_color_theme}Neue Version gefunden!{main_color_theme} Aktualisierung läuft...")
    try:
        new_script_path = script_name + ".new"
        urllib.request.urlretrieve(script_file_url, new_script_path)

        os.remove(script_name)

        os.rename(new_script_path, script_name)

        print(f"{good}Update erfolgreich!{main_color_theme} Starte das Skript neu...")
        time.sleep(2)
        os.system(f"python {script_name}") 
        sys.exit()

    except Exception as e:
        print(f"{red}Fehler beim Aktualisieren des Skripts:{main_color_theme} {e}")
        os.system("pause")

latest_version = get_latest_version()
if latest_version and latest_version != scriptversion:
    update_script()
else:
    print(f"{good}Skript ist auf dem neuesten Stand!{main_color_theme}")

files = {
    "RatColors": "RatColors.py",
    "RatSpreadVars": "RatSpreadVars.py",
    "Settings": "Settings.py",
}

base_path = os.path.dirname(__file__)

def download_file(module_name, file_name):
    file_path = os.path.join(base_path, file_name)
    if not os.path.exists(file_path):
        print(f"{Secondary_color_theme}{module_name}{main_color_theme} nicht gefunden, wird heruntergeladen...")
        os.system("pause")
        try:
            urllib.request.urlretrieve(repo_base_url + file_name, file_path)
            print(f"{good}{main_color_theme}Download von {Secondary_color_theme}{module_name} {main_color_theme}erfolgreich!")
            os.system("pause")
        except Exception as e:
            print(f"Fehler beim Herunterladen von {Secondary_color_theme}{module_name}{main_color_theme}:{red} {e}")
            os.system("pause")
            return False
    return True

for module, file in files.items():
    download_file(module, file)

try:
    import RatColors
except ImportError:
    print(f"{red}Fehler beim Importieren von {Secondary_color_theme}RatColors.{main_color_theme}")
    os.system("pause")
