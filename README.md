# Flaskteroids Lexxy

The upstream Lexxy **1.0.2** editor runtime and stylesheets, packaged with their
licenses and provenance. This package has **no runtime dependencies**.
Rich-text integration remains in Flaskteroids.

New browser applications include this package. To add it to an existing app:

```sh
uv add 'flaskteroids-lexxy>=0.1.0,<0.2'
bin/flask rich_text:install
bin/flask db:migrate
```

To upgrade:

```sh
uv lock --upgrade-package flaskteroids-lexxy
uv sync --locked
bin/flask assets:precompile
```

Applications load the editor through import maps without copying assets or
requiring Node, npm, or an editor CDN.

## Development

```sh
uv sync --locked --dev
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

See [RELEASING.md](RELEASING.md) for publishing and
[asset provenance](flaskteroids_lexxy/assets/README.md) for upstream details.
