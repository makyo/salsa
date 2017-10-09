---
layout: default
title: SALSA Weeklies
---

The SALSA Weekly is a weekly curated playlist/post on the SALSA blog, wherein members of SALSA will submit one song they have been digging the past week, and a sentence or two as to why.

## What Sort of Posts Will These Be?

Makyo and Lu will be curating both a post on the SALSA blog with our brief descriptions, and a playlist on Spotify.

## Does the Song Need to Be a New Release?

Heck no! Any song you’ve been really enjoying during the week counts. And hey, if there’s nothing that’s jumped out at you during the week, just submit an old favourite of yours, too. We won’t know!

## Does My Song Need to Be on Spotify?

Heck no! It’s just the easiest place to make a playlist, and if it does exist on Spotify, at least we can share it that way. But if it’s a Bandcamp, SoundCloud, or artist website exclusive, the website blog post will be for embedding those links as well.

## Okay, I’m Game. What Are the Parameters?

Follow this handy guide:

* [Be a SALSAzen](/about)
* The name you want to submit under (including a Twitter handle, if you so choose).
* Song and artist name.
* One to two sentences of why you’ve been digging it.
* Where it can be found (just the name of the website/streaming service. NB: this should be [as silly as possible](/dorks))
* A link to the song so Makyo and I know what we’re looking for.

## When Is This Due?

Starting on Thursdays, we’ll pin this submission spreadsheet to the Telegram chat so that people can submit their songs. We are aiming to have the blog and playlist updated every Sunday, so we need submissions by a nebulous "in the evening on Saturday". We decided on the soft deadline of 10:00 EST, but if you get your submission to us a little after, that’s also okay. The cut-off is more for Makyo and Lu’s sanity than anything else.

## How Will the Spotify Playlist Be Organized?

Randomly, every week. Lu will put everyone’s submissions into a highly scientific randomizer and put the playlist together that way. No one gets favoritism here--we’re all submitting equally cool music.

## Do You Have Any Candy?

Yeah but just Dum-Dums. Sorry, kid.

## List of weekly songs so far

{% for salsazen in site.data.weeklyify %}
### {{ salsazen[0] }}

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
