# Housses Abaya

Le rangement pensé pour la garde-robe du Golfe. « Housses Abaya » est un nom de travail : il sera remplacé par le nom de marque une fois celui-ci choisi et vérifié.

Ce système sert à la boutique Shopify (thème Horizon, copie non publiée), aux visuels Canva et aux publicités TikTok, Snapchat et Instagram. Marchés : Émirats arabes unis, puis Arabie saoudite. Langues : anglais et arabe (de droite à gauche).

## Principes

1. **Le soin avant le luxe affiché.** On montre une abaya bien rangée, pas des dorures. L'or patiné reste un détail.
2. **Calme.** Grands blancs, angles droits, une seule ombre, animations lentes (300 à 600 ms, jamais de rebond).
3. **Fidèle au produit.** Housse blanche opaque, bordures noires, deux poignées, soufflet, zip. Pas de fenêtre transparente. On ne promet que ce qui est vérifié (jamais « imperméable » ou « anti-mites »).
4. **Bilingue dès le départ.** Chaque écran existe en anglais et en arabe, en miroir. L'arabe n'est pas une traduction de dernière minute.

## Ton et écriture

- **Anglais :** phrases courtes, chaleureuses, au « you ». « Your abayas, kept *beautifully*. » Pas de superlatifs (« best », « ultimate »), pas de points d'exclamation en série.
- **Arabe :** au féminin (« اختاري », « أضيفي »), arabe standard moderne clair. À faire relire par une locutrice native avant publication.
- **Prix :** toujours en AED (puis SAR), TVA comprise, avec la mention « VAT included » ou « شامل ضريبة القيمة المضافة ».
- **Délais :** les vrais délais mesurés, en jours, jamais « fast shipping » seul.
- **Avis :** seulement de vrais avis clients. Aucun avis inventé, même pour une maquette.

## Couleurs

Ivoire et sable pour le fond, noir doux pour le texte et les actions, or patiné en touche.

| Rôle | Token | Règle |
|---|---|---|
| Fond de page | `ivory-50` | Fond par défaut. |
| Bande alternée | `sand-100` | Une section sur deux, pour rythmer sans traits. |
| Remplissage | `sand-200` | Emplacements d'images, cartes discrètes. |
| Texte et action | `ink-900` | Texte principal, bouton principal, bloc de clôture. |
| Texte secondaire | `ink-700`, `ink-500` | Descriptions, puis mentions. |
| Or patiné | `gold-700` (texte), `gold-400` (décor) | Un surtitre ou un filet par écran, pas plus. |
| États | `success`, `error` | Toujours avec un texte, jamais la couleur seule. |

Contrastes vérifiés : tout le texte `ink-*` dépasse 4,5:1 sur `ivory-50`, `sand-100` et `sand-200`. `gold-400` ne sert jamais de texte sur fond clair (2,6:1). `border-strong` atteint 3:1 sur `ivory-50` et `sand-100`, pas sur `sand-200`.

## Typographie

- **Titres anglais :** Cormorant Garamond, poids 500. Signature : **un mot en italique** par titre (« kept *beautifully* », « Choose your *set* »).
- **Texte anglais :** Jost, 16px minimum sur mobile.
- **Titres arabes :** Noto Naskh Arabic, poids 600. Pas d'italique : on met le mot clé en `gold-700` à la place.
- **Texte arabe :** IBM Plex Sans Arabic, interlignage large (28px pour 16px).
- Toutes les polices viennent de Google Fonts (pas de fichier à héberger).

## Mise en page

- Conçu d'abord pour mobile (390px), puis ordinateur (1280px, contenu limité à 1200px).
- Gouttière : `space-4` sur mobile, `space-12` sur ordinateur. Sections : `space-8` en haut et en bas sur mobile, `space-16` sur ordinateur.
- Angles : `radius-none` pour les images et cartes, `radius-sm` pour les boutons et champs, `radius-pill` seulement pour les puces de promesse.
- Zones tactiles d'au moins 44px. Boutons d'au moins 48px de haut.
- **Arabe (RTL) :** `dir="rtl"` sur la page, tout est en miroir (flèches, icône camion, ordre des colonnes). Les logos de paiement et les numéros restent de gauche à droite.

## Images

- Pas de visage : des mains, des tissus, des dressings.
- Lumière naturelle chaude, fonds ivoire ou sable.
- Photos générées par IA : toujours partir de la photo fournisseur et vérifier qu'elle reste fidèle au produit réel (voir CLAUDE.md, section 8). Le texte et le logo sont ajoutés ensuite dans Canva, jamais par l'IA.
- Formats : 1:1 (fiche produit), 4:5 (Instagram), 9:16 (TikTok, Snapchat, stories).

## Icônes

Traits fins (1,6px), sans remplissage, couleur `ink-900`. Pas d'emoji. Jeu de départ : menu, panier, retour, camion (livraison), WhatsApp, cadenas (paiement sécurisé), flèche de retour (retours).

## Composants

- **Button** : actions principales et secondaires.
- **OfferSelector** : choix 1 housse / lot de 3 / kit, avec le lot présélectionné.
- **Badge** : « Most popular », « New ».
- **DeliveryNote** : délai réel et seuil de livraison offerte.
- **Accordion** : détails produit et FAQ.
- **StickyBuyBar** : barre d'achat collante sur la fiche produit mobile.

Ce sont des modèles HTML et CSS à reproduire dans les sections du thème Horizon, pas une bibliothèque de code.
