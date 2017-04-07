Greeter - A test Django app that says hello
===========================================

Greeter just says displays a web page that says hello. It is intended
for educational purposes, particularly in order to teach people about
how you deploy Django apps. For example, I have used it in a `deployment
webinar`_.

By default it says "Hello, world!" and shows a default image. It also
has a database table (a Django model) of "greetees" which can be edited
with the Django Admin. If the table is nonempty, instead of greeting the
world the app picks up a greetee at random from the table, and shows
their image.

If the setting ``GREETER_LOG`` is True (by default it's False), then
each visit is logged in the database table ``VisitorLog`` (viewable
through the admin). You would never do this in a serious app; it's just
a way to have the app write to the database on each request in order to
experiment with how much this affects the number of requests it can
serve.

© 2017 Antonis Christofides

To the extent possible under law, I hereby waive all copyright and
related or neighboring rights to Greeter.

.. _deployment webinar: https://www.crowdcast.io/e/deploying-django/
