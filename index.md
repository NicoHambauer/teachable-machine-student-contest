# KI-Challenge der FIDS

Dieser Wettbewerb findet am 14. Februar 2025 während der Regensburger Hochschultage statt. Die Fakultät Informatik und Datascience (FIDS) veranstaltet diesen Wettbewerb. Die Studierenden sollten um 11:50 Uhr wieder am Stand 52 sein, um den Preis von 20€ Amazon-Gutschein zu gewinnen. Der Preis geht an die Person, die als Erste oder Beste um 11:50 Uhr wieder am Stand 52 erscheint.

<link rel="stylesheet" type="text/css" href="styles.css">

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