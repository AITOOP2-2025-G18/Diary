from diaries.AbstractDiary import AbstractDiary

class NaoDiary(AbstractDiary):
    
    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "楽しい一日だった"
    
    def get_author(self):
        return "nao"