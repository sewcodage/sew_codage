"""Génère shopify/templates/product.json : page produit style joaillerie de luxe (thème Helio)."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "templates/product.json"

CSS = """<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&display=swap" rel="stylesheet">
<style>
.lux{--lux-ink:#1a1a1a;--lux-muted:#6f6f6f;--lux-line:#e6e6e6;--lux-gold:#9a7b4f;color:var(--lux-ink)}
.lux-eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--lux-muted);margin:0 0 14px}
.lux-title{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:clamp(26px,2.4vw,34px);line-height:1.15;letter-spacing:.06em;text-transform:uppercase;margin:0}
.lux-lead{font-size:14px;line-height:1.7;color:var(--lux-muted);margin:14px 0 0;max-width:42ch}
.lux-services{list-style:none;margin:0;padding:18px 0 0;border-top:1px solid var(--lux-line);display:grid;gap:12px}
.lux-services li{display:flex;align-items:center;gap:12px;font-size:13px;letter-spacing:.02em}
.lux-services svg{width:18px;height:18px;stroke:var(--lux-ink);fill:none;stroke-width:1.2;flex:none}
.lux-services a{color:inherit;text-underline-offset:3px}
.lux-band{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;text-align:center;padding:8px 0}
.lux-band h3{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:22px;letter-spacing:.04em;margin:14px 0 8px}
.lux-band p{font-size:13px;line-height:1.7;color:var(--lux-muted);margin:0 auto;max-width:30ch}
.lux-band svg{width:26px;height:26px;stroke:var(--lux-ink);fill:none;stroke-width:1}
.lux-edito{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:72px}
.lux-edito img{width:100%;height:auto;display:block}
.lux-edito h2{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:clamp(28px,3vw,42px);letter-spacing:.03em;margin:0 0 20px}
.lux-edito p{font-size:14px;line-height:1.9;color:var(--lux-muted);max-width:46ch;margin:0 0 14px}
.lux-edito a{display:inline-block;margin-top:12px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--lux-ink);text-decoration:none;border-bottom:1px solid var(--lux-ink);padding-bottom:4px}
.product-information .details__header{font-size:12px;letter-spacing:.16em;text-transform:uppercase}
.product-information .details-content{font-size:14px;line-height:1.8;color:#555}
.product-information .add-to-cart-button,.product-information .button-custom{border-radius:0!important;letter-spacing:.16em;text-transform:uppercase;font-size:12px;min-height:54px}
.product-information .variant-option__button-label{border-radius:0!important;font-size:12px;letter-spacing:.06em}
@media(max-width:749px){.lux-band{grid-template-columns:1fr;gap:28px}.lux-edito{grid-template-columns:1fr;gap:28px}}
</style>"""

I_TRUCK = '<svg viewBox="0 0 24 24"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/></svg>'
I_RET = '<svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 0 3-6.2"/><path d="M4 4v4h4"/></svg>'
I_LOCK = '<svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'
I_CHAT = '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>'


def liquid(code, name):
    return {"type": "custom-liquid", "name": name, "settings": {"custom_liquid": code}, "blocks": {}}


def row(heading, html, open_=False):
    return {"type": "_accordion-row", "settings": {"heading": heading, "icon": "none", "open_by_default": open_},
            "blocks": {"t": {"type": "text", "settings": {"text": html, "width": "100%"}, "blocks": {}}},
            "block_order": ["t"]}


def custom_section(name, code, top=80, bottom=80, bg="#FFFFFF"):
    return {"type": "section", "name": name, "blocks": {"c": liquid(code, name)}, "block_order": ["c"],
            "settings": {"section_width": "page-width", "background_color": bg,
                         "padding-block-start": top, "padding-block-end": bottom}}


HEADER = (CSS + '<div class="lux"><p class="lux-eyebrow">Collection Trèfle</p>'
          '<h1 class="lux-title">{{ product.title }}</h1>'
          '<p class="lux-lead">Cinq trèfles ciselés sur une fine chaîne en acier inoxydable couleur or. '
          'Un bijou porte-bonheur, léger et lumineux, à porter seul ou accumulé.</p></div>')

SERVICES = ('<div class="lux"><ul class="lux-services">'
            f'<li>{I_TRUCK}<span>Livraison avec numéro de suivi</span></li>'
            f'<li>{I_RET}<span>14 jours pour changer d’avis</span></li>'
            f'<li>{I_LOCK}<span>Paiement sécurisé</span></li>'
            f'<li>{I_CHAT}<span>Une question ? <a href="/pages/contact">Contactez-nous</a></span></li>'
            '</ul></div>')

BAND = ('<div class="lux"><div class="lux-band">'
        f'<div>{I_TRUCK}<h3>Livraison suivie</h3><p>Chaque commande est expédiée avec un numéro de suivi.</p></div>'
        f'<div>{I_RET}<h3>Retours sous 14 jours</h3><p>Vous changez d’avis ? Vous disposez de 14 jours après réception.</p></div>'
        f'<div>{I_CHAT}<h3>À votre écoute</h3><p>Une question sur un bijou ou une commande ? <a href="/pages/contact">Écrivez-nous</a>.</p></div>'
        '</div></div>')

EDITO = ('<div class="lux"><div class="lux-edito">'
         '<img src="{{ \'bracelet-trefle-porte.jpg\' | file_img_url: \'1600x\' }}" alt="Bracelet trèfle doré porté au poignet" loading="lazy" width="1600" height="1600">'
         '<div><p class="lux-eyebrow">L’histoire</p><h2>Le trèfle, un porte-bonheur intemporel</h2>'
         '<p>Symbole de chance depuis des siècles, le trèfle traverse les modes sans jamais se démoder.</p>'
         '<p>Porté seul, il apporte une touche de lumière discrète. Accumulé avec d’autres bracelets, '
         'il affirme un style plus audacieux. Sept couleurs pour composer le vôtre.</p>'
         '<a href="/collections/bracelets-trefle">Découvrir la collection</a></div></div></div>')

DETAILS = ("<ul><li>Acier inoxydable couleur or</li><li>Cinq trèfles en nacre colorée ou dorés</li>"
           "<li>Longueur : 16,5 cm + 5 cm de chaînette de réglage</li><li>Diamètre d’un trèfle : 1,3 cm</li>"
           "<li>Poids : 9,9 g</li><li>Fermoir mousqueton</li></ul>")
CARE = ("<p>Retirez votre bracelet avant la douche, la baignade ou le sport. Évitez le contact avec le parfum, "
        "les crèmes et les produits ménagers. Nettoyez-le avec un chiffon doux et sec, et rangez-le à l’abri "
        "de l’humidité.</p>")
SHIP = ("<p>Chaque commande est expédiée avec un numéro de suivi ; le délai estimé s’affiche au moment du paiement.</p>"
        "<p>Vous disposez de 14 jours après réception pour exercer votre droit de rétractation. "
        "Contactez-nous via la page Contact et nous vous guidons.</p>")

tpl = {
    "sections": {
        "main": {
            "type": "product-information",
            "blocks": {
                "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
                    "media_presentation": "grid", "media_columns": "two", "image_gap": 4, "large_first_image": True,
                    "icons_style": "chevron", "slideshow_mobile_controls_style": "counter", "aspect_ratio": "1",
                    "media_radius": 0, "extend_media": False, "zoom": True, "hide_variants": True}, "blocks": {}},
                "product-details": {"type": "_product-details", "static": True, "settings": {
                    "width": "fill", "details_position": "flex-start", "gap": 28, "sticky_details_desktop": True,
                    "padding-block-start": 48, "padding-block-end": 48, "padding-inline-start": 24, "padding-inline-end": 24},
                    "blocks": {
                        "header": liquid(HEADER, "En-tête luxe"),
                        "price": {"type": "price", "settings": {"show_sale_price_first": True, "type_preset": "paragraph",
                                  "font": "var(--font-body--family)", "font_size": "1.125rem", "letter_spacing": "normal"}, "blocks": {}},
                        "variant_picker": {"type": "variant-picker", "settings": {"variant_style": "buttons", "show_swatches": False}, "blocks": {}},
                        "buy_buttons": {"type": "buy-buttons", "settings": {"stacking": True, "show_pickup_availability": False}, "blocks": {
                            "quantity": {"type": "quantity", "static": True, "settings": {}, "blocks": {}},
                            "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {
                                "style_class": "button-custom", "custom_button_background": "#1A1A1A",
                                "custom_button_text": "#FFFFFF", "custom_button_border": "#1A1A1A"}, "blocks": {}},
                            "accelerated-checkout": {"type": "accelerated-checkout", "static": True, "settings": {}, "blocks": {}}},
                            "block_order": []},
                        "services": liquid(SERVICES, "Services"),
                        "infos": {"type": "accordion", "settings": {"icon": "plus", "dividers": True, "divider_color": "#E6E6E6", "type_preset": "paragraph"},
                                  "blocks": {"r1": row("Détails du produit", DETAILS, True), "r2": row("Description", "{{ closest.product.description }}"),
                                             "r3": row("Entretien", CARE), "r4": row("Livraison & retours", SHIP)},
                                  "block_order": ["r1", "r2", "r3", "r4"]},
                    },
                    "block_order": ["header", "price", "variant_picker", "buy_buttons", "services", "infos"]},
            },
            "settings": {"content_width": "content-center-aligned", "desktop_media_position": "left", "equal_columns": False,
                         "gap": 48, "enable_sticky_add_to_cart": True, "background_color": "#FFFFFF",
                         "padding-block-start": 0, "padding-block-end": 48}},
        "edito": custom_section("Histoire du trèfle", EDITO, 96, 96, "#F7F5F2"),
        "services": custom_section("Services", BAND, 72, 72),
    },
    "order": ["main", "edito", "services"],
}

OUT.write_text(json.dumps(tpl, ensure_ascii=False, indent=2))
print(OUT, OUT.stat().st_size)
