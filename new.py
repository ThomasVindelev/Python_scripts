def foo_bar(n, d):

    """Loops through dictionary"""

    for i in range(n + 1):
        msg = ""
        for k, v in d.items():
            if i % k == 0:
                msg += v
        if not msg:
            print(i)
        else:
            print(msg)


def foo_bar_optimized(n, d):
    for i in range(n + 1):
        msg = ""
        for k, v in d.items():
            if i % k == 0:
                msg += v
        print(msg or i)

dictionary = {
    3: "Foo",
    4: "Buz",
    5: "Bar",
    7: "Fiz"
}

foo_bar(25, dictionary)

help(foo_bar)