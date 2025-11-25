import os

def list_files_and_folders(directory, output_file):
    """
    Listet alle Dateien und Ordner in einem Verzeichnis und seinen Unterverzeichnissen auf
    und speichert die Pfade in einer Ausgabedatei.

    :param directory: Der Pfad des zu durchsuchenden Verzeichnisses.
    :param output_file: Der Name der Datei, in der die Liste gespeichert werden soll.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Auflistung für das Verzeichnis: {os.path.abspath(directory)}\n")
            f.write("="*50 + "\n\n")

            for root, dirs, files in os.walk(directory):
                f.write(f"Ordner: {root}\n")

                for d in dirs:
                    f.write(f"  -> Unterordner: {os.path.join(root, d)}\n")

                for file in files:
                    f.write(f"  -> Datei: {os.path.join(root, file)}\n")
                
                f.write("\n")

        print(f"Die Liste der Dateien und Ordner wurde erfolgreich in '{output_file}' gespeichert.")

    except FileNotFoundError:
        print(f"Fehler: Das angegebene Verzeichnis '{directory}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    target_directory = "."

    output_filename = "verzeichnisliste.txt"

    list_files_and_folders(target_directory, output_filename)