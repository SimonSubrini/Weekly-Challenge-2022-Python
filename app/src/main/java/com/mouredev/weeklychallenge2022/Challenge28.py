def vendingMachine(coinList,product):
    acceptedMoneyValues=[200,100,50,10,5]
    products={
        1:["Agua", 50],2:["Coca-Cola", 100],4:["Cerveza", 155],5:["Pizza", 200],10:["Donut", 75]
    }
    if product not in products:
        return "El producto con codigo {} no existe".format(product),coinList
    
    
    money=0
    for coin in coinList:
        if coin not in acceptedMoneyValues:
            return "Error, se ha ingresado una moneda no permitida",coinList
        money+=coin
    
    if money<products[product][1]:
        return "Dinero insuficiente para realizar la compra (dinero disponible: {}, precio: {})".format(money,products[product][1]),coinList
    else:
        money=money-products[product][1]
        moneyCont=0
        moneyBackList=[]
        while money>0:
            if money-acceptedMoneyValues[moneyCont]>=0:
                moneyBackList.append(acceptedMoneyValues[moneyCont])
                money-=acceptedMoneyValues[moneyCont]
            else:
                moneyCont+=1
        return "Producto adquirido --> {}, vuelto --> {}".format(products[product][0],moneyBackList),moneyBackList
            
    
    
    
print(vendingMachine([200,100,100,50,50,10,10],5)[0])
print(vendingMachine([100,50,50,10,10],1)[0])
print(vendingMachine([10,10],2)[0])
