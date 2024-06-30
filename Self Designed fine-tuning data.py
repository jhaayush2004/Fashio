import pandas as pd
import numpy as np

data = {
    'sentence 1': [
        "comfortable running shoes",
        "Looking for a red cotton shirt",
        "collared shirt and short sleeves",
        "Searching for a full sleeve men shirt",
        "Want a blue denim jacket",
        "Denim jacket for my girlfriend",
        "Looking for a stylish shoes for my father",
        "men shoes",
        "sandal",
        "search for anti slip shoes",
        "shoes that dry fast",
        "high heels for women",
        "wedding shoe",
        "men slim jeans",
        "show me ankle size women jeans",
        "cotton jeans men",
        "Looking for a men black jeans",
        "hood jacket",
        "exercise women jacket",
        "flip flop crocs",
        "men steelbelt watch",
        'show me track pant for boys',
        'hoddie t shirt for men and in cotton',
        'red shirt men',
        "black men tshirt"
        
        
    ],
    'sentence 2': [
        
        "NYKD Everyday Stylish Running Sports Jacket with Pockets for Women",
        "Cotton Regular Fit Solid Red Shirt",
        "Short Sleeves Camp Collared Shirt for Boys ",
        "Men's Cotton Blend Checkered Shirts Regular Fit Full Sleeves Shirt for Men",
        "Lorate Solid Mens Fashion Full Sleeves Latest Jacket for Men With Button Closure Long Sleeve Casual Torn Lycra Denim Jacket Blue",
        "FUNDAY FASHION Full Sleeve Blue Solid Womens Denim Jacket",
        "Men's Loafer Shoes",
        "Shoes for Crews Everlight Men's Non Slip Breathable Lightweight Lace-UpWater Resistant Work Shoes ",
        "Beslip Womens Mens Garden Clogs Shoes with Arch Support Unisex Comfort Slip-on Sandals",
        "Mens Shower Shoes With Holes Dry Quickly Bath Slippers Womens Non Slip Indoor Home Bedroom Pool Spa Guest College Dorm",
        "YALOX Water Shoes Men's Women's Swim Shoes Outdoor Beach Barefoot Quick Dry Aqua Pool Socks Swimming Yoga Surfing Exercise",
        "Modatop Platform Heels for Women Platform Sandals Womens Chunky Heel Open Toe Pumps Ankle Strap Womens Wedding Party Pumps Shoes",
        "MUCCCUTE Women's Rhinestone Cowboy Boots Cowgirl Western Boots Sparkly Pointed Toe Side Zipper Knee High Mid Heel Wedding Shoes",
        "Urbano Fashion Mens Slim Fit Jeans",
        "PAIGE Women's Mayslie Straight Ankle Jeans",
        "ENNIE FOSTE Men's Poly Cotton Washed Lighe Blue Jeans",
        "DENNIE FOSTE Men Regular Mid Rise Black Jeans",
        "LZLRUN Reflective Vest Jacket Casual Hiphop Windbreaker Night Sporting Coat Hooded Fluorescent Clothing",
        "KORYAK by Zeel Women's Winter Jackets Sport Wear for Trekking Yoga Workout  Jogging  Thermal Hybrid Jacket Cycling Jackets for Women Regular Fit  Blue ",
        "Crocs Unisex-Adult Crocband Flip Flop  Slip-on Sandals  Shower Shoes",
        "Fossil Men's Nate Stainless Steel Quartz Chronograph Watch" ,
        "Pepe Jeans Men's Skinny Track Pants",
        "KLIEGOU Men's Hipster Hip Hop Hoodie Cotton TShirt",
        "cotton Regular Fit Executive Shirt Black",
        "UDNAG Unisex Round Neck Graphic 'Lawyer Lawyer' Polyester T-Shirt White"
        
    ],
    'Label':[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
}

df = pd.DataFrame(data)
