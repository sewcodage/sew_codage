# OfferSelector

Sélecteur d'offre de la fiche produit : 1 housse, lot de 3 (présélectionné) ou kit dressing.

- Ce sont de vrais boutons radio (`<input type="radio">` dans un `<label>`) : utilisable au clavier et lu par les lecteurs d'écran.
- Option sélectionnée : bordure 2px `ink-900`. Les autres : 1px `border-strong`, fond `white`.
- Le lot de 3 est coché par défaut et porte le Badge « Most popular ».
- Chaque option affiche son prix total et, pour les lots, le prix par housse en `ink-700`.
- Dans Shopify : une option de produit « Set » avec 3 variantes (1 bag / Set of 3 / Wardrobe kit), ou des produits séparés reliés par une application de lots. À décider en phase 5.
- Les prix restent entre crochets tant que le coût fournisseur n'est pas fixé.
