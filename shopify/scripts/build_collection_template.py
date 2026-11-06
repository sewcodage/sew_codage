"""Génère shopify/templates/collection.json : grille produits + description + storytelling de marque.

Tous les textes utilisent les blocs natifs du thème Helio : ils sont modifiables dans l'éditeur.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "templates/collection.json"
SERIF = "var(--font-primary--family)"
BODY = "var(--font-body--family)"


def text(html, name, preset="paragraph", align="left", maxw="normal", size="", font=BODY, case="none", ls="normal"):
    return {"type": "text", "name": name, "settings": {
        "text": html, "width": "100%", "max_width": maxw, "alignment": align, "type_preset": preset,
        "font": font, "font_size": size, "line_height": "normal", "letter_spacing": ls, "case": case,
        "wrap": "pretty"}, "blocks": {}}


def eyebrow(label, align="left"):
    return text(f"<p>{label}</p>", "Sur-titre", "custom", align, size="0.75rem", case="uppercase", ls="loose")


def group(blocks, order, name, direction="column", gap=16, align="flex-start", **extra):
    s = {"content_direction": direction, "vertical_on_mobile": True, "gap": gap,
         "horizontal_alignment": align, "horizontal_alignment_flex_direction_column": align,
         "vertical_alignment": "center", "vertical_alignment_flex_direction_column": "center",
         "width": "fill", "height": "fit"}
    s.update(extra)
    return {"type": "group", "name": name, "settings": s, "blocks": blocks, "block_order": order}


def section(name, blocks, order, bg, top, bottom, direction="column", align="center", gap=24):
    return {"type": "section", "name": name, "blocks": blocks, "block_order": order, "settings": {
        "content_direction": direction, "vertical_on_mobile": True, "gap": gap,
        "horizontal_alignment": align, "horizontal_alignment_flex_direction_column": align,
        "vertical_alignment": "center", "vertical_alignment_flex_direction_column": "center",
        "section_width": "page-width", "background_color": bg,
        "padding-block-start": top, "padding-block-end": bottom}}


STORY_P1 = ("<p>Tout a commencé par une conviction simple : un beau bijou ne devrait pas être réservé aux grandes "
            "occasions. Il devrait se porter tous les jours, accompagner les petits moments comme les grands, "
            "et devenir peu à peu une part de soi.</p>")
STORY_P2 = ("<p>Nous avons choisi le trèfle, symbole universel de chance, et l’avons décliné en sept couleurs "
            "pour que chacune et chacun trouve celui qui lui ressemble. Des pièces légères et lumineuses, "
            "pensées pour être portées seules ou accumulées.</p>")
STORY_P3 = ("<p>Chaque bijou est sélectionné avec soin, présenté avec simplicité et expédié avec un numéro de suivi. "
            "Notre promesse : vous offrir l’élégance au quotidien, à un prix juste.</p>")

values = [
    ("L’élégance au quotidien", "Des bijoux délicats, faciles à porter, qui subliment chaque tenue."),
    ("Le soin du détail", "Trèfles ciselés, finitions dorées, chaînes fines : chaque détail compte."),
    ("Le plaisir d’offrir", "Une attention qui fait toujours mouche, pour soi ou pour ceux qu’on aime."),
]

tpl = {
    "sections": {
        "section": section("En-tête de collection", {
            "title": text("<h1>{{ closest.collection.title }}</h1>", "Titre", "h2", "center", font=SERIF)},
            ["title"], "#FFFFFF", 56, 32),
        "main": {"type": "main-collection", "blocks": {
            "filters": {"type": "filters", "static": True, "settings": {
                "enable_filtering": True, "filter_style": "horizontal", "filter_width": "centered",
                "enable_sorting": True, "enable_grid_density": True,
                "padding-block-start": 8, "padding-block-end": 8}, "blocks": {}},
            "product-card": {"type": "_product-card", "static": True, "settings": {"product_card_gap": 4}, "blocks": {
                "card-gallery": {"type": "_product-card-gallery", "settings": {"image_ratio": "square", "border_radius": 0}, "blocks": {}},
                "title": {"type": "product-title", "name": "t:names.product_title", "settings": {
                    "type_preset": "rte", "font": BODY, "font_size": "1rem", "padding-block-start": 8}, "blocks": {}},
                "price": {"type": "price", "settings": {"show_sale_price_first": True, "type_preset": "h6",
                          "font": BODY, "font_size": "1rem"}, "blocks": {}}},
                "block_order": ["card-gallery", "title", "price"]}},
            "settings": {"layout_type": "grid", "product_card_size": "large", "mobile_product_card_size": "large",
                         "enable_infinite_scroll": True, "products_per_page": 24, "product_grid_width": "centered",
                         "columns_gap_horizontal": 16, "columns_gap_vertical": 32, "background_color": "#FFFFFF",
                         "padding-block-start": 0, "padding-block-end": 96}},
        "description": section("Description de la collection", {
            "eyebrow": eyebrow("À propos de la collection", "center"),
            "title": text("<h2>{{ closest.collection.title }}</h2>", "Titre", "h3", "center", font=SERIF),
            "desc": text("{{ closest.collection.description }}", "Description (modifiable dans Produits › Collections)",
                         "rte", "center", "narrow")},
            ["eyebrow", "title", "desc"], "#FFFFFF", 16, 88, gap=16),
        "histoire": section("Notre histoire", {
            "image": {"type": "image", "name": "Photo", "settings": {
                "image": "shopify://shop_images/bracelet-trefle-toutes-couleurs.jpg", "image_ratio": "portrait",
                "width": "fill", "border_radius": 0}, "blocks": {}},
            "texte": group({
                "eyebrow": eyebrow("Notre histoire"),
                "title": text("<h2>Des bijoux pensés comme des porte-bonheur</h2>", "Titre", "h2", font=SERIF),
                "p1": text(STORY_P1, "Paragraphe 1", maxw="narrow"),
                "p2": text(STORY_P2, "Paragraphe 2", maxw="narrow"),
                "p3": text(STORY_P3, "Paragraphe 3", maxw="narrow"),
                "cta": {"type": "button", "name": "Bouton", "settings": {
                    "label": "Découvrir tous nos bijoux", "link": "shopify://collections/all",
                    "style_class": "button-secondary"}, "blocks": {}}},
                ["eyebrow", "title", "p1", "p2", "p3", "cta"], "Texte", gap=18,
                **{"padding-inline-start": 24, "padding-inline-end": 24})},
            ["image", "texte"], "#F7F5F2", 96, 96, direction="row", align="flex-start", gap=48),
        "valeurs": section("Nos valeurs", {
            "row": group({f"v{i}": group({
                "h": text(f"<h3>{h}</h3>", "Titre", "h4", "center", font=SERIF),
                "p": text(f"<p>{p}</p>", "Texte", "paragraph", "center", "narrow")}, ["h", "p"],
                f"Valeur {i + 1}", gap=10, align="center") for i, (h, p) in enumerate(values)},
                [f"v{i}" for i in range(len(values))], "Valeurs", direction="row", gap=48, align="center")},
            ["row"], "#FFFFFF", 80, 80),
    },
    "order": ["section", "main", "description", "histoire", "valeurs"],
}

OUT.write_text(json.dumps(tpl, ensure_ascii=False, indent=2))
print(OUT, OUT.stat().st_size)
