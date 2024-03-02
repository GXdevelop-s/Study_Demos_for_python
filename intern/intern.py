# Definition for singly-linked list.


def deco(fun):
    def inner_fun():
        fun()
        print('add')
    return inner_fun


@deco
def be_deco():
    print('original')


if __name__ == '__main__':
    listnode_head = ListNode(99, None)
    listnode_tail = listnode_head
    for i in range(1, 5):
        temp_node = ListNode(i)
        listnode_tail.next = temp_node
        listnode_tail = temp_node
