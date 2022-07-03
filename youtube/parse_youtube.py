
from bs4 import BeautifulSoup
from markdownTable import markdownTable


def make_markdown_table(array):
    """ the same input as above """

    nl = "\n"

    markdown = nl
    markdown += f"| {' | '.join(array[0])} |"

    markdown += nl
    markdown += f"| {' | '.join(['---']*len(array[0]))} |"

    markdown += nl
    for entry in array[1:]:
        markdown += f"| {' | '.join(entry)} |{nl}"

    return markdown


def youtube_channel(need_description=False):
    fpm = open("aaa.md", "w")
    with open('aaa.html') as fp:
        content = fp.read()
        soup = BeautifulSoup(content, 'lxml')
        items = soup.find_all(name='ytd-channel-renderer', attrs={"class": "style-scope ytd-expanded-shelf-contents-renderer"})
        print(len(items))
        channels = [["频道", "订阅数量", "视频数量"]]
        for item in items:
            channel_name = item.find(name='yt-formatted-string', attrs={"id": "text"}).text
            channel_uri = item.find(name='a', attrs={"class": "channel-link"}).attrs["href"]
            video_count = item.find(name='span', attrs={"id": "video-count"}).text
            subscribers = item.find(attrs={"id": "subscribers"}).text
            if subscribers == "":
                subscribers = "数量不详"
            # description = item.find(name='yt-formatted-string', attrs={"id": "description"}).text
            # print(channel_name, channel_uri, subscribers, video_count, description)
            channels.append([f"[{channel_name}](https://youtube.com{channel_uri})", subscribers, video_count])

        markdown = make_markdown_table(channels)
        fpm.write(markdown)
        fpm.close()


youtube_channel(need_description=False)
