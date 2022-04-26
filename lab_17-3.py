# Author: CRS 04/12/22
# Create class
class TV_remote:
    # Define functions
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.On = False
    def to_string(self):
        return "Channel:",self.channel,"Volume:",self.volume,"On:",self.On
# Test
tv = TV_remote()
print(tv.to_string())
    