#!/usr/bin/python3
"""Define a class SinglyLinkedList"""


class Node:
    """ Class Node """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Set data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Get next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Set next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class SinglyLinkedList """
    def __init__(self):

        self.__head = None

    def sorted_insert(self, value):
        """ Insert in sorted linked list """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """ Print the Linked List """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
