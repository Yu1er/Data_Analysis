import numpy as np
import matplotlib.pyplot as plt


def cal(b, e, type):
    temp = 0
    for i in range(b-1, e):
        if type == 1:
            temp = temp + lpn_nums[i]
        elif type == 2:
            temp = temp + md5_nums[i]
        elif type == 3:
            temp = temp + md5_noref_times[i]
        elif type == 4:
            temp = temp + durtime_count[i]
        elif type == 5:
            temp = temp + update_lpn_count[i]
        elif type == 6:
            temp = temp + rehit_durtime_count[i]
    return temp


def draw_lpn_update():
    file_name = './res/lpn_num.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        update_times.append(int(tmpline[0]))
        lpn_nums.append(int(tmpline[1]))
    tmp = 0
    max_times = update_times[-1]
    res = [0] * (max_times + 1)
    res1 = [0] * (max_times + 1)
    for i in range(len(update_times)):
        tmp = tmp + lpn_nums[i]
        res[i] = tmp
    for i in range(1, max_times+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    plt.plot([-100, max_times], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    plt.plot([53, 53], [0, 1], c='r', linestyle='--', linewidth=0.8)
    plt.plot(range(max_times+1), res1)
    # plt.plot([0, 60], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([52, 52], [0, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(0, 60), res1[0:60])
    plt.show()
    print(cal(1, 53, 1)/tmp)
    # tmp = sum(lpn_nums)
    # print(tmp)
    # resx = [1, 2, 3, 4, 5, 6]
    # resy = [0] * 6
    # resy[0] = cal(1, 5, 1) * 1.0 / tmp
    # resy[1] = cal(6, 15, 1) * 1.0 / tmp
    # resy[2] = cal(16, 35, 1) * 1.0 / tmp
    # resy[3] = cal(36, 55, 1) * 1.0 / tmp
    # resy[4] = cal(56, 80, 1) * 1.0 / tmp
    # resy[5] = cal(81, 478, 1) * 1.0 / tmp
    # print(resy)
    # print(sum(resy))
    # xlabels = ['1-5', '6-15', '16-35', '36-55', '56-80', '81-478']
    # plt.xticks(resx, xlabels)  # 设置横坐标
    # plt.bar(resx, resy, color="#5F9EA0", edgecolor='black', linewidth=0.8)
    # plt.show()


def draw_md5_ref():
    file_name = './res/md5_num.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        ref_times.append(int(tmpline[0]))
        md5_nums.append(int(tmpline[1]))
    tmp = 0
    maxx = ref_times[-1]
    res = [0] * (maxx + 1)
    res1 = [0] * (maxx + 1)
    for i in range(len(ref_times)):
        tmp = tmp + md5_nums[i]
        res[i] = tmp
    for i in range(1, maxx+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    # plt.plot([-100, maxx], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([1, 1], [0, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(maxx+1), res1)
    # print(res[0])
    plt.plot([0, 30], [0.8279303834004584, 0.8279303834004584], c='r', linestyle='--', linewidth=0.8)
    plt.plot([1, 1], [0, 1], c='r', linestyle='--', linewidth=0.8)
    plt.plot(range(0, 30), res1[0:30])
    plt.show()
    print(cal(1, 1, 2)/tmp)

    # tmp = sum(md5_nums)
    # print(tmp)
    # resx = [1, 2, 3, 4, 5, 6]
    # resy = [0] * 6
    # # resy[0] = cal(1, 1, 2) * 1.0 / tmp
    # resy[1] = cal(2, 2, 2) * 1.0 / tmp
    # resy[2] = cal(3, 10, 2) * 1.0 / tmp
    # resy[3] = cal(11, 80, 2) * 1.0 / tmp
    # resy[4] = cal(81, 250, 2) * 1.0 / tmp
    # resy[5] = cal(251, 586, 2) * 1.0 / tmp
    # print(resy)
    # print(sum(resy))
    # print(cal(1, 1, 2) * 1.0 / tmp)
    # xlabels = ['1', '2', '3-10', '11-80', '81-250', '251-586']
    # plt.xticks(resx, xlabels)  # 设置横坐标
    # plt.bar(resx, resy, color="#5F9EA0", edgecolor='black', linewidth=0.8)
    # plt.show()


def draw_md5_noref_times():
    file_name = './res/noref_rehit_num6.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        noref_times.append(int(tmpline[0]))
        md5_noref_times.append(int(tmpline[1]))
    tmp = 0
    maxx = noref_times[-1]
    res = [0] * (maxx + 1)
    res1 = [0] * (maxx + 1)
    for i in range(len(noref_times)):
        tmp = tmp + md5_noref_times[i]
        res[i] = tmp
    for i in range(1, maxx+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    # plt.plot([-20, maxx], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([2, 2], [0, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(maxx+1), res1)
    plt.plot([0, 30], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    plt.plot([2, 2], [0, 1], c='r', linestyle='--', linewidth=0.8)
    plt.plot(range(0, 30), res1[0:30])
    plt.show()
    print(cal(1, 3, 3)/tmp)

    # tmp = sum(md5_noref_times)
    # print(tmp)
    # resx = [1, 2, 3, 4, 5]
    # resy = [0] * 5
    # resy[0] = cal(1, 1, 4) * 1.0 / tmp
    # resy[1] = cal(2, 2, 4) * 1.0 / tmp
    # resy[2] = cal(3, 10, 4) * 1.0 / tmp
    # resy[3] = cal(11, 50, 4) * 1.0 / tmp
    # resy[4] = cal(51, len(md5_noref_times), 4) * 1.0 / tmp
    # print(resy)
    # print(sum(resy))
    # # print(cal(1, 1, 3) * 1.0 / tmp)
    # xlabels = ['1', '2', '3-10', '11-50', '51-final']
    # plt.xticks(resx, xlabels, rotation=20)  # 设置横坐标
    # plt.bar(resx, resy, color="#5F9EA0", edgecolor='black', linewidth=0.8)
    # plt.show()


def draw_durtime_count():
    file_name = './res/noref_hit_durtime6.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        durtime.append(int(tmpline[0]))
        durtime_count.append(int(tmpline[1]))
    tmp = 0
    maxx = durtime[-1]
    res = [0] * (maxx + 1)
    res1 = [0] * (maxx + 1)
    for i in range(len(durtime)):
        tmp = tmp + durtime_count[i]
        res[i] = tmp
    for i in range(1, maxx+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    # plt.plot([-20, maxx], [0.2, 0.2], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([19, 19], [0, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(maxx+1), res1)
    plt.plot([0, 300], [0.2579, 0.2579], c='r', linestyle='--', linewidth=0.8)
    plt.plot([75, 75], [0, 1], c='r', linestyle='--', linewidth=0.8)
    plt.plot(range(0, 300), res1[0:300])
    plt.show()
    print(cal(1, 75, 4)/tmp)
    # tmp = sum(durtime_count)
    # print(tmp)
    # resx = [1, 2, 3, 4, 5]
    # resy = [0] * 5
    # resy[0] = cal(1, 1000, 3) * 1.0 / tmp
    # resy[1] = cal(1001, 30000, 3) * 1.0 / tmp
    # resy[2] = cal(30001, 60000, 3) * 1.0 / tmp
    # resy[3] = cal(60001, 90000, 3) * 1.0 / tmp
    # resy[4] = cal(90001, len(durtime_count), 3) * 1.0 / tmp
    # print(resy)
    # print(sum(resy))
    # # print(cal(1, 1, 3) * 1.0 / tmp)
    # xlabels = ['1-1000', '1001-30000', '30001-60000', '60001-90000', '90001-final']
    # plt.xticks(resx, xlabels, rotation=20)  # 设置横坐标
    # plt.bar(resx, resy, color="#5F9EA0", edgecolor='black', linewidth=0.8)
    # plt.show()


def draw_update_lpn_count():
    file_name = './res/noref_hit_lpnupdate6.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        last_lpn_update.append(int(tmpline[0]))
        update_lpn_count.append(int(tmpline[1]))
    tmp = 0
    maxx = last_lpn_update[-1]
    res = [0] * (maxx + 1)
    res1 = [0] * (maxx + 1)
    for i in range(len(last_lpn_update)):
        tmp = tmp + update_lpn_count[i]
        res[i] = tmp
    for i in range(1, maxx+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    # plt.plot([-20, maxx], [0.2, 0.2], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([19, 19], [0, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(maxx+1), res1)
    plt.plot([0, 300], [0.923, 0.923], c='r', linestyle='--', linewidth=0.8)
    plt.plot([80, 80], [0, 1], c='r', linestyle='--', linewidth=0.8)
    plt.plot(range(0, 300), res1[0:300])
    plt.show()
    print(cal(1, 50, 5)/tmp)
    # tmp = sum(update_lpn_count)
    # print(tmp)
    # resx = [1, 2, 3, 4, 5]
    # resy = [0] * 5
    # resy[0] = cal(1, 20, 5) * 1.0 / tmp
    # resy[1] = cal(21, 50, 5) * 1.0 / tmp
    # resy[2] = cal(51, 1000, 5) * 1.0 / tmp
    # resy[3] = cal(1001, 3000, 5) * 1.0 / tmp
    # resy[4] = cal(1001, len(update_lpn_count), 5) * 1.0 / tmp
    # print(resy)
    # print(sum(resy))
    # # print(cal(1, 1, 3) * 1.0 / tmp)
    # xlabels = ['1-20', '21-50', '51-1000', '1001-3000', '3001-final']
    # plt.xticks(resx, xlabels, rotation=20)  # 设置横坐标
    # plt.bar(resx, resy, color="#5F9EA0", edgecolor='black', linewidth=0.8)
    # plt.show()


def draw_rehit_durtime_count():
    file_name = './res/rehit_durtime6.txt'
    readf = open(file_name)
    for line in readf:
        tmpline = line.strip().split(' ')
        rehit_durtime.append(int(tmpline[0]))
        rehit_durtime_count.append(int(tmpline[1]))
    tmp = 0
    maxx = rehit_durtime[-1]
    res = [0] * (maxx + 1)
    res1 = [0] * (maxx + 1)
    for i in range(len(rehit_durtime)):
        tmp = tmp + rehit_durtime_count[i]
        res[i] = tmp
    for i in range(1, maxx+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp

    # plt.plot([0, 500], [0.0637, 0.0637], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([100, 100], [0, 0.1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([0, 40000], [0.204, 0.204], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([23000, 23000], [0, 0.3], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([0, 800000], [0.8, 0.8], c='r', linestyle='--', linewidth=0.8)
    # plt.plot([170000, 170000], [0.5, 1], c='r', linestyle='--', linewidth=0.8)
    # plt.plot(range(0, 800000), res1[0:800000])
    plt.plot(range(0, 50000), res1[0:50000])
    plt.show()
    print(cal(1, 100, 6)/tmp)
    print(cal(1, 23000, 6) / tmp)
    print(cal(1, 170000, 6) / tmp)



if __name__ == '__main__':
    # lpn更新次数、该更新次数的lpn有几个
    update_times, lpn_nums = [], []
    # draw_lpn_update()

    # md5引用次数、该引用次数的md5有几个
    ref_times, md5_nums = [], []
    # draw_md5_ref()

    # 成为未引用数据的次数、有几个成为未引用数据的md5码
    noref_times, md5_noref_times = [], []
    # draw_md5_noref_times()

    # 重删间隔、有几个这样的重删间隔
    durtime, durtime_count = [], []
    # draw_durtime_count()

    # 未被引用的数据再次命中时其变为未引用数据前的最后一个lpn的更新次数、有几个这么多更新次数的lpn
    last_lpn_update, update_lpn_count = [], []
    # draw_update_lpn_count()

    # 重命中的间隔、有多少个这么长间隔的重命中
    rehit_durtime, rehit_durtime_count = [], []
    draw_rehit_durtime_count()



    """
    tmp = 0
    max_times = update_times[-1]
    res = [0] * (max_times + 1)
    res1 = [0] * (max_times + 1)
    for i in range(len(update_times)):
        tmp = tmp + lpn_nums[i]
        res[i] = tmp
    for i in range(1, max_times+1):
        if res[i] == 0:
            res[i] = res[i-1]
        res1[i] = res[i] * 1.0 / tmp
    plt.plot(range(max_times+1), res1)
    plt.show()
    """
