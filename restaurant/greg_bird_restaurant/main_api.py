#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue


class Processor(object):

    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):
            line = line.rstrip()
            # split and handle the commands here
            print('{}:{}'.format(line_i, line))
            parts = line.split(',')
            # call this command's function
            try:
                func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
                func(*parts[1:])
            except Exception as e:
                print('Error: {}'.format(e))


    def cmd_debug(self, *args):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()

    def cmd_song(self, *args):
        print(self.songs_iter.next())

    def cmd_appetizer(self, *args):
        app = self.appetizers.dequeue()
        i = self.waiting.size - 1
        values = []
        if self.waiting.size >= 3:
            while i >= self.waiting.size - 3:
                values.append(self.waiting.get(i))
                i -= 1
        elif self.waiting.size == 2:
            while i >= self.waiting.size - 2:
                values.append(self.waiting.get(i))
                i -= 1
        elif self.waiting.size == 1:
            while i >= self.waiting.size - 1:
                values.append(self.waiting.get(i))
                i -= 1
        else:
            values.append(self.waiting.get(i))
        print('{} >>> {}'.format(app, ', '.join(values)))

    def cmd_appetizer_ready(self, *args):
        self.appetizers.enqueue(args[0])

    def cmd_call(self, *args):
        self.callahead.add(args[0])

    def cmd_arrive(self, *args):
        # check if they were on the callin list
        callaheadSize = self.callahead.size
        waitingSize = self.waiting.size
        callahead = False
        self.buzzers.pop()
        i = 0
        while i < callaheadSize:
            if self.callahead.get(i) == args[0]:
                self.callahead.delete(i)
                callahead = True
                break
            i += 1
        if callahead:
            if waitingSize <= 5:
                self.waiting.insert(0, args[0])
            else:
                self.waiting.insert(waitingSize - 4, args[0])
        else:
            self.waiting.add(args[0])

    def cmd_seat(self, *args):
        try:
            print(self.waiting.get(0))
            self.waiting.delete(0)
            self.buzzers.push('Buzzer')
        except:
            raise IndexError('The given index is not within the bounds of the current list.')

    def cmd_leave(self, *args):
        self.buzzers.push('Buzzer')
        waitingSize = self.waiting.size
        i = 0
        while i < waitingSize:
            if self.waiting.get(i) == args[0]:
                self.waiting.delete(i)
                break
            i += 1


#######################
###   Main loop

with open('data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)
