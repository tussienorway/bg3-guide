# BG3 nybegynnerguide (bard-fokus)

Statisk, selvstendig side – ingen eksterne ressurser, ingen byggesteg nødvendig.

- `index.html` – selve guiden (forsiden for GitHub Pages / Netlify)
- `bg3-nybegynnerguide.html` – identisk kopi
- `build/` – kilde: `content_base.py` (opprinnelig innhold + Dark Urge-tekster), `content.py` (utvidelser: bard-spill, party-guider, utenfor kamp, nybegynnertips), mal i `template.html`. Regenerer med `python3 build/build.py`.

## Publisere
- **GitHub Pages:** legg filene i et repo, Settings → Pages → «Deploy from a branch» → rotmappen.
- **Netlify:** dra mappen inn på app.netlify.com/drop (eller koble repoet; ingen build-kommando, publish-mappe `.`).

Valg (hovedperson, klasse, spoilerbrytere, fremdrift) lagres i nettleserens localStorage under nøkkelen `bg3guide.v1`.
Dark Urge-innhold ligger base64-kodet i kilden og dekodes bare når «The Dark Urge» er valgt.
