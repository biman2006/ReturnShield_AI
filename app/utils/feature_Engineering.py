def create_features(data):
    return_ratio=data.total_returns/data.total_orders 
    is_high_value=1 if data.order_value>3500 else 0 

    return{


        "total_orders":data.total_orders,
        "total_returns":data.total_returns,
        "return_ratio":return_ratio,
        "order_value":data.order_value,
        "acc_age_days": data.acc_age_days,
        "days_since_last_return":data.days_since_last_return,
        "return_last_7_days":data.return_last_7_days,
        "product_category":data.product_category,
        "return_reason":data.return_reason,
        "is_high_value":is_high_value

 







    }