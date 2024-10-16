def change_case():
    str = input()
    str = ''.join("_"+c.lower() if c.isupper() else c for c in str)
    print(str)





change_case()