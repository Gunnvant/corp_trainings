def get_cat(val):
    if val > 5000:
        return "high"
    elif val<=5000 and val>2000:
        return "medium"
    else:
        return "low"