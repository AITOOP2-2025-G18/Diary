from diaries.AbstractDiary import AbstractDiary

class SuzukiDiary(AbstractDiary):
    
    def get_date(self):
        return "2026-11-01"
    
    def get_summary(self):
        return "なにもない一日だった"
    
    def get_author(self):
        return "Suzuki"