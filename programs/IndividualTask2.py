#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    new_text = ''
    with open('fileForProgram.py', 'r') as f:
        save = True
        for line in f:
            for s in line:
                if s == '#':
                    save = not save
                elif s == '\n' and save == False:
                    save = not save
                if save:
                    new_text += s
        print(new_text)
    with open('fileForProgram.py', 'w') as f:
        f.write(new_text)
