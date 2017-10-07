---
layout: default
title: SALSA Weeklies
---

{% for salsazen in site.data.weeklyify %}
## {{ salsazen[0] }}

{% for song in salsazen[1] %}
* {{ song }}{% endfor %}
{% endfor %}

{% comment %}
Good lord, I wish this worked...

{% assign all = "" %}
{% assign seen = "" %}
{% for weekly in site.data %}
    {% for entry in weekly[1] %}
        {% assign seen_entries = seen | split: "%%" %}
        {% assign entry_seen = false %}
        {% for seen_entry in seen_entries %}
            {% if entry.Name == seen_entry %}
                {% assign entry_seen = true %}
            {% endif %}
        {% endfor %}
        {% if seen_entry == false %}
            {% capture all %}{{ all }}%%{{ entry.Name }}?%?{% endcapture %}
            {% capture seen %}{{ seen }}%%{{ entry.Name }}{% endcapture %}
        {% endif %}
        {% assign existing = all | split: "%%" %}
        {% for existing_entry in existing %}
            {% assign parts = existing_entry | split: "?%?" %}
            {% if parts[0] == entry.Name %}
                {% capture existing_entry %}{{ existing_entry }}|{{ entry["Artist - Song Title"] }}{% endcapture %}
            {% endif %}
            {% capture new %}{{ new }}%%{{ existing_entry }}{% endcapture %}
        {% endfor %}
        {% capture all %}{{ new }}{% endcapture %}
        {{ all }}
    {% endfor %}
{% endfor %}

{% assign salsazens = all | split: "%%" %}
{% for salsazen in salsazens %}
{% assign parts = salsazen | split: "?%?" %}
## {{ parts [0] }}
{% assign entries = parts[1] | split: "|" %}
{% for entry in entries %}
* {{ entry }}
{% endfor %}
{% endfor %}
{% endcomment %}
