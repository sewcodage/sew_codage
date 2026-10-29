# StickyBuyBar

Barre d'achat collée en bas de l'écran mobile sur la fiche produit : rappelle l'offre choisie, son prix et le bouton d'ajout au panier.

- Apparaît quand le bouton principal sort de l'écran, disparaît quand il revient (pas de doublon visible).
- Fond `ivory-50`, filet haut `border-strong`, ombre `shadow-sticky` (la seule du système).
- Ajoute `env(safe-area-inset-bottom)` à sa marge basse pour ne pas passer sous la barre de l'iPhone.
- Suit l'offre cochée dans OfferSelector (« Set of 3 · [PRICE] AED »).
- Ordinateur : pas de barre collante, le bloc d'achat reste visible dans la colonne de droite.
