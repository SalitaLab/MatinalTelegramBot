#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

class Queue():

    def __init__(self):
        self.queue = []

    def length(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def push(self, object):
        self.queue.append(object)

    def pop(self):
        if not self.empty():
            result = self.queue[0]
            self.queue = self.queue[1:]
            return result


class Telegram_Queue(Queue):

    def __init__(self):
        Queue.__init__(self)

    def save_in_file(self, path):
        texto = ""
        for i in range(len(self.queue)):
            texto += self.queue[i]
            texto += "\n"

        file = codecs.open(path, "w", encoding='utf8')
        file.write(texto)
        file.close()

    def load_from_file(self, path):
        file = codecs.open(path, "r", encoding='utf8')
        array = file.read().split('\n')
        array = array[:(len(array) - 1)]

        self.queue = array

        file.close()

    def clear(self):
        self.queue = []
