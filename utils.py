# Constants
USER_ITEM_COLS = [
    "ncodpers",
    "ind_ahor_fin_ult1",
    "ind_aval_fin_ult1",
    "ind_cco_fin_ult1",
    "ind_cder_fin_ult1",
    "ind_cno_fin_ult1",
    "ind_ctju_fin_ult1",
    "ind_ctma_fin_ult1",
    "ind_ctop_fin_ult1",
    "ind_ctpp_fin_ult1",
    "ind_deco_fin_ult1",
    "ind_deme_fin_ult1",
    "ind_dela_fin_ult1",
    "ind_ecue_fin_ult1",
    "ind_fond_fin_ult1",
    "ind_hip_fin_ult1",
    "ind_plan_fin_ult1",
    "ind_pres_fin_ult1",
    "ind_reca_fin_ult1",
    "ind_tjcr_fin_ult1",
    "ind_valo_fin_ult1",
    "ind_viv_fin_ult1",
    "ind_nomina_ult1",
    "ind_nom_pens_ult1",
    "ind_recibo_ult1",
]
ITEM_COLS = [
    "ind_ahor_fin_ult1",
    "ind_aval_fin_ult1",
    "ind_cco_fin_ult1",
    "ind_cder_fin_ult1",
    "ind_cno_fin_ult1",
    "ind_ctju_fin_ult1",
    "ind_ctma_fin_ult1",
    "ind_ctop_fin_ult1",
    "ind_ctpp_fin_ult1",
    "ind_deco_fin_ult1",
    "ind_deme_fin_ult1",
    "ind_dela_fin_ult1",
    "ind_ecue_fin_ult1",
    "ind_fond_fin_ult1",
    "ind_hip_fin_ult1",
    "ind_plan_fin_ult1",
    "ind_pres_fin_ult1",
    "ind_reca_fin_ult1",
    "ind_tjcr_fin_ult1",
    "ind_valo_fin_ult1",
    "ind_viv_fin_ult1",
    "ind_nomina_ult1",
    "ind_nom_pens_ult1",
    "ind_recibo_ult1",
]

PRODUCT_NAMES = {
        "ind_ahor_fin_ult1": "Saving Account",
        "ind_aval_fin_ult1": "Guarantees",
        "ind_cco_fin_ult1": "Current Accounts",
        "ind_cder_fin_ult1": "Derivada Account",
        "ind_cno_fin_ult1": "Payroll Account",
        "ind_ctju_fin_ult1": "Junior Account",
        "ind_ctma_fin_ult1": "Más Particular Account",
        "ind_ctop_fin_ult1": "Particular Account",
        "ind_ctpp_fin_ult1": "Particular Plus Account",
        "ind_deco_fin_ult1": "Short-term Deposits",
        "ind_deme_fin_ult1": "Medium-term Deposits",
        "ind_dela_fin_ult1": "Long-term Deposits",
        "ind_ecue_fin_ult1": "E-account",
        "ind_fond_fin_ult1": "Funds",
        "ind_hip_fin_ult1": "Mortgage",
        "ind_plan_fin_ult1": "Pensions",
        "ind_pres_fin_ult1": "Loans",
        "ind_reca_fin_ult1": "Taxes",
        "ind_tjcr_fin_ult1": "Credit Card",
        "ind_valo_fin_ult1": "Securities",
        "ind_viv_fin_ult1": "Home Account",
        "ind_nomina_ult1": "Payroll",
        "ind_nom_pens_ult1": "Pensions",
        "ind_recibo_ult1": "Direct Debit",
    }
NUM_PROC = 4


def change_names(col_names, map_products=None):
    """
    Change column names (e.g."ind_recibo_ult1") to product names (e.g."Direct Debit").
    """
    if map_products is None:
        map_products = PRODUCT_NAMES
    return list(map(lambda col_name: map_products[col_name], col_names))