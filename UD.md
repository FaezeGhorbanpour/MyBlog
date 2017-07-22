After changing app, for Updating site, we follow these instructions:

1. git init
2. git add --all
3. git commit -m 'new update'
4. heroku login
5. git commit heroku master

If models change, we also run this:

6. heroku run python manage.py migrate
