'''A popular e-commerce company, "ShopEasy", wants to implement a recommendation system to suggest products to its customers based on their purchase history. The system should be able to analyze the customer's purchase behavior and provide personalized recommendations.

To achieve this, the company wants to design a Customer class that can store information about a customer's purchases. The class should have attributes such as customer_id, name, and purchase_history, which is a list of products purchased by the customer. The class should also have methods to add new purchases to the customer's history and to get recommendations based on their purchase behavior.

As a software engineer at ShopEasy, your task is to design and implement the Customer class using object-oriented programming principles. You are free to use any programming language of your choice to provide the solution for this question.

'''


class Customer:
    def __init__(self, customer_id, name,purchase):
        self.customer_id = customer_id
        self.name=name 
        self.arr=purchase
    def add_newpurchase_item(self,item):
        self.arr.append(item)


    def get_recommendations(self):
        # This is a simple implementation of a recommendation system
        freq_map={}
        n=len(self.arr)
        for i in self.arr:
            if i in freq_map:
                freq_map[i]+= 1 
            else:
                freq_map[i] = 1 
        d = dict(sorted(freq_map.items(), key=lambda x: x[1],reverse= True))
        maxi=max(d.values())
        ans=[]
        for item,cnt in d.items():
            if cnt==maxi:
                ans.append(item)

        return ans 
obj=Customer(1,'kashish',['clothes','beauty','beauty','electronices'])
obj.add_newpurchase_item('beauty')
print(obj.get_recommendations())
obj=Customer(1,'kashish',['clothes','beauty','beauty','electronices'])

obj.add_newpurchase_item('clothes')

print(obj.get_recommendations())