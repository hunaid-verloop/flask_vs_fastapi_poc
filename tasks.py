def compute_fibanocci(k: int):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return compute_fibanocci(k-1) + compute_fibanocci(k-2)