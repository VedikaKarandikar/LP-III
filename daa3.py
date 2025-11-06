class Item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value

def fractional_knapsack(items,capacity):
    value_weight_ratio=[(item.value/item.weight,item ) for item in items]
    value_weight_ratio.sort(reverse=True)
    total_value=0.0
    knapsack=[]
    for ratio,item in value_weight_ratio:
        if capacity==0:
            break
        weight=min(item.weight,capacity)
        total_value+=weight*ratio
        capacity-=weight
        knapsack.append((item,weight))
    return total_value,knapsack

if __name__=="__main__":
    items=[Item(10,60),Item(20,100),Item(30,120)]
    max_capacity=50
    max_value,selected_items=fractional_knapsack(items,max_capacity)

    for item, weight in selected_items:
        print(f"Item with weight {item.weight} and value {item.value} (fraction taken {weight/item.weight})")
    print(f" Maximum value achievable: {max_value}")
        
