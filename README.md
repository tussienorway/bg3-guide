# BG3 nybegynnerguide (bard-fokus)

Statisk, selvstendig side – ingen eksterne ressurser. Den ferdige siden kan publiseres som den er. Kjør byggestegget når du har endret kilden.

- `index.html` – selve guiden (forsiden for GitHub Pages / Netlify)
- `bg3-nybegynnerguide.html` – identisk kopi
- `build/` – kilde: `content_base.py` (opprinnelig innhold + Dark Urge-tekster), `content.py` (utvidelser: bard-spill, party-guider, utenfor kamp, nybegynnertips), mal i `template.html`, og `build.py`.

## Bygge

Ingen ekstra pakker, bare Python 3. Fra repo-roten:

```bash
python3 build/build.py
```

Skriptet leser `build/content.py` og `build/template.html`, setter inn innholdet, og skriver `index.html` og `bg3-nybegynnerguide.html`. Dark Urge-tekster base64-kodes i samme steg og dekodes i nettleseren bare når «The Dark Urge» er valgt.

## Publisere
- **GitHub Pages:** legg filene i et repo, Settings → Pages → «Deploy from a branch» → rotmappen. Ingen build-kommando; `index.html` i roten er siden.
- **Netlify:** dra mappen inn på app.netlify.com/drop (eller koble repoet; ingen build-kommando, publish-mappe `.`).

Valg (hovedperson, klasse, spoilerbrytere, fremdrift) lagres i nettleserens localStorage under nøkkelen `bg3guide.v1`.
Dark Urge-innhold ligger base64-kodet i kilden og dekodes bare når «The Dark Urge» er valgt.
