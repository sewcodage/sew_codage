# Phase 5 — Mise en place Shopify

Avancement au 29/10/2026. Rien n'est publié ni visible par les clientes.

## Fait

| Élément | État | Détail |
|---|---|---|
| Copie du thème | « Horizon – Housses Abaya (brouillon) », **non publiée** | Couleurs du design system (fond ivoire `#f7f3ec`, texte `#1f1c18`, secondaire `#4a443b`, filets `#ddd3c3`, bordures de champs `#8a7f70`), titres en Cormorant 500 (italique en accent), texte en Jost 16px, angles 0–2px, badges en capitales. Le thème en ligne n'a pas bougé. |
| Marché Émirats | « United Arab Emirates », **brouillon** | Devise AED, prix TTC (TVA incluse). |
| Langues | Anglais et arabe ajoutés, **non publiés** | Le français reste la langue principale pour l'instant. |
| Pages | « Help » et « Our story », **non publiées** | Contenu de la page Aide (FAQ, livraison, retours, contact) avec des crochets à remplir. |
| Politiques | Brouillons dans `politiques-brouillon.md` | Pas encore dans Shopify, car Shopify les publie à l'enregistrement. |

## Différence avec le design system

- La bibliothèque de polices Shopify propose **Cormorant**, pas Cormorant Garamond. Le dessin est très proche : on garde Cormorant.
- Les polices Shopify ne couvrent pas l'arabe. Les polices arabes (Noto Naskh Arabic, IBM Plex Sans Arabic) seront chargées par une feuille de style dédiée quand l'arabe sera activé (phase 6).

## Bloqué (décisions de Kishan)

1. **Forfait Shopify** : obligatoire pour vendre, activer le marché et publier les langues.
2. **Coût fournisseur et livraison** : pour créer les variantes 1 housse / lot de 3 / kit avec de vrais prix.
3. **Nom de marque** : pour renommer la boutique et le fournisseur (« Ma boutique »).
4. **Langue principale** : passer l'anglais en langue principale (dans l'admin : Paramètres → Langues), puisque la France n'est pas la cible.
5. **Collection vide « collection privé couvrement »** : la supprimer ou la renommer « Closet Organizers ».
6. **Informations légales** pour les politiques : forme juridique, SIRET, adresse, e-mail, WhatsApp.

## Reste à faire une fois débloqué

- Créer les variantes et leurs prix ; passer le lot de 3 en variante par défaut.
- Composer l'accueil et la fiche produit dans la copie du thème selon les wireframes (sections Horizon).
- Menus (Shop, Our story, Help + EN/AR) et pied de page.
- Paiements (Tabby/Tamara si disponibles aux Émirats, paiement à la livraison), livraison (zone Émirats, tarif et seuil gratuit).
- Activer le marché Émirats, publier l'anglais puis l'arabe.
- Pixels Meta, TikTok et Snapchat.
- Publication du thème : **par Kishan uniquement**, après la recette (phase 7).
