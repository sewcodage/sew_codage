#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tri_photos.py — Outil de tri manuel des photos de tapis (Maison DIYA).

Principe :
    1. Parcourt un dossier de photos en vrac (ordre alphabétique, stable).
    2. Ouvre chaque photo dans Aperçu (application par défaut sur Mac).
    3. Demande dans le terminal le numéro de balle correspondant.
    4. COPIE la photo vers  photos-tapis/Balle_XX/photo-01.jpg
       (photo-02.jpg, photo-03.jpg... si plusieurs photos pour la même balle).
    5. Sauvegarde la progression dans .tri_progress.json (dans le dossier
       source) : en cas d'interruption, le script reprend où il s'était arrêté.

Garanties :
    - Les photos originales ne sont JAMAIS modifiées ni déplacées (copie seule).
    - Bibliothèque standard Python uniquement (aucune installation requise).

Utilisation :
    python3 tri_photos.py [dossier_photos_en_vrac] [dossier_destination]

    Les deux arguments sont optionnels : le script demande les chemins
    au lancement s'ils ne sont pas fournis.

Réponses possibles à l'invite :
    12          → copie vers photos-tapis/Balle_12/
    sn          → copie vers photos-tapis/Balle_SN/  (balles sans numéro)
    s           → passer cette photo (on pourra y revenir plus tard)
    r           → rouvrir la photo dans Aperçu
    q           → quitter (la progression est sauvegardée)
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

# Extensions d'images reconnues dans le dossier en vrac
EXTENSIONS_IMAGES = {".jpg", ".jpeg", ".png", ".heic", ".webp", ".tif", ".tiff", ".bmp", ".gif"}

# Nom du fichier de progression (créé dans le dossier source)
FICHIER_PROGRESSION = ".tri_progress.json"

# Nom du dossier de destination par défaut
DESTINATION_DEFAUT = "photos-tapis"


def demander_dossier_source() -> Path:
    """Demande (ou lit en argument) le dossier contenant les photos en vrac."""
    if len(sys.argv) > 1:
        chemin = Path(sys.argv[1]).expanduser()
    else:
        reponse = input("Chemin du dossier contenant les photos en vrac : ").strip()
        chemin = Path(reponse).expanduser()
    if not chemin.is_dir():
        print(f"❌ Dossier introuvable : {chemin}")
        sys.exit(1)
    return chemin.resolve()


def demander_dossier_destination(source: Path) -> Path:
    """Détermine le dossier de destination (argument 2 ou photos-tapis/ à côté du dossier source)."""
    if len(sys.argv) > 2:
        destination = Path(sys.argv[2]).expanduser()
    else:
        defaut = source.parent / DESTINATION_DEFAUT
        reponse = input(f"Dossier de destination [{defaut}] : ").strip()
        destination = Path(reponse).expanduser() if reponse else defaut
    destination.mkdir(parents=True, exist_ok=True)
    return destination.resolve()


def lister_photos(source: Path) -> list[Path]:
    """Liste triée (donc stable entre deux lancements) des images du dossier source."""
    photos = [
        f for f in sorted(source.iterdir(), key=lambda p: p.name.lower())
        if f.is_file() and f.suffix.lower() in EXTENSIONS_IMAGES and not f.name.startswith(".")
    ]
    return photos


def charger_progression(source: Path) -> dict:
    """Charge le fichier de progression ; structure : {nom_fichier: destination ou "passee"}."""
    fichier = source / FICHIER_PROGRESSION
    if fichier.exists():
        try:
            return json.loads(fichier.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("⚠️  Fichier de progression illisible, on repart de zéro.")
    return {}


def sauvegarder_progression(source: Path, progression: dict) -> None:
    """Écrit la progression sur disque après chaque photo (résiste aux interruptions)."""
    fichier = source / FICHIER_PROGRESSION
    fichier.write_text(json.dumps(progression, indent=2, ensure_ascii=False), encoding="utf-8")


def ouvrir_photo(photo: Path) -> None:
    """Ouvre la photo dans l'application par défaut (Aperçu sur Mac)."""
    try:
        subprocess.run(["open", str(photo)], check=False)
    except FileNotFoundError:
        # Environnement non-Mac : on affiche simplement le chemin
        print(f"   (impossible d'ouvrir automatiquement : {photo})")


def nom_dossier_balle(reponse: str) -> str:
    """Convertit la réponse utilisateur en nom de dossier : 7 → Balle_07, sn → Balle_SN."""
    if reponse == "sn":
        return "Balle_SN"
    numero = int(reponse)  # la validation a déjà eu lieu
    return f"Balle_{numero:02d}"


def prochain_nom_photo(dossier_balle: Path, extension: str) -> Path:
    """Trouve le premier nom libre photo-01, photo-02... dans le dossier de la balle."""
    indice = 1
    while True:
        candidat = dossier_balle / f"photo-{indice:02d}{extension}"
        if not candidat.exists():
            return candidat
        indice += 1


def copier_photo(photo: Path, destination: Path, reponse: str) -> Path:
    """Copie la photo vers le dossier de la balle et renvoie le chemin créé."""
    dossier_balle = destination / nom_dossier_balle(reponse)
    dossier_balle.mkdir(parents=True, exist_ok=True)
    extension = photo.suffix.lower()
    if extension == ".jpeg":
        extension = ".jpg"
    cible = prochain_nom_photo(dossier_balle, extension)
    shutil.copy2(photo, cible)  # copy2 conserve les métadonnées (date de prise de vue...)
    return cible


def reponse_valide(reponse: str) -> bool:
    """Une réponse valide est un numéro de balle (1-999) ou 'sn'."""
    if reponse == "sn":
        return True
    return reponse.isdigit() and 1 <= int(reponse) <= 999


def trier(photos: list[Path], progression: dict, source: Path, destination: Path) -> None:
    """Boucle principale : une photo à la fois, sauvegarde après chaque action."""
    # Photos restantes = jamais vues + éventuellement celles passées si l'utilisateur le demande
    restantes = [p for p in photos if p.name not in progression]
    passees = [p for p in photos if progression.get(p.name) == "passee"]

    if passees and not restantes:
        choix = input(f"{len(passees)} photo(s) passée(s) précédemment. Les revoir ? (o/n) : ").strip().lower()
        if choix == "o":
            restantes = passees
            for p in passees:
                del progression[p.name]

    total_deja_fait = len(photos) - len(restantes)
    print(f"\n📷 {len(photos)} photo(s) trouvée(s), {total_deja_fait} déjà traitée(s), {len(restantes)} restante(s).")
    print("   Réponses : numéro de balle / sn / s = passer / r = rouvrir / q = quitter\n")

    for position, photo in enumerate(restantes, start=1):
        ouvrir_photo(photo)
        while True:
            invite = f"[{position}/{len(restantes)}] {photo.name} — Numéro de balle ? (s=passer, q=quitter) : "
            reponse = input(invite).strip().lower()

            if reponse == "q":
                sauvegarder_progression(source, progression)
                print("\n💾 Progression sauvegardée. Relancez le script pour reprendre.")
                return
            if reponse == "s":
                progression[photo.name] = "passee"
                sauvegarder_progression(source, progression)
                break
            if reponse == "r":
                ouvrir_photo(photo)
                continue
            if reponse_valide(reponse):
                cible = copier_photo(photo, destination, reponse)
                progression[photo.name] = str(cible.relative_to(destination))
                sauvegarder_progression(source, progression)
                print(f"   ✅ Copiée vers {cible.relative_to(destination.parent)}")
                break
            print("   ⚠️  Réponse non reconnue. Attendu : un numéro (ex. 12), sn, s, r ou q.")

    print("\n🎉 Tri terminé !")
    resumer(progression, destination)


def resumer(progression: dict, destination: Path) -> None:
    """Petit bilan de fin : nombre de balles, de photos copiées, de photos passées."""
    copiees = [v for v in progression.values() if v != "passee"]
    passees = [v for v in progression.values() if v == "passee"]
    balles = {Path(v).parts[0] for v in copiees}
    print(f"   Photos copiées : {len(copiees)}")
    print(f"   Balles distinctes : {len(balles)}")
    print(f"   Photos passées : {len(passees)}")
    print(f"   Destination : {destination}")


def main() -> None:
    print("═" * 60)
    print("  Tri des photos de tapis — Maison DIYA")
    print("  (les originaux ne sont jamais modifiés)")
    print("═" * 60)

    source = demander_dossier_source()
    destination = demander_dossier_destination(source)
    photos = lister_photos(source)

    if not photos:
        print(f"❌ Aucune image trouvée dans {source}")
        print(f"   Extensions reconnues : {', '.join(sorted(EXTENSIONS_IMAGES))}")
        sys.exit(1)

    progression = charger_progression(source)
    trier(photos, progression, source, destination)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C : la progression est déjà sauvegardée après chaque photo
        print("\n\n💾 Interruption — la progression est sauvegardée. Relancez pour reprendre.")
