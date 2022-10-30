# import the desired packages
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import string

updated_df = pd.read_excel('/Users/macbookpro/Desktop/OrderPay/Product Labelling using ML/Data/updated_pc_df.xlsx')
df_c1 = updated_df.loc[: ,['product_name', 'category_1']]
df_c2 = updated_df.loc[: ,['product_name', 'category_2']]
Gluten_free = ['gf', 'gluten free', '(gf)']

# Category 1
X_1 = df_c1['product_name']
Y_1 = df_c1['category_1']

model_1 = make_pipeline(TfidfVectorizer(binary = True, max_df = 0.1, norm = 'l2'),
                        MultinomialNB(alpha = 0.9, fit_prior = True))
model_1.fit(X_1, Y_1)

# Category 2
df_c2 = df_c2.dropna()
X_2 = df_c2['product_name']
Y_2 = df_c2['category_2']

model_2 = make_pipeline(TfidfVectorizer(binary = False, max_df = 0.1, norm = 'l1'),
                        MultinomialNB(alpha = 0.5, fit_prior = False))

model_2.fit(X_2, Y_2)

# Category 3
def model_3(X):
    cat_3 = []
    for row in X.values.ravel():
        if any(gf in row.upper() for gf in Gluten_free):
            cat_3.append('Gluten Free')
        else:
            cat_3.append('Not Gluten Free')
    return cat_3


def preprocess_products(L):
    product_names = L.copy()
    cleaned_product_name = []
    numbers = '0123456789'

    for product in product_names:
        product = product.lower()
        for word in product:
            if word in string.punctuation:
                product = product.replace(word, '')
            if word in numbers:
                product = product.replace(word, '')
        cleaned_product_name.append(product)

    df = pd.DataFrame(list(zip(cleaned_product_name, product_names)),
                columns=['CLEAN_PRODUCT_NAME', 'PRODUCT_NAME'])
    return df


def generate_categories(L):
    df = preprocess_products(L)
    product_name = df['CLEAN_PRODUCT_NAME']

    cat_1 = model_1.predict(product_name)
    cat_2 = model_2.predict(product_name)
    cat_3 = model_3(product_name)

    df.loc[:, 'CATEGORY_1'] = cat_1
    df.loc[:, 'CATEGORY_2'] = cat_2
    df.loc[:, 'CATEGORY_3'] = cat_3
    df = df.drop('CLEAN_PRODUCT_NAME', axis = 1)

    return df






