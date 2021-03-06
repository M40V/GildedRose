# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            #Sulfuras is a legendary item, it never changes
            if item.name in "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                item.sell_in = "never"
            else:
                if item.name not in "Aged Brie" and item.name not in "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        #Conjured items decreases twice as fast as regular items
                        if "Conjured" in item.name :
                            item.quality = item.quality - 2
                        else :
                            item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        if item.name in "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.name not in "Aged Brie":
                        if item.name not in "Backstage passes to a TAFKAL80ETC concert":
                            if "Conjured" in item.name :
                                if item.quality > 1 :
                                    item.quality = item.quality - 2
                                else:
                                    item.quality = 0 
                            elif item.quality > 0:
                                item.quality = item.quality - 1
                        else:
                            item.quality = 0
                    else:
                        if item.quality < 50:
                            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
