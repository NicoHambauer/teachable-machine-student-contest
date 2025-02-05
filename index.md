# KI-Challenge der FIDS

Dieser Wettbewerb findet am 14. Februar 2025 während der Regensburger Hochschultage statt. Die Fakultät Informatik und Datascience (FIDS) veranstaltet diesen Wettbewerb. Die Studierenden sollten um 11:50 Uhr wieder am Stand 52 sein, um den Preis von 20€ Amazon-Gutschein zu gewinnen.

## Leaderboard

<table>
  <thead>
    <tr>
      <th>Pseudonym</th>
      <th>Genauigkeit</th>
    </tr>
  </thead>
  <tbody>
    {% assign sorted_leaderboard = site.data.leaderboard | sort: 'accuracy' | reverse %}
    {% for row in sorted_leaderboard %}
    <tr>
      <td>{{ row.pseudonym }}</td>
      <td>{{ row.accuracy }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>