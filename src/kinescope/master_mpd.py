from mpegdash.parser import MPEGDASHParser

from kinescope.quality import KinescopeQuality


class MasterMpd:
    def __init__(self, content: str):
        mpd = MPEGDASHParser.parse(content)
        adaptation_sets = mpd.periods[0].adaptation_sets
        mime_types = {
            adaptation_set.mime_type: adaptation_set
            for adaptation_set in adaptation_sets
        }
        self.video_adaptation_set = mime_types["video/mp4"]
        self.audio_adaptation_set = mime_types["audio/mp4"]

    def audio(self) -> list:
        representation = max(self.video_adaptation_set.representations, key=lambda r: int(r.audio_sampling_rate))
        return [segment_url.media for segment_url in representation.segment_lists[0].segment_urls]

    def video(self, quality: KinescopeQuality) -> list:
        representation = max(self.video_adaptation_set.representations, key=lambda r: r.width)
        return [segment_url.media for segment_url in representation.segment_lists[0].segment_urls]
