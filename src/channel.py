import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel_data = self.print_info()
        self.title = channel_data['items'][0]['snippet']['title']
        self.description = channel_data['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA'
        self.subscriberCount = channel_data['items'][0]['statistics']['subscriberCount']
        self.video_count = channel_data['items'][0]['statistics']['videoCount']
        self.view_count = channel_data['items'][0]['statistics']['viewCount']




    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY1')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

