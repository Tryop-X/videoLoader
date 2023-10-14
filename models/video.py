class Contenido:
    def __init__(self, start="", end="", content=""):
        self.start = start
        self.end = end
        self.content = content

    def to_dict(self):
        return {
            'start': self.start,
            'end': self.end,
            'content': self.content
        }
class Video:
    def __init__(self, url="", transcription=None, description=None, resume="", category="", cod="", title=""):
        self.url = url
        self.transcription = transcription
        self.description = description
        self.resume = resume
        self.category = category
        self.cod = cod
        self.title = title

    def to_dict(self):
        return {
            'url': self.url,
            'transcription': [t.to_dict() for t in self.transcription] if self.transcription else None,
            'description': self.description,
            'resume': self.resume,
            'category': self.category,
            'cod': self.cod,
            'title': self.title
        }