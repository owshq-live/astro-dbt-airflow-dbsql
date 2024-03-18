{% macro gen_id() %}
CAST(FLOOR(random() * (10000 - 1 + 1)) + 1 AS INTEGER)
{% endmacro %}