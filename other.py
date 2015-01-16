def getvocab():
    f = open('text.txt')
    array = [line.strip() for line in open('text.txt')]
    f.close()
    return array