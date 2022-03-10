#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        save = False
        frase = ''
        result = []

        for l in text:
            if l == '"':
                if save:
                    result.append(frase)
                    frase = ''
                save = not save
                continue
            if save:
                frase += l

        print(result)
