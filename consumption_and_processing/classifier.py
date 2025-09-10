from consumption_and_processing.hostile_lists import HostileLists


class Classifier:
    very_hostile = HostileLists().get_very_hostile_list()
    hostile = HostileLists().get_hostile_list()
    very_hostile_weight = 2
    line_is_bds = 5
    line_none = 3
    line_medium = 4
    line_high = 6
    def __init__(self,text):
        self.text = text.lower()
        self.count_very_hostile = 0
        self.count_hostile = 0

    def check_text(self):
        for word in Classifier.very_hostile:
            if word in self.text:
                self.count_very_hostile += 1
        for word in Classifier.hostile:
            if word in self.text:
                self.count_hostile += 1

    def get_percent(self):
        bds_percent = ((self.count_very_hostile * Classifier.very_hostile_weight) + self.count_hostile) / (len(self.text.split(" "))) * 100
        return bds_percent

    def get_is_bds(self):
        if self.get_percent() > Classifier.line_is_bds:
            return True
        return False

    def classify(self):
        if self.get_percent() < Classifier.line_none:
            return "none"
        elif self.get_percent() < Classifier.line_medium:
            return "medium"
        return "high"




