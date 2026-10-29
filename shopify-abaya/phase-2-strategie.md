# Phase 2 — Stratégie

Projet : marque de housses pour abayas (Shopify, Émirats puis Arabie saoudite).
Version 1 du 29/10/2026, à valider par Kishan avant la phase 3 (wireframes).

Toutes les personas, tous les chiffres de marché et tous les taux cibles ci-dessous sont des **hypothèses de départ**. Le test publicitaire servira à les confirmer ou à les corriger.

---

## 1. Objectif de la phase de test

| Indicateur | Cible de départ | Pourquoi |
|---|---|---|
| Budget test | 300 à 500 € | Fixé dans la feuille de route. |
| Coût d'acquisition (CPA) | Inférieur à la marge avant pub de l'offre vendue | Au-delà, chaque vente fait perdre de l'argent (voir CLAUDE.md, section 4). |
| Panier moyen | Plus de 60 % des commandes en lot de 3 ou en kit | Le produit seul ne laisse pas assez de marge pour payer la pub. |
| Taux de conversion fiche produit | 1,5 à 3 % (ordre de grandeur DTC mobile) | Sert à repérer tôt si c'est la page ou la pub qui bloque. |
| Signal de continuation | Au moins 10 ventes et un ROAS supérieur au point mort | En dessous, on corrige l'offre ou les visuels avant de remettre du budget. |

**Prérequis bloquant :** un coût d'achat compatible avec la règle du ×3 (voir CLAUDE.md, section 4). Tant que le fournisseur est à 12,99 € la housse, aucune pub ne peut être rentable.

---

## 2. Personas (hypothèses)

### A. Mariam, 27 ans, Dubaï, active
- **Situation :** salariée, appartement avec dressing limité. Elle possède 15 à 30 abayas, dont quelques pièces brodées chères.
- **Problème :** ses abayas de soirée se froissent et prennent la poussière. Les housses de pressing sont trop courtes.
- **Canaux :** Instagram et TikTok tous les jours. Elle achète sur mobile avec Apple Pay ou Tabby.
- **Ce qui la convainc :** une vidéo qui montre que l'abaya tient entièrement dans la housse, et un rendu dressing « propre » qui fait envie.
- **Offre visée :** lot de 3.

### B. Noura, 38 ans, Abu Dhabi ou Charjah, mère de famille
- **Situation :** grande maison. Elle gère la garde-robe de la famille, avec des achats massifs avant le Ramadan et l'Aïd.
- **Problème :** l'organisation, les voyages en famille, ranger les tenues d'occasion entre deux saisons.
- **Canaux :** Snapchat et Instagram. Elle commande volontiers par WhatsApp et paie à la livraison.
- **Ce qui la convainc :** le lot (rapport quantité/prix), le côté pratique (les deux poignées pour le voyage) et des délais clairs.
- **Offre visée :** kit dressing ou plusieurs lots.

### C. L'acheteuse cadeau (sœur, mère ou amie d'une future mariée)
- **Situation :** elle prépare le trousseau (« jihaz ») ou un cadeau d'Aïd.
- **Problème :** trouver un cadeau utile et joliment présenté.
- **Canaux :** Instagram (recherche, inspiration) et TikTok.
- **Ce qui la convainc :** le coffret, la présentation et la date de livraison garantie avant l'événement.
- **Offre visée :** kit, puis le futur coffret trousseau.

**Pourquoi ces trois profils :** ils couvrent les trois moments d'achat du produit (besoin personnel, organisation familiale, cadeau) et correspondent aux trois offres prévues (lot, kit, coffret).

---

## 3. Proposition de valeur et messages

**Promesse centrale :** « Le rangement pensé pour la garde-robe du Golfe ». Une housse assez longue pour une abaya entière, respirante, élégante.

| Message | Preuve (caractéristique réelle) | Persona |
|---|---|---|
| Votre abaya tient en entier, sans pli en bas. | Environ 180 cm, à vérifier sur échantillon. | A, B |
| Protégée de la poussière, sans enfermer l'humidité. | Non tissé respirant. | A, B |
| De la place pour les coupes amples et brodées. | Soufflet latéral qui s'élargit vers le bas. | A |
| Prête pour le voyage et les visites familiales. | Deux poignées. | B |
| Un dressing net et harmonieux. | Blanc, bordures noires, lot de 3. | A, C |

**À ne jamais promettre** (non vérifié) : imperméable, anti-mites, anti-UV, « qualité premium » sans échantillon reçu.

### Objections et réponses

| Objection | Réponse |
|---|---|
| « C'est juste une housse, pourquoi ce prix ? » | Vendre surtout le lot et le kit (prix par housse plus bas) et montrer le résultat dans un dressing. |
| « Ça arrive quand ? » | Délai réel affiché sur la fiche produit et au paiement. En dropshipping depuis la Chine, c'est souvent 10 à 20 jours (à mesurer avec les échantillons). Ne pas cacher ce délai : c'est la première cause de litiges. |
| « Et si ça ne me plaît pas ? » | Politique de retour claire et lien WhatsApp visible. |
| « Est-ce que mon abaya tient dedans ? » | Dimensions précises plus une vidéo de l'abaya mise dans la housse (à tourner avec l'échantillon). |

---

## 4. Structure de l'offre

| Offre | Rôle | Statut |
|---|---|---|
| 1 housse | Prix d'entrée, ancrage | Existe. Prix à revoir. |
| **Lot de 3** | **Offre principale** (option par défaut sur la fiche produit) | À créer quand le coût sera connu. |
| Kit dressing (3 housses + 6 cintres + 1 sachet) | Panier le plus élevé, cadeau | À sourcer (cintres, sachet). |

- **Pourquoi le lot par défaut :** une abaya va rarement seule, et le lot fait monter le panier moyen sans dépense publicitaire supplémentaire.
- **Livraison offerte :** à partir d'un seuil placé juste au-dessus du prix du lot, pour pousser vers le kit. Le montant sera fixé quand les prix seront recalculés.

---

## 5. Arborescence du site

### Version de lancement (1 produit, trafic venant surtout des pubs)
```
Accueil
├── Boutique → fiche produit (sélecteur : 1 / lot de 3 / kit)
├── Notre histoire
├── Aide
│   ├── FAQ
│   ├── Livraison
│   ├── Retours et remboursements
│   └── Contact (WhatsApp + formulaire)
└── [EN | AR]
Pied de page : CGV, confidentialité, mentions légales, livraison, retours
```
**Pourquoi si peu de pages :** avec un seul produit, des catégories vides ou des menus profonds font « boutique vide ». La navigation reste à 4 entrées plus la bascule de langue, comme prévu dans le brief.

### Version cible (quand la gamme existera)
```
Accueil
├── Boutique
│   ├── Housses (Garment Bags)
│   ├── Cintres et organiseurs (Closet Organizers)
│   └── Coffrets et cadeaux
├── Occasions
│   ├── Ramadan et Aïd
│   └── Trousseau de mariée
├── Journal (articles SEO)
├── Aide
└── [EN | AR]
```
Collections Shopify correspondantes : « Garment Bags » existe déjà. La collection vide « collection privé couvrement » pourrait devenir « Closet Organizers ».

---

## 6. Parcours par canal

**Principe :** les pubs envoient directement vers la **fiche produit**, pas vers l'accueil. Chaque clic en plus fait perdre des clientes sur mobile.

| Canal | Rôle | Format | Destination | Point clé |
|---|---|---|---|---|
| **TikTok** | Découverte, volume | Vidéo UGC verticale : abaya froissée → mise dans la housse → dressing rangé | Fiche produit, lot de 3 présélectionné | Les 2 premières secondes montrent le problème. Pas de texte IA en arabe. |
| **Snapchat** | Fort aux Émirats, très fort en Arabie saoudite | Vidéo courte plein écran, offre visible | Fiche produit | Canal prioritaire pour la future ouverture saoudienne. |
| **Instagram** | Crédibilité, cadeau, reciblage | Reels plus carrousel avant/après, stories | Fiche produit, ou page coffret pour le persona C | Le profil sert de vitrine : 9 premiers posts soignés avant de lancer la pub. |
| **WhatsApp** | Conversion et rassurance | Bouton sur la fiche produit, confirmation des commandes payées à la livraison | Conversation | Réduit les refus à la livraison (surtout en Arabie saoudite). |

### Parcours type (mobile)
1. Vidéo TikTok ou Snapchat.
2. Fiche produit : visuel « abaya entière dans la housse », lot de 3 présélectionné, délai affiché, bouton d'achat collant.
3. Paiement : Apple Pay, carte, Tabby ou Tamara si disponible, paiement à la livraison en option.
4. Proposition de passer au kit après l'achat (plus 1 clic).
5. Confirmation WhatsApp, suivi du colis, puis demande d'avis avec photo à J+7 après la livraison.

**Reciblage :** les visiteuses de la fiche produit sans achat voient, sur 7 jours, une vidéo avant/après puis un rappel de l'offre lot. Pixels Meta, TikTok et Snapchat à installer en phase 5.

---

## 7. Calendrier commercial (dates à confirmer)

| Période | Événement | Usage |
|---|---|---|
| Fin novembre 2026 | White Friday (Black Friday du Golfe) | Trop tôt pour un lancement propre. Ne pas forcer. |
| 2 décembre 2026 | Fête nationale des Émirats | Possible lancement en douceur ou première prise de parole. |
| Décembre 2026 – janvier 2027 | Dubai Shopping Festival et saison des mariages (hiver) | Persona C : trousseau. |
| **Début février 2027** | **Début du Ramadan** (vers le 8 février selon le calendrier lunaire) | **Fenêtre principale.** Campagnes à lancer 3 à 4 semaines avant, soit vers mi-janvier. |
| Vers le 9 mars 2027 | Aïd al-Fitr | Cadeaux et rangement des tenues d'Aïd. |

**Conséquence :** avec des délais de 10 à 20 jours depuis la Chine, les commandes du Ramadan doivent être passées dès la mi-janvier. Il faut donc une boutique prête et testée **avant le 15 janvier 2027**. C'est l'objectif de calendrier que je propose pour les phases 3 à 7.

---

## 8. Décisions à valider par Kishan

1. Les 3 personas : on garde, on modifie, ou il en manque un ?
2. Le lot de 3 comme offre principale présélectionnée.
3. L'arborescence de lancement réduite (4 entrées) plutôt que la version cible dès maintenant.
4. La priorité des canaux : TikTok et Snapchat pour l'acquisition, Instagram pour la vitrine et le reciblage, WhatsApp pour la conversion.
5. Une boutique prête avant le 15 janvier 2027, pour le Ramadan.
6. Une condition avant toute pub : un fournisseur moins cher (2 à 4 € la housse) et les échantillons reçus.
