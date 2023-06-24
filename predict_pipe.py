import pandas as pd
import numpy as np
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from metrics import mapk
from tqdm import tqdm
from sklearn.metrics.pairwise import pairwise_distances
from utils import USER_ITEM_COLS, ITEM_COLS, NUM_PROC, change_names



















def main():

    data = pd.read_csv("data/train_ver2.csv")
    df_train_0716 = data[data.fecha_dato == "2015-07-28"]
    df_test_0816 = data[data.fecha_dato == "2015-08-28"][:11]
    popularity_outcome = popularity_based(df_train_0716)
    with ProcessPoolExecutor(max_workers=NUM_PROC) as executor:
        # Set all but one worker making salads
        futures = []
        # executor._shutdown_thread = True
        for idx in range(NUM_PROC):
            futures.append(
                executor.submit(
                    evaluation,
                    df_train_0716,
                    df_test_0816[
                        int(len(df_test_0816) / NUM_PROC * idx) : int(
                            len(df_test_0816) / NUM_PROC * (idx + 1)
                        )
                    ],
                    popularity_outcome,
                )
            )
        done, not_done = wait(futures, return_when=ALL_COMPLETED)
        # print(done)
        # print(futures)
        # for future in futures:
        #     print(future.result())
        for future in done:
            # получаем результат
            result = future.result()
            print(f"Результат {result}")


if __name__ == "__main__":
    main()
