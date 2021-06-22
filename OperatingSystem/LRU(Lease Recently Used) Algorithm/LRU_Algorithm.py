num_page_frame = 4
allocated_pages = [2, 6, 1, 4]
reference_string = [5, 1, 2, 1, 4, 5, 6, 4, 5]

    
def LRU_replace(num_page_frame, allocated_pages, reference_string):
    for data in reference_string:
        #allocated_pages리스트는 참조한지 오래된 순으로 저장
        if data not in allocated_pages:
            allocated_pages.pop(0)
            allocated_pages.append(data)
        else:
            allocated_pages.remove(data)
            allocated_pages.append(data)
    
    return allocated_pages


result_pages = LRU_replace(num_page_frame, allocated_pages, reference_string)
print(result_pages)