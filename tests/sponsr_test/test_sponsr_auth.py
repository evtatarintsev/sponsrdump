from sponsr.sponsr_auth import SponsrAuth, Cookie


class TestSponsrAuth:
    def test_read_cookie_from_file(self, tmp_path):
        auth = tmp_path / "sponsrdump_auth.txt"
        auth.write_text("SESS=1111")

        assert SponsrAuth(auth).cookie() == Cookie("SESS", "1111")
