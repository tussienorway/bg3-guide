# BG3 nybegynnerguide (bard-fokus)

Statisk, selvstendig side – ingen eksterne ressurser. Den ferdige siden kan publiseres som den er. Kjør byggestegget når du har endret kilden.

- `index.html` – selve guiden (forsiden for GitHub Pages / Netlify)
- `bg3-nybegynnerguide.html` – identisk kopi
- `build/` – kilde: `content_base.py` (opprinnelig innhold + Dark Urge-tekster), `content.py` (utvidelser, inkludert kartlenker), mal i `template.html` (blant annet søk og kart), og `build.py`.

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

## Kart: hvorfor siden ikke viser spillkart

Kart-delen lenker til områdene. Den laster ingen kartbilder, verken lokalt eller fra andre nettsteder. Sjekken under er gjort 10. oktober 2026. Konklusjonen er at det ikke finnes en kilde som tydelig tillater å kopiere akt 1-kartene inn i dette repoet.

### Larian Studios, Baldur's Gate 3

BG3 har egne vilkår, ikke den generelle fanpolitikken:

- [Baldur's Gate 3 Fan Content Terms](https://baldursgate3.game/bg3-fan-content-terms/) (sist oppdatert 31. juli 2025). De gjelder bare BG3. [Larians generelle Fan Content Policy](https://larian.com/fan-content-policy) sier selv at den ikke gjelder BG3.
- Faninnhold er der definert som kreative verk (fanart, fanfiction, cosplay), audiovisuelle verk (strømmer og videoer) og mods. Vilkårene sier at Larian ikke kan gi tillatelser utover det som står der. Spørsmål utenfor vilkårene skal til Wizards of the Coast.
- Vilkårene gir ikke et løyve til å kopiere ut og legge ut spillkart på en fanside.
- [BG3-EULA](https://items.gog.com/BG3_EULA_en.txt) tillater skjermbilder bare til personlig, ikke-kommersiell bruk, med mindre Fan Content Terms sier noe mer. Det gjør de ikke for viderepublisering av kartfiler.
- [Larians FAQ om IP for innholdsskapere](https://larian.com/support/faqs/intellectual-property-ip-usage-by-content-creators-for-streaming-recording-and-original-content_67) sier at man kan dele bilder og opptak ikke-kommersielt, men også: ikke bruk spillinnhold (blant annet maps) i andre spill eller apper. FAQ-en peker videre til den generelle fanpolitikken, som altså ikke gjelder BG3.

BG3-vilkårene viser i sin helhet til [Wizards of the Coast Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy) (sist oppdatert 15. november 2017). Der står det at faninnhold er noe du selv lager, og at ordrett kopiering og viderepublisering av Wizards' IP ikke er faninnhold, selv om det er gratis. En fanside kan bruke kunst etter politikken, men det er ikke et tydelig løyve til å legge ut uthentede kartfiler fra spillet.

Guiden er uoffisiell, gratis og ikke godkjent av Larian eller Wizards.

### bg3.wiki

- [bg3wiki:Licensing](https://bg3.wiki/wiki/bg3wiki:Licensing) og [bg3wiki:Copyrights](https://bg3.wiki/wiki/bg3wiki:Copyrights): tekst bidragsytere selv skriver, er CC BY-NC-SA 4.0, og fra 20. juli 2024 også CC BY-SA 4.0. Det gjelder ikke automatisk spillbilder.
- Opplastede filer skal ha lisens på filsiden. Skjermbilder antas å falle under Larians eller Wizards' fanpolitikk. Det er ikke en egen lisens som tillater at andre kopierer filen.
- Filsider sjekket, uten lisensmal: [File:BG3 Map.webp](https://bg3.wiki/wiki/File:BG3_Map.webp), [File:Dank Crypt Map.jpg](https://bg3.wiki/wiki/File:Dank_Crypt_Map.jpg), [File:Druid Grove Map.png](https://bg3.wiki/wiki/File:Druid_Grove_Map.png), [File:GoblinCampOuterMap.png](https://bg3.wiki/wiki/File:GoblinCampOuterMap.png). De ligger i [Category:Location map images](https://bg3.wiki/wiki/Category:Location_map_images), som dekker både uthentede kart og skjermbilder.

Derfor er kartene ikke kopiert inn, og de blir heller ikke hotlinket. Hvert kartkort lenker til områdets side på bg3.wiki og til Map Genie med dyp lenke (`regions` eller `locationIds`). Det er det interaktive kartet wiki-en selv peker til, blant annet fra forsiden og fra sider som Zhalk (`locationIds`). Lista med steder under hvert kort er guidens egen tekst.
