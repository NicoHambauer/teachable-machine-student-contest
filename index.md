# KI-Challenge der FIDS

**Willkommen zur KI-Challenge** der Fakultät für Informatik & Data Science (FIDS) der Universität Regensburg.

Hier kannst du ganz einfach dein eigenes KI-Modell für die Klassifikation von Bildern entwerfen!

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