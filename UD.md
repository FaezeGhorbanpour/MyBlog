After changing app, for Updating site, we follow these instructions:

1. git init
1. git add --all
2. git commit 'new update'
3. heroku login
4. git commit heroku master

If models change, we also run this:
5. heroku run python manage.py migrate
