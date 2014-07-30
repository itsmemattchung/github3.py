from .helper import IntegrationHelper

import github3


class TestGist(IntegrationHelper):
    def test_comments(self):
        """Show that a user can iterate over the comments on a gist."""
        cassette_name = self.cassette_name('comments')
        with self.recorder.use_cassette(cassette_name):
            gist = self.gh.gist(3342247)
            assert gist is not None
            for comment in gist.comments():
                assert isinstance(comment, github3.gists.comment.GistComment)

    def test_iter_commits(self):
        cassette_name = self.cassette_name('commits')
        with self.recorder.use_cassette(cassette_name,
                                        preserve_exact_body_bytes=True):
            gist = self.gh.gist(1834570)
            assert gist is not None
            for commit in gist.iter_commits():
                assert isinstance(commit, github3.gists.history.GistHistory)

    def test_iter_forks(self):
        cassette_name = self.cassette_name('forks')
        with self.recorder.use_cassette(cassette_name,
                                        preserve_exact_body_bytes=True):
            gist = self.gh.gist(1834570)
            assert gist is not None
            for commit in gist.iter_forks():
                assert isinstance(commit, github3.gists.gist.Gist)
