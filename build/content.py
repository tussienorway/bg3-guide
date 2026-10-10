# -*- coding: utf-8 -*-
"""Innhold til BG3-guiden. Grunninnholdet ligger i content_base.py; her utvides det.
Formater:
  - scene-node: id, act, title, summary, basics[], tips[], cards[]
  - seksjon (bard / guides): id, title, (label), (summary), basics[], tips[], cards[]
  - tips/basics kan være streng eller {text, cls?, pro?, hideOrigin?}
  - kort: {kind: build|story|du, title, html, cls?, pro?}
"""
import copy
from content_base import DATA as _BASE, DU

DATA = copy.deepcopy(_BASE)

def L(href, text):
    return '<a href="#%s">%s</a>' % (href, text)

# ------------------------------------------------------------------
# 1. Bard: dypere spillguide
# ------------------------------------------------------------------
BARD_PLAY = {
 "id": "bard-play", "title": "Slik spiller du barden – tur for tur",
 "basics": [
  "<b>Før kampen:</b> Bardic Inspiration varer til lange hvil. Del den ut til tyven, warlocken og frontkjemperen <i>før</i> dere angriper. Da slipper du å bruke bonushandlinger på den midt i kampen.",
  "<b>Fast rekkefølge hver tur:</b> 1) Har noen falt? <i>Healing Word</i>. 2) Kan én formular slå ut den farligste fienden eller flere fiender? Bruk kontroll. 3) Ellers gjør du skade med <i>Vicious Mockery</i> eller hand crossbow. 4) Har du bonushandlingen til overs, gir du <i>Bardic Inspiration</i> til den som skal gjøre turens viktigste kast.",
  "<b>Bare én bonushandling per tur:</b> Healing Word og Bardic Inspiration er begge bonushandlinger, så du får bare én av dem per tur. Gjenoppliving går foran inspirasjon.",
  "<b>Ikke spar på inspirasjonen:</b> før nivå 5 har du 3 ladninger som bare lades på lange hvil. Fra nivå 5 (<i>Font of Inspiration</i>) lades alle også på korthvil. Ladninger du ikke har brukt når du hviler, er bortkastet.",
  "<b>Hvem skal ha inspirasjon?</b> Tyven før et angrep med Sneak Attack (det må treffe). Den som snart må slå et redningskast mot lammelse, sjarm eller frykt. Den som skal dirke en vanskelig lås eller ta en viktig samtale. Barden kan ikke inspirere seg selv.",
  "<b>Vicious Mockery eller våpen?</b> <i>Vicious Mockery</i> gjør 1d4 psykisk skade (2d4 fra nivå 5). Den bruker redningskast (Wisdom) i stedet for angrepskast, så du får ikke ulempe når en fiende står inntil deg. I tillegg får målet ulempe på sitt neste angrep. Bruk den mot store slåsskjemper med lav Wisdom som er på vei mot en alliert. En <i>hand crossbow</i> (1d6 + Dex) gjør ofte mer skade på lave nivåer og får bonus fra høyt terreng. Men den skyter med ulempe når en fiende står inntil deg.",
  "<b>Hvem du kontrollerer først:</b> 1) fiendtlige trollmenn og healere (<i>Silence</i>, <i>Hold Person</i>, <i>Dissonant Whispers</i>), 2) bueskyttere på høyt terreng, 3) den som slår hardest. Grupper som står tett: <i>Sleep</i> tidlig og <i>Hypnotic Pattern</i> fra nivå 5. Ikke bruk kontroll på fiender som dør neste tur uansett.",
  "<b>Konsentrasjon:</b> du kan bare holde én konsentrasjonsformular av gangen (Faerie Fire, Hold Person, Tasha's Hideous Laughter, Heroism, Silence, Hypnotic Pattern …). Kaster du en ny, avsluttes den gamle. Tar du skade, slår du et Constitution-redningskast for å holde den (DC 10 eller halve skaden, det som er høyest). Stå bak frontlinjen og utenfor rekkevidde for bueskyttere.",
  "<b>Mens du konsentrerer deg:</b> velg formularer som ikke krever konsentrasjon (Dissonant Whispers, Sleep, Shatter, Thunderwave, Healing Word). Konsentrasjon gjelder per karakter: warlocken kan holde <i>Hex</i> samtidig som du holder <i>Hold Person</i>.",
 ],
 "tips": [
  {"text": "<b>Hold Person + nærkamp:</b> nærkampangrep mot et lammet mål blir kritiske treff, og kritiske treff dobler også tyvens Sneak Attack-terninger. Målet slår et nytt redningskast på slutten av hver tur, så la tyven og frontkjemperen slå til med en gang. Se " + L("party-synergy", "Bard + tyv + warlock") + "."},
  {"text": "<b>Når flere i gruppa har tur etter hverandre,</b> kan du velge rekkefølgen selv. Da kan barden kaste kontroll eller Faerie Fire først, og tyven angripe med fordel etterpå."},
 ],
 "cards": [
  {"kind": "build", "title": "Mønster for en typisk tidlig kamp", "html":
   "<ol><li><b>Før kampen:</b> Inspiration på tyv og warlock. Snik gruppa i posisjon (se " + L("rogue-stealth", "snik og skjul") + ").</li>"
   "<li><b>Runde 1:</b> barden kaster <i>Faerie Fire</i> på klyngen eller <i>Hold Person</i> på den sterkeste. Tyven angriper med fordel og Sneak Attack. Warlocken legger <i>Hex</i> (bonushandling) og skyter <i>Eldritch Blast</i>.</li>"
   "<li><b>Runde 2+:</b> barden holder konsentrasjonen, bruker Vicious Mockery eller armbrøst, og har Healing Word klar. Warlocken bruker Repelling Blast til å dytte fiender bort fra barden eller ned fra kanter.</li>"
   "<li><b>Etter kampen:</b> korthvil hvis warlocken har brukt plassene sine (de lades da). Song of Rest gir et ekstra korthvil.</li></ol>"},
  {"kind": "build", "cls": "bard", "title": "Lore-barden: Cutting Words", "html":
   "<p><i>Cutting Words</i> er en reaksjon som bruker en inspirasjonsladning til å trekke terningen fra en fiendes angrep, evnesjekk eller skadekast. Bruk den når et fiendtlig treff er på vei til å slå ned noen. Med Font of Inspiration fra nivå 5 har du råd til det oftere.</p>"},
 ],
}

BARD_LEVELS = {
 "id": "bard-levels", "title": "Formularvalg nivå 1–6",
 "basics": [
  "<b>Nivå 1</b> (2 cantrips, 4 formularer): <i>Vicious Mockery</i> + <i>Friends</i> eller <i>Minor Illusion</i>. Formularer: <i>Healing Word</i> (må ha), <i>Dissonant Whispers</i>, <i>Faerie Fire</i> og én av <i>Sleep</i>, <i>Tasha's Hideous Laughter</i> eller <i>Thunderwave</i>.",
  "<b>Nivå 2</b> (+1 formular): ta den av Sleep, Tasha's eller Thunderwave du ikke valgte, eller en nytteformular som <i>Speak with Animals</i>, <i>Disguise Self</i> eller <i>Feather Fall</i>. Se " + L("oc-magic", "nyttemagi") + ".",
  "<b>Nivå 3</b> (nivå 2-formularer, +1 formular): <i>Hold Person</i> er det beste valget. Gode alternativer: <i>Shatter</i> (område-skade), <i>Silence</i> (stopper fiendtlige trollmenn), <i>Invisibility</i>, <i>Enhance Ability</i> og <i>Heat Metal</i>.",
  "<b>Nivå 4</b> (+1 formular, +1 cantrip, feat): cantrip som <i>Mage Hand</i> eller <i>Minor Illusion</i>. Feat: <i>Ability Improvement</i> på Charisma (til 18 eller 20). Formular: én til av nivå 2-listen, gjerne <i>Shatter</i> eller <i>Invisibility</i>.",
  "<b>Nivå 5</b> (nivå 3-formularer, +1 formular): <i>Hypnotic Pattern</i> er en av spillets beste kontrollformularer. Pass på at den også treffer allierte i området. Alternativer: <i>Fear</i>, <i>Glyph of Warding</i> og <i>Speak with Dead</i> (utenfor kamp).",
  "<b>Nivå 6</b> (+1 formular): én til av nivå 3-listen. <b>Lore-barder</b> får også <i>Magical Secrets</i>: to formularer fra andre klasser (opp til nivå 3), for eksempel <i>Counterspell</i>, <i>Haste</i> eller <i>Fireball</i>.",
  "<b>Bytt ut svake valg:</b> hver gang du går opp i nivå, kan du bytte ut én formular. <i>Sleep</i> blir svakere når fiendene får mer HP, og er en god kandidat å bytte bort.",
 ],
 "tips": [],
 "cards": [
  {"kind": "build", "title": "Hvorfor disse valgene?", "html":
   "<ul><li>Healing Word og Bardic Inspiration er begge bonushandlinger. Velg derfor formularer som bruker <i>handlingen</i> din godt (kontroll).</li>"
   "<li>Ha bare 2–3 konsentrasjonsformularer. Du kan uansett bare holde én av gangen.</li>"
   "<li>Med en tyv i gruppa trenger du ikke <i>Knock</i>. Er warlocken Pact of the Tome, har dere <i>Guidance</i> fra den.</li></ul>"},
 ],
}

BARD_MULTI = {
 "id": "bard-multi", "title": "Multiklasse (valgfritt)",
 "basics": [
  "Multiklasse betyr at du tar nivåer i en annen klasse når du går opp i nivå. Det er helt valgfritt, og en ren bard fungerer utmerket hele spillet.",
  "For første gjennomspilling: hold deg til ren bard i hvert fall til nivå 5–6 (Font of Inspiration, nivå 3-formularer og Lore-bardens Magical Secrets).",
 ],
 "tips": [],
 "cards": [
  {"kind": "build", "title": "Multiklasse-notater for barden", "html":
   "<ul><li><b>Bard + 2 nivåer warlock:</b> gir Eldritch Blast med Agonizing Blast og Repelling Blast, og strålene øker med <i>karakternivå</i>. Begge klassene bruker Charisma. Warlock-plassene lades på korthvil.</li>"
   "<li><b>Swords/Valour + paladin:</b> våpenbard med Divine Smite. Også her er Charisma felles.</li>"
   "<li><b>Bard + sorcerer:</b> mer magi og Metamagic, felles Charisma. Passer for en ren trollmannsbard.</li>"
   "<li><b>Ulemper:</b> du får de høyeste formularnivåene og klasseevnene senere. Maks nivå er 12, så hvert nivå i en annen klasse er et bardnivå mindre. Omskolering hos Withers koster 100 gull, så det er trygt å prøve.</li></ul>"},
 ],
}

# Utvid eksisterende bard-seksjoner
bard = {s["id"]: s for s in DATA["bard"]}
bard["bard-spells"]["basics"].append("Se " + L("bard-levels", "Formularvalg nivå 1–6") + " for en konkret plan per nivå.")
bard["bard-subclass"]["cards"].append(
 {"kind": "build", "title": "Med tyv og warlock i gruppa", "html":
  "<ul><li><b>Lore</b> passer fortsatt best til en støttebard. Tyven dekker låser og feller, så bruk Lore-bardens ekstra ferdigheter på det gruppa mangler (Perception, Insight, Arcana).</li>"
  "<li><b>Glamour</b> er enklest å lykkes med: <i>Mantle of Inspiration</i> gir tyven og warlocken midlertidige HP, og det er nettopp de to som tåler minst.</li>"
  "<li>Velg <b>Swords/Valour</b> bare hvis du selv vil stå i nærkamp. Da har gruppa to i nærkamp (barden og tyven) og trenger en healer mer enn en tank.</li></ul>"})
bard["bard-party"]["basics"].append("Gruppa di (bard, tyv og warlock) har mye skade og kontroll, men lite HP. Se " + L("party-synergy", "Bard + tyv + warlock") + " for samspillet.")

order = ["bard-core", "bard-play", "bard-spells", "bard-levels", "bard-subclass", "bard-multi", "bard-face", "bard-perform", "bard-gear", "bard-party"]
bard.update({"bard-play": BARD_PLAY, "bard-levels": BARD_LEVELS, "bard-multi": BARD_MULTI})
DATA["bard"] = [bard[i] for i in order]
for s in DATA["bard"]:
    s.setdefault("tips", [])

# ------------------------------------------------------------------
# 2. Party-medlemmer: tyv, warlock, samspill
# ------------------------------------------------------------------
PARTY = {"id": "party", "nav": "Party-medlemmer", "title": "Party-medlemmer: tyven og warlocken",
 "summary": "Slik spiller du tyven (rogue) og warlocken smart, og hvordan de virker sammen med barden. Grunnreglene vises alltid, og byggtips ligger i spoilerkort.",
 "sections": [
 {"id": "rogue-core", "label": "Tyv (Rogue)", "title": "Tyven: Sneak Attack og Cunning Action",
  "basics": [
   "{astarion}",
   "<b>Sneak Attack</b> gir ekstra skade: 1d6 på nivå 1–2, 2d6 på nivå 3, 3d6 på nivå 5 og så videre (+1d6 hvert andre nivå). Den krever et <i>finesse-</i> eller <i>avstandsvåpen</i> (rapier, kortsverd, dolk, kortbue, armbrøst).",
   "<b>Krav:</b> du har <b>fordel</b> på angrepet, <i>eller</i> en alliert står innen 1,5 m av målet og du har <b>ikke</b> ulempe. Sneak Attack kan brukes <b>én gang per tur</b>. I BG3 har den egne knapper (nærkamp og avstand) som lyser opp når kravene er oppfylt.",
   "Kritiske treff dobler også Sneak Attack-terningene. Derfor er lammede mål (<i>Hold Person</i>) gull for tyven.",
   "<b>Cunning Action</b> (nivå 2) lar deg bruke <i>Dash</i>, <i>Disengage</i> eller <i>Hide</i> som bonushandling. Typiske turer: angrip og bruk Disengage før du går bort uten å bli slått. Bruk Dash for å nå høyt terreng og skyte. Eller skyt og bruk Hide etterpå.",
   "<b>Expertise</b> på nivå 1 og 6 gir dobbel ferdighetsbonus i to ferdigheter. Det beste valget er nesten alltid <i>Sleight of Hand</i> og <i>Stealth</i>, eventuelt <i>Perception</i>.",
   "Sett Dexterity høyest, deretter Constitution. Med to våpen er angrepet med venstre hånd også en bonushandling, så det konkurrerer med Cunning Action.",
  ],
  "tips": [{"cls": "bard", "text": "Gi tyven <b>Bardic Inspiration</b> før kampen. Bommer det store Sneak Attack-angrepet, kan terningen redde det."}],
  "cards": []},
 {"id": "rogue-stealth", "label": "Tyv (Rogue)", "title": "Snik, skjul og angrep fra skjul",
  "basics": [
   "<b>Snik</b> (sneak-knappen eller hurtigtast) viser synsfeltene til NPC-ene. Går du inn i et synsfelt, slår du Stealth mot deres Perception.",
   "<b>Hide</b> i kamp (handling, eller bonushandling med Cunning Action) krever at ingen fiender ser deg tydelig. Lykkes du, er du skjult, og ditt neste angrep får <b>fordel</b> og dermed Sneak Attack. Å angripe avslører deg vanligvis.",
   "<b>Overraskelse:</b> starter du kampen mens du er skjult, blir fiender som ikke har oppdaget deg <i>overrasket</i> og mister første tur. Snik hele gruppa i posisjon før du angriper.",
   "Skygger og mørke gjør det lettere å holde seg skjult. Sterkt lys gjør det vanskeligere.",
   "Vil du flytte én karakter alene, kobler du den fra gruppa (dra portrettet ut av rekken). Ellers følger de andre etter og kan bli oppdaget.",
  ],
  "tips": [], "cards": []},
 {"id": "rogue-skills", "label": "Tyv (Rogue)", "title": "Låser, feller, lommetyveri og posisjon",
  "basics": [
   "<b>Låser:</b> Thieves' Tools i sekken + <i>Sleight of Hand</i> (Dexterity). Tyven starter med Thieves' Tools. Kjøp flere hos handelsfolk, så du alltid har reserve.",
   "<b>Feller:</b> først må noen oppdage fellen med Perception. Så desarmerer du den med et <i>Trap Disarm Toolkit</i> og Sleight of Hand, eller går rundt. Send tyven først i ruiner og krypter.",
   "<b>Lommetyveri:</b> snik deg inntil en NPC og velg <i>Pickpocket</i>. Detaljer og konsekvenser finner du i " + L("oc-hands", "Utenfor kamp → Sleight of Hand") + ".",
   "<b>Høyt terreng</b> gir +2 på avstandsangrep, og lavt terreng gir −2. En tyv med bue på et tak, og en alliert inntil målet, får Sneak Attack hver tur uten å trenge fordel.",
   "Det finnes ingen egen flankeringsbonus i BG3. Det holder at en alliert står ved siden av målet.",
  ],
  "tips": [], "cards": []},
 {"id": "rogue-sub", "label": "Tyv (Rogue)", "title": "Undervalg (nivå 3) og tidlig utstyr",
  "basics": [
   "<b>Thief:</b> <i>Fast Hands</i> gir en <b>ekstra bonushandling</b>. Det er det enkleste og sterkeste valget for nybegynnere: Hide + angrep med venstre hånd, eller Dash + Disengage, samme tur.",
   "<b>Arcane Trickster:</b> wizard-formularer (Intelligence) og en forbedret <i>Mage Hand</i>. Mer fleksibel, men mer å holde styr på, og den trenger Intelligence ved siden av Dexterity.",
   "<b>Assassin:</b> <i>Assassinate</i> gir fordel mot fiender som ikke har hatt sin tur ennå, og kritiske treff mot overraskede fiender. Den er sterkest i den første runden, så du må snike deg til gode åpninger.",
   "<b>Swashbuckler</b> (kom i Patch 8): nærkamptyv som lettere får Sneak Attack når den står alene mot en fiende. Den bruker også Charisma.",
  ],
  "tips": [], "cards": [
   {"kind": "build", "title": "Anbefaling og gode gjenstander i akt 1", "html":
    "<p><b>Anbefaling:</b> Thief hvis tyven skal være dirker og skadeleverandør. Assassin hvis du liker å åpne kamper fra skjul.</p><ul>"
    "<li><b>Smuggler's Ring</b>: bonus på Stealth. Den ligger på et skjelett ved den ødelagte broen på Risen Road.</li>"
    "<li><b>Gloves of Thievery</b>: bedre Sleight of Hand. Selges av Brem i Zhentarim-skjulestedet (Waukeen's Rest) etter oppdraget «Missing Shipment».</li>"
    "<li><b>Drow Studded Leather</b>: lett rustning med +1 Stealth (Underdark).</li>"
    "<li><b>Knife of the Undermountain King</b>: dolk som gir kritisk treff på 19–20 (selges i githyanki-krèchen).</li>"
    "<li><b>Disintegrating Night Walkers</b>: støvler med Misty Step og beskyttelse mot nett og glatte flater (Grymforge).</li></ul>"
    "<p>Beliggenhetene kan variere litt med ruten din. Sjekk handelsfolk underveis.</p>"},
  ]},
 {"id": "wl-core", "label": "Warlock", "title": "Warlocken: Eldritch Blast og invokasjoner",
  "basics": [
   "{wyllwl}",
   "<b>Eldritch Blast</b> er warlockens hovedangrep: en cantrip med 1d10 force-skade og angrepskast. Du får 2 stråler på karakternivå 5 og 3 på nivå 10. Hver stråle slår eget angrepskast og kan rettes mot forskjellige mål.",
   "<b>Agonizing Blast</b> (invokasjon, nivå 2): legger Charisma-modifikatoren til skaden på <i>hver</i> stråle. Den bør du nesten alltid ta.",
   "<b>Repelling Blast</b> (invokasjon): hvert treff kan dytte målet opptil 4,5 m unna (én gang per mål per kast). Bruk den til å dytte fiender ned fra kanter, inn i flammer eller bort fra barden. Den kan slås av og på.",
   "Andre gode tidlige invokasjoner: <i>Devil's Sight</i> (se i magisk mørke), <i>Beguiling Influence</i> (Persuasion og Deception) og <i>Mask of Many Faces</i> (Disguise Self uten å bruke plass).",
   "Sett Charisma høyest. Warlocken er også god i dialog, så den kan ta samtalen hvis barden ikke er der.",
  ],
  "tips": [], "cards": []},
 {"id": "wl-hex", "label": "Warlock", "title": "Hex, Hunter's Mark og konsentrasjon",
  "basics": [
   "<b>Hex</b>: bonushandling, nivå 1-plass, konsentrasjon. Hvert treff warlocken gjør på målet gir +1d6 necrotic, og det gjelder <i>hver</i> Eldritch Blast-stråle. Målet får også ulempe på evnesjekker med én evne du velger. Det gjelder ikke redningskast.",
   "Dør målet, kan du flytte Hex til en ny fiende uten å bruke en ny plass (<i>Reapply Hex</i>). I BG3 varer Hex til konsentrasjonen brytes, så én plass kan holde gjennom en hel kamp.",
   "<b>Hunter's Mark</b> er en ranger-formular som bare virker på <i>våpenangrep</i>. Eldritch Blast er et formularangrep, og warlocken lærer ikke Hunter's Mark selv. Velg derfor Hex.",
   "<b>Konsentrasjon:</b> Hex, Darkness, Hold Person og Hunger of Hadar krever alle konsentrasjon. Bare én av dem kan være aktiv om gangen. Tar warlocken skade, kan den miste Hex.",
  ],
  "tips": [], "cards": []},
 {"id": "wl-slots", "label": "Warlock", "title": "Pact Magic: få plasser, ladet på korthvil",
  "basics": [
   "Warlocken har svært få formularplasser (1 på nivå 1, deretter 2). Til gjengjeld lades de på <b>korthvil</b>, og de er alltid på høyeste nivå du har (nivå 2 fra warlock-nivå 3, nivå 3 fra nivå 5).",
   "Bruk plassene hver kamp, og ta korthvil etterpå. Du har to korthvil per lange hvil.",
   "Siden plassene alltid kastes på høyeste nivå, får formularer som blir sterkere med nivået mest ut av dem, for eksempel <i>Armour of Agathys</i>. Hex blir ikke sterkere av en høyere plass.",
  ],
  "tips": [{"cls": "bard", "text": "<b>Song of Rest</b> (bard nivå 2) gir hele gruppa et ekstra korthvil, og warlocken får alle plassene tilbake. Barden og warlocken passer derfor godt sammen."}],
  "cards": []},
 {"id": "wl-patron", "label": "Warlock", "title": "Patron (nivå 1) og Pact Boon (nivå 3)",
  "basics": [
   "<b>The Fiend:</b> midlertidige HP når du dreper en fiende, og ild- og skadeformularer i den utvidede listen. Robust og enkel, og et godt valg for en Eldritch Blast-warlock.",
   "<b>The Great Old One:</b> mer kontroll og skremsel. Lett å spille som en ren avstandswarlock.",
   "<b>The Archfey:</b> sjarm og frykt rundt seg, og formularer som <i>Faerie Fire</i> og <i>Sleep</i>. Overlapper litt med barden.",
   "<b>The Hexblade</b> (kom i Patch 8): bruker Charisma til våpenangrep og har <i>Hexblade's Curse</i>. Det beste valget hvis warlocken skal kjempe i nærkamp.",
   "<b>Pact of the Blade:</b> et pakt-våpen som bruker Charisma. Til nærkamp-warlock, gjerne sammen med Hexblade.",
   "<b>Pact of the Chain:</b> en tjenerånd (familiar, for eksempel imp eller quasit) til speiding, Help og ekstra skade.",
   "<b>Pact of the Tome:</b> en bok med <i>Guidance</i>, <i>Vicious Mockery</i> og <i>Thorn Whip</i>. På nivå 5 får du også Animate Dead, Call Lightning og Haste. Guidance gir +1d4 på ferdighetssjekker, og det har bard-gruppa god bruk for.",
  ],
  "tips": [],
  "cards": [
   {"kind": "build", "title": "Hva bør en nybegynner velge?", "html":
    "<ul><li><b>Avstand (enklest):</b> Fiend eller Great Old One + Pact of the Tome. Eldritch Blast hver tur, Hex på den farligste fienden og Guidance før dialog og dirking.</li>"
    "<li><b>Nærkamp:</b> Hexblade + Pact of the Blade. Da kan Darkness-kombinasjonen under gi mening.</li>"
    "<li>Er du usikker, kan Withers omskolere warlocken for 100 gull.</li></ul>"},
  ]},
 {"id": "wl-spells", "label": "Warlock", "title": "Gode tidlige formularer og utstyr",
  "basics": [
   "<b>Cantrips:</b> Eldritch Blast + <i>Minor Illusion</i>, <i>Mage Hand</i> eller <i>Friends</i>.",
   "<b>Nivå 1:</b> <i>Hex</i> (må ha), <i>Armour of Agathys</i> (midlertidige HP og kuldeskade på dem som slår deg, blir sterkere med plassnivået) og <i>Hellish Rebuke</i> (reaksjon).",
   "<b>Nivå 3 (nivå 2-plasser):</b> <i>Misty Step</i> (teleport, bonushandling), <i>Hold Person</i> og <i>Darkness</i> (med Devil's Sight).",
   "<b>Nivå 5 (nivå 3-plasser):</b> <i>Hunger of Hadar</i>, <i>Counterspell</i> eller <i>Hypnotic Pattern</i>. Hypnotic Pattern har barden kanskje allerede.",
  ],
  "tips": [],
  "cards": [
   {"kind": "build", "title": "Darkness + Devil's Sight", "html":
    "<p>Kast <i>Darkness</i> (nivå 2-plass, konsentrasjon) slik at skyen dekker warlocken og fiendene rundt den. Med <i>Devil's Sight</i> ser warlocken normalt i skyen, mens de andre der inne blir <b>blindet</b>. Angrep mot blindede har fordel, og de angriper selv med ulempe.</p>"
    "<ul><li>Ifølge spillets beskrivelse kan man ikke bruke avstandsangrep inn i eller ut av skyen. Kombinasjonen passer derfor best for en <b>nærkamp-warlock</b> (Hexblade eller Pact of the Blade), eller for å beskytte warlocken mot bueskyttere.</li>"
    "<li>Darkness tar konsentrasjonen, så du kan ikke ha Hex samtidig.</li>"
    "<li>Allierte uten Devil's Sight blir også blindet i skyen. Hold barden ute, og la tyven bruke kanten av skyen til å gjemme seg.</li></ul>"},
   {"kind": "build", "title": "Utstyr i akt 1 for warlocken", "html":
    "<ul><li><b>The Spellsparkler</b> (stav): skade med formularer gir Lightning Charges. Belønning for å redde Counsellor Florrick ved Waukeen's Rest.</li>"
    "<li><b>Daredevil Gloves</b>: +1 på formularangrep, og formularangrep tett inntil en fiende blir nærkampangrep (ingen ulempe). Selges i githyanki-krèchen.</li>"
    "<li><b>Disintegrating Night Walkers</b>: Misty Step og beskyttelse mot nett og glatte flater (Grymforge).</li>"
    "<li>Alt som gir AC eller redningskast (for eksempel en <i>Ring of Protection</i>), siden warlocken har lite HP.</li></ul>"},
  ]},
 {"id": "party-synergy", "label": "Samspill", "title": "Bard + tyv + warlock: slik spiller dere sammen",
  "basics": [
   "<b>Inspirasjon på tyven:</b> før kampen og før vanskelige låser. Det store Sneak Attack-angrepet må treffe.",
   "<b>Kontroll gir Sneak Attack:</b> <i>Faerie Fire</i> gir fordel på angrep mot målene, så tyven får Sneak Attack også på avstand. <i>Hold Person</i> gjør nærkamptreff kritiske og dobler Sneak Attack-terningene. Mot sovende mål (<i>Sleep</i>) har du fordel, men målet våkner når det tar skade. La derfor tyven ta det store slaget.",
   "<b>Warlocken beskytter barden:</b> Repelling Blast dytter nærkjempere bort fra barden og ned fra kanter. Hex på den fienden tyven også går etter, gjør at den dør raskere.",
   "<b>Hvil:</b> warlocken trenger korthvil for å få plassene tilbake, og barden kan gi et ekstra med Song of Rest. Fra nivå 5 lader korthvilene også bardens inspirasjon.",
   "<b>Utenfor kamp:</b> barden snakker (Persuasion), tyven dirker og finner feller, og warlocken med Pact of the Tome gir <i>Guidance</i> før viktige kast.",
   "<b>Fjerde plass:</b> alle tre har lite HP. En frontkjemper (for eksempel Lae'zel eller Karlach) gir tyven en alliert ved siden av målet, og alle bak frontlinjen får ro til å jobbe. Shadowheart (cleric) er alternativet hvis dere heller trenger helbreding.",
  ],
  "tips": [], "cards": []},
 ]}

# ------------------------------------------------------------------
# 3. Utenfor kamp
# ------------------------------------------------------------------
OOC = {"id": "ooc", "nav": "Utenfor kamp", "title": "Utenfor kamp: ferdigheter og nyttetriks",
 "summary": "Mye av BG3 avgjøres i dialog, med låser og ved å snike. Her ser du hvordan sjekkene fungerer, og hvordan du får sjansene på din side.",
 "sections": [
 {"id": "oc-checks", "title": "Ferdighetssjekker: slik regnes de",
  "basics": [
   "<b>Formel:</b> d20 + evnemodifikator + ferdighetsbonus (hvis du er trent) mot vanskelighetsgraden (DC) som står på terningen.",
   "<b>Evnemodifikator:</b> 10–11 gir +0, 12–13 gir +1, 14–15 gir +2, 16–17 gir +3, 18–19 gir +4 og 20 gir +5. 8–9 gir −1.",
   "<b>Ferdighetsbonus (proficiency):</b> +2 på nivå 1–4, +3 på nivå 5–8 og +4 på nivå 9–12. <b>Expertise</b> dobler den (bard nivå 3 og 10, tyv nivå 1 og 6). Bardens <i>Jack of All Trades</i> gir halv bonus på det du ikke er trent i.",
   "<b>Hvilken evne?</b> Strength: Athletics. Dexterity: Acrobatics, Sleight of Hand og Stealth. Intelligence: Arcana, History, Investigation, Nature og Religion. Wisdom: Animal Handling, Insight, Medicine, Perception og Survival. Charisma: Deception, Intimidation, Performance og Persuasion.",
   "I dialogkast lykkes en naturlig 20 alltid, og en naturlig 1 feiler alltid. Noen sjekker (særlig Perception) slås automatisk i bakgrunnen når du går forbi noe skjult.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-boost", "title": "Slik øker du sjansene",
  "basics": [
   "<b>Guidance</b> (cantrip): +1d4 på evnesjekker. Shadowheart har den, og det samme har druider og warlocks med Pact of the Tome. Kast den rett før samtalen eller låsen. Den krever konsentrasjon og at du står inntil den du kaster den på.",
   "<b>Bardic Inspiration</b>: inspirasjonsterningen legges til neste evnesjekk. Gi den til den som skal snakke eller dirke.",
   "<b>Inspiration fra bakgrunnen</b> (ikke det samme som Bardic Inspiration): lar deg slå om en mislykket sjekk. Du tjener poeng ved å handle i tråd med bakgrunnen din.",
   "<b>Fordel (advantage),</b> der du slår to terninger og bruker den beste: <i>Friends</i> (Charisma-sjekker mot en som ikke er fiendtlig), <i>Enhance Ability</i> (for eksempel Charisma eller Dexterity) og enkelte gjenstander. Har du både fordel og ulempe, opphever de hverandre.",
   "<b>Velg riktig person:</b> den som er trent i (eller har Expertise i) ferdigheten, bør ta sjekken. Se " + L("oc-dialog", "hvem som snakker") + ".",
  ],
  "tips": [{"cls": "bard", "text": "<b>Stabling før en viktig samtale:</b> Friends (fordel) + Guidance fra warlocken eller Shadowheart (+1d4). En alliert kan også ta samtalen med Bardic Inspiration fra deg (+1d6/d8). Barden kan ikke inspirere seg selv."}],
  "cards": []},
 {"id": "oc-dialog", "title": "Dialog: overtale, lure, true – og hvem som snakker",
  "basics": [
   "<b>Persuasion</b> overtaler ærlig, <b>Deception</b> lyver og <b>Intimidation</b> truer. Følgesvennene liker og misliker ulike tilnærminger (approval).",
   "<b>Insight</b> avslører løgner og skjulte motiver, og gir ofte et ekstra, bedre svaralternativ.",
   "<b>Den som snakker, slår terningen.</b> Den valgte karakteren (det aktive portrettet) starter samtalen og tar sjekkene. Bytt til barden før du klikker på en viktig NPC.",
   "Mange NPC-er starter samtalen selv med den som kommer nærmest. Koble barden fra gruppa og gå først, så det er barden som blir snakket til.",
   "Merkede valg som [BARD], [TIEFLING] eller [RELIGION] viser at klassen, rasen eller ferdigheten åpner et eget alternativ. Det er ofte et godt valg.",
   "Ser sjansen dårlig ut (høy DC), kan du velge et annet svar eller lagre før du prøver.",
  ],
  "tips": [],
  "cards": [
   {"kind": "story", "title": "Konkrete tidlige eksempler", "html":
    "<ul><li><b>Roadside Cliffs:</b> buret med Lae'zel kan ofte løses med Persuasion eller Intimidation, uten kamp.</li>"
    "<li><b>Overgrown Ruins:</b> folkene ved inngangen er ikke helt ærlige om hvem de er. Insight kan avsløre det før du bestemmer deg.</li>"
    "<li><b>Emerald Grove:</b> konfrontasjonen med Kagha kan løses med Persuasion, Intimidation eller Insight. Høy Charisma gir flest muligheter.</li>"
    "<li><b>Goblinleiren:</b> du kan snakke deg forbi vaktene ved porten. Mislykkes du, kan det bli kamp mot mange.</li></ul>"},
  ]},
 {"id": "oc-find", "title": "Feller og skjulte ting: Perception og Investigation",
  "basics": [
   "<b>Perception</b> slås automatisk og hver for seg for alle i gruppa når dere kommer nær feller, skjulte brytere og gjemte gjenstander. La den med høyest Perception gå først.",
   "Oppdagede feller blir markert. Desarmer dem (Trap Disarm Toolkit + Sleight of Hand), gå rundt, eller utløs dem med vilje på avstand (for eksempel ved å kaste noe på trykkplaten eller bruke Mage Hand).",
   "<b>Investigation</b> brukes når du undersøker bøker, lik, mekanismer eller spor. Det gir ofte ekstra informasjon eller nye valg.",
   "På PC fremhever <b>venstre Alt</b> alt du kan samhandle med i nærheten. Bruk den i hvert rom.",
   "Har en kiste eller dør ingen lås du klarer å dirke, kan mange slås i stykker eller åpnes med en nøkkel som ligger i nærheten.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-hands", "title": "Sleight of Hand: låser og lommetyveri",
  "basics": [
   "<b>Dirking:</b> krever Thieves' Tools i sekken. DC står på låsen. Mislykkes du, kan du som regel prøve igjen så lenge du har verktøy. Ha alltid noen sett i reserve.",
   "<i>Knock</i> (bard, nivå 2-formular) åpner låser uten sjekk. Med en tyv i gruppa sparer du heller plassen.",
   "<b>Lommetyveri:</b> snik deg inntil en NPC (helst bakfra og ute av syne for andre) og velg <i>Pickpocket</i>. Hver gjenstand har sin egen sjekk. Dyre og tunge ting er vanskeligere.",
   "<b>Blir du oppdaget,</b> konfronterer NPC-en deg. Det kan ende med samtale, bot eller kamp, og andre i nærheten kan bli fiendtlige.",
   "Stjålne gjenstander er merket som stjålet. Eieren og deres venner reagerer hvis de ser dem på deg.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-stealth", "title": "Sniking og kriminalitet",
  "basics": [
   "Slå på <b>Sneak</b> for å se synsfeltene til NPC-ene. Utenfor synsfeltet blir du ikke sett. Inne i det slår du Stealth.",
   "<b>Forbudte områder</b> (trespassing) varsles på skjermen. Blir du sett der, blir du bedt om å gå, eller verre.",
   "<b>Kriminalitet</b> omfatter tyveri, innbrudd og angrep på nøytrale. Gjør du det mens noen ser på, får det konsekvenser: konfrontasjon, en hel gruppe som blir fiendtlig, eller tapte handelsfolk og oppdrag.",
   "<b>Hjelpemidler:</b> <i>Invisibility</i>, <i>Minor Illusion</i> (trekker oppmerksomheten bort), mørke og skygger, og <i>Pass without Trace</i> (+10 Stealth til gruppa, fra druid, ranger eller Trickery-cleric).",
   "Lagre før du stjeler noe verdifullt i et befolket område.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-lore", "title": "Kunnskapssjekker, Insight, Medicine og Animal Handling",
  "basics": [
   "<b>Arcana:</b> magi, runer, magiske gjenstander og vesener. <b>History:</b> gamle steder, slekter og hendelser. <b>Religion:</b> guder, hellige symboler og vandøde. <b>Nature:</b> planter, dyr, vær og terreng.",
   "<b>Medicine:</b> undersøk lik (dødsårsak) og hjelp syke eller skadde NPC-er. <b>Insight:</b> les folk. <b>Survival:</b> spor og villmark.",
   "<b>Animal Handling:</b> ro ned eller bli venn med dyr som ellers ville angrepet. Ofte unngår du en unødvendig kamp.",
   "Intelligence-sjekker er ofte svakheten til en Charisma-gruppe. Bytt til Gale (wizard) hvis han er med, eller la barden bruke Jack of All Trades. Guidance hjelper også.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-magic", "title": "Nyttemagi utenfor kamp",
  "basics": [
   "<b>Speak with Animals</b> (bard nivå 1, ritual): snakk med dyr. Det gir informasjon, små oppdrag og mye humor. Som ritual koster den ingen plass utenfor kamp, og det finnes også drikker med samme effekt.",
   "<b>Speak with Dead</b> (bard nivå 3-formular): still spørsmål til et lik. Det løser mysterier og gir spor.",
   "<b>Disguise Self</b> (bard nivå 1): endre utseende for å unngå oppmerksomhet eller komme forbi folk som ville kjent deg igjen.",
   "<b>Mage Hand</b> (cantrip): en spøkelseshånd som flytter og kaster ting, trykker på knapper og plater, utløser feller på avstand og henter ting som ligger utenfor rekkevidde.",
   "<b>Feather Fall</b> (bard nivå 1, ritual): ingen fallskade. Hopp ned fra klipper som snarvei, eller redd gruppa hvis bakken forsvinner under dere.",
   "<b>Minor Illusion</b> (cantrip): lager en lyd eller et bilde som NPC-er går for å undersøke. Det er perfekt før sniking eller lommetyveri.",
  ],
  "tips": [],
  "cards": [
   {"kind": "story", "title": "Hvor nyttemagien lønner seg tidlig", "html":
    "<p>Akt 1 har mange dyr med noe å fortelle, blant annet en hund, flere fugler og husdyr i Emerald Grove. Speak with Animals gir ofte små sidehistorier og hint. Senere ligger det en bok som lar deg bruke Speak with Dead uten plass. Lik du finner langs veien, forteller ofte hva som skjedde.</p>"},
  ]},
 {"id": "oc-move", "title": "Hopp, dytt og kast",
  "basics": [
   "<b>Jump</b> (bonushandling): lengden avhenger av Strength. Hopp opp på kanter og tak for å nå høyt terreng eller korte ned veien.",
   "<b>Shove</b> (bonushandling): dytt fiender ned fra kanter, i vann eller i flammer. Det virker også som åpning før kamp hvis du står riktig.",
   "<b>Throw</b> (handling): kast gjenstander, tønner og drikker. En kastet helbredende drikk helbreder alle i området der den knuses. Grease Bottles og Alchemist's Fire lager overflater.",
   "<b>Miljøet:</b> eksploderende tønner, fett + ild, vann + lyn eller kulde. Utenfor kamp kan du flytte kasser for å klatre eller sperre veien.",
   "<b>Dip:</b> dypp våpenet i ild (fakler, bål) for ekstra ildskade.",
  ],
  "tips": [], "cards": []},
 {"id": "oc-dice", "title": "Lagre på nytt, eller godta terningen?",
  "basics": [
   "<b>Å laste inn igjen er helt lov</b> på Explorer og Balanced (men ikke i Honour Mode). Gjør det gjerne før valg som betyr mye for deg.",
   "<b>Godta terningen</b> når det er småting. BG3 er laget slik at mislykkede sjekker ofte åpner andre veier og morsomme situasjoner. Feil er sjelden \u00abgame over\u00bb.",
   "Et godt kompromiss: hurtiglagre før viktige samtaler, og bestem deg på forhånd om du vil godta resultatet.",
   "I innstillingene finnes <b>Karmic Dice</b>, som demper lange rekker med uflaks.",
  ],
  "tips": [], "cards": []},
 ]}

# ------------------------------------------------------------------
# 4. Generelle nybegynnertips
# ------------------------------------------------------------------
TIPS = {"id": "gtips", "nav": "Nybegynnertips", "title": "Generelle nybegynnertips",
 "summary": "20 råd som sparer deg for mye frustrasjon. Ingen historiespoilere.",
 "sections": [
 {"id": "tips-top", "title": "De 20 viktigste tipsene", "ordered": True,
  "basics": [
   "<b>Lagre ofte.</b> Hurtiglagre (F5 på PC) og lag egne lagringer før store valg. Spillet har ikke alltid et autolagringspunkt der du trenger det.",
   "<b>Ta lange hvil regelmessig.</b> Mange historiescener i leiren utløses bare ved lange hvil. Et fullt hvil koster 40 Camp Supplies på Balanced (mat og drikke i sekken).",
   "<b>Bruk korthvil</b> mellom kamper. Du har to per lange hvil. Warlocken får plassene tilbake, og flere evner lades.",
   "<b>Send mat og tunge ting til leiren.</b> Bruk «Send to Camp» og leirkisten (Traveller's Chest) så du ikke blir overlastet.",
   "<b>Ikke selg historiegjenstander.</b> Unike gjenstander og oppdragsgjenstander er ofte viktige senere. Når du er i tvil, legger du dem i leirkisten.",
   "<b>Velg riktig vanskelighetsgrad.</b> Explorer eller Balanced passer for første gjennomspilling. Du kan bytte underveis (unntatt i Honour Mode).",
   "<b>Les tooltipene.</b> De viser nøyaktig rekkevidde, redningskast, om noe krever konsentrasjon, og hvordan det lades.",
   "<b>Bruk høyt terreng og miljøet:</b> høyde (+2 på avstandsangrep), dytt fra kanter, fett + ild og tønner som eksploderer.",
   "<b>Help</b> (handling) reiser opp en falt alliert inntil deg. <i>Healing Word</i> gjør det på avstand som bonushandling.",
   "<b>Drikker er en bonushandling.</b> Kastede helbredende drikker treffer flere på en gang.",
   "<b>Alle kan bruke skrullruller,</b> også de som ikke er trollmenn. Ha Revivify-ruller i reserve.",
   "<b>Forbered formularer i leiren.</b> Cleric, druid, paladin og wizard kan bytte forberedte formularer utenfor kamp. Barder, warlocks og sorcerers velger når de går opp i nivå.",
   "<b>Withers</b> i leiren omskolerer (respec) for 100 gull og gjenoppliver falne følgesvenner for 200 gull. Det er ikke farlig å ha valgt feil.",
   "<b>Snakk med følgesvennene</b> i leiren etter store hendelser. Godkjenning (approval) åpner samtaler, oppdrag og romanser.",
   "<b>Undersøk alt.</b> Hold venstre Alt (PC) for å fremheve ting, og les bøker og brev. De gir både hint og oppdrag.",
   "<b>Snik før kamp</b> og plasser gruppa. En overraskelsesrunde kan avgjøre kampen før den begynner.",
   "<b>Turbasert modus utenfor kamp</b> (Shift+Space på PC) gjør det lettere å snike, desarmere feller og stjele med flere karakterer.",
   "<b>Hopp i stedet for å gå</b> over hindringer og opp på kanter. Det sparer tid og gir deg høyt terreng.",
   "<b>Bygg en balansert gruppe:</b> en som tåler slag, en som helbreder, en som snakker og en som gjør skade. Du kan bytte følgesvenner i leiren.",
   "<b>Ta deg tid, men følg med:</b> enkelte hendelser endrer seg når du hviler eller går videre i historien. Gjør det som haster for deg før lange hvil.",
  ],
  "tips": [
   {"cls": "bard", "text": "Som bard: les også " + L("bard-play", "Slik spiller du barden") + " og " + L("oc-boost", "Slik øker du sjansene") + "."},
  ],
  "cards": []},
 ]}

DATA["guides"] = [PARTY, OOC, TIPS]

# ------------------------------------------------------------------
# Lenker fra scenene
# ------------------------------------------------------------------
nodes = {n["id"]: n for n in DATA["nodes"]}
def add(nid, tip):
    nodes[nid]["tips"].append(tip)

add("start", {"cls": "any", "text": "Ny i BG3? Les " + L("tips-top", "De 20 viktigste tipsene") + " og " + L("oc-checks", "hvordan ferdighetssjekker regnes") + "."})
add("start", {"cls": "bard", "text": "Før første kamp: se " + L("bard-play", "Slik spiller du barden – tur for tur") + " og " + L("bard-levels", "Formularvalg nivå 1–6") + "."})
add("nautiloid", {"cls": "bard", "text": "Mer om når du bør bruke inspirasjon og når Vicious Mockery slår armbrøsten: " + L("bard-play", "tur for tur") + "."})
add("beach", {"cls": "any", "hideOrigin": "astarion", "text": "Astarion er tyv (rogue). Slik får du mest ut av ham: " + L("rogue-core", "Sneak Attack og Cunning Action") + "."})
add("crypt", {"cls": "any", "text": "Feller og låser: se " + L("oc-find", "Perception og Investigation") + " og " + L("rogue-skills", "tyvens verktøy") + "."})
add("camp", {"cls": "bard", "text": "Song of Rest + warlock: et ekstra korthvil gir warlocken alle plassene tilbake. Se " + L("wl-slots", "Pact Magic") + "."})
add("camp", {"cls": "any", "text": "Hvil, leirforsyninger og Withers: se " + L("tips-top", "nybegynnertipsene") + "."})
add("gate", {"cls": "bard", "text": "Hvem du skal kontrollere først, og hvordan du holder konsentrasjonen: " + L("bard-play", "tur for tur") + "."})
add("gate", {"cls": "any", "hideOrigin": "wyll", "text": "Wyll er warlock. Se " + L("wl-core", "Eldritch Blast og invokasjoner") + " og " + L("wl-hex", "Hex") + "."})
add("grove", {"cls": "any", "text": "Mye dialog og mange fristelser til å stjele her. Se " + L("oc-dialog", "hvem som snakker") + " og " + L("oc-stealth", "sniking og kriminalitet") + " før du forsyner deg."})
add("grove", {"cls": "bard", "text": "Før store samtaler: stable Friends + Guidance. Se " + L("oc-boost", "Slik øker du sjansene") + "."})
add("village", {"cls": "bard", "text": "Nivå 3 nærmer seg: " + L("bard-levels", "formularvalg") + " (Hold Person!) og " + L("bard-subclass", "College-valget") + "."})
add("village", {"cls": "any", "text": "Tyven får undervalg på nivå 3: se " + L("rogue-sub", "Thief, Arcane Trickster, Assassin") + "."})
add("goblincamp", {"cls": "any", "text": "Vil du snike eller snakke deg gjennom? Se " + L("rogue-stealth", "snik og skjul") + " og " + L("oc-dialog", "dialog") + "."})
add("goblincamp", {"cls": "bard", "text": "Kamp i tempelet: Hypnotic Pattern eller Sleep mot klynger, og Hold Person for tyvens kritiske treff. Se " + L("party-synergy", "samspillet") + "."})
add("onward", {"cls": "bard", "text": "Nivå 5–6 kommer ofte her: " + L("bard-levels", "nye formularer") + " og eventuelt " + L("bard-multi", "multiklasse") + "."})

# ------------------------------------------------------------------
# 5. Smarte hurtigtaster (standardoppsett PC, sjekket mot bg3.wiki «Options → Keybinds»)
# ------------------------------------------------------------------
def k(*keys):
    return ' + '.join('<kbd>%s</kbd>' % x for x in keys)

KEYS = {"id": "keys", "nav": "Smarte hurtigtaster", "title": "Smarte hurtigtaster",
 "summary": "Standardtaster på PC (Patch 8), sjekket mot tastaturoversikten på bg3.wiki. Alt kan endres under <i>Options → Keybinds</i>. Har du endret noe selv, gjelder ditt oppsett. Det som er merket <i>kan variere</i>, har jeg ikke kunnet bekrefte.",
 "sections": [
 {"id": "keys-explore", "title": "Utforsking og samhandling",
  "basics": [
   k("Venstre Alt") + " (hold): viser navn på alle gjenstander og ting du kan samhandle med i nærheten. Bruk den i hvert rom og etter hver kamp.",
   k("`") + " (tasten under Esc): fremhever personer og vesener.",
   k("Venstre Shift") + " (hold): viser synsfeltene til NPC-ene, nyttig når du sniker.",
   k("C") + ": slå sniking (Hide) av og på for den valgte karakteren. " + k("Shift", "C") + ": hele gruppa sniker.",
   k("G") + ": slå gruppemodus av og på. Da går alle sammen, eller hver for seg.",
   k("Space") + ": ta alt fra en åpen kiste eller beholder. I dialog hopper den over replikken.",
   k("Ctrl", "venstreklikk") + " (eller høyreklikk): åpner hurtigmenyen på en gjenstand eller person, med for eksempel Pickpocket, Send to Camp og Examine.",
   k("Alt", "høyreklikk") + ": ping, altså markere et punkt (mest nyttig i flerspiller).",
   "Kamera: " + k("W") + k("A") + k("S") + k("D") + " flytter, " + k("Q") + "/" + k("E") + " roterer, " + k("Page Up") + "/" + k("Page Down") + " eller musehjulet zoomer, og " + k("Home") + " sentrerer på karakteren. " + k("O") + " slår på taktisk kamera (ovenfra).",
  ], "tips": [], "cards": []},
 {"id": "keys-combat", "title": "Handlinger og kamp",
  "basics": [
   k("Z") + ": hopp. " + k("V") + ": dytt (Shove). " + k("X") + ": kast.",
   k("Space") + ": avslutt turen (trykk igjen for å angre).",
   k("Shift", "Space") + ": gå inn i eller ut av turbasert modus utenfor kamp. Samme tastekombinasjon brukes til å flykte fra kamp.",
   k("Y") + ": korthvil.",
   k("F") + ": bytt våpensett (nærkamp og avstand). " + k("R") + ": slå to våpen av og på. " + k("U") + ": trekk eller stikk bort våpenet.",
   k("Venstre Ctrl") + ": gjør klar hovedangrepet.",
   k("1") + "–" + k("0") + ", " + k("-") + " og " + k("=") + ": plass 1–12 på hurtiglinjen.",
   k("Venstre Shift") + ": slå klatring av og på.",
  ], "tips": [], "cards": []},
 {"id": "keys-panels", "title": "Menyer, vinduer og lagring",
  "basics": [
   k("F5") + ": hurtiglagre. " + k("F8") + ": hurtiglast.",
   k("I") + ": inventar og utstyr. " + k("Tab") + ": oversikt over gruppa. " + k("N") + ": karakterark. " + k("K") + ": trylleformularer.",
   k("J") + ": dagbok (journal). " + k("M") + ": kart. " + k("L") + ": reaksjoner (for eksempel å slå av en reaksjon du ikke vil bruke automatisk).",
   k("H") + ": alkymi. " + k("P") + ": inspirasjon (bakgrunnsmål). " + k("B") + ": illithid-evner.",
   k("T") + ": undersøk eller fest et tooltip. Hold " + k("Venstre Alt") + " for å utvide tooltipet med flere detaljer.",
   k("F1") + "–" + k("F4") + ": velg karakter 1–4. " + k("]") + "/" + k("[") + ": neste eller forrige karakter.",
   k("Esc") + ": avbryt eller lukk. " + k("F10") + ": skjul brukergrensesnittet (for skjermbilder).",
  ], "tips": [], "cards": []},
 {"id": "keys-tricks", "title": "Praktiske triks med mus og tastatur",
  "basics": [
   "<b>Koble fra og til gruppa:</b> dra et portrett bort fra de andre for å koble karakteren løs, og dra det tilbake for å koble til igjen. " + k("G") + " gjør det samme for hele gruppa. Koble fra barden før dialog og tyven før dirking.",
   "<b>Send til leiren:</b> høyreklikk (eller " + k("Ctrl", "klikk") + ") på en gjenstand i inventaret og velg <i>Send to Camp</i>. Det er perfekt for mat (Camp Supplies) og tunge ting.",
   "<b>Flytt ting mellom karakterer:</b> dra gjenstanden over til et annet portrett.",
   "<b>Del en bunke:</b> hold " + k("Venstre Shift") + " mens du drar den.",
   "<b>Plukk opp, flytt og kast:</b> dra gjenstander i verden med musen. " + k("X") + " kaster, og fungerer også på drikker, flasker og tønner.",
   "<b>Fest tooltips</b> med " + k("T") + " for å sammenligne utstyr, og hold " + k("Venstre Alt") + " for detaljer om redningskast og varighet.",
   "<b>Synsfelt + sniking:</b> hold " + k("Venstre Shift") + " for å se synsfeltene, " + k("Shift", "C") + " for å snike med hele gruppa, og " + k("Shift", "Space") + " for turbasert modus når timingen er viktig.",
  ], "tips": [], "cards": []},
 {"id": "keys-controller", "title": "Kontroller og Steam Deck – det viktigste",
  "basics": [
   "På kontroller (og på Steam Deck i kontrollermodus) bruker spillet <b>radialmenyer</b> i stedet for den lange hurtiglinjen. Du blar mellom hjulene og legger dine egne favoritter inn. Nøyaktig hvilke knapper som åpner og blar, <i>kan variere</i> med oppsettet. Se spillets kontrolloversikt.",
   "Bekreftet standard: <b>trykk inn høyre styrespak</b> fremhever gjenstander. <b>Y / Triangel</b> avslutter turen. <b>Hold D-pad ned</b> sniker med hele gruppa. <b>Hold høyre styrespak ned</b> gir taktisk kamera. <b>LT / L2</b> sentrerer kameraet.",
   "Under <i>Options → Gameplay → Input Mode</i> kan du låse spillet til tastatur eller kontroller hvis det hopper mellom dem.",
  ], "tips": [], "cards": []},
 {"id": "keys-settings", "title": "Nyttige innstillinger",
  "basics": [
   "<b>Karmic Dice</b> (Gameplay, på som standard): demper lange rekker med uflaks. Slå av hvis du vil ha helt tilfeldige terninger.",
   "<b>Autosave</b> og <b>antall hurtiglagringer</b> (Gameplay → Save Options): standard er 25 av hver. Øk gjerne antall hurtiglagringer, så du kan gå lenger tilbake.",
   "<b>Dynamic Combat Camera</b>: kameraet følger den som har tur. Slå av hvis det blir urolig. <b>Edge Panning</b>: flytt kameraet med musen mot skjermkanten.",
   "<b>Autoselect character after combat</b>: velg om hovedpersonen eller sist valgte karakter skal være aktiv etter kamp.",
   "<b>Vis alt bytte:</b> det finnes ingen fast innstilling som jeg har kunnet bekrefte. Bruk " + k("Venstre Alt") + " (hold) for å vise alle gjenstander.",
   "<b>Tooltips og kamplogg:</b> plassering og forsinkelse <i>kan variere</i> mellom versjoner. Se under <i>Interface</i>. Kamploggen er nyttig for å se hvorfor et angrep bommet.",
   "<b>Pause:</b> BG3 har ingen automatisk pause i sanntid. Bruk turbasert modus (" + k("Shift", "Space") + ") når du trenger ro, for eksempel ved feller og sniking.",
  ], "tips": [], "cards": []},
 ]}

# ------------------------------------------------------------------
# 6. Skjulte ting tidlig – god start (plasseringer bak «loot»-spoilere)
# ------------------------------------------------------------------
def loot(hint, name, html):
    return {"kind": "loot", "hint": hint, "title": name, "html": html}

LOOT = {"id": "loot", "nav": "Skjulte ting tidlig", "title": "Skjulte ting tidlig – god start",
 "summary": "13 tidlige funn i akt 1 som gjør starten lettere, valgt for en gruppe med bard, tyv og warlock. Hintet er alltid synlig, mens nøyaktig sted og fremgangsmåte ligger bak spoilerbryteren «Vis plassering av funn» (eller «Vis denne» på hvert kort). Sted og innhold er sjekket mot bg3.wiki.",
 "sections": [
 {"id": "loot-start", "title": "Nautiloiden og krasjstedet",
  "basics": ["Se deg grundig rundt før du forlater nautiloiden. Du kan ikke vende tilbake.", "Ved krasjstedet er det verdt å klatre: flere ting ligger på avsatser du må hoppe opp til (" + k("Z") + ")."],
  "tips": [], "cards": [
   loot("Et tidlig magisk tohåndssverd ombord på nautiloiden – vanskelig å få tak i", "Everburn Blade",
    "<p>Båret av <b>Commander Zhalk</b> ved roret (the Helm). Du må beseire ham, eller få ham til å slippe sverdet med <i>Command: Drop</i> (han klarer ofte redningskastet). Kampen er farlig på nivå 1, og du trenger ikke å kjempe den. Sverdet passer best for en frontkjemper (Lae'zel eller Karlach), ikke for gruppa di. Lagre før du prøver.</p>"),
   loot("En amulett som gir hele gruppa bedre ferdighetssjekker – høyt oppe sørvest for druidelunden", "Silver Pendant",
    "<p>Ligger på et skjelett ved <b>Harper-utposten</b> (Ravaged Beach, ca. X 152 / Y 366), sørvest for Emerald Grove. Du må hoppe opp to små avsatser og klatre opp en trestige. Amuletten gir <i>Guidance</i> (+1d4 på evnesjekker) ubegrenset. Gi den til en som ikke har Guidance selv, så gruppa alltid har den.</p>"),
   loot("Gravde skatter langs stranda og ved ruinene", "Begravde kister (Ravaged Beach)",
    "<p>bg3.wiki oppgir begravde kister på Ravaged Beach (blant annet rundt X 202 / Y 386, X 289 / Y 310 og X 303 / Y 337), og to ved Overgrown Ruins. Du finner jordhaugene med Perception eller Survival, og trenger som regel en <b>spade (Shovel)</b> i sekken for å grave. Innholdet er tilfeldig. Koordinatene er omtrentlige.</p>"),
  ]},
 {"id": "loot-crypt", "title": "Overgrown Ruins og Dank Crypt",
  "basics": ["Krypten har feller, så la tyven gå først. Se " + L("oc-find", "feller og skjulte ting") + "."],
  "tips": [], "cards": [
   loot("En amulett for å snakke med de døde – i et skjult rom i krypten", "The Amulet of Lost Voices",
    "<p>Ligger i en <b>heavy chest</b> i det skjulte rommet der <b>Withers</b> ligger (Dank Crypt, ca. X −290 / Y −235). Rommet åpnes med en knapp på sideveggen bak den store skjelettstatuen (Jergal). Pass på: knappen vekker skjelettene i rommet, så plasser gruppa først. Amuletten gir <i>Speak with Dead</i> én gang per lange hvil.</p>"),
  ]},
 {"id": "loot-grove", "title": "Emerald Grove",
  "basics": ["Lunden har både skjulte kister og oppdrag med gode belønninger. Lagre før du gjør noe ulovlig."],
  "tips": [], "cards": [
   loot("En bard-hatt i en låst kiste, gjemt ved det hellige bassenget", "Cap of Curing",
    "<p>I en <b>låst forgylt kiste bak en søyle</b> ved Sacred Pool, der tiefling-barden Alfira sitter og skriver sangen sin (ca. X 289 / Y 488). Dirk låsen med tyven. Når barden gir Bardic Inspiration, helbreder målet også 1d6.</p>"),
   loot("En sterk tidlig ring (AC og redningskast) som belønning i lunden", "Ring of Protection",
    "<p>Belønning fra <b>Mol</b> i Tiefling Hideout for oppdraget <i>Steal the Sacred Idol</i>. +1 AC og +1 på alle redningskast. Oppdraget handler om å stjele noe i lunden, så det kan få følger hvis du blir sett. Lagre først og les " + L("oc-stealth", "sniking og kriminalitet") + ".</p>"),
  ]},
 {"id": "loot-village", "title": "Blighted Village",
  "basics": ["Landsbyen er full av goblins som vakter. Se " + L("rogue-stealth", "snik og skjul") + " og " + L("oc-dialog", "dialog") + " (barden har et eget [BARD]-valg ved sørporten)."],
  "tips": [], "cards": [
   loot("En hjelm som gir ekstra fart i starten av hver kamp – i en mosegrodd kiste midt i landsbyen", "Haste Helm",
    "<p>I en <b>Moss-Covered Chest</b> ved en vogn midt i landsbyen, like ved waypointet (ca. X 29 / Y 405). Nøkkelen (<i>Moss-Covered Key</i>) bæres av en goblin (Goblin Booyahg) på taket av apoteket, men du kan også dirke kisten. Hjelmen gir <i>Momentum</i> (mer bevegelse) de første rundene av hver kamp.</p>"),
   loot("En hel stabel med dirkeverktøy og fellesett – i en kjeller i landsbyen", "Thieves' Tools og Trap Disarm Toolkits",
    "<p>I smiekjelleren (<b>Blacksmith's Forge</b>) under smia nord for østporten. Gå ned gjennom de låste dørene med <i>Old Key</i> (ligger på en kasse i smia), eller ødelegg nettet over hullet i gulvet og hopp ned. Kasser og skap der inneholder minst 6 sett Thieves' Tools og/eller Trap Disarm Toolkits. Det er nok til tyven en god stund.</p>"),
  ]},
 {"id": "loot-road", "title": "Risen Road, Waukeen's Rest og Owlbear-hulen",
  "basics": ["Disse ligger litt lenger unna. Ta dem når gruppa er nivå 2–4."],
  "tips": [], "cards": [
   loot("En ring for tyven (Stealth og Sleight of Hand) – skjult langs elva ved en ødelagt bro", "Smuggler's Ring",
    "<p>På et skjelett gjemt i en busk på den nedre stien langs elva, ved den ødelagte delen av broen på <b>Risen Road</b> (ca. X 58 / Y 516). Den gir +2 Stealth og +2 Sleight of Hand, men −1 Charisma. Gi den til tyven, ikke barden.</p>"),
   loot("Hansker med fordel på dirking – solgt av en lyssky handler etter et oppdrag", "Gloves of Thievery",
    "<p>Selges av <b>Brem</b> i Zhentarim-kjelleren (Zhentarim Basement) under Waukeen's Rest etter oppdraget <i>Find the Missing Shipment</i>. De gir <b>fordel</b> på Sleight of Hand-sjekker (låser, feller og lommetyveri).</p>"),
   loot("En stav som lader formularene med lyn – belønning for en redning ved et brennende vertshus", "The Spellsparkler",
    "<p>Belønning fra <b>Counsellor Florrick</b> når du redder henne fra det brennende vertshuset ved <b>Waukeen's Rest</b> (oppdraget <i>Rescue the Grand Duke</i>). Skade med formularer gir Lightning Charges. Sterk for warlocken (Eldritch Blast) eller barden.</p>"),
   loot("En amulett som beskytter mot motangrep når du er skadet – i en farlig hule", "Moondrop Pendant",
    "<p>I en <b>Selûnite gilded chest</b> i <b>Owlbear Nest</b> (ca. X −321 / Y −135). Les bønnearket (<i>Selûnite Prayer Sheet</i>) foran kisten for å åpne den. Arket ligger bak Selûne-statuen og krever en Perception-sjekk. Hulen har en farlig owlbear, så vent til nivå 3–4 eller snik deg inn. Med 50 % HP eller mindre utløser du ikke motangrep (Attacks of Opportunity). Perfekt for tyven.</p>"),
  ]},
 {"id": "loot-goblin", "title": "Goblinleiren",
  "basics": ["Handelsfolk i goblinleiren selger god utrustning, også om du kommer fredelig."],
  "tips": [], "cards": [
   loot("En god tidlig bue med bonus på initiativ – til salgs inne i goblinenes tempel", "Bow of Awareness",
    "<p>Selges av <b>Roah Moonglow</b>, til venstre rett innenfor inngangen til <b>Shattered Sanctum</b> (ca. X 272 / Y −31). +1 kortbue med +1 på initiativ og <i>Hamstring Shot</i> (halverer farten til målet). God for tyven, siden en tidlig tur gir flere Sneak Attack-muligheter.</p>"),
  ]},
 ]}

DATA["guides"].insert(0, KEYS)
DATA["guides"].append(LOOT)
# hurtigtaster og funn gjør nybegynnertipsene mer konkrete
nodes["nautiloid"]["tips"].append({"cls": "any", "text": "Første gang med tastatur? Se " + L("keys-explore", "Smarte hurtigtaster") + ": hold " + k("Venstre Alt") + " for å se alt du kan plukke opp."})
nodes["beach"]["tips"].append({"cls": "any", "text": "Gode tidlige funn her i nærheten: se " + L("loot-start", "Skjulte ting tidlig") + "."})
nodes["crypt"]["tips"].append({"cls": "any", "text": "En nyttig amulett i krypten: se " + L("loot-crypt", "Skjulte ting tidlig") + "."})
nodes["grove"]["tips"].append({"cls": "bard", "text": "Bard-hatten og en sterk ring: se " + L("loot-grove", "Skjulte ting tidlig") + "."})
nodes["village"]["tips"].append({"cls": "any", "text": "Hjelm og dirkeverktøy i landsbyen: se " + L("loot-village", "Skjulte ting tidlig") + "."})

# ------------------------------------------------------------------
# 7. Skjematiske kart (ingen spillkart-bilder; nåler peker til avsnitt)
# ------------------------------------------------------------------
def pin(x, y, label, href, spoiler=None, card=None, pro=None):
    p = {"x": x, "y": y, "label": label, "href": href}
    if spoiler:
        p["spoiler"] = spoiler
    if card:
        p["card"] = card
    if pro:
        p["pro"] = pro
    return p

DATA["maps"] = {
 "title": "Akt 1 – skjematiske kart",
 "summary": "Kartene viser omtrent hvordan områdene ligger i forhold til hverandre, ikke avstander eller form. Nåler hopper til riktig avsnitt. Funn, historie og Dark Urge tegnes bare når den tilhørende spoilerbryteren er på. Under hvert kart er den samme lista, så det fungerer uten å zoome.",
 "links": [
  {"href": "https://bg3.wiki/wiki/Wilderness", "label": "Wilderness på bg3.wiki"},
  {"href": "https://mapgenie.io/baldurs-gate-3", "label": "Interaktivt kart (lenken bg3.wiki bruker)"},
 ],
 "areas": [
  {"id": "map-nautiloid", "title": "Nautiloiden",
   "blurb": "Prologen går bare én vei: fra kapselen, forbi operasjon og impekamp, til roret. Du kan ikke vende tilbake etter krasjet.",
   "links": [{"href": "https://bg3.wiki/wiki/Nautiloid", "label": "Nautiloid på bg3.wiki"}],
   "pins": [
    pin(16, 52, "Startkapselen", "nautiloid"),
    pin(38, 50, "Lae'zel og impekampen", "nautiloid"),
    pin(68, 48, "Shadowhearts kapsel", "nautiloid"),
    pin(86, 50, "Roret (the Helm)", "nautiloid"),
    pin(86, 68, "Everburn Blade", "loot-start", "loot", "loot-start:0"),
   ]},
  {"id": "map-beach", "title": "Krasjstedet (Ravaged Beach)",
   "blurb": "Vraket ligger ved elva. Følgesvennene står spredt mellom stranda og klippene mot lunden. Kapellruinene er i nærheten.",
   "links": [{"href": "https://bg3.wiki/wiki/Ravaged_Beach", "label": "Ravaged Beach på bg3.wiki"}],
   "pins": [
    pin(28, 54, "Vraket", "beach"),
    pin(18, 64, "Shadowheart ved vraket", "beach"),
    pin(42, 66, "Astarion", "beach"),
    pin(52, 30, "Gale ved waypointet (Roadside Cliffs)", "beach"),
    pin(74, 26, "Lae'zel i buret", "beach"),
    pin(12, 28, "Silver Pendant (Harper-utposten)", "loot-start", "loot", "loot-start:1"),
    pin(48, 78, "Begravde kister", "loot-start", "loot", "loot-start:2"),
   ]},
  {"id": "map-crypt", "title": "Overgrown Ruins og Dank Crypt",
   "blurb": "Kapellet ligger over bakken. Trappa går ned i krypten, med feller på veien og Withers innerst.",
   "links": [
    {"href": "https://bg3.wiki/wiki/Overgrown_Ruins", "label": "Overgrown Ruins på bg3.wiki"},
    {"href": "https://bg3.wiki/wiki/Dank_Crypt", "label": "Dank Crypt på bg3.wiki"},
   ],
   "pins": [
    pin(30, 28, "Kapellporten", "crypt"),
    pin(28, 74, "Feller i krypten", "crypt"),
    pin(75, 76, "Withers / Jergal-statuen", "crypt"),
    pin(75, 64, "The Amulet of Lost Voices", "loot-crypt", "loot", "loot-crypt:0"),
   ]},
  {"id": "map-grove", "title": "Druidelunden (Emerald Grove)",
   "blurb": "Porten er inngangen. Inne ligger The Hollow, det hellige bassenget og druidenes indre område.",
   "links": [{"href": "https://bg3.wiki/wiki/Emerald_Grove", "label": "Emerald Grove på bg3.wiki"}],
   "pins": [
    pin(50, 90, "Kampen ved porten", "gate"),
    pin(42, 72, "Zevlor", "gate"),
    pin(64, 74, "Wyll", "gate"),
    pin(38, 54, "The Hollow og handelsfolk", "grove"),
    pin(76, 30, "Kagha og Arabella", "grove"),
    pin(50, 28, "Alfira ved Sacred Pool", "grove"),
    pin(60, 18, "Cap of Curing", "loot-grove", "loot", "loot-grove:0"),
    pin(16, 56, "Ring of Protection (Tiefling Hideout)", "loot-grove", "loot", "loot-grove:1"),
    pin(64, 14, "Alfira senere i historien", "grove", "story", "grove:0", "notdu"),
   ]},
  {"id": "map-village", "title": "Blighted Village",
   "blurb": "En liten landsby med sørport, vindmølle og smie. Goblinleiren ligger videre vest.",
   "links": [{"href": "https://bg3.wiki/wiki/Blighted_Village", "label": "Blighted Village på bg3.wiki"}],
   "pins": [
    pin(46, 84, "Sørporten", "village"),
    pin(75, 42, "Vindmøllen og Barcus", "village"),
    pin(46, 50, "Haste Helm", "loot-village", "loot", "loot-village:0"),
    pin(30, 30, "Smia og dirkeverktøy", "loot-village", "loot", "loot-village:1"),
   ]},
  {"id": "map-goblin", "title": "Goblinleiren og Shattered Sanctum",
   "blurb": "Ytre leir, så broen inn til tempelet der de tre lederne holder til.",
   "links": [
    {"href": "https://bg3.wiki/wiki/Goblin_Camp", "label": "Goblin Camp på bg3.wiki"},
    {"href": "https://bg3.wiki/wiki/Shattered_Sanctum", "label": "Shattered Sanctum på bg3.wiki"},
   ],
   "pins": [
    pin(18, 58, "Vaktene ved porten", "goblincamp"),
    pin(28, 36, "Volo", "goblincamp"),
    pin(50, 50, "Inngangen til tempelet", "goblincamp"),
    pin(86, 38, "Priestess Gut", "goblincamp"),
    pin(86, 58, "Dror Ragzlin", "goblincamp"),
    pin(78, 74, "Minthara", "goblincamp"),
    pin(62, 20, "Bow of Awareness (Roah Moonglow)", "loot-goblin", "loot", "loot-goblin:0"),
    pin(24, 80, "Valget: lunden eller goblinene", "goblincamp", "story", "goblincamp:0"),
   ]},
  {"id": "map-overview", "title": "Veien ut av akt 1",
   "blurb": "Slik henger områdene sammen. Underdark og fjellpasset er de to veiene videre mot akt 2. Pilene er omtrentlige.",
   "links": [
    {"href": "https://bg3.wiki/wiki/Wilderness", "label": "Wilderness på bg3.wiki"},
    {"href": "https://bg3.wiki/wiki/Underdark", "label": "Underdark på bg3.wiki"},
    {"href": "https://bg3.wiki/wiki/Mountain_Pass", "label": "Mountain Pass på bg3.wiki"},
   ],
   "pins": [
    pin(5, 8, "Nautiloiden", "nautiloid"),
    pin(5, 31, "Krasjstedet", "beach"),
    pin(5, 59, "Overgrown Ruins", "crypt"),
    pin(40, 31, "Emerald Grove", "grove"),
    pin(40, 8, "Risen Road og Waukeen's Rest", "loot-road"),
    pin(40, 59, "Blighted Village", "village"),
    pin(76, 59, "Goblinleiren", "goblincamp"),
    pin(76, 8, "Fjellpasset (mot akt 2)", "onward"),
    pin(54, 82, "Underdark (mot akt 2)", "onward"),
    pin(58, 26, "Smuggler's Ring", "loot-road", "loot", "loot-road:0"),
    pin(66, 26, "Gloves of Thievery", "loot-road", "loot", "loot-road:1"),
    pin(74, 28, "The Spellsparkler", "loot-road", "loot", "loot-road:2"),
    pin(48, 52, "Moondrop Pendant (Owlbear-hulen)", "loot-road", "loot", "loot-road:3"),
   ]},
 ],
}
