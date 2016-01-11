
def format_number(value):
    return value


def field(title, value, short=True):
    return {
        'title': title,
        'value': value,
        'short': short
    }


def link(url, title, followers=''):
    if followers:
        followers = format_number(followers)
        followers = " ({} followers)".format(followers)

    return "<{url}|{title}>{followers}".format(url=url, title=title, followers=followers)


def aboutme(aboutme_dict):
    aboutme_handle = aboutme_dict.get('handle')
    if not aboutme_handle:
        return ''
    value = link("https://about.me/{}".format(aboutme_handle), aboutme_handle)
    return field('AboutMe', value)


def angellist(angellist_dict):
    angellist_handle = angellist_dict.get('handle')
    if not angellist_handle:
        return ''
    value = link("https://angel.co/{}".format(angellist_handle),
                 angellist_handle,
                 angellist_dict['followers'])
    return field('AngelList', value)


def github(github_dict):
    github_handle = github_dict.get('handle')
    if not github_handle:
        return ''
    value = link("https://github.com/{}".format(github_handle),
                 github_handle,
                 github_dict['followers'])
    return field('GitHub', value)


def facebook(facebook_dict):
    facebook_handle = facebook_dict.get('handle')
    if not facebook_handle:
        return ''
    value = link("https://www.facebook.com/{}".format(facebook_handle), facebook_handle)
    return field('Facebook', value)


def twitter(twitter_dict):
    twitter_handle = twitter_dict.get('handle')
    if not twitter_handle:
        return ''
    value = link("http://twitter.com/{}".format(twitter_handle),
                 twitter_handle,
                 twitter_dict['followers'])
    return field('Twitter', value)


def linkedin(linkedin_dict):
    linkedin_handle = linkedin_dict.get('handle')
    if not linkedin_handle:
        return ''
    value = link("https://www.linkedin.com/{}".format(linkedin_handle), linkedin_handle)
    return field('LinkedIn', value)
