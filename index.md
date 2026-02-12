# KI-Challenge der FIDS

**Willkommen zum KI-Wettbewerb** der Fakultät für Informatik & Data Science (FIDS) der Universität Regensburg (UR). <br>
**Datum:** 13. Februar 2026 <br>
**Zeitraum der FIDS-KI-Challenge:** 9:00 - 13:00 Uhr <br>
**Ort:** Stand 50 - Information Systems / Wirtschaftsinformatik B.Sc. / B.A. <br>

**Preisverleihung:** Der Preis wird um **13:15 Uhr** an den **ersten Platz** im Leaderboard vergeben.

<link rel="stylesheet" type="text/css" href="style.css">

## Leaderboard

<table>
  <thead>
    <tr>
      <th>Platz</th>
      <th>Pseudonym</th>
      <th>Genauigkeit</th>
    </tr>
  </thead>
  <tbody>
    {% assign sorted_leaderboard = site.data.leaderboard | sort: 'accuracy' | reverse %}
    {% for row in sorted_leaderboard %}
    <tr class="{% if forloop.first %}first-place{% endif %}">
      <td>{{ forloop.index }}</td>
      <td>{{ row.pseudonym }}</td>
      <td>{{ row.accuracy }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Wie kannst du teilnehmen?

**Merk dir dein Pseudonym**, um später zu sehen, ob du gewonnen hast!

## Wie funktioniert die KI-Challenge?

Trainiere dein eigenes KI-Modell, und finde heraus, wie genau es ist! 
Nimm dazu Bilder von vier verschiedenen Gegenständen an unserem Stand auf und trainiere dein Modell mit diesen Bildern. 


## Was kannst du gewinnen?

Die Person mit der besten Genauigkeit erhält einen 20€ Gutschein.

## Welche Vorkenntnisse benötige ich?

Es ist ganz einfach und für die Teilnahme benötigst du keine Vorkenntnisse in KI oder Programmierung.

## Was verstehe Ich unter Genauigkeit?

Wir haben ungefähr 1000 Test-Bilder selbst aufgenommen.
Deine Genauigkeit wird berechnet, indem die Anzahl der korrekt klassifizierten Bilder durch die Gesamtzahl der Test-Bilder geteilt wird.

Eine Genauigkeit von 50% bedeutet, dass dein Modell 500 von 1000 Test-Bildern korrekt klassifiziert hat.

## Was sagt meine Genauigkeit aus?

Die Genauigkeit deines Modells ist in folgenden Bereichen zu verorten:
- **< 40%**: Gut gemacht! Du hast die Grundlagen der KI verstanden.
- **40% - 50%**: Sehr gut! Du hast ein solides Verständnis für KI-Modelle.
- **50% - 65%**: Hervorragend! Du bist ein echter KI-Enthusiast.
- **> 65%**: Fantastisch! Du bist ein KI-Profi!

## Wie finde Ich weitere Stände auf dem Regensburger Hochschultag?

[Übersicht der Stände und Stand Information Systems / Wirtschaftsinformatik (Seite 8)](https://www.regensburger-hochschultag.de/wp-content/uploads/2026/01/RHT_2026_Programmheft_Web.pdf)


Wir hoffen, dass du Spaß an unserer Challenge hattest und freuen uns, dich an der FIDS für ein Studium begrüßen zu dürfen.