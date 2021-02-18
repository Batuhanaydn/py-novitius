def delete_nth(order,max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x)
            
    return answer
