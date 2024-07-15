def writer(path="text.txt"):
    def _(callback):
        def __(*args, **kwargs):
            res = callback(*args, **kwargs)
            f = open(path, "w")
            f.write(res)
            # print("inside inner in writer decorator")
            f.close()

            return res

        return __

    return _


@writer(path="output.txt")
def process():
    return "MK112"


process()
