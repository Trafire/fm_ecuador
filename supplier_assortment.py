import excel_to_dict


def get_assort(filename):
    product = excel_to_dict.get_dict_gen(filename)
    print(product)

get_assort('assortment/vanzanten_assort.xlsx')