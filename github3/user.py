"""
github3.user
============

This module contains the classes related to user information.

"""

from .models import GitHubCore

class Plan(object):
    def __init__(self, data):
        super(Plan, self).__init__()
        self._collab = data.get('collaborators')
        self._name = data.get('name')
        self._private = data.get('private_repos')
        self._space = data.get('space')

    def collaborators(self):
        return self._collab

    def is_free(self):
        return self._name == 'free'

    def name(self):
        return self._name

    def private_repos(self):
        return self._private

    def space(self):
        return self._space


_large = Plan({'name': 'large', 'private_repos': 50,
    'collaborators': 25, 'space': 0})
_medium = Plan({'name': 'medium', 'private_repos': 20,
    'collaborators': 10, 'space': 0})
_small = Plan({'name': 'small', 'private_repos': 10,
    'collaborators': 5, 'space': 0})
_micro = Plan({'name': 'micro', 'private_repos': 5,
    'collaborators': 1, 'space': 0})
_free = Plan({'name': 'free', 'private_repos': 0,
    'collaborators': 0, 'space': 0})

plans = {'large': _large, 'medium': _medium, 'small': _small,
        'micro': _micro, 'free': _free}


class User(GitHubCore):
    def __init__(self, data):
        super(User, self).__init__()

        # Public information
        ## e.g. https://api.github.com/users/self._login
        self._api_url = data.get('url')

        self._avatar = data.get('avatar_url')
        self._bio = data.get('bio')
        self._blog = data.get('blog')
        self._company = data.get('company')
        self._email = data.get('email')

        ## The number of people following this user
        self._followers = data.get('followers')

        ## The number of people this user follows
        self._following = data.get('following')

        ## The number of people this user folows
        self._grav_id = data.get('gravatar_id')

        self._hire = data.get('hireable')
        self._id = data.get('id')
        self._location = data.get('location')
        self._login = data.get('login')

        ## e.g. first_name last_name
        self._name = data.get('name')

        ## The number of public_gists
        self._public_gists = data.get('public_gists')

        ## The number of public_repos
        self._public_repos = data.get('public_repos')

        ## e.g. https://github.com/self._login
        self._url = data.get('html_url')

        # Private information
        self._disk = data.get('disk_usage')
        if data.get('plan'):
            _plan = data.get('plan')
            self._plan = plans[_plan['name'].lower()]
            self._plan._space = _plan['space']
        else:
            self._plan = None

        ## The number of private repos
        self._private_repos = data.get('total_private_repos')
        self._private_gists = data.get('total_private_gists')

        self._owned_private_repos = data.get('owned_private_repos')

    def __repr__(self):
        return '<User [%s:%s]>' % (self._login, self._name)

    @property
    def avatar(self):
        return self._avatar

    @property
    def bio(self):
        return self._bio

    @property
    def blog(self):
        return self._blog

    @property
    def company(self):
        return self._company

    @property
    def disk_usage(self):
        return self._disk

    @property
    def email(self):
        return self._email

    @property
    def followers(self):
        return self._followers

    @property
    def following(self):
        return self._following

    @property
    def for_hire(self):
        return self._hire

    @property
    def html_url(self):
        return self._url

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    @property
    def login(self):
        return self._login

    @property
    def name(self):
        return self._name

    @property
    def owned_private_repos(self):
        return self._owned_private_repos

    @property
    def private_gists(self):
        return self._private_gists

    @property
    def plan(self):
        return self._plan

    @property
    def public_gists(self):
        return self._public_gists

    @property
    def public_repos(self):
        return self._public_repos

    @property
    def total_private_repos(self):
        return self._private_repos