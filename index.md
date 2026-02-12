# KI-Challenge der FIDS

**Willkommen zum KI-Wettbewerb** der Fakultät für Informatik & Data Science (FIDS) der Universität Regensburg (UR).

Trainiere dein eigenes KI-Modell, und finde heraus, wie genau es ist! Die Person mit der besten Genauigkeit erhält einen 20€ Gutschein.
Nimm dazu Bilder von vier verschiedenen Gegenständen an unserem Stand auf und trainiere dein Modell mit diesen Bildern. 
Es ist ganz einfach und für die Teilnahme benötigst du keine Vorkenntnisse in KI oder Programmierung.

**Datum:** 13. Februar 2026  
**Zeit:** 8:30 - 14:00 Uhr

**Zeitraum der FIDS-KI-Challenge:** 9:00 - 12:30 Uhr
**Ort:** Stand 50 - Information Systems / Wirtschaftsinformatik B.Sc. / B.A. 

**Preisverleihung:** 12:30 Uhr. Der Preis (20€ Gutschein) wird an den **ersten Platz** im Leaderboard vergeben ([Link zum Leaderboard](https://nicohambauer.github.io/teachable-machine-student-contest/))

[Übersicht der Stände und Stand Information Systems / Wirtschaftsinformatik (Seite 8)](https://www.regensburger-hochschultag.de/wp-content/uploads/2026/01/RHT_2026_Programmheft_Web.pdf)

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

**Merk dir dein Pseudonym**, um später zu sehen, ob du gewonnen hast!  

Die Genauigkeit deines Modells ist in folgenden Bereichen zu verorten:
- **< 40%**: Gut gemacht! Du hast die Grundlagen der KI verstanden.
- **40% - 50%**: Sehr gut! Du hast ein solides Verständnis für KI-Modelle.
- **50% - 65%**: Hervorragend! Du bist ein echter KI-Enthusiast.
- **> 65%**: Fantastisch! Du bist ein KI-Profi!

Wir hoffen, dass du Spaß an unserer Challenge hattest und freuen uns, dich an der FIDS für ein Studium begrüßen zu dürfen.