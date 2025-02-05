# Teachable Machine Leaderboard

This page displays the most recent leaderboard for the students.

## Leaderboard

<table>
  <thead>
    <tr>
      <th>Pseudonym</th>
      <th>Accuracy</th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.leaderboard %}
    <tr>
      <td>{{ row.pseudonym }}</td>
      <td>{{ row.accuracy }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>