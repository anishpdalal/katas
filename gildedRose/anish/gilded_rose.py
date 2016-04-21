class GildedRose(object):

    def __init__(self, item):
        self.item = item

    def update_quality(self):
        special_items = {"Aged Brie" : self.aged_brie,
                            "Sulfuras" : self.sulfuras,
                            "Backstage passes" : self.backstage_passes,
                            "Conjured" : self.conjured
        }

        if self.item.name in special_items:
            special_items[self.item.name]()
        else:
            self.other_items()

    def other_items(self):
        if self.item.sell_in < 0 and self.item.quality >= 2:
            self.item.quality -= 2
        elif self.item.quality <= 1:
            self.item.quality = 0
        else:
            self.item.quality -= 1

        self.item.sell_in -= 1

    def aged_brie(self):
        if self.item.quality <= 49:
            self.item.quality += 1
        else:
            self.item.quality = 50
        
        self.item.sell_in -= 1
     
    def sulfuras(self):
        self.item.sell_in = None
        self.item.quality = 80

    def backstage_passes(self):
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in <= 5:
            self.item.quality += 3
        elif self.item.sell_in <= 10:
            self.item.quality += 2
        else:
            self.item.quality += 1

        self.item.sell_in -= 1

    def conjured(self):
        if self.item.quality <= 2:
            self.item.quality = 0
        else:
            self.item.quality -= 2

        self.item.sell_in -= 1
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)