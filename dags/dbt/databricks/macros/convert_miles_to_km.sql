{% macro convert_miles_to_km(miles) %}
{{ return(miles | float * 1.60934) }}
{% endmacro %}