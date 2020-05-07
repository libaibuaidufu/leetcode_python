#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 11:43
# @File    : add_two_nums.py
# @author  : dfkai
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  # 头结点，无存储，指向链表第一个结点
        node = head  # 初始化链表结点
        carry = 0  # 初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            print(x, y)
            sum = x + y + carry  # 对每一位求和
            print(sum)
            carry = sum // 10  # 地板除，求进一（其为0或1）
            print(carry)
            node.next = ListNode(sum % 10)  # 取余数，求本位结点
            if l1:  # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:  # 同上
                l2 = l2.next
            node = node.next  # 更新指针
        if carry != 0:  # 验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next  # 返回头结点的下一个结点，即链表的第一个结点


if __name__ == '__main__':
    so = Solution()
    data = so.addTwoNumbers(ListNode(142), ListNode(564))
    print(data.val, data.next.val)
