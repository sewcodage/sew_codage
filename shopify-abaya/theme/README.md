# Fichiers modifiés dans la copie du thème

Thème : « Horizon – Housses Abaya (brouillon) » (non publié, id 209229611340). Seuls les fichiers modifiés sont copiés ici.

- `config/settings_data.json` (bloc `current`) : couleurs, polices, angles du design system (phase 5).
- `snippets/arabic-fonts.liquid` : nouveau, polices et typographie arabes (phase 6).
- `snippets/card-hover-effect-styles.liquid` : une ligne ajoutée à la fin, `{% render 'arabic-fonts' %}`. Ce snippet est rendu dans `<head>` par `layout/theme.liquid`, ce qui évite de modifier le layout.
