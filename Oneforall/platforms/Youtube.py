import aiohttp

API_URL = "http://45.77.174.241:9090"


class YouTubeAPIClient:

    def __init__(self):
        self.api = API_URL

    async def _get_token(self, video_id: str, media_type: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.api}/download",
                params={"url": video_id, "type": media_type},
                timeout=aiohttp.ClientTimeout(total=20)
            ) as res:
                if res.status != 200:
                    return None, None

                data = await res.json()
                token = data.get("download_token")

                stream_url = f"{self.api}/stream/{video_id}?type={media_type}"

                return stream_url, token

    async def get_audio(self, video_id: str):
        return await self._get_token(video_id, "audio")

    async def get_video(self, video_id: str):
        return await self._get_token(video_id, "video")
