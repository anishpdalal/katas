import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_items(self):
        item = Item("foo", 0, 0)
        self.assertEquals("foo", item.name)
        self.assertEquals(0, item.sell_in)
        self.assertEquals(0, item.quality)

    def test_other_items_update_quality(self):
    	item = Item("food", 10, 5)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.sell_in, 9)
    	self.assertEqual(gilded_rose.item.quality, 4)

    def test_other_items_selldate_passed(self):
    	item = Item("food", -1, 5)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.sell_in, -2)
    	self.assertEqual(gilded_rose.item.quality, 3)

    def test_quality_never_negative(self):
    	item1 = Item("food", 0, 1)
    	item2 = Item("food", 1, 0)
    	gilded_rose1 = GildedRose(item1)
    	gilded_rose2 = GildedRose(item2)
    	gilded_rose1.update_quality()
    	gilded_rose2.update_quality()
    	self.assertEqual(gilded_rose1.item.quality, 0)
    	self.assertEqual(gilded_rose2.item.quality, 0)

    def test_aged_brie_update_quality(self):
    	item = Item("Aged Brie", 5, 10)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.sell_in, 4)
    	self.assertEqual(gilded_rose.item.quality, 11)

    def test_quality_fifty_threshold(self):
    	item1 = Item("Aged Brie", -2, 49.5)
    	item2 = Item("Aged Brie", -2, 49)
    	gilded_rose1 = GildedRose(item1)
    	gilded_rose2 = GildedRose(item2)
    	gilded_rose1.update_quality()
    	gilded_rose2.update_quality()
    	self.assertEqual(gilded_rose1.item.quality, 50)
    	self.assertEqual(gilded_rose2.item.quality, 50)

    def test_sulfuras_no_change(self):
    	item = Item("Sulfuras", None, 80)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.sell_in, None)
    	self.assertEqual(gilded_rose.item.quality, 80)

    def test_backstage_passes(self):
    	item = Item("Backstage passes", 12, 30)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.quality, 31)
    	self.assertEqual(gilded_rose.item.sell_in, 11)

    def test_backstage_passes_10_days(self):
    	item = Item("Backstage passes", 10, 30)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.quality, 32)
    	self.assertEqual(gilded_rose.item.sell_in, 9)

    def test_backstage_passes_5_days(self):
    	item = Item("Backstage passes", 5, 30)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.quality, 33)
    	self.assertEqual(gilded_rose.item.sell_in, 4)
  	
    def test_backstage_passes_0_days(self):
    	item = Item("Backstage passes", 0, 30)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.quality, 33)
    	self.assertEqual(gilded_rose.item.sell_in, -1)

    def test_conjure(self):
    	item = Item("Conjured", -2, 1)
    	gilded_rose = GildedRose(item)
    	gilded_rose.update_quality()
    	self.assertEqual(gilded_rose.item.quality, 0)
    	self.assertEqual(gilded_rose.item.sell_in, -3)



if __name__ == '__main__':
    unittest.main()