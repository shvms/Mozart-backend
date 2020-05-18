# REST backend for multi-streaming-platform playlist sharing app.
The idea is for a platform where users can post their favourite songs from
different streaming platforms under their main playlist. The backend
keeps track of the songs by unique track URI (provided by streaming
platform) & the streaming platform itself (currently supported &mdash;
Spotify, SoundCloud).

## Stack
**Django** used coupled with **Django-REST-Framework**. Authentication is
provided via JSONWebToken mechanism. Uses *django-activity-stream* for generating
user feeds.

## Features
* User registration via `api/auth/register/` endpoint.
* Login via `api/auth/login/` endpoint.
* JWT token refresh via `api/auth/login/refresh/` endpoint.
* User info and songs in the playlist is publicly available via relevant endpoints.
* User info page & playlist page is cached as it remains static for longer time but accessed frequently.
* Users can follow/unfollow each other via simple endpoints.
* Private endpoints to view followers/following list.
* Feed endpoint to gather feeds back. A new song added results in addition in feed.

## Structure
This service is divided into 3 Django apps &mdash; `user_management`,
`playlist` & `follow` (should have been named `activity` :sweat: ).
