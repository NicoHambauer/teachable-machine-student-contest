# Teachable Machine Leaderboard

This page displays the most recent leaderboard for the students.

## Leaderboard

| Pseudonym | Accuracy |
|-----------|----------|
{% for row in site.data.leaderboard %}
| {{ row.pseudonym }} | {{ row.accuracy }} |
{% endfor %}