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
    write_file = 'lpn_update_num_2.txt'
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
    write_file = 'md5_num_2.txt'
    writef = open(write_file, 'w')
    writef = open(write_file, 'a')
    for key in sorted_key:
        writef.write(str(key) + ' ' + str(md5_num[key]) + '\n')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    file_name = '../traces/cheetah.cs.fiu.edu-110108-113008.2.blkparse'
    # 记录原始数据的lba、siz、typ、md5
    lba, siz, typ, md5 = [], [], [], []
    # 写命令的次数、读命令的次数、写blk的个数、读blk的个数、写唯一数据的blk个数、读唯一数据blk的个数、写入数据是重复数据的blk个数
    w_num, r_num, w_siz, r_siz, w_uniq, r_uniq, sam = 0, 0, 0, 0, 0, 0, 0
    # 每个lpn被更新的次数、每个md5码在写请求中要求写入的次数
    lpn, md5_n = {}, {}
    # 写入过的lba、读取过的lba、读写过的lba
    w_lba = set()
    r_lba = set()
    wr_lba = set()
    num = red(file_name)
    for i in range(num):
        lba_b = lba[i]
        lba_e = lba_b + siz[i]
        if typ[i] == 'W':
            w_num = w_num + 1
            w_siz = w_siz + siz[i]

            lpn_b = int(lba_b / 8)
            lpn_e = int(lba_e / 8)
            for j in range(lpn_b, lpn_e):
                if j in lpn:
                    lpn[j] = lpn[j] + 1
                else:
                    lpn[j] = 1
            if lpn_b == lpn_e:
                lpn[lpn_b] = lpn[lpn_b] + 1

            for j in range(lba_b, lba_e):
                w_lba.add(j)
                wr_lba.add(j)
                # t = int(j / 8)
                # if t in lpn:
                #     lpn[t] = lpn[t] + 1
                # else:
                #     lpn[t] = 1
            if md5[i] in md5_n:
                md5_n[md5[i]] = md5_n[md5[i]] + 1
                sam = sam + siz[i]
            else:
                md5_n[md5[i]] = 1
                w_uniq = w_uniq + siz[i]
        else:
            r_num = r_num + 1
            r_siz = r_siz + siz[i]
            for j in range(lba_b, lba_e):
                r_lba.add(j)
                wr_lba.add(j)
            if md5[i] in md5_n and md5_n[md5[i]] == 1:
                r_uniq = r_uniq + siz[i]

    write_file = 'res_2.txt'
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

    writef.write('负载重复数据的大小：' + str(sam * 1.0 / 2 / 1024 / 1024) + ' GB \n')

    lpn_update_times()
    md5_count()

