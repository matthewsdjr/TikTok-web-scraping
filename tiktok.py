from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("JHMw1PNkv6pOvK-LzDzrRcxAN1t3pPo2DjbDefL5_krLG4E5eFclzutATFfU1iIXIITfENnLR21Wc4FAO-w4ewx1uRD8P8imsy4GiQf_7YwXS4uDRvH9c4vhj3zK2xVSjqouXMY", None)  # set your own ms_token


async def get_hashtag_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens="FlebSKjUW3FNGLZ47xu0H0bol2Rch-rn8PnH-0CBJ4jiFgBxyXVSrdoiOoHygd-bmCdqV6t4mnvdPw38oU2XNC-2uN0z2la6to_zg5Fa75qaHcOnNr6nO8UGnZt2PHOXkvk8qsU", num_sessions=1, sleep_after=3)
        tag = api.hashtag(name="funny")
        async for video in tag.videos(count=30):
            print(video)
            print(video.as_dict)


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())