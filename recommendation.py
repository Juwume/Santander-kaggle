import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from tqdm import tqdm

from metrics import mapk
from utils import USER_ITEM_COLS, ITEM_COLS


def recommendation(user_id, df_train, hybrid_outcome):
    """
    Function that returns a list of recommendations for a given user.
    :param user_id: id of specific user
    :param df_train: Data about users that we already know
    :param hybrid_outcome:
    :return:
    """
    # products that the user already owns
    df_train = df_train[USER_ITEM_COLS]
    user_row = df_train[df_train.ncodpers == user_id]
    user_products = list(
        filter(lambda product: user_row[product].to_numpy()[0] == 1, user_row)
    )
    # removes products that the user already owns
    recom = {
        key: hybrid_outcome[key] for key in hybrid_outcome if key not in user_products
    }
    recom_sort = dict(sorted(recom.items(), key=lambda item: item[1], reverse=True))
    return list(recom_sort.keys())

def popularity_method(df):
    """
    Function that calculates the probability of a product occurring.
    Probability range is <0, 1>.
    """
    top_col = {}
    df = df[ITEM_COLS]
    for col in df.columns:
        top_col[col] = df[col].value_counts()[1]

    # sorted by most popular
    top_col = dict(sorted(top_col.items(), key=lambda it: it[1], reverse=True))

    for k, v in top_col.items():
        top_col[k] = np.around(v / df.shape[0], decimals=4)

    return top_col

def collaborative_method(df_train):
    # create the user-item similarity matrix
    # removes index names
    sim_matrix = 1 - pairwise_distances(df_train, metric="cosine")
    # computes the index in the user-item similarity matrix for a given user_id
    user_ids = df_train.
    user_indexes = list(df_train.index)
    cos_id = user_indexes.index(user_id)

    # number of similar users
    k = 0
    sim_min = 0.79
    user_sim_k = {}

    while k < 20:
        # creates the dictionary {'similar user':'similarity'}
        for user in range(len(df)):
            # 0.99 because I don`t want the same user as user_id
            if sim_min < sim_matrix[cos_id, user] < 0.99:
                user_sim_k[user] = sim_matrix[cos_id, user]
                k += 1
        sim_min -= 0.025
        # if there are no users with similarity at least 0.65, the recommendation probability will be set to 0
        if sim_min < 0.65:
            break
    # sorted k most similar users
    user_sim_k = dict(
        sorted(user_sim_k.items(), key=lambda item: item[1], reverse=True)
    )
    user_id_k = list(user_sim_k.keys())
    # dataframe with k most similar users
    df_user_k = df.iloc[user_id_k]
    df_user_k_T = df_user_k.T
    # change the user index to the cosine index
    df_user_k_T.columns = user_id_k
    # mean of ownership by k similar users
    ownership = []
    usit = {}
    for row_name, row in df_user_k_T.iterrows():
        for indx, own in row.items():
            ownership.append(own)

        usit[row_name] = np.mean(ownership)
        ownership = []
    # if there are no users with similarity at least 0.65, the recommendation probability is 0
    if pd.isna(list(usit.values())[0]) == True:
        usit = {key: 0 for (key, value) in usit.items()}

    return usit

def rec_test(user_id, df_train, df_test):
    """
    Function that returns a list of test recommendations for a given user.
    """
    actual, recom_test = [], []
    data_after = np.array(df_test[df_test.ncodpers == user_id][ITEM_COLS].values[0])
    try:
        data_before = np.array(
            df_train[df_train.ncodpers == user_id][ITEM_COLS].values[0]
        )
    except IndexError:
        return df_train[ITEM_COLS].columns[data_after.astype(bool)]

    for idx, col in enumerate(df_train[ITEM_COLS].columns):
        if data_before[idx] == 0 and data_after[idx] == 1:
            recom_test.append(col)

    return recom_test


def evaluation(df_train, df_test, popularity_outcome):
    """
    Function that returns the average precision metric for given users.
    """
    # Real purchased products

    #     print(y_real)
    # Recommended products

    actual, predicted = [], []
    users = df_test.ncodpers.unique()
    print(f"User amount: {len(users)}")
    for user_id in tqdm(users):
        #     hybrid_outcome = hybrid_recommend(df_train)
        # print(user_id)
        y_real = rec_test(user_id, df_train, df_test)
        predicted.append(recommendation(user_id, df_train, popularity_outcome))
        actual.append(y_real)
    #     print(y_pred)
    return mapk(actual, predicted)