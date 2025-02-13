# KI-Challenge der FIDS

**Willkommen zum KI-Wettbewerb** der Fakultät für Informatik & Data Science (FIDS) der Universität Regensburg.

**Datum:** 14. Februar 2025  
**Zeit:** 9:00 - 11:50 Uhr  
**Ort:** Stand 52

**Preisverleihung:** 11:50 Uhr für die beste Teilnehmerin / den besten Teilnehmer.

[Übersicht der Stände (Seite 7 von 11)](https://www.regensburger-hochschultag.de/wp-content/uploads/2025/01/RHT_2025_Programmheft_Web.pdf)

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
Wir hoffen, dass du Spaß an unserer Challenge hattest und freuen uns, dich an der FIDS für ein Studium begrüßen zu dürfen.

**Hinweis:** Der Wettbewerb endet um 11:50 Uhr, um eine einfachere Abreise zu ermöglichen. Der / Die beste zu diesem Zeitpunkt wird den Preis erhalten.