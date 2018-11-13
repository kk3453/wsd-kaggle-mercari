import pandas as pd

def split_category_name(df):
    df_category = df['category_name'].str.split('/',n=2,expand=True)
    df_category.columns = ['category1', 'category2', 'category3']
    df = df.drop(['category_name'], axis=1)
    df = pd.concat([df, df_category], axis=1)

    return df

if __name__ == '__main__':
    # データタイプを指定
    types_dict_train = {'train_id':'int64', 'item_condition_id':'int8', 'price':'float64', 'shipping':'int8'}
    types_dict_test = {'test_id':'int64', 'item_condition_id':'int8', 'shipping':'int8'}

    # tsvファイルからPandas DataFrameへ読み込み
    train = pd.read_table('train.tsv',dtype=types_dict_train)
    test = pd.read_table('test.tsv',dtype=types_dict_test)
    #train = pd.read_table('train_5line.tsv',dtype=types_dict_train)
    #test = pd.read_table('test_5line.tsv',dtype=types_dict_test)

    print(split_category_name(train))