#-*- coding: utf-8 -*-

# Supported by HJSAMO
def split_tika_content(content):
    """tika에서 반환된 content를 엔진에서 활용할 body만 걸러내기 위해 split"""
    
    header_idx = content.find('제1조')
    if (header_idx < 0) : header_idx = content.find('제 1조')
    if (header_idx < 0) : header_idx = content.find('제1 조')
    if (header_idx < 0) : header_idx = content.find('제 1 조')
    if (header_idx < 0) : header_idx = 0
    
    for n in range(1, 1000):
        r = [content.find('제%d조' %n)
             , content.find('제 %d조' %n)
             , content.find('제%d 조' %n)
             , content.find('제 %d 조' %n)]
        r.sort()
        if r[3] < 0 : break
        last_num_idx = r[3]
    last_enter_idx = content[last_num_idx:].find('\n\n')

    if last_num_idx >= 0 and last_enter_idx >= 0 : body_idx = last_num_idx + last_enter_idx
    else : body_idx = len(content)
    
    return (content[0:header_idx], content[header_idx:body_idx], content[body_idx:])