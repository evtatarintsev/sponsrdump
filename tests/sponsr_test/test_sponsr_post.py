from pathlib import Path

from sponsr.sponsr_post import SponsrPostPreview


class TestSponsrProjectPage:
    def test_kinescope_links__extracted_from_post_html(self):
        pape_file = Path(__file__).parent / "fixtures"/ "post_preview.html"
        with pape_file.open() as f:
            html = f.read()

        assert SponsrPostPreview("", html).video_ids() == ["90c1f6ae-2950-4f73-b99c-f2d0e88c93e2"]

    def test_kinescope_links__extracted_from_post_html__with_many_iframes(self):
        pape_file = Path(__file__).parent / "fixtures"/ "post_preview_with_many_frames.html"
        with pape_file.open() as f:
            html = f.read()

        assert SponsrPostPreview("", html).video_ids() == [
            "90c1f6ae-2950-4f73-b99c-f2d0e88c93e2",
            "60c1f6ae-2950-4f73-b99c-f2d0e88c93e2"
        ]
