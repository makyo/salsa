---
layout: post
title: "The SALSA Weekly: 9/17"
author: The SALSAzens
---

Welcome to [The SALSA Weekly](/weekly)! The SALSA Weekly is a curated playlist/post on the blog, wherein members of SALSA will submit one song they have been digging the past week and why.

<style>
iframe { margin: 0 auto; display: block; width: 100%; }
</style>

## The List

For your listening pleasure, here are our picks in one handy dandy [Spotify playlist](https://open.spotify.com/user/drabmakyo/playlist/3qDJnA9iVWHWMHBzHRRRk3). Scroll down for what we have to say!

<iframe src="https://open.spotify.com/embed/user/drabmakyo/playlist/3qDJnA9iVWHWMHBzHRRRk3" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>

-----

{% for entry in site.data.weekly-2017-09-17 %}
## {{ entry["Name"] }}: [*{{ entry["Artist - Song Title"]|replace: "-", "---"|markdown }}*]({{ entry["Link just in case"] }})

{{ entry["Why you dig it (HTML and Markdown okay)"]|markdown }}

<small>Found on: <em>{{ entry["Where to find it"] }}</em></small>
{% endfor %}
