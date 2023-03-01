def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = list(filter(lambda x: x % 2 == 1, kwargs["odd"]))

    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
