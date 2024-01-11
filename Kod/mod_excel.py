import pandas as pd

class order:
    def __init__(self, order, product_list) -> None:
        self.product_list = pd.read_csv(product_list)

        self.df = pd.read_csv(order)
        self.df["Lokacja"] = self.df["Lokacja"].apply(lambda x: str(x[:-2]) + self.__even_to_odd(x[-2:]))    

        self.result = pd.merge(self.df, self.product_list.loc[:, self.product_list.columns != "Nazwa Produktu"], on="ID Produktu") 
        self.result = self.result.rename(columns={self.df.columns[3]: 'Ilosc'})
    def __even_to_odd(self, value_str):
        value = int(value_str)
        if not value % 2 :
            if(value - 1 < 10):
                 return "0" + str(value - 1)
            else:
                return  str(value - 1)

        else:
            if(value - 1 < 10):
                 return "0" + str(value)
            else:
                return  str(value)
            
    def get_data4packing(self):#STAD BEDZIEMY ZBIERAC DANE NA TEMAT 2 ETAPU
        return self.result[["ID Produktu","Nazwa Produktu", "Ilosc", "Waga (kg)", "Wymiary (mm)"]]

    def get_df(self):
        return self.result
    
    def get_data4road(self): #STAD BEDZIEMY ZBIERAC DANE NA TEMAT 1 ETAPU
        dane = self.result[["ID Produktu","Nazwa Produktu", "Lokacja","Ilosc", "Waga (kg)"]].copy()
        dane["Lokacja"] = dane["Lokacja"].apply(lambda x: str(x[:4] + x[5:]))
        return dane