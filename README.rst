Clearbit Slack Notifier
=======================
pypi:: clearbit-slack-python
-----------------------------

Clean beautiful customer data. Now in Slack.

.. image:: https://cloud.githubusercontent.com/assets/739782/8149387/3f89cd68-1276-11e5-863c-5529237bfe6c.png

Installation
------------

Add to your application's requirements.txt file:

::

    clearbit-slack-python

Or pip install:

::

    $ pip install clearbit-slack-python

Configuration
-------------

To use, instantiate a :py:class:`~clearbit_slack.notifier.Notifier`
object with your Slack token, channel, and data :py:class:`dict` built
from part of the body of the POST request sent by Clearbit.

::

    import json

    from clearbit_slack import Notifier


    slack_token = 'xoxp-1234567890-6789012345-5432109876-12ab34'
    slack_channel = '#signups'
    body_data = json.loads(request_body)
    attrs = body_data.get('body', {})

    notifier = Notifier(slack_token, slack_channel, attrs=attrs)
    notifier.notify()

Contributing
------------

1. Fork it (https://github.com/15five/clearbit-slack-python/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

