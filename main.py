import itertools
#関数従属集合の閉包を計算する
def closure(elems, fds):
    #２つの引数をset型に変更
    unused = set(fds)
    #反射を実行
    closure = set(elems)
    length = 0
    while length != len(closure):
        length = len(closure)
        #fdsの要素数でループ
        for i in range(0, len(fds)):
            #closureの中にfdsの要素があるかチェック
            # print(fds[i % len(fds)][0][0], fds[i % len(fds)][1])
            count = 0
            for j in range (0, len(fds[i % len(fds)][0])):
                if fds[i % len(fds)][0][j] in closure:
                    count += 1
            if count == len(fds[i % len(fds)][0]):
                #closureに該当要素の従属部分を追加
                closure.add(fds[i % len(fds)][1])
    return closure
if __name__ == "__main__":
    lis = ['A','B','C','D','E']
    f = open('result_closure.txt', 'w')
    for number in range(1,len(lis)+1):
        for elems in itertools.combinations(lis, number):
            fds = [("A","C"),("B","D"),("C","A"),(("A", "B"), "E"),(("A", "D", "E"),"B"),(("B", "E"), "C")]
            result = closure(elems,fds)
            for j in range(0, len(elems)):
                f.write(elems[j])
            f.write(" -> {")
            chara = []
            for i in range(1,len(list(result))+1):
                chara.append(list(result)[i-1])
            chara = sorted(chara)
            for i in range(1,len(chara)):
                f.write(chara[i-1])
                f.write(", ")
            string = [chara[len(chara)-1], "}", '\n']
            f.writelines(string)
