import pandas as pd


df = pd.read_json("orders_simple.json")
# print(df.head(10))
# print(type(df))

# 1
df["total_amount"] = df["total_amount"].str.replace("$",'').astype(float)
df["shipping_days"] = df["shipping_days"].astype(int)
df["customer_age"] = df["customer_age"].astype(int)
df["rating"] = df["rating"].astype(float)
df["order_date"] = pd.to_datetime(df['order_date'])

# print(df["total_amount"])

# 2
df["items_html"] = df["items_html"].str.replace("<br>", " ").str.replace("</b>", " ").str.replace("<b>", " ")
# print(df["items_html"])

# 3
df["coupon_used"] = df["coupon_used"].replace("", "no coupon")
# print(df["coupon_used"].to_string())

# 4
df['order_month'] = pd.to_datetime(df['order_date']).dt.month
# print(df["order_month"])

# 5
new_c = df["total_amount"] > df["total_amount"].mean()
df["high_value_order"] = new_c
# print(df["high_value_order"])

df = df.sort_values(by=["total_amount", ], ascending=False)
# print(df["total_amount"])

# 7
filter_ = df[(df["total_amount"] > 1000) & df[(df["rating"] > 4.5)]
# print(df["total_amount"])
# 8
# if df["shipping_days"] > 7:
#     new_c = df["delivery_status"] = "delayed"
# else:
#     new_c = df["delivery_status"] = "on time"
# print(df["delivery_status"])

# 9
# df = df.to_csv("clean_orders_[ID_NUMBER].csv")
# print(df)

