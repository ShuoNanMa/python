import pandas as pd

data = pd.read_csv(r'中国石油化工交易衍生指标2011-2019.csv', encoding='utf_16', sep='\t')
pb_dict = {}
for i in range(0, data.shape[0]):
    pb_dict[data['TradingDate'].iloc[i]] = round(data['PB'].iloc[i], 2)

print(pb_dict)


