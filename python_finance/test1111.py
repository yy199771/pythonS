# coding:utf-8
# 构建双边队列
class Deque():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    #插入元素，在头插入
    def addFront(self, item):
        self.items.append(item)
    #插入元素，在尾插入
    def addRear(self, item):
        self.items.insert(0, item)
    #去头，返回头元素的值
    def removeFront(self):
        return self.items.pop()
    #去尾，返回尾元素的值
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

#检测是否是回文
def Palindrome_checker(aString):

    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    flag = True
    #首位呼应弹出，并比较大小，直到剩下一个或0个元素为止
    while flag and chardeque.size() > 1:
        if chardeque.removeRear() != chardeque.removeFront():
            flag = False
    return flag

print Palindrome_checker('shittihs')
print Palindrome_checker('fkda')