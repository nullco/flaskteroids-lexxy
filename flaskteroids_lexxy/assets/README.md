# Packaged Lexxy assets

Lexxy 1.0.2: https://github.com/basecamp/lexxy (MIT; see LEXXY-LICENSE).

Unmodified `app/assets/javascript/lexxy.min.js` (packaged as `lexxy.js`)
and the four `app/assets/stylesheets/lexxy*.css` files from the official release:
https://rubygems.org/downloads/lexxy-1.0.2.gem

Release gem SHA-256:
5d0329955071b8b834fe1cf75e5f9cf6a2ad79a5e77c14a58e43d40e33a35030

The runtime bundles Lexical, DOMPurify, Marked, and Prism. Upstream notices remain
in the bundle; full license texts are adjacent in LEXICAL-LICENSE,
DOMPURIFY-LICENSE, MARKED-LICENSE, and PRISM-LICENSE. The DOMPurify notice identifies
version 3.3.0. DOMPurify is dual-licensed under Apache-2.0 or MPL-2.0; the other
components are MIT-licensed.

To update, verify the official release gem checksum, replace the runtime and
stylesheets, preserve all dependency licenses, and update this provenance.
