# data_list = [1, 2, 3, 4, 5, 6]
#
# data_list = [num for num in range(0, 500000)]  # 500,000 items
#
# interestin_points = [num for num in range(0, 100)]  # 100 items
#
#
# for i in interestin_points:
#     pt = find_point_by_id_in_list(data_list, i)
#     interestin_points.append(pt)
#
#
import collections
import datetime
import random

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


def main():
    print("Creatin data..")

    # sys.stdout.flush()

    data_list = []
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))

    print("\nDone")

    # sys.stdout.flush()

    print("Simulating randomized data ....")
    # sys.stdout.flush()

    data_list.sort(key=lambda d: d.quality)

    print("Done.")

    # Create a list of random ID's to locate without duplication

    interesting_ids = list({random.randint(0, len(data_list)) for _ in range(0, 100)})
    print("Creating {} interesting ID's to seek.".format(len(interesting_ids)))

    print("Locating data in list....")
    # sys.stdout.flush()

    t0 = datetime.datetime.now()
    interesting_points = []
    for i in interesting_ids:
        pt = find_point_by_id_in_list(data_list, i)
        interesting_points.append(pt)

    t1 = datetime.datetime.now()
    dt_list = (t1 - t0).total_seconds()

    print("Done")
    # sys.stdout.flush()

    print("DT: {} sec".format(dt_list))

    print("Creating dictionary...")
    data_lookup = {d.id: d for d in data_list}

    print("Done")

    print("Locating data in dictionary....")

    t0 = datetime.datetime.now()
    interesting_points = []
    for i in interesting_ids:
        item = data_lookup[i]
        interesting_points.append(item)
    # use data_lookup to find by id, add to intersting_points

    t1 = datetime.datetime.now()
    dt_dict = (t1 - t0).total_seconds()

    print("Done")
    # sys.stdout.flush()

    print("DT: {} sec".format(dt_list))
    # print(interesting_points)
    print("Speedup from dict: {:,.0f}x".format(round(dt_list / dt_dict)))


def find_point_by_id_in_list(data_list, i):
    for d in data_list:
        if d.id == i:
            return d

    return None


if __name__ == '__main__':
    main()
