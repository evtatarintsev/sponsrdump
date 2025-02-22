from pathlib import Path

from sponsr.sponsr_project import SponsrProjectPage


class TestSponsrProjectPage:
    def test_project_id__extracted_from_page_html(self):
        pape_file = Path(__file__).parent / "fixtures"/ "project_page.html"
        with pape_file.open() as f:
            html = f.read()

        assert SponsrProjectPage(html).project_id() == 248
