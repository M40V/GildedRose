# GildedRose
Gilded Rose Refactoring Kata Python
--------------------------------------------------------------------------------------

The Gilded Rose is a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison. They also buy and sell only the finest goods. Unfortunately, their goods are constantly degrading in quality as they approach their sell by date. They have a system in place that updates their inventory for them. Here an introduction to their system:

All items have a SellIn value which denotes the number of days they have to sell the item
All items have a Quality value which denotes how valuable the item is
At the end of each day their system lowers both values for every item
Once the sell by date has passed, Quality degrades twice as fast
The Quality of an item is never negative
"Aged Brie" actually increases in Quality the older it gets
The Quality of an item is never more than 50
"Sulfuras", being a legendary item, never has to be sold or decreases in Quality
"Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
"Conjured" items degrade in Quality twice as fast as normal items

--------------------------------------------------------------------------------------

You can import the GildedRose and Items class from the gilded_rose.py 

You will find tests in the test_gilded_rose.py file that you can run with the following command :

    python test_gilded_rose.py

Finally you can observe the evolution of these items with the texttest_fixture.py script :
    
    python texttest_fixture.py
