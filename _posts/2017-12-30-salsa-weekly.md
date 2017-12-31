---
layout: post
title: "The SALSA Weekly: 12/30"
author: The SALSAzens
---

Welcome to [The SALSA Weekly](/weekly)! Last one of the year! The SALSA Weekly is a curated playlist/post on the blog, wherein members of SALSA will submit one song they have been digging the past week and why.

<style>
iframe { margin: 0 auto; display: block; width: 100%; }
</style>

## The List

For your listening pleasure, here are our picks in one handy dandy [Spotify
playlist](https://open.spotify.com/user/drabmakyo/playlist/1GNXcXuCKGpps5IUP3Y6Lg). Scroll down for what we have to say!

<iframe
src="https://open.spotify.com/embed/user/drabmakyo/playlist/1GNXcXuCKGpps5IUP3Y6Lg" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>

-----

{% for entry in site.data.weekly-2017-12-30 %}
## {{ entry["Name"] }}: [*{{ entry["Artist - Song Title"]|replace: "-", "---"|markdown }}*]({{ entry["Link"] }})

{{ entry["Why you dig it (HTML and Markdown okay)"]|markdown }}

<small>Found on: <em>{{ entry["Where to find it"] }}</em></small>
{% endfor %}
