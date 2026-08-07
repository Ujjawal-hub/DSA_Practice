class Key:

    def __init__(self,name,value = None):

        self.value = value
        self.keyname = name

    def __str__(self):

        return str(self.keyname)


class Hash_Table:

    def __init__(self, capacity):

        self._list1 = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def hash(self, keyname):

        return hash(keyname) % self.capacity

    # for the add function it will go on for looking empty space if it finds in the
    # first look then this operation is BigO(1) in time , if not then it will
    # keep looking result in time get closer to BigO(n) it tells the importance of
    # hashfunction ,hashfunction should give indexs such get each key get gets differnt
    # index as much as possible ,it saves time this method does not take care of updating value neiher uniquness of key

    # def add(self,keyname,value):

    #     if self.size < self.capacity:
    #         key = Key(keyname,value)

    #         index = self.hash(keyname)

    #         while True:

    #             a = self._list1[index]

    #             if a == None or (isinstance(a,str) and "None" in a) :

    #                 self._list1[index] =  key

    #                 break

    #             index = (index +1)%self.capacity

    #         self.size += 1
    #     else:

    #         print("no seats available")

    # in the below add implemaentaion i have take care of uniqueness of key and updating upon
    # finding same key which make this operation BigO(n) because it had look entire list ,
    # rather than just directly strat looking from index which hash fuction gives because
    # for example suppose you add hello , upon adding it looks and space is occupied by say
    # jello, now hello will find next index and add it there, now you remove jello, now that
    # space occupied by dummy key, now add hello again so this time it will directly go see
    # space is occupied by dummy key so it replace the dummy key with itself and program stop
    # here it did not even has a chance to check if another hello is stored somewhere else,
    # it hoped if there was hello it will update it and it should have existed in its hash
    # index ,but unfortunately first hello gets jump to another index
    # so second hello did not even have the chace to check, because it get index it first go.
    # to solve this issue you have to check entire list of same key before adding

    # Because you scan the entire table first checking for duplicates before inserting.  The cost of correctness with linear probing is BigO(n) you can't know a duplicate doesn't exist without checking everything between the hash index and the next None.

    # But real hash tables are O(1) average — here's why:

    # The key assumption is low load factor — meaning the table is mostly empty. If your table has 100 slots and only 10 items, collisions are rare. Most operations find their slot in 1-2 probes on average.

    # So O(1) average is a statistical claim, not a guaranteed claim. It holds when:

    # Hash function distributes keys evenly
    # Table isn't too full (load factor typically kept below 0.7)

    # When the table gets full, everything degrades toward O(n) — which is exactly why real hash tables resize when load factor gets too high.

    def add(self, keyname, value):

        index = self.hash(keyname)

        i = index

        c = True

        while True:

            a = self._list1[i]

            if isinstance(a, Key):

                if a.keyname == keyname:
                    a.value = value

                    c = False

                    break

            elif a == None:

                break

            i = (i + 1) % self.capacity

            if i == index:
                break

        if c:

            if self.size < self.capacity:
                key = Key(keyname, value)

                index = self.hash(keyname)

                while True:

                    a = self._list1[index]

                    if a == None or (isinstance(a, str) and "None" in a):
                        self._list1[index] = key

                        break

                    index = (index + 1) % self.capacity

                self.size += 1
            else:

                print("no seats available")

    # this exists function will look at the name try to find the index asociate with it,
    # if it finds in the fisrst place then this operation is BigO(1)
    # other wise it will keep lokking till it find then this opreation will get to BigO(n)
    def exists(self, keyname):

        index = self.hash(keyname)

        i = index

        while True:

            a = self._list1[i]

            if isinstance(a, Key):

                if a.keyname == keyname:
                    return True

            elif a == None:

                return False

            i = (i + 1) % self.capacity

            if i == index:
                return False

    def get(self, keyname):

        index = self.hash(keyname)

        i = index

        while True:

            a = self._list1[i]

            if isinstance(a, Key):

                if keyname == a.keyname:
                    return a.value

            elif a == None:

                return "key does not exists"

            i = (i + 1) % self.capacity

            if i == index:
                return "key does not exists"

    # while removing we need to replace it some dummy key ,beacuse previously
    # during adding some key ,key might have jump to another index due to presence of this
    # , so if in future we want to serach that key our program can jump from
    # dummy key to find the correct index of that key.

    def remove(self, keyname):

        index = self.hash(keyname)

        i = index

        while True:

            a = self._list1[i]

            if isinstance(a, Key):

                if a.keyname == keyname:
                    self._list1[i] = "None"

                    self.size -= 1

                    break

            elif a == None:

                return "key does not exists"

            i = (i + 1) % self.capacity

            if i == index:
                return "key does not exists"

    def __str__(self):

        list2 = list()

        for a in self._list1:

            if isinstance(a, Key):
                list2.append(a.keyname)

        return str(list2)

        # liner probing


