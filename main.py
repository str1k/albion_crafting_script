import requests

return_rate = 0.367
expected_return = 1.57
weight = 3090 + 92 + 163
refining_price = 399
ore_weight = {"T2_ORE": 0.2,
              "T3_ORE": 0.2,
              "T4_ORE": 0.3,
              "T5_ORE": 0.8,
              "T6_ORE": 1.1,
              }
recipes = {"T2_METALBAR": {"T2_ORE": 1}
    , "T3_METALBAR": {"T2_METALBAR": 1, "T3_ORE": 2}
    , "T4_METALBAR": {"T3_METALBAR": 1, "T4_ORE": 2}
    , "T5_METALBAR": {"T4_METALBAR": 1, "T5_ORE": 3}
    , "T6_METALBAR": {"T5_METALBAR": 1, "T6_ORE": 4}
    , "T7_METALBAR": {"T6_METALBAR": 1, "T7_ORE": 5}
    , "T8_METALBAR": {"T7_METALBAR": 1, "T8_ORE": 5}
           }

accum_refining_price = {"T2_METALBAR": 0,
                        "T3_METALBAR": 0,
                        "T4_METALBAR": 0,
                        "T5_METALBAR": 0,
                        "T6_METALBAR": 0,
                        "T7_METALBAR": 0,
                        "T8_METALBAR": 0,
                        }

ore_price = {
    "T2_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
               "city_buy_max": ""}
    , "T3_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}
    , "T4_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}
    , "T5_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}
    , "T6_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}
    , "T7_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}
    , "T8_ORE": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                 "city_buy_max": ""}

}

metal_price = {
    "T2_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                    "city_buy_max": ""}
    , "T3_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}
    , "T4_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}
    , "T5_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}
    , "T6_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}
    , "T7_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}
    , "T8_METALBAR": {"min_price": 99999, "city_min": "", "max_price": 1, "city_max": "", "max_buy_price": 1,
                      "city_buy_max": ""}

}
response = requests.get(
    "https://east.albion-online-data.com/api/v2/stats/Prices/T2_ORE,T3_ORE,T4_ORE,T5_ORE,T6_ORE,T7_ORE,T8_ORE?locations=Lymhurst,Bridgewatch,Fort%20Sterling,Martlock,Thetford")

for item in response.json():
    if ore_price[item['item_id']]["min_price"] > item['sell_price_min']:
        ore_price[item['item_id']]["min_price"] = item['sell_price_min']
        ore_price[item['item_id']]["city_min"] = item['city']

    if ore_price[item['item_id']]["max_price"] < item['sell_price_min']:
        ore_price[item['item_id']]["max_price"] = item['sell_price_min']
        ore_price[item['item_id']]["city_max"] = item['city']

    if ore_price[item['item_id']]["max_buy_price"] < item['buy_price_max']:
        ore_price[item['item_id']]["max_buy_price"] = item['buy_price_max']
        ore_price[item['item_id']]["city_buy_max"] = item['city']

reponse_bar = requests.get(
    "https://east.albion-online-data.com/api/v2/stats/Prices/T2_METALBAR,T3_METALBAR,T4_METALBAR,T5_METALBAR,T6_METALBAR,T7_METALBAR,T8_METALBAR?locations=Lymhurst,Bridgewatch,Fort%20Sterling,Martlock,Thetford")

for item in reponse_bar.json():
    if metal_price[item['item_id']]["min_price"] > item['sell_price_min']:
        metal_price[item['item_id']]["min_price"] = item['sell_price_min']
        metal_price[item['item_id']]["city_min"] = item['city']

    if metal_price[item['item_id']]["max_price"] < item['sell_price_min']:
        metal_price[item['item_id']]["max_price"] = item['sell_price_min']
        metal_price[item['item_id']]["city_max"] = item['city']

    if metal_price[item['item_id']]["max_buy_price"] < item['buy_price_max']:
        metal_price[item['item_id']]["max_buy_price"] = item['buy_price_max']
        metal_price[item['item_id']]["city_buy_max"] = item['city']

profitability = {
    "T2_METALBAR": {"nutrition_cost": 0,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0,
                    "sell_at": ""},
    "T3_METALBAR": {"nutrition_cost": 0.9,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0
        , "sell_at": ""},
    "T4_METALBAR": {"nutrition_cost": 1.8,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0
        , "sell_at": ""},
    "T5_METALBAR": {"nutrition_cost": 3.6,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0
        , "sell_at": ""},
    "T6_METALBAR": {"nutrition_cost": 7.2,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0,
                    "sell_at": ""},
    "T7_METALBAR": {"nutrition_cost": 14.4,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0,
                    "sell_at": ""},
    "T8_METALBAR": {"nutrition_cost": 28.8,
                    "buy_metal_at": "",
                    "buy_ore_at": "",
                    "profit": 0,
                    "revenue": 0,
                    "total_cost": 0,
                    "sell_at": ""},
}
for r in recipes:
    cost = 0
    for k in recipes[r]:
        if 'ORE' in k:
            cost += (ore_price[k]['min_price'] * recipes[r][k])
            profitability[r]['buy_ore_at'] = ore_price[k]['city_min']
        elif 'METALBAR' in k:
            cost += (metal_price[k]['min_price'] * recipes[r][k])
            profitability[r]['buy_metal_at'] = metal_price[k]['city_min']
    cost += (profitability[r]['nutrition_cost'] * refining_price / 100)
    profitability[r]['total_cost'] = cost
    profitability[r]['revenue'] = expected_return * metal_price[r]['max_buy_price']
    profitability[r]['profit'] = profitability[r]['revenue'] - profitability[r]['total_cost']
    profitability[r]['sell_at'] = metal_price[r]['city_buy_max']
