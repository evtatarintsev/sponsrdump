from pathlib import Path

import pytest

from kinescope.quality import KinescopeQuality
from kinescope.master_mpd import MasterMpd


class TestMasterMpd:
    def test_video__return_chunks_urls(self):
        xml_file = Path(__file__).parent / "fixtures" / "master.mpd.xml"
        with xml_file.open() as f:
            xml = f.read()

        mpd = MasterMpd(xml)

        assert mpd.video(KinescopeQuality.p1080) == [
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/0/79178561/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/79178561/157546688/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/157546688/237435793/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/237435793/315947512/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/315947512/394334796/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/394334796/472679825/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/472679825/551124995/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/551124995/629986180/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/629986180/709783317/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/709783317/786982994/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/786982994/865528863/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/865528863/944040633/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/944040633/1023711219/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/1023711219/1102551945/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/1102551945/1105643881/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAABAr0A',
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ce-a597-742b-b9d6-a1786f5e3786/1102551945/1105643881/1080p.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7&kcd=AAAAAACgnkA'
        ]

    def test_audio__return_chunks_urls(self):
        xml_file = Path(__file__).parent / "fixtures" / "master.mpd.xml"
        with xml_file.open() as f:
            xml = f.read()

        mpd = MasterMpd(xml)

        assert mpd.audio() == [
            'https://edge-ams-1.kinescopecdn.net/3e324c4c-4135-42a7-a393-6399d9062f6c/videos/c688e141-7f66-4e8e-b822-f53498ef6c95/assets/019515ca-1f90-74b4-8502-ec869131fe26/audio_0.mp4?kinescope_project_id=0683e0d0-cd8b-4760-996b-80b002fd64d7'
        ]

    @pytest.mark.parametrize(
        "quality", [
            KinescopeQuality.p360,
            KinescopeQuality.p480,
            KinescopeQuality.p720,
            KinescopeQuality.p1080
        ]
    )
    def test_find_video_representation__(self, quality):
        xml_file = Path(__file__).parent / "fixtures" / "master.mpd.xml"
        with xml_file.open() as f:
            xml = f.read()

        mpd = MasterMpd(xml)

        assert mpd.find_video_representation(quality).height == quality

    def test_find_video_representation__if_not_found_return(self):
        xml_file = Path(__file__).parent / "fixtures" / "master.mpd_720_1080_video.xml"
        with xml_file.open() as f:
            xml = f.read()

        mpd = MasterMpd(xml)

        assert mpd.find_video_representation(KinescopeQuality.p480).height == KinescopeQuality.p720
