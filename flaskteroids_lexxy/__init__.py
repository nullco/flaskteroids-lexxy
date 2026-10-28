"""Packaged upstream Lexxy assets; rich-text integration belongs to Flaskteroids."""

PUBLIC_ASSETS = {
    name: ("flaskteroids_lexxy", f"assets/{name}")
    for name in (
        "lexxy.js",
        "lexxy.css",
        "lexxy-content.css",
        "lexxy-editor.css",
        "lexxy-variables.css",
    )
}
