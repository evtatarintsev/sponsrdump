from pathlib import Path

from kinescope.quality import KinescopeQuality
from kinescope.master_mpd import MasterMpd


class TestMasterMpd:
    def test_video__return_chunks_urls(self):
        xml_file = Path(__file__).parent / "fixtures" / "master.mpd.xml"
        with xml_file.open() as f:
            xml = f.read()

        mpd = MasterMpd(xml)

        assert mpd.video(KinescopeQuality.THE_BEST) == []
