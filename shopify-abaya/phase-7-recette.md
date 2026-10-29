# Phase 7 — Recette

Recette du 29/10/2026 sur la copie non publiée « Horizon – Housses Abaya (brouillon) » et sur les données de la boutique.

**Limite :** l'aperçu de la boutique n'est pas accessible depuis l'environnement de Claude Code (réseau bloqué, boutique protégée par mot de passe en essai). La recette porte donc sur les fichiers du thème et les données Shopify. Le rendu à l'écran, la vitesse et l'arabe doivent être vérifiés par Kishan avec la grille de test manuel en bas de page.

## Ce qui est bon

| Point | Résultat |
|---|---|
| Thème en ligne | Inchangé. Toutes les modifications sont sur la copie non publiée. |
| Contrastes | Texte principal 15:1, secondaire 8,7:1, discret 6,4:1 sur le fond ivoire ; bordures de champs 3,6:1. Conforme AA. |
| Sens de lecture arabe | Géré par le layout Horizon (`dir` selon la langue) ; fichier de traduction de l'interface `locales/ar.json` présent dans le thème. |
| Polices arabes | Chargées seulement sur les pages arabes (`snippets/arabic-fonts.liquid`). |
| Données structurées | Product (fiche produit) et Article (blog) déjà générés par Horizon. Ajouté : Organization sur l'accueil. FAQPage prêt mais désactivé (réponses encore entre crochets). |
| Barre d'achat collante | Activée ; pleine largeur sur mobile, au-dessus de la barre de l'iPhone. |
| SEO | Titre et description Google sur le produit et la collection, en anglais et en arabe. Adresse produit lisible. |
| Textes alternatifs | Présents sur les 11 images (génériques). |

## À corriger

| # | Problème | Gravité | Qui |
|---|---|---|---|
| 1 | **Accueil = modèle Horizon par défaut** (« Browse our latest products », « Shop all ») : rien des wireframes n'est encore monté. | Bloquant | Claude, après validation |
| 2 | **Prix et offre** : 25,99 € (règle du ×3 non respectée), une seule variante, pas de sélecteur 1 / lot de 3 / kit. | Bloquant | Kishan (coûts), puis Claude |
| 3 | **Forfait Shopify en essai** : impossible de vendre. | Bloquant | Kishan |
| 4 | **Politiques absentes** (retours, livraison, CGV, mentions légales). Les plateformes pub les vérifient. | Bloquant | Kishan (infos légales), puis Claude |
| 5 | **Menus** (partagés avec le thème en ligne) : libellés en français, un lien « Home page » qui pointe vers la collection, pied de page réduit à « Rechercher ». À refaire au moment de publier, sinon les liens vers les pages en brouillon seraient cassés sur la boutique actuelle. | Élevée | Claude, au lancement |
| 6 | **Titres de fiche produit et de pages en police de texte** (Jost) au lieu de Cormorant : réglage « Font » des blocs titre sur « Body ». | Moyenne | Claude (2 réglages) |
| 7 | **Bloc « Disclosures » vide** sur la fiche produit : à remplacer par Details / What's in the box / Delivery & returns. | Moyenne | Claude |
| 8 | **Pas de bloc délai de livraison** au-dessus du bouton d'achat (prévu dans les wireframes). | Moyenne | Claude, quand le délai sera mesuré |
| 9 | **Langue principale = français**, marché Émirats en brouillon, anglais et arabe non publiés. | Élevée | Kishan (forfait + réglage langue) |
| 10 | **Pas de nom de marque ni de logo** (« Ma boutique », fournisseur « Ma boutique »). | Élevée | Kishan |
| 11 | **Arabe non relu** par une locutrice native. | Élevée | Kishan |
| 12 | Paiements (Tabby/Tamara, paiement à la livraison), zone de livraison Émirats et seuil gratuit : non configurés. | Élevée | Kishan (comptes), puis Claude |
| 13 | Pixels Meta, TikTok, Snapchat : non installés. | Moyenne, avant la pub | Kishan (comptes) |
| 14 | Photos : textes alternatifs génériques, vidéo « abaya entière dans la housse » à tourner avec l'échantillon. | Moyenne | Kishan |

## Grille de test manuel (Kishan, sur téléphone puis ordinateur)

Aperçu : admin → Boutique en ligne → Thèmes → « Horizon – Housses Abaya (brouillon) » → Aperçu.

1. Fond ivoire, texte noir doux, titres en serif (Cormorant), texte en Jost : OK ?
2. Fiche produit : photos, prix, bouton, barre collante en faisant défiler : OK ?
3. Panier : ajout, modification de quantité, passage au paiement : OK ?
4. Pages Help et Our story (via leur adresse `/pages/help`, `/pages/our-story`) : lisibles ?
5. Quand l'arabe sera publié : `/ar` → page à l'endroit (de droite à gauche), polices arabes, pas d'italique.
6. Vitesse : passer la fiche produit dans PageSpeed Insights (mobile). Objectif LCP < 2,5 s, CLS < 0,1.
7. Données structurées : tester la fiche produit dans le test des résultats enrichis de Google.

## Avant de publier (liste de contrôle)

- [ ] Forfait choisi
- [ ] Prix et variantes conformes à la règle du ×3
- [ ] Nom de marque, logo, fournisseur renommé
- [ ] Politiques en ligne (retours, livraison, CGV, mentions légales)
- [ ] Accueil et fiche produit montés selon les wireframes
- [ ] Menus refaits (Shop, Our story, Help + EN/AR)
- [ ] Anglais en langue principale ; marché Émirats activé ; arabe relu puis publié
- [ ] Pages Help et Our story complétées puis publiées ; FAQPage activé (`faq_ready`)
- [ ] Paiements et livraison configurés ; commande test réalisée
- [ ] Pixels installés
- [ ] Grille de test manuel passée
- [ ] **Publication du thème par Kishan**
