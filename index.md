# KI-Challenge der FIDS

Willkommen zum KI-Wettbewerb der Fakultät für Informatik & Data Science (FIDS) der Universität Regensburg.

Die Challenge findet am 14. Februar 2025 von 9:00 bis 11:50 Uhr am Stand 52 statt.
Die beste Teilnehmerin / der beste Teilnehmer erhält den Preis um 11:50 Uhr.

[Hier findet ihr eine Übersicht der Stände auf Seite 12](https://www.regensburger-hochschultag.de/wp-content/uploads/2025/01/RHT_2025_Programmheft_Web.pdf)

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

Wir freuen uns, dass du dein eigenes Modell für die KI-Challenge der FIDS erstellt hast!
Merk dir dein Pseudonym, um später zu sehen, ob du gewonnen hast!
Wir hoffen, dass du Spaß an unserer Challenge hattest und freuen uns dich an der FIDS für ein Studium begrüßen zu dürfen.

P.s.: Damit ihr genügend Zeit habt und eine einfachere Abreise von der Uni ermöglicht wird, werden wir um 11:50 Uhr den Wettbewerb beenden. Der / Die beste zu diesem Zeitpunkt wird den Preis erhalten.