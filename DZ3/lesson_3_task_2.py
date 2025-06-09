from smartphone import Smartphone


smartphone1 = Smartphone('Meizu', 'X8', '+79064860000')
smartphone2 = Smartphone('Xiaomi', 'Redmi Note 8', '+79286950000')
smartphone3 = Smartphone('OPPO', 'A31', '+79287410000')
smartphone4 = Smartphone('Samsung', 'A31', '+79287460000')
smartphone5 = Smartphone('Huawei', 'P40', '+79289170000')
catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for smartphone in catalog:
    print(smartphone)
