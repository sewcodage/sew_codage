# Phase 6 — Contenus et SEO EN/AR

Avancement au 29/10/2026. Tout reste invisible pour les clientes : l'arabe n'est pas publié, et les pages et l'article sont en brouillon.

## Fait dans Shopify

| Élément | Anglais | Arabe |
|---|---|---|
| Fiche produit | Titre, description, SEO déjà faits. Adresse raccourcie : `/products/long-abaya-garment-bag-180-cm` (redirection automatique depuis l'ancienne). | Titre, description, type, SEO enregistrés en traduction. |
| Collection « Garment Bags » | Description + SEO title/meta ajoutés. | Titre « أكياس حفظ العبايات », description, SEO. |
| Page Help (brouillon) | Contenu avec crochets. | Traduction enregistrée. |
| Page Our story (brouillon) | Contenu avec crochets. | Traduction enregistrée. |
| Blog | « Actualités » renommé « Journal » (`/blogs/journal`). | À traduire quand l'article sera validé. |
| Article de fond (brouillon) | « How to store abayas so they stay beautiful » : 7 conseils généraux + lien vers la fiche produit. | À faire. |
| Thème (copie non publiée) | — | `snippets/arabic-fonts.liquid` : charge Noto Naskh Arabic et IBM Plex Sans Arabic sur les pages arabes, supprime l'italique, élargit l'interlignage. Le sens de lecture (RTL) est déjà géré par Horizon. |

**Toutes les traductions arabes sont à faire relire par une locutrice native** avant de publier l'arabe (application Translate & Adapt, ou Paramètres → Langues).

## Plan de mots-clés (volumes à vérifier dans Google Keyword Planner, Émirats et Arabie saoudite)

| Intention | Anglais | Arabe | Page cible |
|---|---|---|---|
| Produit | abaya garment bag, abaya cover, long garment bag | كيس حفظ العبايات، غطاء عباية، أكياس حفظ الملابس | Fiche produit |
| Catégorie | abaya storage, garment bags | تخزين العبايات، أكياس حفظ | Collection Garment Bags |
| Organisation | closet organizer, wardrobe organizer | منظم خزانة، ترتيب الخزانة | Future collection Closet Organizers |
| Conseil | how to store abayas, how to keep abayas from creasing | طريقة حفظ العبايات، كيف أرتب عباياتي | Article « How to store abayas » |
| Cadeau | bridal trousseau gift, eid gift for her | جهاز العروس، هدية العيد | Futures pages Trousseau, Ramadan et Aïd |
| Gamme | abaya hanger, velvet hangers, scarf organizer | علاقة عبايات، منظم طرح | Futurs produits |

## Articles de fond suivants (calendrier proposé)

1. **How to store abayas so they stay beautiful** : rédigé (brouillon). Mot-clé : « how to store abayas ».
2. **Packing abayas for travel without creases** : mi-novembre 2026. Met en avant les deux poignées.
3. **Preparing your wardrobe before Ramadan** : début janvier 2027, avant la fenêtre du Ramadan (vers le 8 février).
4. **The bridal trousseau checklist (jihaz)** : décembre 2026, pendant la saison des mariages.
5. **Caring for embroidered and beaded abayas** : février 2027.

Chaque article : 600 à 1 000 mots, un lien vers la fiche produit ou la collection, une version arabe rédigée pour le marché arabe (pas une traduction mot à mot).

## Technique SEO

- **hreflang :** Shopify l'ajoute automatiquement quand l'anglais et l'arabe sont publiés sur le marché Émirats. Rien à coder.
- **Données structurées :** Horizon génère le balisage Product. À ajouter en phase 7 : FAQPage sur la page Help, Organization (nom de marque, logo, WhatsApp), BreadcrumbList si absent.
- **Textes alternatifs :** faits en anglais, génériques. À affiner image par image (voir CLAUDE.md, section 5) et à traduire en arabe.
- **Images :** Shopify sert déjà du WebP et charge les images en différé. Garder les photos sous 300 Ko avant import.
- **Langue principale :** passer l'anglais en langue principale (Paramètres → Langues) pour que l'adresse principale de la boutique soit en anglais et non en français.

## Reste à faire

- Relecture native de tout l'arabe.
- Traduire en arabe l'article et les textes alternatifs.
- SEO title/meta des pages Help et Our story (après validation des textes).
- Textes des pages Ramadan & Eid et Trousseau, quand le kit existera.
- Compléter les crochets (délais, prix, numéro WhatsApp, nom de marque).
