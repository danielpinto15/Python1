#função que devolva: Maior numero da lista, o menor numero da lista e a media
numberList = [5, 6, 9, 10, 22, 42, 68]

def biggest(list):
    return max(list)

def smallest(list):
    return min(list)

def mean(list):
    return sum(list) / len(list)

def allTheValues(list):
    min = smallest(list)
    max =  biggest(list)
    media = mean(list)
    return {
        "min": min,
        "max": max,
        "mean": int(media)
    }

print(allTheValues(numberList))