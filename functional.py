def sequential_map(*args):
    return func_chain(*args[:-1])(args[-1])


def consensus_filter(*args):
    container = args[-1]

    for func in args[:-1]:
        container = filter(func, container)

    return list(container)


def conditional_reduce(func1, func2, container):
   filt_container = list(filter(func1, container))
   len_ = len(filt_container)

   if len_ <= 1:
       raise Exception('Not enough data for function 2')
   else:
       while len(filt_container) >= 2:
           filt_container = [func2(*filt_container[:2])] + filt_container[2:]

   return filt_container[0]


def func_chain(*args):
    def apply_funcs(container):
        try:
            iter(container)
        except TypeError:
            container = [container]

        for func in args:
            container = map(func, container)

        return list(container)

    return apply_funcs


def multiple_partial(*args, **kwargs):
    funcs = []
    options = []
    new_funcs = []
    for arg in args:
        try:
            if type(arg) == type(multiple_partial):
                funcs.append(arg)
            else:
                options.append(arg)
        except TypeError:
            options.append(arg)

    for func in funcs:

        def partial(func, /, *args, **keywords):
            def newfunc(*fargs, **fkeywords):
                newkeywords = {**keywords, **fkeywords}
                return func(*args, *fargs, **newkeywords)
            newfunc.func = func
            newfunc.args = args
            newfunc.keywords = keywords
            return newfunc

        new_funcs.append(partial(func, *options, **kwargs))

    if len(new_funcs) == 1:
        return new_funcs[0]
    else:
        return new_funcs
