---
layout: post
title: "The SALSA Weekly: 6/23"
author: The SALSAzens
---

Welcome to [The *final* SALSA Weekly](/weekly)! The SALSA Weekly is a curated playlist/post on the blog, wherein members of SALSA will submit one song they have been digging the past week and why. This week, we picked songs to answer a question: **What's a song that you feel is almost somehow written about you?**

After this, we'll probably do something different :D

<style>
iframe { margin: 0 auto; display: block; width: 100%; }
</style>

## The List

For your listening pleasure, here are our picks in one handy dandy [Spotify
playlist](https://open.spotify.com/playlist/7twz7PT7RnuqthQq0OSTj8?si=I3s5E3A1RuaSXiwCKOGc2w). Scroll down for what we have to say!

<iframe
src="https://open.spotify.com/embed/user/drabmakyo/playlist/7twz7PT7RnuqthQq0OSTj8" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>

-----

{% for entry in site.data.weekly-2019-06-23 %}
## {{ entry["Name"] }}: [*{{ entry["Artist - Song Title"]|replace: "-", "---"|markdown }}*]({{ entry["Link"] }})

{{ entry["Why you dig it (HTML and Markdown okay)"]|markdown }}

<small>Found on: <em>{{ entry["Where to find it"] }}</em></small>
{% endfor %}
