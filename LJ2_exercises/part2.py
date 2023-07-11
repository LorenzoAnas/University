def main():    
    item_1_price = 270
    item_2_price = 850
    item_3_price = 1000
    combo_pack = 0.8
    gift_pack = 0.5

    print(
        f"""
        Online Store
        ---------------------------
        Product(S)                 Price
        Item 1                     {item_1_price}
        Item 2                     {item_2_price}
        Item 3                     {item_3_price}
        Combo 1(Item 1 + 2)        {(item_1_price + item_2_price) * combo_pack}
        Combo 2(Item 2 + 3)        {(item_2_price + item_3_price) * combo_pack}
        Combo 3(Item 1 + 3)        {(item_1_price + item_3_price) * combo_pack}
        Combo 4(Item 1 + 2 + 3)    {(item_1_price + item_2_price + item_3_price) * gift_pack}
        -------------------------- 
        For delivery Contact:98764678899
        """)
    
main()