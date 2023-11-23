###第一题:
class Ship:
        
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20    
        
Titanic = Ship(15, 10)
print(Titanic.is_worth_it())

treasure_ship = Ship(35.1, 10)
print(treasure_ship.is_worth_it())
###第二题:
class Block(object):
    def __init__(self, wlh):
        self.w, self.l, self.h = w,l,h = wlh
        self.v = w*h*l
        self.a = 2 * (w*l + w*h + l*h)
    
    def get_width(self):        return self.w
    def get_length(self):       return self.l
    def get_height(self):       return self.h
    def get_volume(self):       return self.v
    def get_surface_area(self): return self.a
###第三题:
import math

class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)
    
    # 总页数
    def page_count(self):
        
        # 总条目数 / 每页条目数，然后向上取整
        return math.ceil(self.item_count() / self.items_per_page)
    
    def page_item_count(self, page_index):
        
        # 页数为负数或者页数超过总页数
        if page_index < 0 or page_index >= self.page_count():
            return -1

        # 最后一页
        elif page_index == self.page_count() - 1: 
            
            # 如果是6%4，那么最后一页就是2
            # 如果是8%4，那么最后一页就是0，说明最后一页是满的，应该返回4
            last_page = self.item_count() % self.items_per_page
            
            return self.items_per_page if last_page == 0 else last_page
        
        # 其他页
        else:
            return self.items_per_page
        
    def page_index(self, item_index):
        # 非法的情况
        if item_index < 0 or item_index >= self.item_count():
            return -1
        else:
            return item_index // self.items_per_page
###第四题:
from math import sqrt

class Vector:

    def __init__(self, iterable):
        self._v = tuple(x for x in iterable)

    # 把打印元组时的空格去掉
    def __str__(self):
        return str(self._v).replace(' ', '')
    
    # 检查两个向量是否长度相等    
    def check(self, other):
        if not len(self._v) == len(other._v):
            raise ValueError('Vectors of different length')

    def add(self, other):
        self.check(other)
        return Vector(s + o for s, o in zip(self._v, other._v))

    def subtract(self, other):
        self.check(other)
        return Vector(s - o for s, o in zip(self._v, other._v))

    def dot(self, other):
        self.check(other)
        return sum(s * o for s, o in zip(self._v, other._v))

    def norm(self):
        return sqrt(sum(pow(x,2) for x in self._v))

    def equals(self, other):
        return self._v == other._v
###第五题:
class User ():    
    def __init__ (self):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.rank_index = 0
        self.progress = 0
        
    def inc_progress (self, rank):
        rank_index = self.RANKS.index(rank)
        
        # 计算rank的差，得出可以获得多少进度
        
        # 完成的是同等级的题目
        if rank_index == self.rank_index:
            self.progress += 3
            
        # 完成的是比当前等级低一级的题目
        elif rank_index == self.rank_index - 1:
            self.progress += 1
            
        # 完成的是比当前等级高的题目
        elif rank_index > self.rank_index:
            difference = rank_index - self.rank_index
            self.progress += 10 * difference * difference
        
        if self.rank == 8:
                self.progress = 0
                return
        # 如果进度大于100，升级，每减去100进度，升一级    
        while self.progress >= 100:
            
            self.rank_index += 1
            self.rank = self.RANKS[self.rank_index]
            self.progress -= 100    
            
            if self.rank == 8:
                self.progress = 0
                return
        
            # 如果升到8级（最高级），进度被置为0