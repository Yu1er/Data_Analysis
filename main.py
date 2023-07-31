# -*- coding:utf-8 -*-

def red(file_name):
    readf = open(file_name)
    num = 0
    for line in readf:
        tmpline = line.strip().split(' ')
        lba.append(int(tmpline[3]))
        siz.append(int(tmpline[4]))
        typ.append(tmpline[5])
        md5.append(tmpline[8])
        num = num + 1
    return num


def lpn_update_times():
    lpn_num = {}  # 统计每个lpn被更新的次数的个数，即比如被更新4次的lpn有几个
    for key in lpn:
        nums = lpn[key]
        if nums in lpn_num:
            lpn_num[nums] = lpn_num[nums] + 1
        else:
            lpn_num[nums] = 1
    sorted_key = sorted(lpn_num)
    # print(sorted_key)
    write_file = 'lpn_update_num_' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(lpn_num[key]) + '\n')


def md5_count():
    md5_num = {}  # 统计每个md5被引用的次数的个数，即比如被引用4次的md5码有几个
    for key in md5_n:
        nums = md5_n[key]
        if nums in md5_num:
            md5_num[nums] = md5_num[nums] + 1
        else:
            md5_num[nums] = 1
    sorted_key = sorted(md5_num)
    # print(sorted_key)
    write_file = 'md5_num_' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(md5_num[key]) + '\n')


def noref_rehit_count():
    noref_rehit_num = {}  # 统计 未被引用的数据被重新命中的次数的个数，即比如 4次成为未被引用数据后重新命中的 md码有几个
    for key in noref_hit_md5:
        nums = noref_hit_md5[key]
        if nums in noref_rehit_num:
            noref_rehit_num[nums] = noref_rehit_num[nums] + 1
        else:
            noref_rehit_num[nums] = 1
    sorted_key = sorted(noref_rehit_num)
    # print(sorted_key)
    write_file = 'noref_rehit_num' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(noref_rehit_num[key]) + '\n')


def noref_hit_durtime_count():
    sorted_key = sorted(noref_hit_durtime)
    # print(sorted_key)
    write_file = 'noref_hit_durtime' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(noref_hit_durtime[key]) + '\n')


def noref_hit_lpnupdate_count():
    sorted_key = sorted(noref_hit_lpnupdate)
    # print(sorted_key)
    write_file = 'noref_hit_lpnupdate' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(noref_hit_lpnupdate[key]) + '\n')


def cold_in_hit_count():
    cold_in_hit_times = {}  # 统计 以cold-lpn写入后命中的次数 的个数，即比如 以cold-lpn写入 且 命中4次的 md码有几个
    for key in cold_in_hit:
        nums = cold_in_hit[key]
        if nums in cold_in_hit_times:
            cold_in_hit_times[nums] = cold_in_hit_times[nums] + 1
        else:
            cold_in_hit_times[nums] = 1
    sorted_key = sorted(cold_in_hit_times)
    # print(sorted_key)
    write_file = 'cold_in_hit_num' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(cold_in_hit_times[key]) + '\n')
    print('以cold-LPN写入的数据:' + str(len(cold_in_md5) * 8.0 / 2 / 1024 / 1024) + 'GB\n')
    print('以cold-LPN写入且命中的数据:' + str(len(cold_in_hit) * 8.0 / 2 / 1024 / 1024) + 'GB\n')


def cold_hot_percent(p):
    hlpn_hmd5, clpn_hmd5, hlpn_cmd5, clpn_cmd5 = 0, 0, 0, 0
    for key in lpn_to_md5:
        data = lpn_to_md5[key]
        if lpn[key] <= int(lpn_thresh):
            if md5_ref_live[data] <= int(md5_thresh):
                clpn_cmd5 = clpn_cmd5 + 1
            else:
                clpn_hmd5 = clpn_hmd5 + 1
        else:
            if md5_ref_live[data] <= int(md5_thresh):
                hlpn_cmd5 = hlpn_cmd5 + 1
            else:
                hlpn_hmd5 = hlpn_hmd5 + 1
    sum0 = clpn_cmd5 + clpn_hmd5 + hlpn_cmd5 + hlpn_hmd5
    write_file = 'cold_hot_percent_' + x + '.txt'
    writef = open(write_file, 'a')
    writef.write('At ' + p + '\n')
    writef.write('hot_lpn-hot_md5:' + str(hlpn_hmd5) + '  percent:' + str(hlpn_hmd5 * 1.0 / sum0) + '\n')
    writef.write('cold_lpn-hot_md5:' + str(clpn_hmd5) + '  percent:' + str(clpn_hmd5 * 1.0 / sum0) + '\n')
    writef.write('hot_lpn-cold_md5:' + str(hlpn_cmd5) + '  percent:' + str(hlpn_cmd5 * 1.0 / sum0) + '\n')
    writef.write('cold_lpn-cold_md5:' + str(clpn_cmd5) + '  percent:' + str(clpn_cmd5 * 1.0 / sum0) + '\n\n')


def rehit_durtime_count():
    sorted_key = sorted(rehit_durtime)
    # print(sorted_key)
    write_file = 'rehit_durtime' + x + '.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(rehit_durtime[key]) + '\n')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    x = str(input('file:'))
    open('cold_hot_percent_' + x + '.txt', 'w')
    lpn_thresh = input('lpn_thresh:')
    md5_thresh = input('md5_thresh:')
    file_name = '../traces/cheetah.cs.fiu.edu-110108-113008.' + x + '.blkparse'
    # 记录原始数据的lba、siz、typ、md5
    lba, siz, typ, md5 = [], [], [], []
    # 写命令的次数、读命令的次数、写blk的个数、读blk的个数、写唯一数据的blk个数、读唯一数据blk的个数、写入数据是重复数据的blk个数
    w_num, r_num, w_siz, r_siz, w_uniq, r_uniq, sam = 0, 0, 0, 0, 0, 0, 0
    # 每个lpn被更新的次数、每个md5码在写请求中要求写入的次数、lpn到md5的映射表、md5码实时的引用次数、md5码的引用次数变为0的时间
    lpn, md5_n, lpn_to_md5, md5_ref_live, md5_noref_time = {}, {}, {}, {}, {}
    # "未被引用的数据"又被命中时与它成为未被引用数据的间隔、有哪些md5码成为"未被引用的数据"后又被命中、md5成为未引用数据前最后一次写入的lpn、未被引用数据重新命中时md5之前最后一个对应的lpn的更新次数
    noref_hit_durtime, noref_hit_md5, md5_to_lpn, noref_hit_lpnupdate = {}, {}, {}, {}
    # 首次以cold_LPN写入的md5码、以cold-lpn写入并被hit的次数(变为未引用数据前)
    cold_in_md5, cold_in_hit, hot_in_md5 = {}, {}, {}
    # 相同数据上一次写入的时候的时间、两个重复数据间写入了多少数据
    rehit_time, rehit_durtime = {}, {}
    # md5码对应的md5-lpn指纹无效但是md5码又被命中的次数
    invalid_hit = 0
    zw_md5_lpn, zw_lpn_md5 = {}, {}
    # 写入过但是此时未被引用的数据又被命中的次数、总共产生过的“未被引用的数据”
    noref_hit_times, noref_num = 0, 0
    # 写入过的lba、读取过的lba、读写过的lba
    w_lba = set()
    r_lba = set()
    wr_lba = set()
    # 记录这是第几个写命令
    wi = 0
    num = red(file_name)
    for i in range(num):
        lba_b = lba[i]
        lba_e = lba_b + siz[i]
        md5_now = md5[i]
        if typ[i] == 'W':
            wi = wi + 1
            w_num = w_num + 1
            w_siz = w_siz + siz[i]
            for j in range(lba_b, lba_e):
                w_lba.add(j)
                wr_lba.add(j)
            if md5[i] in md5_n:
                if md5_ref_live[md5_now] == 0:  # 当前要写入的md5码被写入过，但是此时的引用次数为0
                    noref_hit_times = noref_hit_times + 1
                    if md5_now in noref_hit_md5:
                        noref_hit_md5[md5_now] = noref_hit_md5[md5_now] + 1
                    else:
                        noref_hit_md5[md5_now] = 1

                    dt = wi - md5_noref_time[md5_now]
                    if dt in noref_hit_durtime:
                        noref_hit_durtime[dt] = noref_hit_durtime[dt] + 1
                    else:
                        noref_hit_durtime[dt] = 1

                    last_lpn = md5_to_lpn[md5_now]
                    last_lpn_update = lpn[last_lpn]
                    if last_lpn_update in noref_hit_lpnupdate:
                        noref_hit_lpnupdate[last_lpn_update] = noref_hit_lpnupdate[last_lpn_update] + 1
                    else:
                        noref_hit_lpnupdate[last_lpn_update] = 1
                    md5_to_lpn[md5_now] = lba_b / 8

                if (lba_b / 8 not in lpn_to_md5) or (lpn_to_md5[lba_b / 8] != md5_now):  # 只有当原来这个lpn中的内容不是md5时引用计数才增加
                    md5_ref_live[md5_now] = md5_ref_live[md5_now] + 1
                md5_n[md5_now] = md5_n[md5_now] + 1
                sam = sam + siz[i]

                dt = wi - rehit_time[md5_now]
                rehit_time[md5_now] = wi
                if dt in rehit_durtime:
                    rehit_durtime[dt] = rehit_durtime[dt] + 1
                else:
                    rehit_durtime[dt] = 1

                if zw_md5_lpn[md5_now] == -1:  # 如果当前写入的md5的md5-lpn映射是无效的，则本次写入看作是第一次写入，更新md5-lpn映射
                    zw_md5_lpn[md5_now] = lba_b / 8
                    invalid_hit = invalid_hit + 1
                if lba_b / 8 in zw_lpn_md5:
                    old_md5 = zw_lpn_md5[lba_b / 8]
                    zw_lpn_md5[old_md5] = -1
                zw_lpn_md5[lba_b / 8] = md5_now

                if (md5_now in cold_in_md5) and (
                        md5_now not in md5_noref_time):  # 如果当前的md5码在这个md5_noref_time中说明曾经成为过未引用数据
                    #
                    if md5_now in cold_in_hit:
                        cold_in_hit[md5_now] = cold_in_hit[md5_now] + 1
                    else:
                        cold_in_hit[md5_now] = 1
            else:
                md5_n[md5_now] = 1
                md5_ref_live[md5_now] = 1
                w_uniq = w_uniq + siz[i]
                rehit_time[md5_now] = wi  # 第一次写入时记录写入的时间
                zw_md5_lpn[md5_now] = lba_b / 8  # md5码第一次写入时会记录md5-lpn映射
                if lba_b / 8 in zw_lpn_md5:
                    old_md5 = zw_lpn_md5[lba_b / 8]
                    zw_md5_lpn[old_md5] = -1
                zw_lpn_md5[lba_b / 8] = md5_now

            lpn_b = int(lba_b / 8)
            lpn_e = int(lba_e / 8)
            if md5_now not in md5_to_lpn:
                md5_to_lpn[md5_now] = lpn_b  # 如果该md5只在第一次写入时被引用，则这个lpn就是成为未引用数据前的最后一个lpn
            for j in range(lpn_b, lpn_e):
                if j in lpn:
                    # lpn[j] = lpn[j] + 1
                    md5_bef = lpn_to_md5[j]
                    if md5_bef != md5_now:  # 当前要写入的lpn有对应的md5，但是和当前要写入的md5不一样（即lpn被更新为其他数据），此时要将原md5的引用数量减1
                        lpn[j] = lpn[j] + 1
                        md5_ref_live[md5_bef] = md5_ref_live[md5_bef] - 1
                        if md5_ref_live[md5_bef] == 0:
                            noref_num = noref_num + 1
                            md5_noref_time[md5_bef] = wi  # 成为未被引用的数据的时间
                            # md5_to_lpn[md5_bef] = lpn_b  # md5在成为未引用数据前的最后一个对应的lpn
                else:
                    lpn[j] = 1
                lpn_to_md5[j] = md5_now
            if lpn_b == lpn_e:
                lpn[lpn_b] = lpn[lpn_b] + 1

            if (md5_n[md5_now] == 1) and (lpn[lpn_b] <= lpn_thresh):  # 以cold-lpn写入
                cold_in_md5[md5_now] = 1

        else:
            r_num = r_num + 1
            r_siz = r_siz + siz[i]
            for j in range(lba_b, lba_e):
                r_lba.add(j)
                wr_lba.add(j)
            if md5[i] in md5_n and md5_n[md5[i]] == 1:
                r_uniq = r_uniq + siz[i]

        if i == num / 4:
            cold_hot_percent('25%')
        elif i == num / 2:
            cold_hot_percent('50%')
        elif i == num / 4 * 3:
            cold_hot_percent('75%')
        elif i == num - 1:
            cold_hot_percent('100%')

    write_file = 'res_' + x + '.txt'
    writef = open(write_file, 'w')
    writef.write('写次数：' + str(w_num) + '\n')
    writef.write('读次数：' + str(r_num) + '\n\n')

    writef.write('负载数据集写入：' + str(w_siz * 1.0 / 2 / 1024 / 1024) + ' GB\n')
    writef.write('负载数据集读取：' + str(r_siz * 1.0 / 2 / 1024 / 1024) + ' GB\n')
    writef.write('负载数据集读写总共：' + str((w_siz + r_siz) * 1.0 / 2 / 1024 / 1024) + ' GB\n\n')

    writef.write('负载工作集写lba:' + str(len(w_lba)) + '\n')
    writef.write('负载工作集读lba:' + str(len(r_lba)) + '\n')
    writef.write('负载工作集读写总lba:' + str(len(wr_lba)) + '\n\n')

    writef.write('负载读写比IOPS:' + str(r_num * 1.0 / w_num) + '\n')
    writef.write('负载读写比bandwidth:' + str(r_siz * 1.0 / w_siz) + '\n\n')

    writef.write('平均写请求大小：' + str(w_siz * 512 * 1.0 / w_num) + ' B \n')
    writef.write('平均读请求大小：' + str(r_siz * 512 * 1.0 / r_num) + ' B \n\n')

    writef.write('写入的数据是唯一数据的大小：' + str(w_uniq * 1.0 / 2 / 1024 / 1024) + ' GB \n')
    writef.write('读取的数据是唯一数据的大小：' + str(r_uniq * 1.0 / 2 / 1024 / 1024) + ' GB \n\n')

    writef.write('负载重复数据的大小：' + str(sam * 1.0 / 2 / 1024 / 1024) + ' GB \n\n\n')

    writef.write(
        '产生过的"未被引用的数据"(一个md5码多次变为"未被引用的数据"则单次计数)：' + str(len(md5_noref_time) * 8.0 / 2 / 1024 / 1024) + ' GB \n')
    writef.write('产生过的"未被引用的数据"(一个md5码多次变为"未被引用的数据"则多次计数)：' + str(noref_num * 8.0 / 2 / 1024 / 1024) + ' GB \n')
    writef.write('"未被引用的数据"被用于重删：' + str(noref_hit_times * 8.0 / 2 / 1024 / 1024) + ' GB \n')
    writef.write('"未被引用的数据"被用于重删的几率("未被引用的数据"被用于重删/产生过的"未被引用的数据")：' + str(noref_hit_times * 1.0 / noref_num) + ' \n')

    print('lba更新后其指纹被再次命中的概率(/总数据量)：' + str(invalid_hit * 8.0 / w_siz) + ' \n')
    print('lba更新后其指纹被再次命中的概率(/重复数据量)：' + str(invalid_hit * 8.0 / sam) + ' \n')

    lpn_update_times()
    md5_count()
    noref_rehit_count()
    noref_hit_durtime_count()
    noref_hit_lpnupdate_count()
    cold_in_hit_count()
    rehit_durtime_count()
