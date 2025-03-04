import os
import shutil

# Definition der Quell- und Zielpfade
source_path = r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Neue Bilder"
destination_paths = {
    "-p1.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 1",
    "-m1.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 1",
    "-p2.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 2",
    "-m2.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 2",
    "-p3.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 3",
    "-m3.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 3",
    "-p4.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 4",
    "-m4.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 4",
    "-p5.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 5",
    "-m5.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 5",
    "-p6.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 6",
    "-m6.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 6",
    "-p7.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 7",
    "-m7.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 7",
    "-skizze.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 8",
    "-m8.jpg": r"S:\FOTOSTUDIO-PROZESS\AAA - ALLGEMEIN\Upload Bilder PIM\Bild 8"
}

def move_files(source_path, destination_paths):
    # Überprüfen, ob das Quellverzeichnis existiert
    if not os.path.exists(source_path):
        print(f"Fehler: Das Quellverzeichnis {source_path} existiert nicht.")
        return

    # Durchlaufen aller Dateien im Quellverzeichnis
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        if os.path.isfile(file_path):
            # Überprüfen, ob die Datei in eines der Zielverzeichnisse verschoben werden soll
            for suffix, dest_path in destination_paths.items():
                if filename.endswith(suffix):
                    if not os.path.exists(dest_path):
                        # Zielverzeichnis erstellen, falls es nicht existiert
                        try:
                            os.makedirs(dest_path)
                        except OSError as e:
                            print(f"Fehler: Konnte das Verzeichnis {dest_path} nicht erstellen. OS-Fehler: {e}")
                            continue
                    try:
                        # Datei in das entsprechende Verzeichnis verschieben
                        shutil.move(file_path, os.path.join(dest_path, filename))
                        print(f"Verschoben: {filename} -> {dest_path}")
                    except Exception as e:
                        print(f"Fehler beim Verschieben von {filename} nach {dest_path}: {e}")
                    break

if __name__ == "__main__":
    move_files(source_path, destination_paths)
