class Cell(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    #  def __str__(self):
        #  return "(head: {} (id: {})\ntail: {} (id {}))".format(\
                #  self.head, id(self.head),
                #  self.tail, id(self.tail))


class LinkedList(object):
    def __init__(self, arg_list):
        arg_list.reverse()
        self.cell = arg_list[0]
        for elem in arg_list[1:]:
            self.cell = Cell(elem, self.cell)

    def __str__(self):
        ret = "( "
        target = self.cell
        while type(target) is Cell:
            ret += str(target.head) + " "
            target = target.tail
        else:
             ret += str(target) + " )"
        return ret


if __name__ == "__main__":
    list = LinkedList([1, 2, 3])
    """
    内部構造としては下のようになる
    list.cell = Cell(1, Cell(2, 3)) 

    実際のコンスセルの構造に寄せたのだけど合ってるかしら
    python の実装上、
    list.cell.head は、int(1) っていう値ではなく
    ポインタを意味するみたいだし
    """
    print(list)

