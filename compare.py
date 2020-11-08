
def clean_lst(lst):
    cleaned_lst = []
    for data in lst:
        if (data != ''):
            cleaned_lst.append(data.split('==')[0])
    
    return cleaned_lst
        
        
        

def compare_files(small_file, big_file):
    match = []
    unmatch = []
    # 
    for data in small_file:
        if (big_file.count(data) > 0):
            match.append(data)
        else:
            unmatch.append(data)
    
    return match,unmatch




file1 = 'req_old.txt'
file2 = 'req.txt'

file1 = clean_lst(open(file1,'r').read().split('\n'))
file2 = clean_lst(open(file2,'r').read().split('\n'))


compare_files = compare_files(file1,file2)
# 0 = match, 1 = unmatch

print(compare_files[1])
# ['dj-database-url', 'docutils', 'gunicorn', 'psycopg2', 'raven', 'redis']

